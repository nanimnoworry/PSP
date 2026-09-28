# PSP Repository Map

`nanimnoworry/PSP`는 난임 프로젝트의 **공식 프로젝트 허브**입니다.

## 읽기 순서

1. `README.md` — 공식 결과와 저장소 역할
2. `docs/model_lineage.md` — 1안 → 2안 → 3안 → 최종 채택 계보
3. `deliverables/final_submission/MANIFEST.md` — 팀 제공 최종 제출물 identity
4. `historical/README.md` — 과거 개발 notebook 보존 원칙
5. `post_submission/README.md` — 제출 이후 재현성/개선 연구
6. `reports/v6_2_notebook_audit.md` — v6.2 감사 기록

## 디렉토리 역할

| 경로 | 역할 |
|---|---|
| `/` | 현재 실행 계약과 핵심 안내만 유지 |
| `deliverables/final_submission/` | 실제 제출 당시 artifact identity와 보존 기준 |
| `docs/` | 계보, 저장소 지도, 설명 문서 |
| `historical/` | 공식 개발 과정의 과거 notebook archive |
| `post_submission/` | 제출 이후 재현성·구조 개선 계열 설명 |
| `scripts/` | 실행/검증 스크립트 |
| `tests/` | notebook contract 검증 |
| `reports/` | 감사·검증 보고서 |

## 루트에 남겨야 하는 실행 파일

현재 `scripts/validate_v6_2_notebook.py`는 다음 파일명을 루트 기준으로 직접 참조합니다.

```text
00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb
```

따라서 해당 notebook과 연결된 v6.2 실행 계열은 무리하게 이동하지 않습니다.

## 정리 원칙

- 파일명보다 hash identity를 우선합니다.
- 최고 제출 AUC와 최종 채택 submission 모델을 구분합니다.
- 공식 제출 계보와 `planB` 후속 연구 계보를 구분합니다.
- 동작 중인 실행 계약을 깨뜨리기 위한 미관상 이동은 하지 않습니다.
- 과거 연구는 삭제보다 archive와 역할 표기를 우선합니다.
