# Repository Cleanup Status

## Completed

- Official final result separated from highest submitted AUC.
- Final artifact manifest created.
- Official model lineage documented.
- Post-submission research separated from official submission lineage.
- Historical notebook identity index recorded.
- Historical notebooks moved to `historical/notebooks/` with their existing Git blob SHA preserved.
- Legacy PNG/screenshots moved to `historical/assets/` with their existing Git blob SHA preserved.
- Active v6.2 execution contract preserved.
- Repository root reduced to the active notebooks, README, and purpose-specific directories.

## Root policy

The repository root now keeps the active execution surface small:

```text
README.md
00.Project_Fertility_PSP_v6.2.ipynb
00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb

deliverables/
docs/
historical/
post_submission/
reports/
scripts/
tests/
```

## Why the two v6.2 notebooks remain at root

The final literature merged notebook is referenced by `scripts/validate_v6_2_notebook.py` through its exact root-level filename:

```text
00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb
```

Moving it without changing the validation contract would reduce reproducibility, so it stays at root deliberately.

## Preservation result

The archive move was performed by reusing the existing blob SHA values instead of rewriting notebook content. Therefore the repository became easier to browse without silently modifying historical research artifacts.
