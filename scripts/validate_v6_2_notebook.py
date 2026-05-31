#!/usr/bin/env python3
"""Validate and optionally execute the v6.2 final literature merged notebook.

The script separates lightweight static checks from notebook execution:

* ``--mode smoke`` creates a tiny synthetic fixture with train.csv, test.csv,
  and sample_submission.csv and executes the notebook with PSP_RUN_MODE=smoke.
* ``--mode full`` executes against the requested data directory (default: data/)
  without forcing a synthetic fixture.
* ``--skip-execution`` performs only path/static checks and output-contract checks.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import csv

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_NAME = "00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb"
REQUIRED_INPUTS = ("train.csv", "test.csv", "sample_submission.csv")
EXPECTED_OUTPUT_DIR = "outputs/team_report_v6_2"
EXPECTED_SUBMISSION_PREFIX = "submission_team_report_v6_2"
REQUIRED_OUTPUT_PATTERNS = {
    "oof": ("oof", "v6_2", ".csv"),
    "prediction_bank": ("prediction_bank", "v6_2", ".csv"),
    "ensemble_weights": ("ensemble_weights", "v6_2", ".csv"),
    "submission": (EXPECTED_SUBMISSION_PREFIX, ".csv"),
}


@dataclass(frozen=True)
class ValidationResult:
    mode: str
    notebook: Path
    data_dir: Path
    output_dir: Path
    executed: bool
    generated_files: list[Path]
    submission_files: list[Path]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--notebook", type=Path, default=REPO_ROOT / NOTEBOOK_NAME)
    parser.add_argument("--data-dir", type=Path, default=REPO_ROOT / "data")
    parser.add_argument("--output-dir", type=Path, default=REPO_ROOT / EXPECTED_OUTPUT_DIR)
    parser.add_argument("--mode", choices=("smoke", "full"), default="smoke")
    parser.add_argument("--skip-execution", action="store_true")
    parser.add_argument(
        "--use-synthetic-smoke-data",
        action="store_true",
        help="Create a temporary smoke fixture instead of reading --data-dir. Intended for CI only.",
    )
    parser.add_argument("--timeout", type=int, default=1800)
    return parser.parse_args()


def load_notebook(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def notebook_text(nb: dict) -> str:
    return "\n".join("".join(cell.get("source", "")) for cell in nb.get("cells", []))


def assert_static_contract(nb: dict) -> None:
    text = notebook_text(nb)
    required_snippets = [
        EXPECTED_OUTPUT_DIR,
        EXPECTED_SUBMISSION_PREFIX,
        "validate_submission_frame",
        "submission row count must match sample_submission",
        "submission ID column order must match sample_submission",
        "probability column must not contain null values",
        "probability values must be within [0, 1]",
        "train shape:",
        "test shape:",
        "target column:",
        "sample_submission columns:",
    ]
    missing = [snippet for snippet in required_snippets if snippet not in text]
    if missing:
        raise AssertionError(f"Notebook is missing required sanity-check snippets: {missing}")


def assert_input_files(data_dir: Path) -> None:
    missing = [name for name in REQUIRED_INPUTS if not (data_dir / name).exists()]
    if missing:
        raise FileNotFoundError(
            f"Missing required input files under {data_dir}: {missing}. "
            "Use --use-synthetic-smoke-data for CI smoke execution, or pass --data-dir."
        )


def create_synthetic_smoke_data() -> tempfile.TemporaryDirectory[str]:
    tmp = tempfile.TemporaryDirectory(prefix="psp_v6_2_smoke_")
    data_dir = Path(tmp.name)
    rows = 48
    test_rows = 12
    train_header = ["ID", "여성 나이", "시술 유형", "배아 수", "난자 수", "이식 횟수", "임신 성공 여부"]
    test_header = ["ID", "여성 나이", "시술 유형", "배아 수", "난자 수", "이식 횟수"]
    train_rows = []
    for i in range(rows):
        train_rows.append([
            f"TR_{i:03d}",
            25 + (i % 14),
            "IVF" if i % 2 else "ICSI",
            "" if i % 5 == 0 else i % 4,
            "" if i % 7 == 0 else 2 + (i % 6),
            i % 3,
            i % 2,
        ])
    test_rows_data = []
    for i in range(test_rows):
        test_rows_data.append([
            f"TE_{i:03d}",
            27 + (i % 10),
            "IVF" if i % 2 else "ICSI",
            "" if i % 4 == 0 else i % 5,
            "" if i % 3 == 0 else 3 + (i % 4),
            i % 2,
        ])

    with (data_dir / "train.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(train_header)
        writer.writerows(train_rows)
    with (data_dir / "test.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(test_header)
        writer.writerows(test_rows_data)
    with (data_dir / "sample_submission.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["ID", "probability"])
        writer.writerows([[row[0], 0.0] for row in test_rows_data])
    return tmp


def execute_notebook(notebook: Path, data_dir: Path, output_dir: Path, mode: str, timeout: int) -> None:
    try:
        import nbformat
        from nbclient import NotebookClient
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise RuntimeError("nbformat and nbclient are required for notebook execution validation") from exc

    output_dir.mkdir(parents=True, exist_ok=True)
    nb = nbformat.read(notebook, as_version=4)
    env = os.environ.copy()
    env.update(
        {
            "PSP_RUN_MODE": mode,
            "PSP_DATA_DIR": str(data_dir),
            "PSP_OUTPUT_DIR": str(output_dir),
        }
    )

    old_env = os.environ.copy()
    os.environ.update(env)
    try:
        client = NotebookClient(nb, timeout=timeout, kernel_name="python3", resources={"metadata": {"path": str(REPO_ROOT)}})
        client.execute()
    finally:
        os.environ.clear()
        os.environ.update(old_env)


def collect_generated_files(output_dir: Path) -> list[Path]:
    if not output_dir.exists():
        return []
    return sorted(path for path in output_dir.rglob("*") if path.is_file())


def assert_outputs(generated_files: Iterable[Path], output_dir: Path) -> None:
    names = [path.name for path in generated_files]
    missing_labels = []
    for label, parts in REQUIRED_OUTPUT_PATTERNS.items():
        if not any(all(part in name for part in parts) for name in names):
            missing_labels.append(label)
    if missing_labels:
        raise AssertionError(f"Missing expected output artifacts in {output_dir}: {missing_labels}. Found: {names}")


def assert_submission_matches_sample(submission_files: list[Path], data_dir: Path) -> None:
    if not submission_files:
        raise AssertionError("No submission file found")
    submission_path = max(submission_files, key=lambda path: path.stat().st_mtime)
    with (data_dir / "sample_submission.csv").open(encoding="utf-8", newline="") as handle:
        sample_reader = csv.DictReader(handle)
        sample_header = sample_reader.fieldnames or []
        sample_rows = list(sample_reader)
    with submission_path.open(encoding="utf-8", newline="") as handle:
        submission_reader = csv.DictReader(handle)
        submission_header = submission_reader.fieldnames or []
        submission_rows = list(submission_reader)
    if len(submission_rows) != len(sample_rows):
        raise AssertionError(f"Submission row count {len(submission_rows)} != sample_submission row count {len(sample_rows)}")
    if submission_header != sample_header:
        raise AssertionError("Submission columns do not match sample_submission columns")
    id_candidates = ["ID", "id", "시술 ID", "환자 ID"]
    id_col = next((col for col in id_candidates if col in sample_header), None)
    if id_col is not None and [row[id_col] for row in submission_rows] != [row[id_col] for row in sample_rows]:
        raise AssertionError("Submission ID order does not match sample_submission")
    probability_col = next((col for col in submission_header if col != id_col), submission_header[-1])
    probabilities = [row.get(probability_col, "") for row in submission_rows]
    if any(value == "" for value in probabilities):
        raise AssertionError("Submission probability column contains null values")
    try:
        probability_values = [float(value) for value in probabilities]
    except ValueError as exc:
        raise AssertionError("Submission probability column contains non-numeric values") from exc
    if not all(0 <= value <= 1 for value in probability_values):
        raise AssertionError("Submission probability values are outside [0, 1]")


def validate(args: argparse.Namespace) -> ValidationResult:
    notebook = args.notebook.resolve()
    nb = load_notebook(notebook)
    assert_static_contract(nb)

    tmp_data = None
    data_dir = args.data_dir.resolve()
    if args.use_synthetic_smoke_data:
        if args.mode != "smoke":
            raise ValueError("Synthetic data is only allowed in smoke mode")
        tmp_data = create_synthetic_smoke_data()
        data_dir = Path(tmp_data.name)

    try:
        assert_input_files(data_dir)
        output_dir = args.output_dir.resolve()
        if not args.skip_execution:
            if output_dir.exists():
                shutil.rmtree(output_dir)
            execute_notebook(notebook, data_dir, output_dir, args.mode, args.timeout)

        generated_files = collect_generated_files(output_dir)
        if not args.skip_execution:
            assert_outputs(generated_files, output_dir)
            submission_files = [path for path in generated_files if path.name.startswith(EXPECTED_SUBMISSION_PREFIX) and path.suffix == ".csv"]
            assert_submission_matches_sample(submission_files, data_dir)
        else:
            submission_files = [path for path in generated_files if path.name.startswith(EXPECTED_SUBMISSION_PREFIX) and path.suffix == ".csv"]

        return ValidationResult(
            mode=args.mode,
            notebook=notebook,
            data_dir=data_dir,
            output_dir=output_dir,
            executed=not args.skip_execution,
            generated_files=generated_files,
            submission_files=submission_files,
        )
    finally:
        if tmp_data is not None:
            tmp_data.cleanup()


def main() -> int:
    args = parse_args()
    result = validate(args)
    print(json.dumps(
        {
            "mode": result.mode,
            "notebook": str(result.notebook),
            "data_dir": str(result.data_dir),
            "output_dir": str(result.output_dir),
            "executed": result.executed,
            "generated_files": [str(path) for path in result.generated_files],
            "submission_files": [str(path) for path in result.submission_files],
        },
        ensure_ascii=False,
        indent=2,
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
