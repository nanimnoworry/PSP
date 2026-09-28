# Public Notebook Sanitization Record

This document records the default-branch sanitation applied to public notebooks on 2026-09-28.

## Why

Several public notebooks retained executed cell outputs containing competition-data row previews, including synthetic row identifiers such as `TRAIN_...` / `TEST_...` and domain columns.  
The repository intentionally does **not** publish the competition `train.csv` / `test.csv` files, so the default branch was aligned with that boundary.

## What changed

For public notebook copies on the default branch:

- code and markdown cells were preserved;
- code-cell `outputs` were cleared;
- code-cell `execution_count` values were cleared;
- notebook source logic was not intentionally changed by the sanitation step.

This is a **public-surface sanitation**, not a claim that prior Git history was rewritten.

## PSP notebook identity map

| Notebook | Pre-sanitization source blob | Current public blob | Status |
|---|---|---|---|
| `00.Project_Fertility_PSP_v6.2.ipynb` | `3220a9158ab3ee27dd06ae166488b8a1c0a9d62c` | `3220a9158ab3ee27dd06ae166488b8a1c0a9d62c` | already clean |
| `00.Project_Fertility_PSP_v6.2_final_literature_merged.ipynb` | `0cbd1e93d08121fced0fb07e1a2122c58b608b1b` | `fe36190a2a6d9d540eaea6e3de35c95dee9791c4` | outputs cleared |
| `historical/notebooks/00.Project_Fertility_PSP.ipynb` | `ae7d899ab6f674657e497ce3992c7ba6037a7c0c` | `9fca4572fe46083250d5e68f3c5c06b4e2c7d531` | outputs cleared |
| `historical/notebooks/00.Project_Fertility_PSP_v3.ipynb` | `741e6891d1737322618bf786a8bdd8ca2d75b439` | `801bd02918553f4637fcca8b23f1bf4f259f5aab` | outputs cleared |
| `historical/notebooks/00.Project_Fertility_PSP_v4.ipynb` | `b1e5e174d6ed252de3ebb8a3c9a2ce44c47ad422` | `228acf496bf2841f5008ec343e7138d8432ca7a0` | outputs cleared |
| `historical/notebooks/00.Project_Fertility_PSP_v5.1.ipynb` | `a464aae3dd3a7233e89c80247b1f4815015b6955` | `4cbd7eb2d38d0fa03d9e3637fb98cc7de4b21f25` | outputs cleared |
| `historical/notebooks/00.Project_Fertility_PSP_v5.ipynb` | `e6eec0a6512bfa20fca2b9a4eaf700d1b5cdad87` | `e0a2946304470cf41a9d84e45f052eefbf44d440` | outputs cleared |
| `historical/notebooks/00.Project_Fertility_PSP_v6_experimental.ipynb` | `0254892e84981d3f9174ea18c18e5f298bf86dde` | `0254892e84981d3f9174ea18c18e5f298bf86dde` | already clean |
| `historical/notebooks/00_Project_Fertility_PSP_v6_3.ipynb` | `6313449158d2c3ec641f0d7d94192451b08a451e` | `4b845f67bbdd7fbb69f172ec47f699b74099f92b` | outputs cleared |
| `historical/notebooks/prototype_PSP_Full_Code .ipynb` | `761a551440bb47140fbaefccb92d2961ea35f005` | `c784af93427d6f416c23b527e63cec836de72326` | outputs cleared |
| `historical/notebooks/second_PSP_Full_Code.ipynb` | `5b50cca14ef2e1268e43f748141a0eec7c244cea` | `60df54a109ef34417267371e8daa9e59f25313d5` | outputs cleared |

## BS notebook identity map

| Notebook | Pre-sanitization source blob | Current public blob | Status |
|---|---|---|---|
| `3안 모델.ipynb의 사본` | `5f3352bcf8ff1d326e6cbb532e5fc4d4b78285b6` | `e633a84131bb4c5cf9aa38e3309c8878b2d062b0` | outputs cleared |

## Verification

After sanitation, every public notebook listed above was re-read from the default branch and checked for:

- remaining code-cell outputs: **0**
- non-null execution counts: **0**
- `TRAIN_` / `TEST_` identifiers inside outputs: **0**
- target-column text inside outputs: **0**

## Provenance boundary

The pre-sanitization blob SHAs above are retained as provenance identifiers.  
Because this operation did not rewrite repository history, older commits/blob objects may still contain the prior executed-output state.

If a competition license or data-removal requirement demands **complete historical erasure**, that is a separate destructive operation requiring Git history rewrite and any necessary platform cache/purge procedure. It should not be conflated with normal repository cleanup.

## Canonical artifact boundary

The team-supplied final submission artifact hashes in `deliverables/final_submission/MANIFEST.md` remain the identity source for the actual supplied final materials.  
A sanitized public notebook copy is not claimed to be byte-identical to those original artifacts.
