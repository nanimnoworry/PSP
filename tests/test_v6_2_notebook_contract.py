from __future__ import annotations

import ast
import json
from pathlib import Path

NOTEBOOK = Path("00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb")
EXPECTED_OUTPUT_DIR = "outputs/team_report_v6_2"
EXPECTED_SUBMISSION_PREFIX = "submission_team_report_v6_2"


def load_notebook() -> dict:
    with NOTEBOOK.open(encoding="utf-8") as handle:
        return json.load(handle)


def notebook_text(nb: dict) -> str:
    return "\n".join("".join(cell.get("source", "")) for cell in nb.get("cells", []))


def test_notebook_json_is_valid() -> None:
    nb = load_notebook()
    assert nb["nbformat"] >= 4
    assert isinstance(nb.get("cells"), list)


def test_code_cells_compile() -> None:
    nb = load_notebook()
    for index, cell in enumerate(nb["cells"]):
        if cell.get("cell_type") == "code":
            source = "".join(cell.get("source", ""))
            ast.parse(source, filename=f"{NOTEBOOK}:cell_{index}")


def test_output_directory_contract() -> None:
    text = notebook_text(load_notebook())
    assert EXPECTED_OUTPUT_DIR in text


def test_submission_prefix_contract() -> None:
    text = notebook_text(load_notebook())
    assert EXPECTED_SUBMISSION_PREFIX in text


def test_sample_submission_structure_validation_is_present() -> None:
    text = notebook_text(load_notebook())
    required = [
        "validate_submission_frame",
        "submission row count must match sample_submission",
        "submission columns must match sample_submission",
        "submission ID column order must match sample_submission",
        "probability column must not contain null values",
        "probability values must be within [0, 1]",
    ]
    for snippet in required:
        assert snippet in text
