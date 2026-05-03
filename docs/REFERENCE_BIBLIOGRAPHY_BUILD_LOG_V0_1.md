# Reference Bibliography Build Log v0.1

## Purpose

This log documents how the draft `references.bib` file was created from the verified reference packs.

The bibliography is a draft support artifact for a bioRxiv v0.1 manuscript candidate. It is not a final public bibliography, and it does not make the preprint submission-ready.

## Inputs inspected

- `docs/VERIFIED_REFERENCE_PACK_BIORXIV_V0_1.md`
- `docs/VERIFIED_REFERENCE_PACK_BIORXIV_V0_2.md`
- `docs/CITATION_PLACEHOLDER_MAP_BIORXIV_V0_1.md`
- `docs/CITATION_PLACEHOLDER_MAP_BIORXIV_V0_2.md`
- `docs/REFERENCE_VERIFICATION_QUEUE_BIORXIV_V0_1.md`

## Included entries

| Placeholder key | BibTeX key | Inclusion rationale | Draft caveat |
| --- | --- | --- | --- |
| `REF_BRAINPEPS_DATABASE` | `brainpeps_2012` | Verified title, lead author form, year, venue, DOI. | Author list uses supplied lead-author form plus `and others`; human bibliography review required. |
| `REF_B3PDB_DATABASE` | `b3pdb_2021` | Verified title, lead author form, year, venue, DOI. | Author list uses supplied lead-author form plus `and others`; human bibliography review required. |
| `REF_B3PRED` | `b3pred_2021` | Verified title, lead author form, year, venue, DOI. | Author list uses supplied lead-author form plus `and others`; human bibliography review required. |
| `REF_BBPPRED` | `bbppred_2021` | Verified title, lead author form, year, venue, DOI. | Author list uses supplied lead-author form plus `and others`; human bibliography review required. |
| `REF_BBPPREDICT` | `bbppredict_2022` | Verified title, lead author form, year, venue, DOI. | Author list uses supplied lead-author form plus `and others`; human bibliography review required. |
| `REF_PRAUC_IMBALANCE` | `saito_rehmsmeier_2015_prauc` | Verified title, authors, year, venue, DOI. | None beyond final formatting review. |
| `REF_MCC_BINARY_CLASSIFICATION` | `chicco_jurman_2020_mcc` | Verified title, authors, year, venue, DOI. | None beyond final formatting review. |
| `REF_SCIKIT_LEARN` | `scikit_learn_2011` | Verified title, author form, year, venue, volume, pages. | No DOI was supplied in the verified pack; entry intentionally omits DOI. |
| `REF_PANDAS` | `pandas_2010` | Verified title, author, year, venue, DOI. | Proceedings metadata may need final style review. |
| `REF_MATPLOTLIB` | `matplotlib_2007` | Verified title, author, year, venue, DOI. | None beyond final formatting review. |
| `REF_PRACTICPP_IMBALANCE` | `practicpp_2024` | Verified title, lead author form, year, venue, DOI. | Author list uses supplied lead-author form plus `and others`; title may need final full-title expansion if required. |
| `REF_BBB_SHUTTLE_REVIEW` | `bbb_shuttle_review_2016` | Verified supplied authors, title, year, venue, DOI. | Author names are limited to the supplied form; final accenting/full names require human review. |
| `REF_AUGUR` | `augur_2024` | Verified title, lead author form, year, venue, DOI. | Author list uses supplied lead-author form plus `and others`; human bibliography review required. |
| `REF_BRAINPEPPASS` | `brainpeppass_2024` | Verified title, lead author form, year, venue, DOI. | Author list uses supplied lead-author form plus `and others`; human bibliography review required. |
| `REF_DEEPB3P3` | `deepb3p3_2023` | Verified supplied authors, title, year, venue, DOI. | Author names are limited to supplied form. |
| `REF_ESM_BBB_PRED` | `esm_bbb_pred_2025` | Verified title, lead author form, year, venue, DOI. | Author list uses supplied lead-author form plus `and others`; human bibliography review required. |
| `REF_B3BPFN` | `b3bpfn_2026` | Verified title, lead author form, year, venue, DOI. | Author list uses supplied lead-author form plus `and others`; human bibliography review required. |
| `REF_PERSEUCPP` | `perseucpp_2025` | Verified title, lead author form, year, venue, DOI. | Author list uses supplied lead-author form plus `and others`; human bibliography review required. |

## Deferred entries

| Placeholder key | Reason deferred | Required next action |
| --- | --- | --- |
| `REF_DATASETS_FOR_DATASETS` | DOI and final bibliographic details were not supplied in the verified pack. | Complete metadata before bibliography insertion. |
| `REF_PROTPARAM_FEATURES` | Canonical citation, year, venue, DOI/PMID/URL were not supplied. | Verify canonical feature/tool citation or decide on a web/manual entry policy. |
| `REF_PEPBENCHMARK` | Partial benchmark-standardization lead; no DOI/stable URL supplied and exact citation type is unclear. | Verify OpenReview/PDF details before use; do not make precise k-mer/homology claims without support. |
| `REF_CPP_COMPUTATIONAL_REVIEW` | Title, venue, year, and DOI supplied, but no author metadata supplied. | Add only after author metadata is provided or an approved no-author bibliography convention is chosen. |
| `REF_CPP_CLINICAL_REVIEW` | No second-pass metadata supplied. | Keep candidate-only unless later verified. |

## Boundary checks

- No PMID, URL, pages, issue, abstract, license, or permission fields were invented.
- No partial references were inserted into `references.bib`.
- Draft author forms using `and others` are explicitly marked for human bibliography review.
- The bibliography does not claim public preprint readiness.
- The bibliography does not change manuscript claims, metrics, data, figures, or result artifacts.
