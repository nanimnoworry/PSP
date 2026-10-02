<picture>
  <source media="(max-width: 640px)" srcset="./docs/assets/readme/hero-mobile.svg" />
  <img src="./docs/assets/readme/hero.svg" width="100%" alt="Fertility PSP official evidence ledger" />
</picture>

<h1 align="center">🧬 Fertility PSP</h1>

<p align="center">
  <strong>대회 제공 난임 시술 데이터 기반 임신 성공 여부 예측 연구</strong><br />
  Official project SSOT · structural missingness · OOF validation · reproducible model lineage
</p>

<p align="center">
  LG Aimers 6기 Phase2 · <a href="https://dacon.io/competitions/official/236452">DACON 공식 대회</a> · ROC-AUC
</p>

## Start Here

이 저장소는 nanimnoworry Organization의 **공식 프로젝트 기준점(SSOT)** 입니다.

- **Organization overview** — [nanimnoworry](https://github.com/nanimnoworry)
- **공식 모델 계보** — [docs/model_lineage.md](docs/model_lineage.md)
- **최종 제출 artifact identity** — [deliverables/final_submission/MANIFEST.md](deliverables/final_submission/MANIFEST.md)
- **Public Notebook sanitation provenance** — [docs/PUBLIC_NOTEBOOK_SANITIZATION.md](docs/PUBLIC_NOTEBOOK_SANITIZATION.md)

> 처음 보는 경우 이 README → model lineage → final submission manifest 순서가 가장 빠릅니다.

## Official Result

<picture>
  <source media="(max-width: 640px)" srcset="./docs/assets/readme/official-lineage-mobile.svg" />
  <img src="./docs/assets/readme/official-lineage.svg" width="100%" alt="Official lineage separating highest submitted Plan 2 from final adopted Plan 3" />
</picture>

공식 발표 기준 결과는 다음 두 문장을 분리해서 읽어야 합니다.

- **Highest submitted AUC:** 2안 · **0.74232**
- **Final adopted submission model:** 3안 · **0.74231**

3안 채택은 제출 점수 하나만으로 결정하지 않고, 모델 복잡도 · 검증 부담 · seed 변동성 · 추론 비용 · 운영 단순성을 함께 고려한 결과입니다.

<details>
<summary><strong>발표 기준 1안·2안·3안 수치 보기</strong></summary>

- **1안** — OOF 기반 boosting/ensemble baseline · 내부 OOF AUC ≈ 0.74058 · 제출 AUC 0.74213
- **2안** — feature 확장 + weighted / stacking · 내부 OOF AUC ≈ 0.74088 · 제출 AUC **0.74232**
- **3안** — OOF + Multi-Seed · 내부 OOF AUC ≈ 0.74060 · 제출 AUC 0.74231 · **최종 채택**

> 실험안별 split · seed · 전처리 조건이 달라 OOF의 미세 차이를 직접 순위화하지 않습니다.

</details>

## Research System

### Structural Missingness

IVF·DI 시술 과정 차이에 따라 배아·난자·이식 관련 결측의 의미가 달라질 수 있으므로, 단순 누락과 **시술 구조상 비해당 가능성**을 분리해 검토했습니다.

### Domain-Aware Feature Engineering

연령 · IVF/DI/ICSI · 난자/배아 수 · 이식 시점 · 기증자 정보 · 과거 시술/임신/출산 이력과 이들의 조합·비율·missing indicator를 연구했습니다.

### OOF-First Validation

단일 hold-out 하나보다 K-Fold OOF를 중심으로 비교하며, split · seed · feature contract가 다른 결과를 같은 조건처럼 취급하지 않습니다.

### Ensemble Diversity

주요 모델은 CatBoost · LightGBM · XGBoost이며, Weighted · Rank · Multi-Seed · Stacking을 비교했습니다. Rank 계열은 ROC-AUC와 calibration 특성이 다를 수 있어 LogLoss도 함께 확인했습니다.

## Artifact & Reproducibility Boundary

<picture>
  <source media="(max-width: 640px)" srcset="./docs/assets/readme/artifact-boundary-mobile.svg" />
  <img src="./docs/assets/readme/artifact-boundary.svg" width="100%" alt="Artifact boundary separating official final, post-submission reproducibility, and historical material" />
</picture>

이 저장소는 **파일명보다 artifact identity와 역할을 우선**합니다.

- **Official final** — 팀이 실제 제출·발표에 사용한 원본 identity를 hash로 기록
- **Post-submission** — 제출 이후 재현성, 실행 구조, 문헌 merge, audit
- **Historical** — 과거 중간 Notebook과 탐색 기록
- **Private follow-up** — planB의 후속 모델 연구는 공식 발표 결과와 별도 계보

Canonical raw artifact 전부를 public repository에 호스팅한다는 의미는 아닙니다. 정확한 파일명·SHA-256·Git blob identity는 [MANIFEST.md](deliverables/final_submission/MANIFEST.md)를 기준으로 합니다.

## Current Execution Surface

현재 default branch에서 재현성·실행 구조를 점검하는 주요 surface:

<pre>
00.Project_Fertility_PSP_v6.2.ipynb
00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb
scripts/validate_v6_2_notebook.py
reports/v6_2_notebook_audit.md
</pre>

이 v6.2 계열은 **post-submission reproducibility asset**이며, canonical final submission artifact와 동일 파일이라고 주장하지 않습니다.

## Repository Guide

<pre>
PSP/
├── README.md
├── 00.Project_Fertility_PSP_v6.2.ipynb
├── 00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb
├── deliverables/final_submission/
├── docs/
├── historical/
├── post_submission/
├── reports/
├── scripts/
└── tests/
</pre>

- [docs/model_lineage.md](docs/model_lineage.md) — 공식 / post-submission 계보 분리
- [post_submission/README.md](post_submission/README.md) — 제출 이후 재현성 surface
- [historical/README.md](historical/README.md) — 과거 개발 자료
- [docs/repository_map.md](docs/repository_map.md) — 저장소 역할 지도

## Related Research

- [nanimnoworry/BS](https://github.com/nanimnoworry/BS) — Plan 3 연계 모델 비교 · 5-Fold OOF · Weighted / Rank Ensemble
- planB *(private)* — 공식 제출 이후 후속 모델 연구 · bootstrap / slice 검증
- Research-Papers *(private)* — 임상·문헌 근거 · 발표자료 provenance

## Public Data Boundary

대회 원본 train.csv / test.csv는 이 public repository에 포함하지 않습니다. Default-branch public Notebook은 code-cell output과 execution count를 제거한 상태로 관리하며, source/current blob mapping은 [PUBLIC_NOTEBOOK_SANITIZATION.md](docs/PUBLIC_NOTEBOOK_SANITIZATION.md)에 기록합니다.

**Scope boundary:** 해커톤·연구 결과이며 실제 의료 환경의 임상 검증, 진단 또는 의사결정 성능을 주장하지 않습니다. **Not a clinical diagnostic or medical decision system.**

---

### License and Rights

**Public view · no public reuse license.**  
별도 서면 허가 없는 재사용 · 수정 · 재배포를 허용하지 않습니다. 대회 데이터, 예측/제출 산출물, 제3자 시각 자료, 라이브러리와 인용 문헌은 각 권리·조건을 따릅니다.

[LICENSE](LICENSE) · [RIGHTS.md](RIGHTS.md) · [CONTRIBUTORS.md](CONTRIBUTORS.md)
