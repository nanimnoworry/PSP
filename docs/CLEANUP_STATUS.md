# Repository Cleanup Status

## Completed

- Official final result separated from highest submitted AUC.
- Final artifact manifest created.
- Official model lineage documented.
- Post-submission research separated from official submission lineage.
- Historical notebook identity index recorded.
- Active v6.2 execution contract preserved.

## Intentionally not moved yet

Historical notebooks remain at root until the repository tree move can be performed atomically while preserving their existing blob SHA values. No content rewrite is needed for these files.

The files scheduled for archive are listed in `historical/INDEX.md`.

## Keep at root

```text
README.md
00.Project_Fertility_PSP_v6.2.ipynb
00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb
```

The final literature merged notebook is referenced by `scripts/validate_v6_2_notebook.py` through its exact root-level filename, so moving it without updating the validation contract would break reproducibility.
