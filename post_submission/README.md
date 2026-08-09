# Post-Submission Research & Reproducibility

이 디렉토리는 **실제 대회/프로젝트 최종 제출 이후에 진행된 재현성 개선, 코드 구조 개선, 감사(audit), literature merge 작업**을 공식 제출 계보와 분리하기 위한 안내 문서입니다.

## 현재 보존 위치

과거 개발·실험 notebook은 정리 과정에서 내용 변경 없이 `historical/notebooks/`로 이동했습니다.

```text
historical/notebooks/
├── 00.Project_Fertility_PSP_v5.1.ipynb
├── 00.Project_Fertility_PSP_v6_experimental.ipynb
└── 00_Project_Fertility_PSP_v6_3.ipynb
```

현재 실행 계약에 직접 연결된 v6.2 계열은 저장소 루트에 유지합니다.

```text
00.Project_Fertility_PSP_v6.2.ipynb
00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb
scripts/validate_v6_2_notebook.py
reports/v6_2_notebook_audit.md
```

이 파일들은 유용한 연구 자산이지만 **공식 최종 제출 당시 파일과 동일한 의미로 취급하지 않습니다.**

## 분류 원칙

| 분류 | 의미 |
|---|---|
| `official final` | 실제 제출/발표에 사용된 자료와 그 identity 기록 |
| `post-submission` | 제출 이후 재현성·구조·문헌·실험 개선 |
| `historical` | 과거 중간 버전과 탐색 기록 |

실제 팀 제공 최종 artifact는 파일명보다 `deliverables/final_submission/MANIFEST.md`의 hash identity를 우선합니다.

## v6.2 계열의 가치

v6.2 계열은 다음과 같은 재현성 개선을 가지고 있어 루트의 active execution surface로 보존합니다.

- `train.csv`, `test.csv`, `sample_submission.csv` 중심의 독립 실행 구조
- smoke / full 실행 모드
- output directory 계약
- submission 구조 검증
- notebook static / smoke validation script
- 문헌 해석과 실행 코드를 결합한 보고서형 notebook

다만 이 장점은 **사후 정리·재현성 자산으로서의 장점**이며, 실제 최종 제출물의 역사적 신원을 대체하지 않습니다.

## 왜 v6.2 final notebook은 루트에 남아 있나

`scripts/validate_v6_2_notebook.py`가 다음 exact filename을 루트 기준으로 참조합니다.

```text
00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb
```

따라서 미관상 이동보다 현재 검증 계약의 재현성을 우선합니다.

## 관련 문서

- [공식/후속 모델 계보](../docs/model_lineage.md)
- [실제 최종 제출 artifact manifest](../deliverables/final_submission/MANIFEST.md)
- [Historical archive](../historical/README.md)
- [Repository map](../docs/repository_map.md)
- [프로젝트 메인 README](../README.md)
