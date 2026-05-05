# Permea First Paper Supplement v0.1

## 1. Supplement Status Note

This supplement draft supports internal review of manuscript v0.5. It is not public-submission-ready and does not approve public release of row-level datasets or row-level derived artifacts.

Public bioRxiv remains **Hold / not submission-ready**.

## 2. Scope and Claim Boundary

This supplement uses aggregate-safe summaries and path-level artifact references only. It supports a conservative in-silico computational manuscript about learnable BBB-related peptide classification signal from sequence-derived physicochemical features.

It does not claim:

- state-of-the-art performance
- leakage-free status
- robust generalization
- biological, wet-lab, in-vivo, therapeutic, or clinical validation
- public dataset redistribution permission
- external expert review or peer review

## 3. Dataset Surface Summary Without Row-Level Redistribution

Current benchmark surface:

- 2,959 rows
- sequence-derived fields: `length`, `charge`, `gravy`, `pI`, `aromaticity`
- supervised target: `label`
- operational identifiers: `sequence_id`, `source`

Path-level source:

- `data/processed/legacy_bbb_dataset_with_features.csv`
- `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`

These paths are provided for internal traceability only. This supplement does not redistribute row-level peptide sequences, labels, or features.

## 4. Feature Representation Summary

The feature representation is intentionally small and sequence-derived:

- length
- charge
- gravy
- pI
- aromaticity

The representation is a baseline surface and is not a complete mechanistic model of BBB transport.

## 5. Baseline Model Summary

Baseline families:

- Dummy most-frequent classifier
- Logistic Regression
- Random Forest

Configuration path references:

- `configs/models/dummy.yaml`
- `configs/models/logistic_regression.yaml`
- `configs/models/random_forest.yaml`
- `configs/features/physicochemical.yaml`
- `configs/eval/default.yaml`

## 6. Evaluation Metric Summary

Reported metrics include:

- ROC-AUC
- PR-AUC
- MCC

PR-AUC is included because the task is class-imbalanced. MCC is included as an additional binary-classification summary.

## 7. Random-Stratified Evaluation Summary

Aggregate random-stratified metrics:

| Model | ROC-AUC | PR-AUC | MCC |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 |
| Logistic Regression | 0.8605 | 0.4903 | 0.3618 |
| Random Forest | 0.8489 | 0.5002 | 0.4331 |

Traceability:

- `results/tables/model_comparison_summary.csv`
- `results/metrics/legacy_bbb_dummy_v01_metrics.json`
- `results/metrics/legacy_bbb_lr_v01_metrics.json`
- `results/metrics/legacy_bbb_rf_v01_metrics.json`

These are aggregate result references only.

## 8. Leakage Audit Summary

Prior leakage audit findings:

- 4 exact duplicate sequence groups, all same-label, crossing reconstructed folds
- 0 exact label conflicts
- 73 near-duplicate pairs, all same-label, including 56 cross-fold pairs
- 33 high k-mer Jaccard pairs, all same-label, including 29 cross-fold pairs
- single coarse source value: `legacy_bbb_import`
- overall benchmark optimism risk: Moderate

Aggregate traceability:

- `results/audits/leakage_audit_summary.json`

Blocked from public-facing supplement:

- `results/audits/near_duplicate_pairs.csv`
- `results/audits/fold_similarity_leakage_summary.csv`

## 9. Leakage-Aware Sensitivity Summary

Aggregate leakage-aware sensitivity metrics:

| Model | ROC-AUC | PR-AUC | MCC |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 |
| Logistic Regression | 0.8587 | 0.5024 | 0.3747 |
| Random Forest | 0.8718 | 0.5807 | 0.5084 |

Relative to random-stratified baseline:

| Model | ROC-AUC delta | PR-AUC delta | MCC delta |
| --- | ---: | ---: | ---: |
| Logistic Regression | -0.0018 | +0.0121 | +0.0130 |
| Random Forest | +0.0229 | +0.0805 | +0.0753 |

Traceability:

- `results/sensitivity/leakage_aware_metrics_summary.json`
- `results/sensitivity/leakage_aware_model_comparison_summary.csv`
- `results/sensitivity/leakage_aware_model_comparison_per_fold.csv`

This is a bounded sensitivity setting, not proof of leakage-free status.

## 10. Aggregate Result Traceability Matrix

| Manuscript result | Aggregate support | Release posture |
| --- | --- | --- |
| Random-stratified model metrics | `results/tables/model_comparison_summary.csv` | Candidate after review. |
| Model-specific metrics | `results/metrics/legacy_bbb_*_metrics.json` | Candidate after review. |
| Leakage-aware summary | `results/sensitivity/leakage_aware_model_comparison_summary.csv` | Candidate after review. |
| Leakage-aware per-fold metrics | `results/sensitivity/leakage_aware_model_comparison_per_fold.csv` | Candidate after review. |
| Leakage audit summary | `results/audits/leakage_audit_summary.json` | Candidate after review. |
| Grouping/split aggregate summaries | `results/sensitivity/grouping_summary_combined.json`; `results/sensitivity/combined_group_stratified_split_summary.json` | Candidate after review. |

## 11. Figure / Table Inventory Placeholders

Candidate figures after review:

- Figure S1: `figures/dataset_distribution.png`
- Figure S2: `figures/legacy_vs_rerun_metrics.png`
- Figure S3: `figures/benchmark_workflow_outputs.png`
- Figure S4: `figures/regenerated_rf_feature_importance.png`

Blocked from public-facing supplement:

- `figures/candidate_ranking_preview.png`

Candidate tables:

- Table S1: dataset surface summary, no row-level entries
- Table S2: random-stratified aggregate metrics
- Table S3: leakage-aware aggregate metrics
- Table S4: leakage audit aggregate summary
- Table S5: artifact release allow/hold matrix

## 12. Release Allow / Hold Matrix

| Artifact class | Current posture |
| --- | --- |
| Manuscript text | Internal review only. |
| Aggregate metrics | Candidate after founder/manual and claim-boundary review. |
| Aggregate leakage/sensitivity summaries | Candidate after review. |
| Summary figures | Candidate after review. |
| Processed row-level datasets | Do not redistribute publicly without explicit permission. |
| Row-level predictions/rankings | Hold; do not include in public supplement. |
| Split manifests/group assignments | Hold; do not include in public supplement. |
| Sequence-pair leakage CSVs | Do not redistribute publicly without explicit permission. |

## 13. Data / Code Availability Caveats

Code availability is separate from data availability. Code release requires repository URL, release tag, software license, and founder/manual approval.

Processed dataset redistribution is not declared available. Dataset availability depends on source terms, original attribution, licensing, label-source criteria, and manual review.

## 14. Limitations

- Internal-review supplement only.
- No row-level sequences, labels, predictions, rankings, split manifests, group assignments, or sequence-pair leakage tables are included.
- Dataset source/license/redistribution remains unresolved.
- Aggregate artifact release still requires review.
- Supplement captions, numbering, and export manifest remain incomplete.
- No PDF or public export was generated.

## 15. Export / Readiness Blockers

- finalize public-safe artifact allowlist
- finalize dataset source/license/redistribution decision
- finalize figure/table numbering and captions
- finalize source-to-claim review
- finalize data/code availability wording
- finalize founder/manual approval
- generate export only after blockers close
