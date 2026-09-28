from __future__ import annotations

import json
import sys
from pathlib import Path

FORBIDDEN_DATA_BASENAMES = {"train.csv", "test.csv", "sample_submission.csv"}


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures: list[str] = []

    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue

        if path.name.lower() in FORBIDDEN_DATA_BASENAMES:
            fail(f"raw competition data file must not be committed: {path.relative_to(root)}", failures)

        if path.suffix.lower() != ".ipynb":
            continue

        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"invalid notebook JSON: {path.relative_to(root)} ({exc})", failures)
            continue

        for index, cell in enumerate(notebook.get("cells", [])):
            if cell.get("cell_type") != "code":
                continue

            outputs = cell.get("outputs", [])
            if outputs:
                fail(
                    f"notebook output must be cleared: {path.relative_to(root)} cell {index} "
                    f"({len(outputs)} output item(s))",
                    failures,
                )

            if cell.get("execution_count") is not None:
                fail(
                    f"execution_count must be null: {path.relative_to(root)} cell {index}",
                    failures,
                )

    if failures:
        print("Public notebook safety check FAILED:")
        for item in failures:
            print(f"- {item}")
        return 1

    print("Public notebook safety check passed: no raw competition CSVs and all notebook outputs are clear.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
