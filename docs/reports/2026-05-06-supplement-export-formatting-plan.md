# Permea Supplement and Export Formatting Plan - 2026-05-06

## Purpose

This report plans supplement and export formatting work for manuscript v0.2 without modifying manuscript text, references, data files, result artifacts, figure artifacts, model outputs, split artifacts, leakage audit artifacts, or export files.

This is a planning document only. It does not generate PDFs, DOCX files, submission bundles, website archives, or public release artifacts. It does not approve public bioRxiv posting, dataset redistribution, or legal/licensing conclusions.

Public bioRxiv remains **Hold / not submission-ready**. Dataset redistribution remains unresolved.

## Materials Reviewed

- `docs/paper/permea-first-paper-manuscript-v0-2.md`
- `docs/reports/2026-05-05-export-readiness-check.md`
- `docs/reports/2026-05-06-manuscript-v0-2-audit.md`
- `docs/review/2026-05-06-friendly-reviewer-packet-v0-2.md`
- `docs/submission/2026-05-06-dataset-attribution-and-availability-decision-package.md`
- `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`
- `docs/SUPPLEMENT_EXPORT_FORMATTING_CHECKLIST_V0_1.md`
- `docs/FIGURE_INVENTORY.md`
- `docs/BIORXIV_EXPORT_PACKAGE_DRAFT_V0_1.md`
- `docs/FINAL_ARTIFACT_TRACEABILITY_EXPORT_CHECK_V0_1.md`
- `README.md`
- visible `figures/`, `results/`, `data/`, `notebooks/`, `docs/paper/`, `docs/reports/`, `docs/submission/`, and `docs/review/` paths

No top-level `reports/`, `manuscript/`, `paper/`, or `supplement/` directory was present. The active paper path is `docs/paper/`.

## 1. Current Supplement / Export Status

Current status: **not public-submission-ready**.

Internal materials exist:

- manuscript v0.2: `docs/paper/permea-first-paper-manuscript-v0-2.md`
- manuscript v0.2 audit: `docs/reports/2026-05-06-manuscript-v0-2-audit.md`
- friendly reviewer packet: `docs/review/2026-05-06-friendly-reviewer-packet-v0-2.md`
- supplement draft: `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`
- export checklist: `docs/SUPPLEMENT_EXPORT_FORMATTING_CHECKLIST_V0_1.md`
- export manifest draft: `docs/BIORXIV_EXPORT_PACKAGE_DRAFT_V0_1.md`

The existing supplement draft is useful for internal review and artifact traceability, but it is not final export material. It needs v0.2 alignment, section numbering, figure/table selection, captions, artifact traceability checks, data/legal caveat checks, and final export-format decisions.

## 2. Existing Artifact Inventory

### Manuscript and Review Documents

- `docs/paper/permea-first-paper-manuscript-v0-2.md`
- `docs/reports/2026-05-06-manuscript-v0-2-audit.md`
- `docs/review/2026-05-06-friendly-reviewer-packet-v0-2.md`
- `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`
- `docs/SUPPLEMENTARY_OUTLINE_V0_1.md`
- `docs/SUPPLEMENT_EXPORT_FORMATTING_CHECKLIST_V0_1.md`
- `docs/BIORXIV_EXPORT_PACKAGE_DRAFT_V0_1.md`

### Figures

Existing figure files:

- `figures/dataset_distribution.png`
- `figures/legacy_vs_rerun_metrics.png`
- `figures/regenerated_rf_feature_importance.png`
- `figures/benchmark_workflow_outputs.png`
- `figures/candidate_ranking_preview.png`
- `figures/legacy_bbb_dummy_v01_score_distribution.png`
- `figures/legacy_bbb_lr_v01_score_distribution.png`
- `figures/legacy_bbb_rf_v01_score_distribution.png`
- `figures/smoke_test_rf_score_distribution.png`
- `figures/legacy_rf_feature_importance.png`
- `figures/legacy_rf_feature_importance_chart.png`

Candidate public-support figures, pending caption and claim-boundary review:

- `figures/dataset_distribution.png`
- `figures/legacy_vs_rerun_metrics.png`
- `figures/regenerated_rf_feature_importance.png`
- `figures/benchmark_workflow_outputs.png`

Hold or use only with additional caution:

- `figures/candidate_ranking_preview.png` because public captioning must avoid implying experimental validation, validated BBB delivery, therapeutic relevance, or clinical relevance.
- score-distribution figures if selected, because each needs model-specific captioning and leakage/data caveats.
- legacy feature-importance figures if selected, because imported legacy and regenerated artifacts must remain clearly separated.

### Result Tables and Metrics

Core table and metric artifacts:

- `results/tables/model_comparison_summary.csv`
- `results/tables/regenerated_rf_feature_importance.csv`
- `results/metrics/legacy_bbb_dummy_v01_metrics.json`
- `results/metrics/legacy_bbb_lr_v01_metrics.json`
- `results/metrics/legacy_bbb_rf_v01_metrics.json`

Model summary and ranking artifacts:

- `results/tables/legacy_bbb_dummy_v01_summary.csv`
- `results/tables/legacy_bbb_lr_v01_summary.csv`
- `results/tables/legacy_bbb_rf_v01_summary.csv`
- `results/tables/legacy_bbb_dummy_v01_ranking.csv`
- `results/tables/legacy_bbb_lr_v01_ranking.csv`
- `results/tables/legacy_bbb_rf_v01_ranking.csv`

Prediction artifacts:

- `results/predictions/legacy_bbb_dummy_v01_predictions.csv`
- `results/predictions/legacy_bbb_lr_v01_predictions.csv`
- `results/predictions/legacy_bbb_rf_v01_predictions.csv`

These row-level artifacts need legal/source and claim-boundary review before public inclusion because they may expose sequences, labels, scores, or row-level information.

### Leakage Audit and Sensitivity Artifacts

Leakage audit outputs:

- `results/audits/sequence_duplicate_audit.csv`
- `results/audits/label_conflict_audit.csv`
- `results/audits/near_duplicate_pairs.csv`
- `results/audits/sequence_similarity_summary.csv`
- `results/audits/fold_similarity_leakage_summary.csv`
- `results/audits/source_group_leakage_summary.csv`
- `results/audits/leakage_audit_summary.json`

Leakage-aware sensitivity outputs:

- `results/sensitivity/group_assignments_combined.csv`
- `results/sensitivity/grouping_summary_combined.json`
- `results/sensitivity/combined_group_stratified_split_manifest.csv`
- `results/sensitivity/combined_group_stratified_split_summary.json`
- `results/sensitivity/leakage_aware_model_comparison_summary.csv`
- `results/sensitivity/leakage_aware_model_comparison_per_fold.csv`
- `results/sensitivity/leakage_aware_predictions.csv`
- `results/sensitivity/leakage_aware_metrics_summary.json`

Public supplement inclusion of row-level sensitivity outputs requires review because group assignments, split manifests, predictions, labels, and sequence identifiers may raise redistribution or derived-artifact concerns.

### Data and Notebook Artifacts

Data files:

- `data/README.md`
- `data/examples/example_sequences.csv`
- `data/processed/legacy_bbb_dataset_with_features.csv`
- `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`

Notebook files:

- `notebooks/01_dataset_assembly.ipynb`
- `notebooks/02_feature_extraction.ipynb`
- `notebooks/03_baseline_models.ipynb`
- `notebooks/04_candidate_ranking.ipynb`

Processed dataset redistribution remains unresolved. The supplement should not include or imply public redistribution rights for processed data.

## 3. Manuscript Sections Needing Supplement Support

| Manuscript v0.2 section | Supplement support needed | Candidate artifact/source |
| --- | --- | --- |
| Dataset Surface | Field definitions, row count, source caveats, label caveats | `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`; `data/README.md`; dataset decision package |
| Feature Representation | Feature definitions and non-mechanistic boundary | supplement Appendix B; `results/tables/regenerated_rf_feature_importance.csv` only if framed as model-level |
| Baseline Models | Model configs and evaluation policy | `configs/models/`; `configs/eval/default.yaml`; manifests |
| Random-Stratified Baseline Evaluation | Metric table traceability and metric definitions | `results/tables/model_comparison_summary.csv`; metrics JSON files |
| Leakage-Aware Sensitivity Analysis | Split manifest summary, rerun metrics, group caveats | `results/sensitivity/*`; sensitivity reports |
| Leakage Audit Context | Duplicate, near-duplicate, k-mer, source grouping caveats | `results/audits/*`; leakage audit docs |
| Feature-Importance Context | Feature-importance table/figure with non-mechanistic caption | `results/tables/regenerated_rf_feature_importance.csv`; `figures/regenerated_rf_feature_importance.png` |
| Data and Code Availability | Conservative data/code availability wording | dataset decision package; data/code availability draft |
| Supplementary Materials Pointer | Final supplement structure and export manifest | this plan; export checklist |

## 4. Candidate Supplement Structure

Recommended v0.2 supplement structure:

1. Supplement Status and Scope
2. Dataset Surface and Field Definitions
3. Dataset Source, Attribution, Licensing, and Availability Caveats
4. Feature Definitions and Non-Mechanistic Interpretation Boundary
5. Baseline Model Configurations
6. Random-Stratified Evaluation Policy and Metrics
7. Random-Stratified Baseline Results
8. Leakage Audit Summary
9. Leakage-Aware Group Assignment and Split Manifest
10. Leakage-Aware Baseline Rerun Results
11. Random-Stratified versus Leakage-Aware Comparison
12. Feature-Importance Artifact Summary
13. Figure and Table Inventory
14. Artifact Traceability Matrix
15. Reproducibility Command Anchors
16. Data and Code Availability Caveats
17. Limitations and Claim Boundaries
18. Export Manifest Placeholder

This structure should remain computational and internal until all public-release blockers are closed.

## 5. Figure / Table Numbering Plan

### Main Manuscript Candidate Figures

Recommended main figures, pending final selection:

| Proposed ID | Candidate artifact | Proposed use | Required caveat |
| --- | --- | --- | --- |
| Figure 1 | `figures/dataset_distribution.png` | Dataset class distribution / benchmark surface | Dataset provenance, source, and redistribution unresolved |
| Figure 2 | `figures/legacy_vs_rerun_metrics.png` | Baseline metric comparison context | Random-stratified metrics are not leakage-aware generalization estimates |
| Figure 3 | `figures/regenerated_rf_feature_importance.png` | Model-level feature importance | Not mechanistic proof |
| Figure S1 | `figures/benchmark_workflow_outputs.png` | Repository workflow / artifact traceability | Workflow traceability, not validation |

### Supplement-Only Candidate Figures

| Proposed ID | Candidate artifact | Proposed use | Required caveat |
| --- | --- | --- | --- |
| Figure S2 | `figures/legacy_bbb_dummy_v01_score_distribution.png` | Dummy score distribution | Include only if useful; class-prior baseline |
| Figure S3 | `figures/legacy_bbb_lr_v01_score_distribution.png` | Logistic Regression score distribution | Include leakage/data caveats |
| Figure S4 | `figures/legacy_bbb_rf_v01_score_distribution.png` | Random Forest score distribution | Include leakage/data caveats |
| Hold | `figures/candidate_ranking_preview.png` | Candidate-prioritization preview | Hold for public use unless caption is tightly bounded |

### Main Tables

| Proposed ID | Candidate artifact | Proposed use |
| --- | --- | --- |
| Table 1 | `results/tables/model_comparison_summary.csv` | Random-stratified baseline metrics |
| Table 2 | `results/sensitivity/leakage_aware_model_comparison_summary.csv` | Leakage-aware sensitivity metrics |
| Table 3 | manuscript-derived comparison table | Random-stratified versus leakage-aware deltas |

### Supplement Tables

| Proposed ID | Candidate artifact | Proposed use |
| --- | --- | --- |
| Table S1 | dataset field table from supplement draft | Dataset surface and field definitions |
| Table S2 | `results/tables/regenerated_rf_feature_importance.csv` | Feature-importance artifact summary |
| Table S3 | `results/audits/leakage_audit_summary.json` plus audit CSVs | Leakage audit summary |
| Table S4 | `results/sensitivity/combined_group_stratified_split_summary.json` | Split manifest summary |
| Table S5 | `results/sensitivity/leakage_aware_model_comparison_per_fold.csv` | Fold-level sensitivity results |
| Table S6 | artifact inventory | File traceability and release posture |

## 6. Caption Requirements

Every figure/table caption should include:

- artifact path
- whether the artifact is random-stratified baseline, leakage audit, leakage-aware sensitivity, or documentation-only
- metric provenance if metrics are shown
- leakage/data/source caveat where applicable
- explicit non-validation boundary where needed

Caption language must avoid:

- leakage-free
- robust generalization
- validated BBB delivery
- biological validation
- wet-lab validation
- in-vivo validation
- therapeutic efficacy
- clinical efficacy
- feature importance as mechanism
- dataset redistribution permission

Special caption requirements:

- Candidate-ranking figures/tables must state "pre-experimental prioritization only" if used.
- Feature-importance figures/tables must state "model-level artifact, not mechanistic proof."
- Leakage-aware sensitivity figures/tables must state "bounded sensitivity estimate under one manifest."
- Dataset figures/tables must state "dataset source, attribution, licensing, and redistribution remain unresolved."

## 7. Result Artifact Traceability Plan

Recommended traceability method:

1. Create a supplement artifact inventory table with columns:
   - claim/support area
   - artifact path
   - artifact type
   - manuscript/supplement use
   - public release posture
   - caveat
2. Link random-stratified metrics to:
   - `results/tables/model_comparison_summary.csv`
   - `results/metrics/legacy_bbb_dummy_v01_metrics.json`
   - `results/metrics/legacy_bbb_lr_v01_metrics.json`
   - `results/metrics/legacy_bbb_rf_v01_metrics.json`
3. Link leakage-aware metrics to:
   - `results/sensitivity/leakage_aware_model_comparison_summary.csv`
   - `results/sensitivity/leakage_aware_model_comparison_per_fold.csv`
   - `results/sensitivity/leakage_aware_metrics_summary.json`
4. Link leakage audit statements to:
   - `docs/LEAKAGE_AUDIT_REPORT_V0_1.md`
   - `docs/LEAKAGE_AUDIT_FINDINGS_INVESTIGATION_V0_1.md`
   - `results/audits/leakage_audit_summary.json`
5. Link dataset/source caveats to:
   - `docs/submission/2026-05-06-dataset-attribution-and-availability-decision-package.md`
   - `docs/submission/2026-05-05-data-and-code-availability-draft.md`
6. Re-run final claim-boundary and citation checks after supplement formatting, without changing metric values.

Do not include row-level data, predictions, group assignments, split manifests, or rankings in public material until founder/legal and claim-boundary review approves their release posture.

## 8. Export Format Options

### Option A - Internal Markdown Review Package

Current safest route.

Package:

- manuscript v0.2 markdown
- supplement markdown draft
- reviewer packet
- audit reports

Use for friendly/internal review only. No public posting.

### Option B - Public-Ready Markdown Package After Blockers Close

Possible later route.

Requires:

- final dataset/source/legal decision
- final data/code availability wording
- final references cleanup
- final supplement captions and numbering
- final export manifest
- founder/manual approval

### Option C - PDF / DOCX Export

Not currently ready.

Do not generate until:

- metadata and disclosures are finalized
- references are approved
- supplement captions and numbering are finalized
- figure/table inclusion is approved
- final claim-boundary and citation scans pass

### Option D - Website Evidence Archive

Hold.

Requires a separate website claim-boundary review. It must not imply public preprint approval, peer review, external expert review, biological validation, or dataset redistribution permission.

## 9. Formatting Blockers

Current blockers:

- Supplement draft is still v0.1-oriented and needs v0.2 alignment.
- Final supplement section order and numbering are not locked.
- Figure/table inclusion list is not finalized.
- Captions are not final.
- Figure/table numbering is not final.
- Public-release posture for row-level artifacts is unresolved.
- Dataset source, license, attribution, redistribution, and label-source criteria are unresolved.
- `references.bib` still requires human metadata cleanup and final source-to-claim review.
- Data/code availability wording is not final.
- Export manifest is draft-only.
- Public PDF/DOCX/export route has not been selected.
- Founder/manual approval remains required.

## 10. Dataset / Source / Legal Caveats Affecting Supplement

The supplement must preserve these caveats:

- Original dataset source identity remains unresolved.
- Source attribution and license terms remain unresolved.
- Processed dataset redistribution is not declared available.
- Original label-source criteria remain unresolved.
- The operational `source` value `legacy_bbb_import` is too coarse for source-aware split control and is not upstream attribution.
- Row-level artifacts may expose sequence, label, prediction, group, split, or ranking information and require separate release review.
- Aggregate metrics and documentation may be candidates for release only after founder/legal and claim-boundary review.

The supplement must not state that redistribution is permitted unless explicit source terms and manual legal review support that decision.

## 11. Recommended Safe Next Tasks

Recommended next task:

**Task 125 - Commit Supplement and Export Formatting Plan**

Subsequent safe tasks:

1. **Task 126 - Draft Supplement v0.2 Structure From Existing Artifacts**
   - Create a new v0.2 supplement draft without modifying artifacts.
   - Align sections to manuscript v0.2.
   - Preserve all caveats.
2. **Task 127 - Draft Figure and Table Caption Inventory**
   - Create caption candidates only.
   - Include artifact paths and claim-boundary caveats.
   - Do not edit figure or result files.
3. **Task 128 - Draft v0.2 Export Manifest**
   - Create a manifest listing candidate included/excluded files and release posture.
   - Keep public release on Hold.
4. **Task 129 - Audit Supplement v0.2 and Caption Inventory**
   - Check claim boundaries, metric consistency, citation/source caveats, and public-readiness blockers.
5. **Task 130 - Founder/Legal Dataset Release Decision Follow-Up**
   - Resolve or document source/legal decisions before any public data or row-level artifact release.

## Required Conclusions

- Supplement/export is not yet public-submission-ready.
- Manuscript v0.2 remains friendly/internal-review ready.
- Public bioRxiv remains **Hold / not submission-ready**.
- Dataset redistribution remains unresolved.

## No-Change Confirmation

This planning task did not modify:

- manuscript files
- `references.bib`
- data artifacts
- result artifacts
- figure artifacts
- model outputs
- split artifacts
- leakage audit artifacts

No PDF, DOCX, submission bundle, website archive, or public export artifact was generated. No models, leakage audits, or split generation were rerun. No metric values were changed.
