# Citation Insertion Changelog v0.1

## Purpose

This changelog records citation-placeholder insertion into `docs/PREPRINT_DRAFT_V0_1.md`.

Only keys present in `references.bib` were inserted. No partial references, unverified references, final rendered reference text, or new scientific claims were added.

## Inserted citation groups

| Manuscript area | Citation keys inserted | Reason | Boundary note |
| --- | --- | --- | --- |
| Introduction / BBB background | `bbb_shuttle_review_2016` | Supports broad BBB shuttle peptide and brain-delivery framing. | Background only; not Permea validation. |
| Related/dataset context in introduction | `brainpeps_2012`, `b3pdb_2021`, `b3pred_2021`, `bbppred_2021`, `bbppredict_2022` | Supports BBB peptide database and predictor lineage context. | Comparator/source context only; no superiority claim. |
| Feature representation | `b3pred_2021`, `bbppred_2021`, `bbppredict_2022` | Supports sequence-derived BBB peptide predictor context. | Does not claim biological mechanism. |
| Evaluation policy | `saito_rehmsmeier_2015_prauc`, `chicco_jurman_2020_mcc`, `scikit_learn_2011` | Supports PR-AUC/MCC interpretation and software implementation. | Does not validate benchmark generalization. |
| Output/software artifacts | `pandas_2010`, `matplotlib_2007`, `scikit_learn_2011` | Supports software/tooling citations. | Software support only. |
| Related work | `augur_2024`, `brainpeppass_2024`, `deepb3p3_2023`, `esm_bbb_pred_2025`, `b3bpfn_2026`, `perseucpp_2025`, `practicpp_2024` | Supports modern BBB predictor and adjacent CPP benchmark landscape. | No SOTA, robust-generalization, or direct-validation claim. |
| Leakage/limitations context | `practicpp_2024`, `perseucpp_2025` | Supports adjacent benchmark-hygiene and CPP evaluation caution. | Adjacent context only; current leakage findings remain repo-audit findings. |

## References intentionally not inserted

- `REF_DATASETS_FOR_DATASETS` / `datasets_for_datasets` — not present in `references.bib`.
- `REF_PROTPARAM_FEATURES` — not present in `references.bib`.
- `REF_PEPBENCHMARK` — deferred partial lead, not present in `references.bib`.
- `REF_CPP_COMPUTATIONAL_REVIEW` — deferred because author metadata was not supplied, not present in `references.bib`.

## Claim-boundary check

- No metric values were changed.
- No biological or wet-lab validation claim was added.
- No leakage-free or robust-generalization claim was added.
- No public preprint-ready claim was added.
