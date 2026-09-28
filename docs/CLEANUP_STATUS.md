# Repository Cleanup Status

## Completed

- Official final result separated from highest submitted AUC.
- Final artifact manifest created.
- Official model lineage documented.
- Post-submission research separated from official submission lineage.
- Historical notebook identity index recorded.
- Historical notebooks moved to `historical/notebooks/`; original source blob SHA는 provenance로 기록하고 default-branch 공개본의 실행 output은 sanitize.
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

초기 archive 이동은 기존 blob identity를 보존해 수행했습니다. 이후 공개 데이터 경계를 강화하기 위해 default branch의 Notebook 실행 output과 execution count를 제거했으며, pre-sanitization source SHA와 current public SHA를 모두 기록합니다. 자세한 내역은 [`PUBLIC_NOTEBOOK_SANITIZATION.md`](PUBLIC_NOTEBOOK_SANITIZATION.md)를 기준으로 합니다.
