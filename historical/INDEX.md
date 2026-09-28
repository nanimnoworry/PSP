# Historical Artifact Index

이 문서는 PSP 루트 정리와 공개 Notebook sanitation 이후에도 **historical artifact의 출처 identity와 현재 공개본 identity를 함께 추적**하기 위한 색인입니다.

## Historical notebooks

| 현재 경로 | Pre-sanitization source blob | Current public blob |
|---|---|---|
| `notebooks/00.Project_Fertility_PSP.ipynb` | `ae7d899ab6f674657e497ce3992c7ba6037a7c0c` | `9fca4572fe46083250d5e68f3c5c06b4e2c7d531` |
| `notebooks/00.Project_Fertility_PSP_v3.ipynb` | `741e6891d1737322618bf786a8bdd8ca2d75b439` | `801bd02918553f4637fcca8b23f1bf4f259f5aab` |
| `notebooks/00.Project_Fertility_PSP_v4.ipynb` | `b1e5e174d6ed252de3ebb8a3c9a2ce44c47ad422` | `228acf496bf2841f5008ec343e7138d8432ca7a0` |
| `notebooks/00.Project_Fertility_PSP_v5.ipynb` | `e6eec0a6512bfa20fca2b9a4eaf700d1b5cdad87` | `e0a2946304470cf41a9d84e45f052eefbf44d440` |
| `notebooks/00.Project_Fertility_PSP_v5.1.ipynb` | `a464aae3dd3a7233e89c80247b1f4815015b6955` | `4cbd7eb2d38d0fa03d9e3637fb98cc7de4b21f25` |
| `notebooks/00.Project_Fertility_PSP_v6_experimental.ipynb` | `0254892e84981d3f9174ea18c18e5f298bf86dde` | `0254892e84981d3f9174ea18c18e5f298bf86dde` |
| `notebooks/00_Project_Fertility_PSP_v6_3.ipynb` | `6313449158d2c3ec641f0d7d94192451b08a451e` | `4b845f67bbdd7fbb69f172ec47f699b74099f92b` |
| `notebooks/prototype_PSP_Full_Code .ipynb` | `761a551440bb47140fbaefccb92d2961ea35f005` | `c784af93427d6f416c23b527e63cec836de72326` |
| `notebooks/second_PSP_Full_Code.ipynb` | `5b50cca14ef2e1268e43f748141a0eec7c244cea` | `60df54a109ef34417267371e8daa9e59f25313d5` |

변경된 current public blob은 **코드/markdown을 유지하고 code-cell output과 execution count를 제거한 공개본**입니다.  
세부 기록: [Public Notebook Sanitization](../docs/PUBLIC_NOTEBOOK_SANITIZATION.md)

## Historical visual assets

| 현재 경로 | Git blob SHA |
|---|---|
| `assets/second_PSP_Full_Code.png` | `daaf2e2e6ddb3f263fb273de8d6eb4dedf0f4632` |
| `assets/스크린샷 2026-05-27 191231.png` | `0456b489c3769bf567e9a73db167be66dc5d12f4` |

## Identity rule

Pre-sanitization source blob은 과거 연구 artifact의 provenance 식별자이고, current public blob은 default branch에서 공개되는 sanitized copy입니다.

특히 historical `00.Project_Fertility_PSP_v5.ipynb`의 pre-sanitization source blob과 팀 제공 canonical final `00.Project_Fertility_PSP_v5.ipynb`는 파일명이 같아도 서로 다른 artifact입니다.

Canonical final artifact identity는 다음 문서를 기준으로 합니다.

[`../deliverables/final_submission/MANIFEST.md`](../deliverables/final_submission/MANIFEST.md)
