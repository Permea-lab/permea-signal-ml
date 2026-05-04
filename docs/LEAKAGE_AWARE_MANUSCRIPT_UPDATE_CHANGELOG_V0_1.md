# Leakage-Aware Manuscript Update Changelog v0.1

## Purpose

This changelog documents the Task 092 manuscript and support-document updates that incorporate leakage-aware sensitivity findings into the bioRxiv v0.1 candidate package.

This document does not rerun models, rerun the leakage audit, run new split generation, modify result artifacts, change metric values, add references, or approve public posting. Public preprint status remains **Hold / not submission-ready**.

## Source Findings

Source interpretation documents:

- `docs/LEAKAGE_AWARE_BASELINE_RERUN_REPORT_V0_1.md`
- `docs/LEAKAGE_AWARE_BASELINE_RERUN_FINDINGS_INVESTIGATION_V0_1.md`

Committed sensitivity outputs:

- `results/sensitivity/combined_group_stratified_split_manifest.csv`
- `results/sensitivity/leakage_aware_model_comparison_summary.csv`
- `results/sensitivity/leakage_aware_model_comparison_per_fold.csv`
- `results/sensitivity/leakage_aware_metrics_summary.json`

## Documents Updated

- `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`
- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`
- `docs/PREPRINT_CLAIM_BOUNDARY_AUDIT_V0_1.md`
- `docs/BIORXIV_V0_1_READINESS_REASSESSMENT_V0_1.md`
- `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`
- `docs/PREPRINT_CANDIDATE_STATUS_REPORT_V0_1.md`
- `docs/FOUNDER_APPROVAL_SUMMARY_PREPRINT_CANDIDATE_V0_1.md`
- `docs/REVIEW_OPERATIONS_INDEX_V0_1.md`

## Metrics Inserted

Leakage-aware sensitivity metrics under `leakage_aware_group_stratified`:

| Model | ROC-AUC | PR-AUC | MCC |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 |
| Logistic Regression | 0.8587 | 0.5024 | 0.3747 |
| Random Forest | 0.8718 | 0.5807 | 0.5084 |

Random-stratified to leakage-aware deltas:

| Model | ROC-AUC delta | PR-AUC delta | MCC delta |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.0000 | 0.0000 | 0.0000 |
| Logistic Regression | -0.0018 | +0.0121 | +0.0130 |
| Random Forest | +0.0229 | +0.0805 | +0.0753 |

## Claim-Boundary Changes

Allowed conservative interpretation added:

- The leakage-aware sensitivity rerun did not collapse the baseline signal under this specific grouping strategy.
- Logistic Regression remained broadly similar to its random-stratified baseline.
- Random Forest was comparable to or higher than its random-stratified baseline under this manifest.
- The result increases confidence relative to the initial leakage concern.

Forbidden interpretations remain excluded:

- leakage-free status
- leakage fully controlled
- robust generalization proven
- validated BBB delivery
- biological validation
- wet-lab validation
- true BBB performance
- therapeutic efficacy
- clinical efficacy

## Remaining Limitations

- The combined grouping retained the `max_pairs=10000` caveat, so grouping may be incomplete.
- Only one non-singleton group appears under the current combined grouping output.
- The `source` field remains too coarse for source-aware grouping or split control.
- Raw source path, provenance, attribution, licensing, redistribution, and source-chain status remain unresolved.
- Original positive/negative label-source criteria remain unresolved.
- Feature inputs remain limited to sequence-derived physicochemical descriptors.
- No external validation, wet-lab validation, or biological validation was performed.

## Public Preprint Status

Public preprint status remains **Hold / not submission-ready**. The manuscript and supplement now include leakage-aware sensitivity findings, but metadata, legal/dataset, bibliography, supplement/export, and final founder/manual approval blockers remain open.
