# Supplement and Export v0.4 Alignment Plan - 2026-05-07

## 1. Purpose and Scope

This report plans a v0.4-aligned supplement/export package for the current Permea first-paper manuscript:

- `docs/paper/permea-first-paper-manuscript-v0-4.md`

Scope:

- Identify which existing materials can support manuscript v0.4.
- Separate internal-review supplement candidates from public-facing export candidates.
- Exclude row-level restricted artifacts from public-facing supplement/export planning.
- Define figure/table numbering, caption requirements, traceability requirements, and export blockers.

This is a planning report only. It does not modify manuscript files, references, data files, result artifacts, figure artifacts, model outputs, split artifacts, leakage-audit artifacts, or export files.

Public bioRxiv remains **Hold / not submission-ready**.

## 2. Current Manuscript v0.4 Status

Current working manuscript:

- `docs/paper/permea-first-paper-manuscript-v0-4.md`

Current status:

- Suitable for internal review.
- Citation-integrated for verified direct peptide comparators and adjacent compound-level BBB predictors.
- Conservative no-SOTA and no-leaderboard framing preserved.
- Dataset redistribution remains unresolved.
- Row-level processed data and row-level derived artifacts remain blocked from public release.
- Supplement/export formatting remains incomplete.

## 3. Current Supplement / Export Status

Current status: **not public-submission-ready**.

Existing supplement/export support materials:

- `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`
- `docs/SUPPLEMENTARY_OUTLINE_V0_1.md`
- `docs/SUPPLEMENT_EXPORT_FORMATTING_CHECKLIST_V0_1.md`
- `docs/BIORXIV_EXPORT_PACKAGE_DRAFT_V0_1.md`
- `docs/reports/2026-05-06-supplement-export-formatting-plan.md`
- `docs/reports/2026-05-07-dataset-row-level-provenance-redistribution-risk-audit.md`
- `docs/reports/2026-05-07-manuscript-v0-4-citation-source-claim-audit.md`

The existing supplement draft is useful as an internal source, but it is not yet aligned to manuscript v0.4 or to the row-level artifact release restrictions documented in the redistribution risk audit.

## 4. Existing Artifact Inventory

### Manuscript and Review Documents

- `docs/paper/permea-first-paper-manuscript-v0-4.md`
- `docs/reports/2026-05-07-manuscript-v0-4-citation-source-claim-audit.md`
- `docs/reports/2026-05-07-dataset-row-level-provenance-redistribution-risk-audit.md`
- `docs/reports/2026-05-07-deepb3p3-identity-review.md`
- `docs/reports/2026-05-07-verified-comparator-bibtex-candidate-pack.md`
- `docs/reports/2026-05-07-updated-references-bib-post-audit.md`
- `docs/reports/2026-05-07-bbb-landscape-based-manuscript-change-plan.md`

### Candidate Figures

- `figures/dataset_distribution.png`
- `figures/legacy_vs_rerun_metrics.png`
- `figures/benchmark_workflow_outputs.png`
- `figures/regenerated_rf_feature_importance.png`
- `figures/legacy_rf_feature_importance.png`
- `figures/legacy_rf_feature_importance_chart.png`
- `figures/legacy_bbb_dummy_v01_score_distribution.png`
- `figures/legacy_bbb_lr_v01_score_distribution.png`
- `figures/legacy_bbb_rf_v01_score_distribution.png`
- `figures/smoke_test_rf_score_distribution.png`
- `figures/candidate_ranking_preview.png`

### Aggregate Result Artifacts

- `results/tables/model_comparison_summary.csv`
- `results/metrics/legacy_bbb_dummy_v01_metrics.json`
- `results/metrics/legacy_bbb_lr_v01_metrics.json`
- `results/metrics/legacy_bbb_rf_v01_metrics.json`
- `results/sensitivity/leakage_aware_metrics_summary.json`
- `results/sensitivity/leakage_aware_model_comparison_summary.csv`
- `results/sensitivity/leakage_aware_model_comparison_per_fold.csv`
- `results/sensitivity/combined_group_stratified_split_summary.json`
- `results/sensitivity/grouping_summary_combined.json`
- `results/audits/leakage_audit_summary.json`

### Row-Level or Sensitive Artifacts

- `data/processed/legacy_bbb_dataset_with_features.csv`
- `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`
- `results/predictions/legacy_bbb_dummy_v01_predictions.csv`
- `results/predictions/legacy_bbb_lr_v01_predictions.csv`
- `results/predictions/legacy_bbb_rf_v01_predictions.csv`
- `results/sensitivity/leakage_aware_predictions.csv`
- `results/tables/legacy_bbb_dummy_v01_ranking.csv`
- `results/tables/legacy_bbb_lr_v01_ranking.csv`
- `results/tables/legacy_bbb_rf_v01_ranking.csv`
- `results/sensitivity/combined_group_stratified_split_manifest.csv`
- `results/sensitivity/group_assignments_combined.csv`
- `results/audits/near_duplicate_pairs.csv`
- `results/audits/fold_similarity_leakage_summary.csv`

## 5. Artifacts Safe to Use in Internal Supplement

Internal-review supplement can reference the following with caveats:

- `docs/paper/permea-first-paper-manuscript-v0-4.md`
- `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`
- `docs/reports/2026-05-07-manuscript-v0-4-citation-source-claim-audit.md`
- `docs/reports/2026-05-07-dataset-row-level-provenance-redistribution-risk-audit.md`
- `results/tables/model_comparison_summary.csv`
- `results/metrics/legacy_bbb_*_metrics.json`
- `results/sensitivity/leakage_aware_metrics_summary.json`
- `results/sensitivity/leakage_aware_model_comparison_summary.csv`
- `results/sensitivity/leakage_aware_model_comparison_per_fold.csv`
- `results/sensitivity/combined_group_stratified_split_summary.json`
- `results/sensitivity/grouping_summary_combined.json`
- `results/audits/leakage_audit_summary.json`
- `results/tables/regenerated_rf_feature_importance.csv`
- selected summary figures under `figures/`

Internal use does not imply public-release approval.

## 6. Artifacts Likely Safe Only After Review

Likely safe only after founder/manual, legal/source, and claim-boundary review:

- aggregate metric CSV/JSON artifacts
- aggregate leakage/sensitivity summary JSON files
- aggregate model-comparison tables
- run manifest JSONs
- dataset distribution figure
- metric comparison figure
- workflow traceability figure
- feature-importance tables/figures

Required caveats:

- not leakage-free
- not robust generalization
- not biological/wet-lab validation
- not therapeutic/clinical evidence
- dataset source/licensing/redistribution unresolved

## 7. Artifacts Blocked From Public-Facing Supplement / Export

Blocked from public-facing supplement/export unless explicit source/legal permission and claim-boundary approval are documented:

- processed row-level dataset files
- rerun-ready row-level dataset files
- row-level prediction files
- row-level ranking files
- row-level split manifests
- group assignment files containing normalized sequences
- leakage audit files containing explicit sequence pairs
- candidate ranking preview figure

These artifacts may expose sequences, labels, sequence IDs, scores, folds, group assignments, or row-level prioritization.

## 8. Manuscript v0.4 Section-to-Supplement Mapping

| Manuscript v0.4 section | Supplement support needed | Candidate internal artifact(s) | Public-facing caution |
| --- | --- | --- | --- |
| Introduction / Related Work | Comparator citation map and direct/adjacent boundary | `references.bib`; v0.4 citation audit | No SOTA or leaderboard framing. |
| Dataset Surface | Field table, row count, provenance caveats | `docs/DATASET.md`; dataset risk audit | Do not include row-level processed data. |
| Feature Representation | Feature definitions and non-mechanistic boundary | `configs/features/physicochemical.yaml`; feature-importance table | Feature importance is not mechanism. |
| Baseline Models | Model configs and evaluation policy | `configs/models/`; `configs/eval/default.yaml`; manifests | Configuration support only, not validation. |
| Random-Stratified Results | Aggregate metrics and table traceability | `model_comparison_summary.csv`; metrics JSON | Random-stratified estimates may be optimistic. |
| Leakage-Aware Sensitivity | Aggregate sensitivity metrics and caveats | leakage-aware summary artifacts | Bounded sensitivity under one manifest only. |
| Leakage Audit Context | Aggregate leakage findings | `leakage_audit_summary.json`; leakage audit docs | Do not expose sequence-pair CSVs publicly. |
| Data and Code Availability | Conservative release posture | dataset risk audit; availability draft | Row-level redistribution unresolved. |
| Limitations | Provenance, leakage, validation, export caveats | v0.4 audit and dataset risk audit | Preserve all limitations. |

## 9. Proposed Supplement v0.4 Structure

Recommended internal supplement v0.4 structure:

1. Supplement Status and Scope
2. Manuscript v0.4 Claim Boundary Summary
3. Dataset Surface, Row Count, and Field Definitions
4. Dataset Source, Attribution, License, and Redistribution Caveats
5. Direct Peptide and Adjacent Compound Comparator Citation Map
6. Feature Definitions and Non-Mechanistic Interpretation
7. Model Configurations and Evaluation Policy
8. Random-Stratified Baseline Metrics
9. Leakage Audit Summary
10. Leakage-Aware Sensitivity Summary
11. Random-Stratified vs Leakage-Aware Delta Summary
12. Feature-Importance Artifact Summary
13. Figure and Table Inventory
14. Artifact Traceability Matrix
15. Public-Release Allow/Hold Matrix
16. Data and Code Availability Caveats
17. Remaining Public-Submission Blockers
18. Export Manifest Placeholder

This structure is for internal review only until release blockers are closed.

## 10. Figure / Table Numbering Plan

### Candidate Main/Supplement Figures

| Proposed ID | Artifact | Proposed use | Status |
| --- | --- | --- | --- |
| Figure 1 or Figure S1 | `figures/dataset_distribution.png` | Dataset class imbalance | Likely safe after review with provenance caveat. |
| Figure 2 or Figure S2 | `figures/legacy_vs_rerun_metrics.png` | Random-stratified baseline comparison | Likely safe after review with leakage caveat. |
| Figure S3 | `figures/benchmark_workflow_outputs.png` | Workflow/artifact traceability | Likely safe after review. |
| Figure S4 | `figures/regenerated_rf_feature_importance.png` | Model-level feature importance | Likely safe after review with non-mechanistic caveat. |
| Hold | `figures/candidate_ranking_preview.png` | Candidate-prioritization preview | Blocked from public-facing export pending source/legal and claim-boundary review. |

### Candidate Tables

| Proposed ID | Artifact/source | Proposed use | Status |
| --- | --- | --- | --- |
| Table 1 | `results/tables/model_comparison_summary.csv` | Random-stratified baseline metrics | Likely safe after review. |
| Table 2 | `results/sensitivity/leakage_aware_model_comparison_summary.csv` | Leakage-aware sensitivity metrics | Likely safe after review. |
| Table 3 | manuscript-derived values | Random vs leakage-aware deltas | Likely safe after review. |
| Table S1 | dataset field table | Dataset surface summary | Safe if no row-level data included. |
| Table S2 | `results/sensitivity/leakage_aware_model_comparison_per_fold.csv` | Fold-level sensitivity metrics | Likely safe after review. |
| Table S3 | `results/audits/leakage_audit_summary.json` | Aggregate leakage audit summary | Likely safe after review. |
| Table S4 | artifact inventory | Release allow/hold posture | Recommended. |
| Hold | row-level ranking/prediction/split tables | Row-level detail | Blocked from public-facing export. |

## 11. Caption Requirements

Every figure/table caption should include:

- artifact path
- artifact type
- split/evaluation context
- whether values are random-stratified, leakage-aware sensitivity, leakage audit, or documentation-only
- dataset/provenance caveat where relevant
- public-release posture if the artifact is internal-only

Required wording boundaries:

- "in-silico computational benchmark"
- "bounded sensitivity estimate"
- "pre-experimental prioritization only" if rankings are ever shown internally
- "model-level artifact, not mechanistic proof" for feature importance
- "dataset source, licensing, redistribution, and label-source criteria remain unresolved"

Forbidden caption implications:

- leakage-free
- robust generalization
- validated BBB delivery
- biological validation
- wet-lab validation
- in-vivo validation
- therapeutic efficacy
- clinical efficacy
- dataset redistribution permission
- state-of-the-art performance

## 12. Result Traceability Requirements

Supplement v0.4 should trace every metric/table/figure to:

- artifact path
- model family
- split policy
- metric type
- dataset surface
- claim boundary
- release posture

Minimum required traceability links:

- Random-stratified metrics:
  - `results/tables/model_comparison_summary.csv`
  - `results/metrics/legacy_bbb_dummy_v01_metrics.json`
  - `results/metrics/legacy_bbb_lr_v01_metrics.json`
  - `results/metrics/legacy_bbb_rf_v01_metrics.json`
- Leakage-aware sensitivity:
  - `results/sensitivity/leakage_aware_metrics_summary.json`
  - `results/sensitivity/leakage_aware_model_comparison_summary.csv`
  - `results/sensitivity/leakage_aware_model_comparison_per_fold.csv`
- Leakage audit:
  - `results/audits/leakage_audit_summary.json`
  - audit reports under `docs/`
- Dataset/release posture:
  - `docs/reports/2026-05-07-dataset-row-level-provenance-redistribution-risk-audit.md`
  - `docs/submission/2026-05-06-dataset-attribution-and-availability-decision-package.md`

## 13. Dataset / Provenance Caveats

Supplement v0.4 must preserve:

- source context traces to B3Pred/B3Pdb lineage but exact source/version/terms remain unresolved
- raw upstream files are not present in this repo
- processed row-level dataset redistribution remains unresolved
- row-level derived artifacts remain blocked from public-facing export
- labels are benchmark targets, not independently verified biological truth
- operational `source` value is `legacy_bbb_import`, not upstream attribution
- source-aware splitting is limited by coarse source metadata

## 14. Export Format Options

### Option A - Internal Markdown Supplement v0.4

Recommended next route.

Create a markdown supplement draft aligned to v0.4 with:

- aggregate metrics only
- artifact traceability
- release posture table
- no row-level data inclusion
- explicit caveats

### Option B - Internal Review Bundle

Bundle manuscript v0.4, supplement v0.4 markdown, citation/source-claim audit, dataset risk audit, and reviewer notes.

No public posting.

### Option C - Public Markdown/PDF/DOCX Export

Not ready.

Requires:

- final dataset/source/legal decision
- final release allow/hold manifest
- final references/bibliography cleanup
- final captions/numbering
- final source-to-claim and claim-boundary audits
- founder/manual approval

### Option D - Website Evidence Archive

Hold.

Requires a separate website claim-boundary and artifact-release review.

## 15. Public-Release Restrictions

Public-facing supplement/export must not include, link, or imply release approval for:

- row-level processed data
- row-level predictions
- row-level rankings
- row-level split manifests
- group assignments containing normalized sequences
- sequence-pair leakage audit CSVs
- candidate ranking preview

Public-facing text must continue to say:

- dataset redistribution remains unresolved
- row-level processed dataset redistribution is not declared available
- aggregate artifacts may be considered only after review
- public bioRxiv remains Hold / not submission-ready

## 16. Recommended Next Task

Recommended next task:

**Task 147 - Commit Supplement Export v0.4 Alignment Plan**

Recommended follow-up after commit:

**Task 148 - Draft Internal Supplement v0.4 From Aggregate Artifacts Only**

Scope for Task 148:

- Create a new supplement v0.4 markdown draft.
- Use aggregate artifacts and documentation only.
- Include an allow/hold artifact table.
- Exclude row-level data, predictions, rankings, split manifests, group assignments, and sequence-pair artifacts from public-facing supplement sections.
- Do not generate PDFs or export bundles.

## Required Posture

- Internal review only.
- Supplement/export is not yet public-submission-ready.
- Row-level dataset and row-level derived artifacts remain blocked from public release.
- Dataset redistribution remains unresolved.
- Public bioRxiv remains **Hold / not submission-ready**.

