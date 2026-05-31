# Fertility PSP Prediction Report

난임 시술 데이터 기반 임신 성공 여부 예측 모델링 프로젝트입니다.  
본 저장소는 `train.csv`, `test.csv`, `sample_submission.csv`만 사용하는 독립 실행형 분석 노트북과 제출 파일 생성 흐름을 제공합니다.

최종 권장 노트북은 다음 파일입니다.

```text
00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb
```

---

## 1. 프로젝트 목적

본 프로젝트의 목표는 난임 시술 관련 임상·시술 데이터를 바탕으로 임신 성공 가능성을 예측하는 모델을 구축하고, 제출 가능한 `submission.csv` 파일을 생성하는 것입니다.

v6.2 노트북은 다음 두 흐름을 통합한 최종 후보 버전입니다.

```text
v5.1 : v5 기반 문헌 인용 및 결과 해석 보강본
v6   : 코드 구조, 실행 흐름, 검증 구조 개선본
v6.2 : v6 실행 구조 + v5.1 문헌/해석 보강 통합본
```

---

## 2. 주요 파일

```text
.
├── 00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb
├── 00.Project_Fertility_PSP_v6.2.ipynb
├── scripts/
│   └── validate_v6_2_notebook.py
├── tests/
│   └── test_v6_2_notebook_contract.py
├── reports/
│   └── v6_2_notebook_audit.md
└── outputs/
    └── team_report_v6_2/
```

| 파일 | 설명 |
|---|---|
| `00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb` | 최종 권장 노트북. v6 실행 구조에 v5.1 문헌 해석을 반영한 통합본 |
| `00.Project_Fertility_PSP_v6.2.ipynb` | 동일한 감사 반영본으로 정렬된 v6.2 노트북 |
| `scripts/validate_v6_2_notebook.py` | 노트북 정적 검사, smoke 실행, 산출물 검증 스크립트 |
| `reports/v6_2_notebook_audit.md` | v6.2 노트북 감사 보고서 |

---

## 3. 데이터 준비

본 저장소는 원본 대회 데이터를 포함하지 않습니다.  
아래 파일을 `data/` 디렉토리에 직접 배치해야 합니다.

```text
data/
├── train.csv
├── test.csv
└── sample_submission.csv
```

노트북은 외부 submission, public score anchor, 이전 제출 후보 파일을 참조하지 않습니다.  
입력 데이터는 위 3개 파일만 사용합니다.

---

## 4. 실행 모드

v6.2 노트북은 환경변수를 통해 실행 모드를 제어할 수 있습니다.

| 환경변수 | 기본값 | 설명 |
|---|---|---|
| `PSP_RUN_MODE` | `smoke` 또는 노트북 설정값 | `smoke` / `full` 실행 모드 |
| `PSP_DATA_DIR` | `data` | 입력 데이터 디렉토리 |
| `PSP_OUTPUT_DIR` | `outputs/team_report_v6_2` | 산출물 저장 디렉토리 |

### Smoke 모드

빠른 구조 검증용 모드입니다.  
CV split과 모델 반복 수를 줄여 노트북 실행 가능성을 확인합니다.

```bash
PSP_RUN_MODE=smoke \
PSP_DATA_DIR=data \
PSP_OUTPUT_DIR=outputs/team_report_v6_2_smoke
```

### Full 모드

실제 제출 파일 생성을 위한 전체 실행 모드입니다.

```bash
PSP_RUN_MODE=full \
PSP_DATA_DIR=data \
PSP_OUTPUT_DIR=outputs/team_report_v6_2
```

---

## 5. 검증 방법

### 5.1 기본 테스트

```bash
python -m pytest tests/test_v6_2_notebook_contract.py -q
```

### 5.2 검증 스크립트 문법 확인

```bash
python -m py_compile scripts/validate_v6_2_notebook.py
```

### 5.3 Smoke 정적 검증

```bash
python scripts/validate_v6_2_notebook.py \
  --mode smoke \
  --use-synthetic-smoke-data \
  --skip-execution \
  --output-dir outputs/team_report_v6_2_smoke
```

### 5.4 Smoke 실제 실행 검증

`nbformat`, `nbclient`, `ipykernel`이 필요합니다.

```bash
python -m pip install nbformat nbclient ipykernel
```

그다음 실행합니다.

```bash
python scripts/validate_v6_2_notebook.py \
  --mode smoke \
  --use-synthetic-smoke-data \
  --output-dir outputs/team_report_v6_2_smoke \
  --timeout 300
```

### 5.5 Full 실행 검증

실제 `data/train.csv`, `data/test.csv`, `data/sample_submission.csv`가 있는 환경에서 실행합니다.

```bash
python scripts/validate_v6_2_notebook.py \
  --mode full \
  --data-dir data \
  --output-dir outputs/team_report_v6_2 \
  --timeout 7200
```

데이터가 다른 위치에 있다면 `--data-dir`만 바꿉니다.

```bash
python scripts/validate_v6_2_notebook.py \
  --mode full \
  --data-dir /path/to/data \
  --output-dir outputs/team_report_v6_2 \
  --timeout 7200
```

---

## 6. 산출물

Full 실행 후 기본 산출물은 아래 경로에 저장됩니다.

```text
outputs/team_report_v6_2/
```

주요 산출물은 다음과 같습니다.

| 산출물 | 설명 |
|---|---|
| `submission_team_report_v6_2_*.csv` | 최종 제출 후보 파일 |
| OOF bank | OOF 예측 결과 저장 |
| prediction bank | test 예측 결과 저장 |
| ensemble weights | 앙상블 가중치 저장 |
| validation/report files | 실행 및 제출 검증 결과 |

제출 파일은 `sample_submission.csv` 구조를 보존해야 합니다.

검증 항목은 다음과 같습니다.

```text
- row 수가 sample_submission과 동일한가
- 컬럼 구조가 sample_submission과 동일한가
- ID 순서가 sample_submission과 동일한가
- probability에 null이 없는가
- probability 값이 0~1 범위인가
```

---

## 7. 문헌 해석 반영 원칙

v6.2 노트북은 v5.1의 문헌 기반 해석을 반영하되, 고정된 성능 수치나 feature 수를 전제하지 않습니다.

해석 문장은 다음 원칙을 따릅니다.

```text
- 성능 수치와 feature 수는 실행 결과 기준으로 확인한다.
- 임상적 표현은 단정하지 않는다.
- "원인이다"보다는 "관련될 수 있다", "모델이 활용했을 가능성이 있다"처럼 표현한다.
- 출처는 가능한 한 (저자 또는 기관, 연도) 형식으로 간결하게 표기한다.
```

---

## 8. 주의 사항

본 프로젝트는 데이터 분석 및 예측 모델링 실습/보고서 목적입니다.  
모델 결과는 실제 의학적 판단이나 임상 의사결정을 대체할 수 없습니다.

또한 본 저장소의 v6.2 노트북은 독립 실행형 팀 보고서 원칙을 유지합니다.

```text
사용함:
- train.csv
- test.csv
- sample_submission.csv

사용하지 않음:
- 외부 submission blend
- public score anchor
- 이전 stage 연구 결과
- 이전 제출 후보 파일
```

---

## 9. 현재 검증 상태

현재까지 확인된 항목은 다음과 같습니다.

```text
✅ 노트북 JSON 유효성 검사
✅ 코드 셀 compile 검사
✅ output directory 계약 검사
✅ submission prefix 계약 검사
✅ sample_submission 구조 보존 코드 존재 확인
✅ smoke fixture 기반 skip-execution 검증
```

아직 실제 제출 전에는 다음 검증이 필요합니다.

```text
⚠️ nbclient 기반 smoke 실제 실행
⚠️ 실제 train/test/sample_submission 기반 full 실행
⚠️ 실제 submission_team_report_v6_2_*.csv 생성 확인
```

---

## 10. 권장 제출 전 체크리스트

제출 전 아래 항목을 확인합니다.

```text
[ ] Full 모드가 오류 없이 완료되었는가
[ ] outputs/team_report_v6_2/에 제출 파일이 생성되었는가
[ ] submission row 수가 sample_submission과 같은가
[ ] ID 순서가 sample_submission과 같은가
[ ] probability 값에 null이 없는가
[ ] probability 값이 0~1 범위인가
[ ] 보고서 해석 문장이 실행 결과와 충돌하지 않는가
[ ] 외부 submission 또는 public score anchor 참조가 없는가
```

---

## 11. 권장 실행 순서

```bash
# 1. 의존성 설치
python -m pip install nbformat nbclient ipykernel

# 2. 정적 테스트
python -m pytest tests/test_v6_2_notebook_contract.py -q

# 3. smoke 실행 검증
python scripts/validate_v6_2_notebook.py \
  --mode smoke \
  --use-synthetic-smoke-data \
  --output-dir outputs/team_report_v6_2_smoke \
  --timeout 300

# 4. full 실행 검증
python scripts/validate_v6_2_notebook.py \
  --mode full \
  --data-dir data \
  --output-dir outputs/team_report_v6_2 \
  --timeout 7200

# 5. 제출 파일 확인
ls -lah outputs/team_report_v6_2/submission_team_report_v6_2_*.csv
```

---

## 12. License / Data

원본 데이터는 저장소에 포함하지 않습니다.  
데이터 사용 조건은 제공처의 규정을 따릅니다.
