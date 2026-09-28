# Historical Notebook Archive

**Scope:** 공식 개발 과정의 과거 Notebook · 시각 자료  
**Policy:** 연구 내용 보존 · 역할 분리 · source/current hash identity 병기 · 공개 output sanitation

## Rules

- historical 파일 삭제 금지
- v6.2 active execution 계열은 저장소 루트 유지
- historical source blob SHA는 provenance로 기록하고, default branch 공개본은 필요 시 output을 sanitize
- 파일명 충돌 시 [`deliverables/final_submission/MANIFEST.md`](../deliverables/final_submission/MANIFEST.md)의 hash 우선
- 공식 발표 모델 계보: [`docs/model_lineage.md`](../docs/model_lineage.md)

## Structure

```text
historical/
├── README.md
├── INDEX.md
├── notebooks/
│   ├── 00.Project_Fertility_PSP.ipynb
│   ├── 00.Project_Fertility_PSP_v3.ipynb
│   ├── 00.Project_Fertility_PSP_v4.ipynb
│   ├── 00.Project_Fertility_PSP_v5.ipynb
│   ├── 00.Project_Fertility_PSP_v5.1.ipynb
│   ├── 00.Project_Fertility_PSP_v6_experimental.ipynb
│   ├── 00_Project_Fertility_PSP_v6_3.ipynb
│   ├── prototype_PSP_Full_Code .ipynb
│   └── second_PSP_Full_Code.ipynb
└── assets/
    ├── second_PSP_Full_Code.png
    └── 스크린샷 2026-05-27 191231.png
```

**Identity note:** historical source artifact ≠ sanitized public copy ≠ byte-identical official final by default.  
`historical/notebooks/00.Project_Fertility_PSP_v5.ipynb`의 pre-sanitization source blob, 현재 공개본, 2026-08-08 canonical final 제출본은 각각 identity를 구분합니다.

Public sanitation 기록: [`../docs/PUBLIC_NOTEBOOK_SANITIZATION.md`](../docs/PUBLIC_NOTEBOOK_SANITIZATION.md)

## Active Root Notebooks

```text
00.Project_Fertility_PSP_v6.2.ipynb
00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb
```

`scripts/validate_v6_2_notebook.py`의 exact root-path contract 때문에 위치 유지.
