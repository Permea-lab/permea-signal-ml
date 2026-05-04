# bioRxiv Submission Checklist v0.1

## Purpose

This document tracks the current readiness of the BBB-oriented Permea manuscript package for a potential bioRxiv submission. It is intended as a practical readiness layer that separates what is already assembled from what remains placeholder or incomplete.

Detailed metadata, disclosure, reference, dataset/legal, and supplement/export gaps are tracked in `docs/PREPRINT_METADATA_AND_REFERENCE_GAP_CHECKLIST_V0_1.md`. Reference search and verification planning is tracked in `docs/REFERENCE_SEARCH_PLAN_BIORXIV_V0_1.md`. The first and second verified reference packs are tracked in `docs/VERIFIED_REFERENCE_PACK_BIORXIV_V0_1.md` and `docs/VERIFIED_REFERENCE_PACK_BIORXIV_V0_2.md`. A draft `references.bib` now exists, but final human reference review and manuscript citation consistency review are still pending.

Human-provided metadata, disclosure, legal, availability, bibliography, and public-posting decisions should be collected with `docs/HUMAN_METADATA_AND_DISCLOSURE_INPUT_FORM_V0_1.md`. That form is not complete by default and does not make the public preprint ready.

Supplement and export formatting checks are tracked in `docs/SUPPLEMENT_EXPORT_FORMATTING_CHECKLIST_V0_1.md`. That checklist inventories current materials and required formatting checks, but it does not create final export files or make the package submission-ready.

Dataset legal, data availability, code availability, and license-statement wording options are tracked in `docs/DATASET_LEGAL_AND_AVAILABILITY_STATEMENT_OPTIONS_V0_1.md`. Those options require human/legal review and do not authorize dataset redistribution.

Final human cleanup requirements for draft `references.bib` are tracked in `docs/FINAL_REFERENCES_HUMAN_CLEANUP_CHECKLIST_V0_1.md`. That checklist does not finalize references or make the bibliography public-ready.

## Current submission package status

The repository currently contains a preprint draft, manuscript candidate, supplement draft, draft bibliography, preprint assembly document, supplementary outline, paper package planning document, evidence package definition, current figures and tables, and repo-linked benchmark artifacts. Together, these components form a credible internal manuscript candidate package, but not a finalized upload package.

Task 052 manuscript candidate file: `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`. Status: candidate prepared for human review; not submission-ready.

Task 053 claim-boundary audit file: `docs/PREPRINT_CLAIM_BOUNDARY_AUDIT_V0_1.md`. Status: pass with caveats; no major claim-boundary violation found.

Task 054 citation consistency check file: `docs/CITATION_CONSISTENCY_CHECK_V0_1.md`. Status: pass; all citation keys used in the draft and candidate exist in `references.bib`.

Task 055 readiness reassessment file: `docs/BIORXIV_V0_1_READINESS_REASSESSMENT_V0_1.md`. Status: candidate package prepared; not submission-ready until human metadata/legal/reference review is complete.

Task 056 export package draft file: `docs/BIORXIV_EXPORT_PACKAGE_DRAFT_V0_1.md`. Status: draft manifest only; not final export-ready.

Task 060 manuscript candidate fix changelog: `docs/PREPRINT_MANUSCRIPT_CANDIDATE_FIX_CHANGELOG_V0_1.md`. Status: abstract and claim-boundary wording fixes applied after maximum-harsh review; public preprint remains Hold / not submission-ready.

## Manuscript file status

- title — provisional
- abstract — drafted
- introduction — drafted with citation placeholders
- related work — drafted with citation placeholders
- methods — drafted
- results — drafted
- discussion — drafted
- leakage audit and benchmark interpretation — drafted with conservative caveat
- limitations — drafted and placed before discussion in the candidate flow
- conclusion — drafted
- front matter — placeholder sections added; final metadata pending
- formal references — first and second verified reference packs prepared; draft `references.bib` created; citation placeholders inserted into restructured `docs/PREPRINT_DRAFT_V0_1.md`; citation consistency check passed; human reference review still pending

## Figure and table status

- `dataset_distribution.png` — available
- `legacy_vs_rerun_metrics.png` — available, usable with minor cleanup
- `regenerated_rf_feature_importance.png` — available
- `benchmark_workflow_outputs.png` — available, usable with minor cleanup
- `model_comparison_summary.csv` — available as a main comparison table source
- regenerated-only comparison figure — pending / optional

## Provenance and benchmark-readiness status

- dataset surface identifier — `legacy_bbb_dataset_with_features`
- imported processed dataset path — `data/processed/legacy_bbb_dataset_with_features.csv`
- rerun-ready processed dataset path — `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`
- raw source dataset path — unresolved in this repo
- dataset version — still `pending_confirmation` in current manifests
- split policy — recovered as `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`
- random seed — recovered as `42`
- label-source criteria — not yet fully reconstructed
- duplicate / near-duplicate / sequence-similarity leakage status — first audit completed and documented
- leakage audit report — `docs/LEAKAGE_AUDIT_REPORT_V0_1.md`
- leakage audit investigation — `docs/LEAKAGE_AUDIT_FINDINGS_INVESTIGATION_V0_1.md`
- leakage audit summary artifact — `results/audits/leakage_audit_summary.json`
- leakage interpretation — moderate benchmark optimism risk; current metrics may be optimistic and should be treated as random-stratified baseline metrics
- Task 060 claim-boundary update — manuscript candidate and draft now bind metric interpretation more tightly to the random-stratified split and same-label cross-fold similarity caveats
- attribution and licensing — still require confirmation

These items are acceptable for trusted review with the extended packet, but they remain preprint-readiness blockers or explicit-deferral items before public submission.

See `docs/DATASET_PROVENANCE_AND_LABEL_SOURCE_CHECKLIST_V0_1.md` for the current provenance and label-source checklist. The checklist documents current processed paths and fields, but it does not resolve source attribution, licensing, or original label criteria. See the leakage audit report and investigation memo for current duplicate and sequence-similarity findings.

## Supplementary status

Supplementary structure now exists as an outline and a prose draft at `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`. The supplement is not final, not export-formatted, and not submission-ready.

Supplement/export formatting checklist: `docs/SUPPLEMENT_EXPORT_FORMATTING_CHECKLIST_V0_1.md`. Status: prepared for internal formatting review; public export remains blocked pending human metadata, legal, reference, caption, formatting, and approval closure.

## Metadata placeholders

- authors — placeholder
- affiliations — placeholder
- corresponding author — placeholder
- keywords — draft set available
- subject area wording — placeholder
- version date — placeholder
- manuscript status — draft preprint, not submission-ready

## Disclosure and statement placeholders

- author contributions — placeholder
- funding — placeholder
- conflicts of interest — placeholder
- ethics / approvals — placeholder, add only if applicable
- code and data availability statement — placeholder
- metadata/disclosure block source — `docs/PREPRINT_METADATA_BLOCKS_DRAFT_V0_1.md`

## Scope and claim-boundary checks

- no claim of experimental validation
- no claim of mechanistic causality
- no claim of universal prediction
- no claim of therapeutic efficacy
- no claim of broad delivery generalization
- no leakage-free or robust-generalization claim
- no SOTA predictor claim
- BBB-oriented wedge stated explicitly
- computational evidence only stated explicitly
- benchmark-oriented candidate prioritization stated explicitly
- imported versus regenerated distinction preserved
- provenance limitations stated explicitly

## Repository and asset links

- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`
- `docs/PREPRINT_ASSEMBLY_V0_1.md`
- `docs/SUPPLEMENTARY_OUTLINE_V0_1.md`
- `docs/PREPRINT_METADATA_AND_REFERENCE_GAP_CHECKLIST_V0_1.md`
- `docs/V0_1_EVIDENCE_PACKAGE.md`
- `docs/DATASET.md`
- `results/tables/model_comparison_summary.csv`
- `results/tables/regenerated_rf_feature_importance.csv`

## Remaining blockers before submission

- final author metadata, author order, affiliations, corresponding author, and email not finalized; placeholder blocks exist but require human completion
- funding, conflicts, acknowledgements, author contributions, ethics, data availability, and code availability require human-approved wording
- dataset licensing/redistribution and source-chain attribution remain unresolved
- dataset legal and availability options have been drafted, but no final source, license, redistribution, public-release, or availability decision has been made
- final reference human review remains required
- final references cleanup checklist has been prepared, but no final bibliography approval has been completed
- final export formatting remains pending
- draft export package manifest exists, but no final PDF/DOCX/submission bundle was created
- explicit human approval is required before public posting
- draft `references.bib` prepared and citation placeholders inserted, but citation consistency checking, deferred-reference decisions, and final human reference review are not complete
- supplement drafted in prose, but final formatting, captions, and human review remain pending
- figure polish and publication formatting remain pending
- provenance closure remains incomplete
- attribution and licensing confirmation are still needed
- label-source criteria remain partially unresolved
- raw source dataset availability remains unresolved
- leakage audit findings must be reflected with conservative language; same-label duplicate and high-similarity pairs cross reconstructed folds
- abstract and metric caveats have been tightened, but public posting still requires final human review and blocker closure
- leakage-aware or similarity-aware follow-up is likely needed before public benchmark claims are strengthened
- artifact-to-claim traceability should be checked once more before export
- one final manuscript consistency pass would still be useful

## Immediate next steps

- finalize front matter placeholders into real metadata when ready
- use `docs/PREPRINT_METADATA_AND_REFERENCE_GAP_CHECKLIST_V0_1.md` to close metadata, disclosure, reference, and export gaps
- use `docs/REFERENCE_SEARCH_PLAN_BIORXIV_V0_1.md` before adding any formal references
- decide what moves into supplement versus main text
- prepare one final formatting pass
- verify asset completeness before any submission upload
- prepare placeholder disclosure blocks for later completion
- complete `docs/HUMAN_METADATA_AND_DISCLOSURE_INPUT_FORM_V0_1.md` with human-provided values before replacing metadata or disclosure placeholders
