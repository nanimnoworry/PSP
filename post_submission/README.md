# Post-Submission Research & Reproducibility

**Scope:** 공식 최종 제출 이후 재현성 · 코드 구조 · audit · literature merge  
**Boundary:** official final / post-submission / historical 분리

## Active Execution Surface

```text
00.Project_Fertility_PSP_v6.2.ipynb
00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb
scripts/validate_v6_2_notebook.py
reports/v6_2_notebook_audit.md
```

## Historical Notebooks

```text
historical/notebooks/
├── 00.Project_Fertility_PSP_v5.1.ipynb
├── 00.Project_Fertility_PSP_v6_experimental.ipynb
└── 00_Project_Fertility_PSP_v6_3.ipynb
```

과거 Notebook: Git blob 보존 이동.  
루트 v6.2 계열: 현재 실행/검증 계약 유지.

## Classification

| 분류 | 범위 |
|---|---|
| `official final` | 실제 제출/발표 artifact · identity |
| `post-submission` | 제출 이후 재현성 · 구조 · 문헌 · 실험 |
| `historical` | 과거 중간 버전 · 탐색 기록 |

**Artifact identity 우선순위:** 파일명 < [`deliverables/final_submission/MANIFEST.md`](../deliverables/final_submission/MANIFEST.md)의 hash

## v6.2 Contract

- `train.csv` · `test.csv` · `sample_submission.csv` 독립 실행
- smoke / full mode
- output directory contract
- submission schema validation
- notebook static / smoke validation
- literature interpretation + execution code

**역할:** post-submission reproducibility asset. 공식 최종 제출 artifact와 분리.

## Root Path Constraint

`scripts/validate_v6_2_notebook.py` exact reference:

```text
00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb
```

루트 경로 유지 — 검증 계약 우선.

## References

- [Model lineage](../docs/model_lineage.md)
- [Final submission manifest](../deliverables/final_submission/MANIFEST.md)
- [Historical archive](../historical/README.md)
- [Repository map](../docs/repository_map.md)
- [Main README](../README.md)
