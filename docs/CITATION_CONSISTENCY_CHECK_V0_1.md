# Citation Consistency Check v0.1

## Purpose

This check verifies citation placeholders in the preprint draft and manuscript candidate against `references.bib`.

## Materials inspected

- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`
- `references.bib`
- `docs/REFERENCE_BIBLIOGRAPHY_BUILD_LOG_V0_1.md`

## Result

Status: **Pass**

No citation key mismatch was found. No citation fix was required.

## Citation keys used in manuscript files

- `augur_2024`
- `b3bpfn_2026`
- `b3pdb_2021`
- `b3pred_2021`
- `bbb_shuttle_review_2016`
- `bbppred_2021`
- `bbppredict_2022`
- `brainpeppass_2024`
- `brainpeps_2012`
- `chicco_jurman_2020_mcc`
- `deepb3p3_2023`
- `esm_bbb_pred_2025`
- `matplotlib_2007`
- `pandas_2010`
- `perseucpp_2025`
- `practicpp_2024`
- `saito_rehmsmeier_2015_prauc`
- `scikit_learn_2011`

## Checks performed

| Check | Result | Note |
| --- | --- | --- |
| Every citation key in `PREPRINT_DRAFT_V0_1.md` exists in `references.bib` | Pass | All used keys are present. |
| Every citation key in `PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md` exists in `references.bib` | Pass | All used keys are present. |
| No unverified/partial references inserted | Pass | Deferred keys are absent from manuscript citation placeholders. |
| No citation key appears without intended support | Pass with human-review caveat | Keys align with background, related-work, methods, software, metric, or adjacent benchmark-context roles in the citation maps. |
| `references.bib` does not contain unverified references | Pass with draft-author caveat | Entries are sourced from verified packs; several use supplied lead-author forms plus `and others`. |
| Deferred references remain deferred | Pass | `REF_DATASETS_FOR_DATASETS`, `REF_PROTPARAM_FEATURES`, `REF_PEPBENCHMARK`, `REF_CPP_COMPUTATIONAL_REVIEW`, and `REF_CPP_CLINICAL_REVIEW` are not cited or included in `references.bib`. |

## Deferred references not inserted

- `REF_DATASETS_FOR_DATASETS`
- `REF_PROTPARAM_FEATURES`
- `REF_PEPBENCHMARK`
- `REF_CPP_COMPUTATIONAL_REVIEW`
- `REF_CPP_CLINICAL_REVIEW`

## Remaining caveat

This check confirms key consistency, not final reference formatting. Human bibliography review remains required before public posting.
