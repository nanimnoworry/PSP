# v6.2 Final Literature Merged Notebook Audit

## 실행 검증 여부

- 감사 대상 노트북: `00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb`
- 검증 스크립트: `scripts/validate_v6_2_notebook.py`
- CI/로컬 smoke 실행은 `--mode smoke --use-synthetic-smoke-data`로 대규모 학습 없이 수행한다.
- full 실행은 실제 `data/train.csv`, `data/test.csv`, `data/sample_submission.csv`가 준비된 환경에서 `--mode full --data-dir data`로 수행한다.
- 현재 저장소에는 실제 `data/` 입력 파일이 포함되어 있지 않으므로, full 실행은 입력 데이터가 있는 제출 환경에서 별도 수행해야 한다.
- 이 작업 환경에는 `nbformat`, `nbclient`, `pandas`, `numpy`, `scikit-learn`이 설치되어 있지 않아 실제 노트북 실행 검증은 수행하지 못했고, 정적 계약 검사와 smoke fixture 생성 경로만 확인했다.

## 생성 파일 목록

검증 스크립트는 실행 후 `outputs/team_report_v6_2/`에서 다음 산출물을 확인한다.

- `cv_summary_v6_2.csv`
- `oof_bank_v6_2.csv`
- `prediction_bank_v6_2.csv`
- `ensemble_weights_v6_2.csv`
- `submission_team_report_v6_2_YYYYMMDD_HHMMSS.csv`

## submission 검증 결과

노트북 내부와 검증 스크립트 모두 다음 조건을 확인한다.

- 제출 파일 row 수가 `sample_submission.csv`와 동일해야 한다.
- 제출 파일 컬럼명과 컬럼 순서가 `sample_submission.csv`와 동일해야 한다.
- ID 컬럼이 있으면 ID 순서가 `sample_submission.csv`와 동일해야 한다.
- probability 컬럼에 null 값이 없어야 한다.
- probability 값은 0 이상 1 이하 범위여야 한다.

## 문헌 해석 점검 결과

- 특정 feature 수, 고정 AUC, public score, 이전 제출 후보에 대한 문장은 사용하지 않도록 정리했다.
- 문헌 기반 문장은 `(저자 또는 기관, 연도)` 형식으로 유지했다.
- 임상 해석은 원인 단정 대신 “반영할 수 있다”, “예측 신호로 해석해야 한다”, “가능성이 있다” 수준의 완화된 표현으로 정리했다.
- feature명은 현재 노트북에서 생성되는 결측 패턴 feature(`f_embryo_missing_count`, `f_embryo_all_missing`)만 예시로 남겼다.

## 남은 위험 요소

- 실제 대회 데이터가 저장소에 포함되어 있지 않아 이 감사 PR에서는 full run 산출물을 확정할 수 없다.
- smoke fixture는 실행 경로와 산출물 계약을 확인하기 위한 작은 합성 데이터이므로 실제 성능이나 feature 분포를 대표하지 않는다.
- full run 시간은 실제 데이터 크기와 실행 환경 CPU 자원에 따라 달라질 수 있다.
- 노트북은 scikit-learn tree 계열 모델을 사용하므로 패키지 버전 차이에 따라 세부 예측값이 달라질 수 있다.

## 최종 제출 전 수동 확인 항목

1. `data/train.csv`, `data/test.csv`, `data/sample_submission.csv`가 제출 환경에 있는지 확인한다.
2. `python scripts/validate_v6_2_notebook.py --mode full --data-dir data --output-dir outputs/team_report_v6_2`를 실행한다.
3. 생성된 `submission_team_report_v6_2_*.csv`의 row 수, 컬럼명, ID 순서, probability 범위를 다시 확인한다.
4. 노트북 출력의 OOF AUC와 ensemble weights를 보고서에 반영하되, 고정 public score나 외부 submission 기준으로 설명하지 않는다.
5. 최종 제출 파일이 가장 최근 timestamp의 v6.2 submission인지 확인한다.
