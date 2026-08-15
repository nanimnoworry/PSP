<div align="center">

# 🧬 Fertility PSP

### 난임 환자 대상 임신 성공 여부 예측 AI 프로젝트

<p>
  <img src="https://img.shields.io/badge/Task-Binary%20Classification-2563EB?style=flat-square" alt="Task">
  <img src="https://img.shields.io/badge/Metric-ROC--AUC-7C3AED?style=flat-square" alt="Metric">
  <img src="https://img.shields.io/badge/Models-CatBoost%20%7C%20LightGBM%20%7C%20XGBoost-059669?style=flat-square" alt="Models">
  <img src="https://img.shields.io/badge/Final-Plan%203%20%C2%B7%200.74231-EA580C?style=flat-square" alt="Final result">
</p>

난임 시술 데이터 기반 임신 성공 여부 예측 · 구조적 결측 · OOF 검증 · 앙상블

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

**채택 기준:** 제출 점수 단독 최적화 제외 · 모델 복잡도 · 검증 부담 · seed 변동성 · 추론 비용

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

공식 계보: [`docs/model_lineage.md`](docs/model_lineage.md)

## 주요 연구 내용

### 구조적 결측

IVF·DI 시술 과정 차이에 따른 결측 의미 분리.  
DI의 배아·난자·이식 관련 동시 결측은 단순 누락이 아닌 **시술 구조상 비해당**으로 처리.

### Feature Engineering

**기본 축:** 연령 · 시술 유형 · 난자/배아 수 · 이식 시점 · 기증자 정보 · 과거 시술 이력  
**확장:** 연령 구간 · 시술 조합 · 배아/난자 비율 · 상호작용 변수

### OOF와 앙상블

**주요 모델:** `CatBoost` · `LightGBM` · `XGBoost`  
**검증:** K-Fold OOF 중심  
**조합:** Weighted · Rank · Multi-Seed · Stacking

Rank 기반 조합은 ROC-AUC와 확률 보정 특성이 다를 수 있어 LogLoss 병행 확인.

## 발표 기준 성능

| 실험안 | 전략 | 내부 OOF AUC | 제출 AUC | 역할 |
|---|---|---:|---:|---|
| **1안** | boosting 비교 + OOF ensemble | ≈ `0.74058` | `0.74213` | 기초 성능 수립 |
| **2안** | feature 확장 + weighted / stacking | ≈ `0.74088` | **`0.74232`** | 최고 제출 점수 |
| **3안** | OOF + Multi-Seed | ≈ `0.74060` | `0.74231` | **최종 채택** |

**OOF 비교 주의:** 실험안별 split · seed · 전처리 조건 차이. 미세 점수 차이의 직접 순위화 제외.

## 최종 제출 자료

공식 제출 Notebook·발표자료 파일명/SHA256: [`deliverables/final_submission/MANIFEST.md`](deliverables/final_submission/MANIFEST.md)

- `historical/notebooks/` — 과거 개발 Notebook
- `historical/assets/` — 이미지·캡처 자료
- 루트 v6.2 Notebook — 제출 이후 재현성·실행 구조 정비본, 공식 최종 제출본과 구분

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
- [`deliverables/final_submission/MANIFEST.md`](deliverables/final_submission/MANIFEST.md) — 최종 제출 artifact
- [`post_submission/README.md`](post_submission/README.md) — v6.x 후속 작업
- [`historical/README.md`](historical/README.md) — 과거 개발 자료

## Related Repositories

| Repository | 범위 |
|---|---|
| [`BS`](https://github.com/nanimnoworry/BS) | 3안 연계 모델 비교 · OOF · 앙상블 |
| `planB` | 공식 발표 이후 후속 모델 연구 · 강건성 검증 |
| `Research-Papers` | 임상·문헌 근거 · 발표자료 아카이브 |

**용도 제한:** 임상 의사결정용 모델 아님.

---

## License and Rights

**Public view · no public reuse license.**  
별도 서면 허가 없는 재사용 · 수정 · 재배포 불가. 대회 데이터, 예측/제출 산출물, 스크린샷, 의존 라이브러리, 인용 문헌은 각 권리·조건 적용.

[LICENSE](LICENSE) · [RIGHTS.md](RIGHTS.md) · [CONTRIBUTORS.md](CONTRIBUTORS.md)
