# bioRxiv Submission Checklist v0.1

## Purpose

This document tracks the current readiness of the BBB-oriented Permea manuscript package for a potential bioRxiv submission. It is intended as a practical readiness layer that separates what is already assembled from what remains placeholder or incomplete.

Detailed metadata, disclosure, reference, dataset/legal, and supplement/export gaps are tracked in `docs/PREPRINT_METADATA_AND_REFERENCE_GAP_CHECKLIST_V0_1.md`.

## Current submission package status

The repository currently contains a preprint draft, a preprint assembly document, a supplementary outline, a paper package planning document, an evidence package definition, current figures and tables, and repo-linked benchmark artifacts. Together, these components form a credible internal submission candidate, but not yet a finalized upload package.

## Manuscript file status

- title — provisional
- abstract — drafted
- introduction — drafted
- methods — drafted
- results — drafted
- discussion — drafted
- limitations — drafted
- conclusion — drafted
- front matter — placeholder sections added; final metadata pending
- formal references — pending

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
- attribution and licensing — still require confirmation

These items are acceptable for trusted review with the extended packet, but they remain preprint-readiness blockers or explicit-deferral items before public submission.

See `docs/DATASET_PROVENANCE_AND_LABEL_SOURCE_CHECKLIST_V0_1.md` for the current provenance and label-source checklist. The checklist documents current processed paths and fields, but it does not resolve source attribution, licensing, or original label criteria. See the leakage audit report and investigation memo for current duplicate and sequence-similarity findings.

## Supplementary status

Supplementary structure now exists as an outline, but not yet as a full drafted supplement or appendix package.

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

## Scope and claim-boundary checks

- no claim of experimental validation
- no claim of mechanistic causality
- no claim of universal prediction
- no claim of therapeutic efficacy
- no claim of broad delivery generalization
- BBB-oriented wedge stated explicitly
- computational evidence only stated explicitly
- benchmark-oriented candidate prioritization stated explicitly
- imported versus regenerated distinction preserved
- provenance limitations stated explicitly

## Repository and asset links

- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/PREPRINT_ASSEMBLY_V0_1.md`
- `docs/SUPPLEMENTARY_OUTLINE_V0_1.md`
- `docs/PREPRINT_METADATA_AND_REFERENCE_GAP_CHECKLIST_V0_1.md`
- `docs/V0_1_EVIDENCE_PACKAGE.md`
- `docs/DATASET.md`
- `results/tables/model_comparison_summary.csv`
- `results/tables/regenerated_rf_feature_importance.csv`

## Remaining blockers before submission

- authorship and affiliation metadata not finalized
- formal references not yet added
- supplement not yet drafted in full prose
- figure polish and publication formatting remain pending
- provenance closure remains incomplete
- attribution and licensing confirmation are still needed
- label-source criteria remain partially unresolved
- raw source dataset availability remains unresolved
- leakage audit findings must be reflected with conservative language; same-label duplicate and high-similarity pairs cross reconstructed folds
- leakage-aware or similarity-aware follow-up is likely needed before public benchmark claims are strengthened
- artifact-to-claim traceability should be checked once more before export
- one final manuscript consistency pass would still be useful

## Immediate next steps

- finalize front matter placeholders into real metadata when ready
- use `docs/PREPRINT_METADATA_AND_REFERENCE_GAP_CHECKLIST_V0_1.md` to close metadata, disclosure, reference, and export gaps
- decide what moves into supplement versus main text
- prepare one final formatting pass
- verify asset completeness before any submission upload
- prepare placeholder disclosure blocks for later completion
