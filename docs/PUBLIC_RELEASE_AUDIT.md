# PSP Public Release Audit

> Reviewed: 2026-08-09  
> Status: **NOT READY FOR A DIRECT PRIVATE → PUBLIC SWITCH**

This audit records the current public-release boundary for `nanimnoworry/PSP`. It is intentionally conservative: the repository is the project's provenance/SSOT archive, so preserving research history is more important than making the existing Git history public in place.

## Scope reviewed

- current repository root and recursive tree
- active root notebooks
  - `00.Project_Fertility_PSP_v6.2.ipynb`
  - `00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb`
- representative historical notebook output, including `historical/notebooks/00.Project_Fertility_PSP_v5.ipynb`
- obvious credential-pattern checks
- repository metadata / license state

## Findings

### Current working tree

The current branch does **not** expose raw `train.csv`, `test.csv`, or a current raw competition-data directory at the repository root/tree inspected during this audit.

The two active v6.2 notebooks use a relative data contract such as `../data` rather than a personal Google Drive path. Direct inspection did not find Colab `userId` or `authorship_tag` metadata in these two active notebooks.

### Historical notebook output

`historical/notebooks/00.Project_Fertility_PSP_v5.ipynb` contains rendered/sample output from competition training rows, including IDs such as `TRAIN_000000` and associated feature values.

That means the current repository should **not** be made public as-is until competition-data redistribution terms are verified and historical outputs are sanitized or excluded from a clean public copy.

This is a release-safety decision, not a claim that the existing private archive is improper.

### Historical assets

`historical/assets/` contains legacy screenshots/images. They are valid provenance artifacts, but they have not been cleared here for personal information, local paths, account names, or other screen-only details. They remain a public-release blocker until reviewed or omitted from a public snapshot.

### Secrets and local configuration

No obvious `api_key`, `password`, or similar credential signature was identified in the files directly inspected for this audit. This is **not** equivalent to a full secret scan of every reachable Git object.

The current repository also has no root `.gitignore`, so a future public-facing copy should add explicit protection against raw data, `.env` files, local caches, notebook checkpoints, generated models, and OS/editor artifacts.

### License

The repository currently has no declared GitHub license. Before public distribution, the team should decide what code/document license is appropriate. Dataset rights, competition rules, and third-party paper/PDF rights are separate from a software license and must not be implied by it.

### Git history

A visibility switch would expose the repository's reachable Git history, not only the cleaned current tree. This audit did not prove that every historical Git object is safe for public redistribution.

For that reason, rewriting or force-cleaning this provenance repository merely to make it public is **not recommended**.

## Recommended publication model

Keep this repository **Private** as the canonical provenance / official-project SSOT, and publish a **clean-history sanitized snapshot** as the public portfolio artifact.

A public copy should include only intentionally selected materials, for example:

```text
fertility-prediction-public/
├── README.md
├── notebooks/
│   └── official_modeling_sanitized.ipynb
├── docs/
│   ├── model_lineage.md
│   ├── research_credit.md
│   └── methodology.md
├── src/
├── .gitignore
└── LICENSE
```

Do **not** copy raw competition data, rendered raw training rows, personal Colab/Drive metadata, private screenshots, downloaded copyrighted paper PDFs, secret/local configuration, or the private repository's historical Git objects into the public repository.

## Official-result boundary

The public narrative must preserve the project's existing result distinction:

- **Highest submitted AUC:** Plan 2 — `0.74232`
- **Final adopted model:** Plan 3 — `0.74231`

The public showcase must not rewrite this distinction or promote a post-submission experiment as the official final model.

## Decision

```text
DIRECT_PUBLIC_SWITCH = BLOCKED_FOR_NOW
PRIVATE_PROVENANCE_REPO = KEEP
CLEAN_PUBLIC_SNAPSHOT = RECOMMENDED
```

No repository visibility was changed by this audit.
