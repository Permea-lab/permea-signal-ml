# Preprint Metadata and Reference Gap Checklist v0.1

## Purpose

This checklist identifies metadata, reference, disclosure, dataset/legal, and supplement/export gaps that must be closed before a possible bioRxiv v0.1 posting.

This document does not submit the preprint, does not finalize author metadata, does not add fabricated references, and does not make the public preprint ready. Public preprint status remains **Not yet** until the gaps below are closed, explicitly caveated, or intentionally deferred where safe.

## Current preprint readiness status

Status: **Not yet**

The scientific manuscript draft exists, the v0.1 evidence package exists, the artifact traceability package exists, and the first leakage audit has been reflected in the manuscript and evidence documentation. However, metadata, formal references, disclosure statements, dataset/legal status, and supplement/export packaging remain incomplete.

Reference search and verification planning is tracked in `docs/REFERENCE_SEARCH_PLAN_BIORXIV_V0_1.md`. That plan defines search categories, query candidates, and verification criteria; it does not add final citations.

The current literature-survey-derived candidate landscape is tracked in `docs/LITERATURE_SURVEY_SOURCE_LANDSCAPE_V0_1.md`, and the unverified candidate queue is tracked in `docs/REFERENCE_VERIFICATION_QUEUE_BIORXIV_V0_1.md`.

The first verified reference pack has been prepared in `docs/VERIFIED_REFERENCE_PACK_BIORXIV_V0_1.md`, with insertion planning in `docs/CITATION_PLACEHOLDER_MAP_BIORXIV_V0_1.md`. The second verified reference pack has been prepared in `docs/VERIFIED_REFERENCE_PACK_BIORXIV_V0_2.md`, with insertion planning in `docs/CITATION_PLACEHOLDER_MAP_BIORXIV_V0_2.md`. A draft `references.bib` and build log now exist, but final human bibliography review and manuscript citation consistency review remain open. Public preprint status remains **Not yet**.

## Metadata checklist

| Item | Current status | Evidence/source | Required before bioRxiv? | Owner placeholder | Action required | Status |
|---|---|---|---|---|---|---|
| Final author list | Placeholder only | `docs/PREPRINT_DRAFT_V0_1.md`; `docs/PREPRINT_ASSEMBLY_V0_1.md` | Yes | `OWNER_METADATA` | Human operator must provide final author names. | Open |
| Author order | Unspecified | No final author metadata found | Yes | `OWNER_METADATA` | Human operator must confirm order. | Open |
| Affiliations | Placeholder only | `docs/PREPRINT_DRAFT_V0_1.md`; `docs/PREPRINT_ASSEMBLY_V0_1.md` | Yes | `OWNER_METADATA` | Human operator must provide exact affiliations. | Open |
| Corresponding author | Placeholder only | `docs/PREPRINT_DRAFT_V0_1.md`; `docs/PREPRINT_ASSEMBLY_V0_1.md` | Yes | `OWNER_METADATA` | Human operator must identify corresponding author. | Open |
| Corresponding email | Missing | No email found in inspected preprint docs | Yes | `OWNER_METADATA` | Human operator must provide approved email. | Open |
| ORCID IDs | Missing | No ORCID metadata found | If used | `OWNER_METADATA` | Add only if provided by authors. | Open |
| Author contributions | Placeholder | `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` | Yes if journal/preprint norms require | `OWNER_DISCLOSURE` | Draft using author-approved contribution roles only. | Open |
| Keywords | Draft set available | `docs/PREPRINT_ASSEMBLY_V0_1.md`; checklist | Yes | `OWNER_METADATA` | Confirm final keyword list. | Partially drafted |
| Subject area/category | Placeholder | `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` | Yes | `OWNER_METADATA` | Select bioRxiv category/subject area manually. | Open |
| Version date | Placeholder | `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` | Yes | `OWNER_METADATA` | Set only at final export. | Open |
| Abstract finalization | Drafted | `docs/PREPRINT_DRAFT_V0_1.md` | Yes | `OWNER_EDITORIAL` | Final consistency pass after references and metadata. | Drafted |

## Disclosure checklist

| Item | Current status | Evidence/source | Required before bioRxiv? | Owner placeholder | Action required | Status |
|---|---|---|---|---|---|---|
| Acknowledgements | Missing | No final acknowledgement text found | Usually yes if applicable | `OWNER_DISCLOSURE` | Add only operator-approved acknowledgement text. | Open |
| Funding statement | Placeholder | `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` | Yes | `OWNER_DISCLOSURE` | Human operator must provide funding or no-funding statement. | Open |
| Competing interests / conflict of interest | Placeholder | `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` | Yes | `OWNER_DISCLOSURE` | Human operator must provide exact statement. | Open |
| Ethics statement | Placeholder, if applicable | `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` | If applicable | `OWNER_DISCLOSURE` | Determine whether non-human-subject computational work needs a statement. | Open |
| Data availability statement | Placeholder | Checklist and dataset docs | Yes | `OWNER_DATA_LEGAL` | Draft only after dataset redistribution status is resolved or caveated. | Open |
| Code availability statement | Placeholder | Checklist; repo URL exists locally but final public URL/status not finalized here | Yes | `OWNER_METADATA` | Confirm repository URL, branch/tag, and release/archive policy. | Open |
| License statement | Incomplete for data | `LICENSE`; `data/README.md`; dataset checklist | Yes | `OWNER_DATA_LEGAL` | Separate code license from dataset license/redistribution status. | Open |

## Dataset/legal checklist

| Item | Current status | Evidence/source | Required before bioRxiv? | Owner placeholder | Action required | Status |
|---|---|---|---|---|---|---|
| Code license | Repository `LICENSE` exists | `LICENSE` | Yes | `OWNER_DATA_LEGAL` | Confirm whether Apache-2.0 applies to code/docs and how to state it. | Present, needs statement |
| Dataset attribution | Unconfirmed | `docs/DATASET_PROVENANCE_AND_LABEL_SOURCE_CHECKLIST_V0_1.md` | Yes or explicit caveat | `OWNER_DATA_LEGAL` | Recover upstream dataset citation/source or disclose unresolved status. | Open |
| Dataset license / redistribution rights | Unconfirmed | `data/README.md`; dataset checklist | Yes | `OWNER_DATA_LEGAL` | Confirm whether processed dataset can be redistributed or only referenced. | Open |
| Raw source path | Unresolved | `docs/DATASET.md`; dataset checklist | Yes or explicit caveat | `OWNER_DATA_LEGAL` | Locate source, cite source, or state absence clearly. | Open |
| Processed dataset path | Documented | `data/processed/legacy_bbb_dataset_with_features.csv`; rerun-ready path | Yes | `OWNER_DATA_LEGAL` | Decide whether paths can be public supplement references. | Partially ready |
| Public dataset release status | Not ready | Dataset checklist | Yes | `OWNER_DATA_LEGAL` | Decide public data inclusion vs restricted reference language. | Open |
| Dataset version identifier | `pending_confirmation` | `docs/DATASET.md`; manifests | Yes or explicit caveat | `OWNER_DATA_LEGAL` | Confirm version label or keep final caveat. | Open |
| Label-source criteria | Partially unresolved | Dataset checklist | Yes or explicit caveat | `OWNER_DATA_LEGAL` | Recover criteria or state unresolved status in final supplement. | Open |

## Reference gap table

No formal bibliography file, `CITATION.cff`, `.bib`, or final reference list was found in the inspected repository files. The following are reference categories, not fabricated references.

| Reference category | Manuscript section | Why needed | Current status | Placeholder key | Action required |
|---|---|---|---|---|---|
| BBB and biological barrier background | Introduction | Supports the biological-delivery bottleneck context. | No formal citation present | `REF_NEEDED_BBB_BACKGROUND` | Search and select real sources. |
| Peptide permeability / cell-penetrating peptide background | Introduction / Discussion | Grounds peptide and delivery-signal framing. | No formal citation present | `REF_NEEDED_CPP_BACKGROUND` | Search and select real sources. |
| Sequence-derived physicochemical features | Methods | Supports use of length, charge, gravy, pI, aromaticity. | No formal citation present | `REF_NEEDED_SEQUENCE_FEATURES` | Select sources for feature definitions/calculation precedent. |
| Baseline classification methods | Methods | Supports Dummy, Logistic Regression, Random Forest baseline framing. | No formal citation present | `REF_NEEDED_BASELINE_MODELS` | Cite software docs or ML methods sources as appropriate. |
| ROC-AUC / PR-AUC under imbalance | Methods / Results | Supports PR-AUC and class imbalance interpretation. | No formal citation present | `REF_NEEDED_PRAUC_IMBALANCE` | Add real references for imbalanced evaluation metrics. |
| MCC interpretation | Methods / Results | Supports MCC as binary-classification summary under imbalance. | No formal citation present | `REF_NEEDED_MCC_INTERPRETATION` | Add real reference if MCC remains emphasized. |
| Leakage / train-test contamination / similarity-aware evaluation | Methods / Limitations | Supports leakage caveat and future sensitivity-analysis need. | No formal citation present | `REF_NEEDED_LEAKAGE_SIMILARITY` | Add real benchmark-contamination or sequence-similarity evaluation references. |
| Bioinformatics benchmark reproducibility | Introduction / Discussion | Supports benchmark-first and artifact-traceability framing. | No formal citation present | `REF_NEEDED_BENCHMARK_REPRODUCIBILITY` | Add real reproducibility references. |
| Dataset source / inherited benchmark source | Dataset / Methods | Required for attribution and label-source context. | Unconfirmed | `REF_NEEDED_DATASET_SOURCE` | Recover upstream dataset source before public posting. |
| Software dependencies | Methods / Code availability | May support pandas, numpy, scikit-learn, matplotlib, seaborn, PyYAML. | `requirements.txt` lists dependencies; no citations present | `REF_NEEDED_SOFTWARE_CITATIONS` | Decide citation policy and add real package citations if needed. |

## Supplement/export checklist

| Item | Current status | Evidence/source | Required before bioRxiv? | Action required | Status |
|---|---|---|---|---|---|
| Final supplementary file | Outline only | `docs/SUPPLEMENTARY_OUTLINE_V0_1.md` | Strongly recommended | Draft supplement or appendix package. | Open |
| Figure list | Available but not final-captioned | `figures/`; `docs/PREPRINT_ASSEMBLY_V0_1.md` | Yes | Confirm final figure set and captions. | Open |
| Table list | Available but not export-packaged | `results/tables/`; assembly docs | Yes | Confirm table captions and inclusion rules. | Open |
| Leakage audit appendix | Audit outputs exist | `results/audits/`; leakage report/investigation | Strongly recommended | Convert audit outputs into supplement-ready tables/notes. | Open |
| Artifact inventory | Draft traceability exists | `docs/FINAL_ARTIFACT_TRACEABILITY_EXPORT_CHECK_V0_1.md` | Strongly recommended | Convert inventory to supplement/export format. | Open |
| Dataset/provenance appendix | Checklist exists | `docs/DATASET_PROVENANCE_AND_LABEL_SOURCE_CHECKLIST_V0_1.md` | Yes or explicit caveat | Finalize public-safe provenance language. | Open |
| Reproducibility instructions | Partial repo instructions exist | `README.md`; scripts; configs | Yes | Create final command and environment block for supplement. | Open |
| Code availability statement | Placeholder | Checklist | Yes | Confirm final repository URL, tag, branch, and archive policy. | Open |
| Data availability statement | Placeholder | Dataset docs | Yes | Resolve data redistribution status before writing final statement. | Open |
| Final export bundle | Not present | No supplement/export folder found | Yes for upload workflow | Prepare final manuscript, figures, tables, supplement, and availability text. | Open |

## Blocker classification

| Item | Classification | Rationale |
|---|---|---|
| Final author list, order, affiliations, corresponding author, email | Blocker before bioRxiv | Required submission metadata and cannot be invented. |
| Funding, competing interests, author contributions, acknowledgements | Blocker before bioRxiv | Must be provided or approved by human operator. |
| Formal references | Blocker before bioRxiv | Draft `references.bib` exists, but manuscript citation insertion, final reference metadata review, and deferred-reference decisions remain incomplete. |
| Dataset attribution and license / redistribution status | Blocker before bioRxiv | Public data/source handling must be accurate. |
| Data/code availability statements | Blocker before bioRxiv | Must match actual repository and dataset-release policy. |
| Supplement/export bundle | Strongly recommended before bioRxiv | Needed for coherent artifact and leakage-audit support. |
| Leakage-aware split follow-up | Can remain caveated | Current audit is reflected; stronger claims require follow-up. |
| Additional model families or experiments | Future work | Not needed for v0.1 metadata/reference closure. |

## Minimal path to bioRxiv v0.1

1. Finalize author metadata, author order, affiliations, corresponding author, email, and optional ORCID IDs.
2. Add approved funding, competing-interest, author-contribution, acknowledgement, ethics, data-availability, and code-availability statements.
3. Resolve or explicitly caveat dataset attribution, dataset license, redistribution rights, and public dataset release status.
4. Add formal references using real sources only.
5. Finalize supplement/export bundle with figures, tables, leakage audit appendix, provenance appendix, artifact inventory, and reproducibility instructions.
6. Retain leakage caveat: current metrics are random-stratified baseline metrics and may be optimistic.
7. Run one final preprint readiness check before any public posting.

## Recommended next Codex task

Task 048 — Insert Citation Placeholders into `PREPRINT_DRAFT_V0_1.md`
