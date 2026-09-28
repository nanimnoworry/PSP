# Final Submission Artifact Manifest

> Canonical record of the files supplied by the team as the **actual final project/submission materials**.
>
> A same-named file already present in GitHub is **not** treated as identical unless its hash matches.

## Canonical artifact set

The following hashes were calculated from the files supplied directly by the team on 2026-08-08.

| Artifact | Size (bytes) | SHA-256 | Git blob SHA-1 | Role |
|---|---:|---|---|---|
| `00.Project_Fertility_PSP_v5.ipynb` | 1,312,963 | `b8a1c7da27ee8f1199d16a17c1d2ae56bbf47421cebc8113a463dcc2a7438265` | `97b1d34ed14e7e5f07ba1d25a07dd7d310faaf23` | integrated project/model notebook |
| `(예측모델_결과물)_조안_Project_Fertility_PSP_v5.ipynb` | 1,312,963 | `b8a1c7da27ee8f1199d16a17c1d2ae56bbf47421cebc8113a463dcc2a7438265` | `97b1d34ed14e7e5f07ba1d25a07dd7d310faaf23` | submitted model-result copy; byte-identical to the v5 notebook above |
| `01_EDA_basic.ipynb` | 744,320 | `309b3bd18b938b2d540eaa674852b5850cef443024d100935aecb56245e65dfb` | `7b4ec6b16faedde5d0369d7af2182b96ab84600a` | EDA |
| `02_preprocessing_baseline.ipynb` | 441,079 | `222ad0845fdf05a0b7f4db9e3b3235158a6961ec7f3b0d17305c18c84ad0f94b` | `ce771783d69d91bafe85efdb976e19d748b5980f` | preprocessing / baseline |
| `03_rank1_strategy_local.ipynb` | 83,874 | `97e663fa37417efa09383f9d45caae9fc2d5ff3046f7d06a08a9878a82fe6d98` | `16d5548d767a0c347fdd02278e77c6a5648c8213` | local OOF / ensemble workflow |
| `04_modeling_AUC_v3.ipynb` | 141,561 | `f339d4a8c8bfd7a928eb999cc7b170227d46704f1635850e33f3e2247a46bd26` | `244b2d4659eab498cd8e73a005f68c1a24b5f998` | modeling / AUC experiments |
| `(발표자료)난임_환자_대상_임신_성공_여부_예측_AI_프로젝트-v4.pdf` | 13,200,289 | `57f9317f079da50542a948a68ddfafe70143a10f79a0b911deffe8ea1da8640e` | `6e639da18189124422e85fb15c9ec6c0c44f4fc3` | final presentation |

## Important identity check

The older same-named notebook that had been stored in the GitHub repository is now preserved at:

```text
historical/notebooks/00.Project_Fertility_PSP_v5.ipynb
```

Its Git blob SHA is:

```text
e6eec0a6512bfa20fca2b9a4eaf700d1b5cdad87
```

The canonical team-supplied final artifact has Git blob SHA:

```text
97b1d34ed14e7e5f07ba1d25a07dd7d310faaf23
```

Therefore the historical GitHub notebook and the supplied final artifact are **different versions**, despite sharing the same filename.

The historical archive move reused the original blob SHA, so this distinction remains verifiable after repository cleanup.

## Preservation policy

1. This manifest is the source of truth for artifact identity.
2. Existing historical notebooks are not deleted just because a newer or canonical artifact exists.
3. Contest/final-presentation artifacts and post-submission research are documented as separate lineages.
4. Public/leaderboard score, OOF score, and final-adoption status are recorded separately.
5. Exact raw artifacts should only be copied into this directory when byte identity can be preserved; a recreated or reformatted file must never be presented as the original.

## Final presentation result summary

The final presentation compared three experiment plans:

| Plan | Main idea | Internal OOF AUC | Submission AUC | Historical role |
|---|---|---:|---:|---|
| 1안 | core boosting-model comparison / OOF ensemble baseline | ≈ `0.74058` | `0.74213` | baseline / screening |
| 2안 | richer feature expansion + ensemble/stacking | ≈ `0.74088` | **`0.74232`** | highest submitted AUC / upper-bound benchmark |
| 3안 | OOF + Multi-Seed stability | ≈ `0.74060` | `0.74231` | **final adopted submission model** |

The team presentation explicitly chose **3안 as the final adopted submission model** despite 2안 having a marginally higher submission AUC, citing the balance of performance, scalability, latency/compute burden, pipeline complexity, leakage/overfitting risk, and score stability.

See [`../../docs/model_lineage.md`](../../docs/model_lineage.md) for the lineage view.
