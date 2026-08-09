<div align="center">

# 🧬 Fertility PSP

### 난임 환자 대상 임신 성공 여부 예측 AI 프로젝트

<p>
  <img src="https://img.shields.io/badge/Task-Binary%20Classification-2563EB?style=flat-square" alt="Task">
  <img src="https://img.shields.io/badge/Metric-ROC--AUC-7C3AED?style=flat-square" alt="Metric">
  <img src="https://img.shields.io/badge/Models-CatBoost%20%7C%20LightGBM%20%7C%20XGBoost-059669?style=flat-square" alt="Models">
  <img src="https://img.shields.io/badge/Final-Plan%203%20%C2%B7%200.74231-EA580C?style=flat-square" alt="Final result">
</p>

난임 시술 데이터를 이용해 임신 성공 여부를 예측한 팀 프로젝트입니다.  
시술 유형에 따른 결측 구조와 임상 변수를 살펴보고, OOF 검증과 앙상블을 거쳐 최종 모델을 선정했습니다.

</div>

---

## 최종 결과

| 항목 | 결과 |
|---|---:|
| 평가 지표 | ROC-AUC |
| 1안 | OOF 기반 기초 모델 · 제출 `0.74213` |
| 2안 | Feature 확장 + Ensemble / Stacking · **제출 `0.74232`** |
| 3안 | OOF + Multi-Seed · 제출 `0.74231` |
| 최고 제출 점수 | **2안 · 0.74232** |
| 최종 채택 모델 | **3안 · 0.74231** |

2안이 제출 점수는 조금 더 높았지만, 최종 발표에서는 모델 복잡도와 검증 부담, seed 변동성, 추론 비용까지 함께 고려해 3안을 최종 모델로 선택했습니다.

## 모델 흐름

```mermaid
flowchart LR
    A[1안<br/>기초 성능 수립<br/>0.74213]
    B[2안<br/>Feature 확장 + Stacking<br/>0.74232]
    C[3안<br/>OOF + Multi-Seed<br/>0.74231]
    D[Final<br/>Plan 3]
    R[Post-submission<br/>planB]

    A --> B --> C --> D
    D --> R
```

세부 계보는 [`docs/model_lineage.md`](docs/model_lineage.md)에 정리되어 있습니다.

## 주요 연구 내용

### 구조적 결측

IVF와 DI는 시술 과정이 다르기 때문에 같은 결측값이라도 의미가 다를 수 있습니다. 특히 DI에서 배아·난자·이식 관련 값이 함께 비는 패턴을 단순 누락으로 처리하지 않고, 시술 과정에서 해당 정보가 존재하지 않는 구조적 결측으로 해석했습니다.

### Feature Engineering

연령, 시술 유형, 난자·배아 수, 이식 시점, 기증자 정보, 과거 시술 이력을 기본 축으로 사용했습니다. 여기에 연령 구간, 시술별 조합 변수, 배아·난자 관련 비율과 상호작용 변수를 추가해 성능 변화를 확인했습니다.

### OOF와 앙상블

주요 모델은 `CatBoost`, `LightGBM`, `XGBoost`였습니다. 단일 hold-out보다 K-Fold OOF를 중심으로 비교했고, 다음 조합을 함께 실험했습니다.

- Weighted Ensemble
- Rank Ensemble
- Multi-Seed Ensemble
- Stacking

Rank 기반 조합은 ROC-AUC를 높이는 데 도움이 될 수 있지만 확률값의 보정 성능은 달라질 수 있어 LogLoss도 함께 확인했습니다.

## 발표 기준 성능

| 실험안 | 전략 | 내부 OOF AUC | 제출 AUC | 역할 |
|---|---|---:|---:|---|
| **1안** | boosting 비교 + OOF ensemble | ≈ `0.74058` | `0.74213` | 기초 성능 수립 |
| **2안** | feature 확장 + weighted / stacking | ≈ `0.74088` | **`0.74232`** | 최고 제출 점수 |
| **3안** | OOF + Multi-Seed | ≈ `0.74060` | `0.74231` | **최종 채택** |

내부 OOF는 실험안별 split·seed·전처리 조건이 다를 수 있어 아주 작은 차이를 직접적인 순위로 해석하지 않습니다.

## 최종 제출 자료

팀이 최종 제출한 Notebook과 발표자료의 파일명·해시는 [`deliverables/final_submission/MANIFEST.md`](deliverables/final_submission/MANIFEST.md)에 기록했습니다.

과거 개발 과정의 Notebook은 `historical/notebooks/`, 이미지와 캡처 자료는 `historical/assets/`에 보존합니다. 현재 루트의 v6.2 Notebook은 제출 이후 재현성과 실행 구조를 정리한 후속 작업이며, 공식 최종 제출본을 대체하지 않습니다.

## Repository

```text
PSP/
├── README.md
├── 00.Project_Fertility_PSP_v6.2.ipynb
├── 00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb
├── deliverables/final_submission/
├── docs/
├── historical/
│   ├── notebooks/
│   └── assets/
├── post_submission/
├── reports/
├── scripts/
└── tests/
```

- [`docs/model_lineage.md`](docs/model_lineage.md) — 공식 모델 계보
- [`deliverables/final_submission/MANIFEST.md`](deliverables/final_submission/MANIFEST.md) — 최종 제출 artifact 기록
- [`post_submission/README.md`](post_submission/README.md) — v6.x 후속 작업
- [`historical/README.md`](historical/README.md) — 과거 개발 자료

## Related Repositories

| Repository | 내용 |
|---|---|
| [`BS`](https://github.com/nanimnoworry/BS) | 3안과 연결된 모델 비교·OOF·앙상블 연구 |
| `planB` | 공식 발표 이후의 추가 모델 연구와 강건성 검증 |
| `Research-Papers` | 임상·문헌 근거와 발표자료 아카이브 |

연구 결과는 실제 의료 판단이나 임상 의사결정을 위한 모델이 아닙니다.
