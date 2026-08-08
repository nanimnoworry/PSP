# Post-Submission Research & Reproducibility

이 디렉토리는 **실제 대회/프로젝트 최종 제출 이후에 진행된 재현성 개선, 코드 구조 개선, 감사(audit), literature merge 작업**을 공식 제출 계보와 분리하기 위한 안내 문서입니다.

현재 저장소 루트에는 다음과 같은 후속 버전들이 역사적으로 남아 있습니다.

```text
00.Project_Fertility_PSP_v5.1.ipynb
00.Project_Fertility_PSP_v6_experimental.ipynb
00.Project_Fertility_PSP_v6.2.ipynb
00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb
00_Project_Fertility_PSP_v6_3.ipynb
scripts/validate_v6_2_notebook.py
reports/v6_2_notebook_audit.md
```

이 파일들은 유용한 연구 자산이지만 **공식 최종 제출 당시 파일과 동일한 의미로 취급하지 않습니다.**

## 현재 정리 원칙

이번 정리에서는 기존 파일을 성급하게 이동하거나 삭제하지 않습니다.

이유:

- 과거 링크와 commit history를 보존하기 위해서
- 동일 파일명이라도 실제 제출본과 hash가 다를 수 있어서
- v6.x가 제출 당시 모델이 아니라 사후 재현성/통합 연구일 수 있어서
- 연구 계보를 먼저 문서화한 뒤 물리적 폴더 이동 여부를 결정하는 편이 안전해서

따라서 현재 단계에서는 **역할을 먼저 분리**합니다.

| 분류 | 의미 |
|---|---|
| `official final` | 실제 제출/발표에 사용된 자료 |
| `post-submission` | 제출 이후 재현성·구조·문헌·실험 개선 |
| `historical` | 과거 중간 버전과 탐색 기록 |

## v6.2 계열의 가치

v6.2 계열은 다음과 같은 재현성 개선을 가지고 있어 삭제 대상이 아닙니다.

- `train.csv`, `test.csv`, `sample_submission.csv` 중심의 독립 실행 구조
- smoke / full 실행 모드
- output directory 계약
- submission 구조 검증
- notebook static / smoke validation script
- 문헌 해석과 실행 코드를 결합한 보고서형 notebook

다만 이 장점은 **사후 정리·재현성 자산으로서의 장점**이며, 실제 최종 제출물의 역사적 신원을 대체하지 않습니다.

## 관련 문서

- [공식/후속 모델 계보](../docs/model_lineage.md)
- [실제 최종 제출 artifact manifest](../deliverables/final_submission/MANIFEST.md)
- [프로젝트 메인 README](../README.md)
