# Dataset Row-Level Provenance and Redistribution Risk Audit - 2026-05-07

## 1. Purpose and Scope

This report audits local Permea repository files for dataset row-level provenance and redistribution risk.

Scope:

- Inventory data, split, manifest, prediction, metric, figure, notebook, and documentation artifacts.
- Identify which files contain row-level peptide sequence, label, feature, prediction, split, grouping, or leakage information.
- Separate observed repo facts from manual/legal decisions still required.
- Classify public-release risk conservatively.

This is an internal repo-only audit. It does not modify data, results, figures, manuscript files, references, notebooks, or existing documentation. It does not use web search and does not make final legal conclusions.

## 2. Current Repo State

Observed before report creation:

- Branch: `master`
- Working tree: clean before this new report
- Latest pushed commit in task context: `de79c47 docs: add deepb3p3 identity review`
- Current working manuscript: `docs/paper/permea-first-paper-manuscript-v0-4.md`
- Public bioRxiv status: **Hold / not submission-ready**
- Dataset redistribution status: unresolved

## 3. Source-Context Summary

Observed repo facts:

- Current dataset surface: `legacy_bbb_dataset_with_features`
- Current dataset config: `configs/data/legacy_bbb_dataset_with_features.yaml`
- Current rerun-ready dataset path: `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`
- Imported processed dataset path: `data/processed/legacy_bbb_dataset_with_features.csv`
- Current config version: `pending_confirmation`
- Current operational source value: `legacy_bbb_import`
- `data/raw/` contains only `.gitkeep`; no raw upstream dataset file is present in this repo.
- Existing docs report legacy raw filenames:
  - `raw_data/b3pred_dataset3_positive.txt`
  - `raw_data/b3pred_dataset3_negative.txt`
- User-confirmed initial source context: data was downloaded from `https://webs.iiitd.edu.in/raghava/b3pred/`.

Manual/legal decisions still required:

- Confirm exact upstream dataset files and version.
- Confirm source terms, attribution requirements, and redistribution permissions.
- Confirm whether local processed row-level data can be redistributed.
- Confirm original positive/negative label-source criteria.

This audit does not conclude that redistribution is permitted.

## 4. Data Directory Inventory

Observed files:

| Path | Type | Audit classification |
| --- | --- | --- |
| `data/README.md` | Documentation | Safe to expose now, subject to final review. |
| `data/examples/example_sequences.csv` | Tiny synthetic example CSV, 12 rows plus header | Likely safe after review; documented as smoke-test example. |
| `data/interim/.gitkeep` | Placeholder | Safe to expose now. |
| `data/processed/.gitkeep` | Placeholder | Safe to expose now. |
| `data/processed/legacy_bbb_dataset_with_features.csv` | Processed row-level peptide table, 2,959 rows plus header | Do not redistribute publicly without explicit permission. |
| `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv` | Processed row-level peptide table with operational IDs/source, 2,959 rows plus header | Do not redistribute publicly without explicit permission. |
| `data/raw/.gitkeep` | Placeholder | Safe to expose now. |

## 5. Raw Data Inventory

Observed raw-data directory:

- `data/raw/.gitkeep`

No raw B3Pred/B3Pdb source file is present in this repo.

Risk classification:

- `data/raw/.gitkeep`: safe to expose now.
- raw upstream data: absent; no redistribution decision can be made from local raw data because it is not present.

## 6. Processed Data Inventory

### `data/processed/legacy_bbb_dataset_with_features.csv`

Header:

```text
sequence,label,length,charge,gravy,pI,aromaticity
```

Line count:

- 2,960 lines including header
- 2,959 data rows

Risk:

- Contains row-level peptide sequences, binary labels, and sequence-derived features.
- High redistribution risk.
- Do not redistribute publicly without explicit source/license permission.

### `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`

Header:

```text
sequence_id,sequence,label,length,charge,gravy,pI,aromaticity,source
```

Line count:

- 2,960 lines including header
- 2,959 data rows

Risk:

- Contains row-level peptide sequences, labels, sequence-derived features, deterministic operational IDs, and coarse operational source.
- Highest redistribution risk among local data artifacts.
- Do not redistribute publicly without explicit source/license permission.

## 7. Row-Level Sequence / Label / Feature Artifact Inventory

| Artifact | Row-level content | Risk classification |
| --- | --- | --- |
| `data/processed/legacy_bbb_dataset_with_features.csv` | sequence, label, length, charge, gravy, pI, aromaticity | Do not redistribute publicly without explicit permission. |
| `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv` | sequence_id, sequence, label, features, source | Do not redistribute publicly without explicit permission. |
| `data/examples/example_sequences.csv` | synthetic sequence_id, sequence, label, source | Likely safe after review. |
| `results/audits/near_duplicate_pairs.csv` | sequence_a, sequence_b, edit distance | Do not redistribute publicly without explicit permission. |
| `results/audits/fold_similarity_leakage_summary.csv` | sequence_a, sequence_b, similarity, folds | Do not redistribute publicly without explicit permission. |
| `results/audits/sequence_duplicate_audit.csv` | normalized sequence-level duplicate summary | Hold until source/license decision; may expose sequence-derived content. |
| `results/audits/sequence_similarity_summary.csv` | sequence-similarity summary | Hold until source/license decision; inspect before release. |

## 8. Split / Manifest / Provenance Artifact Inventory

| Artifact | Content | Risk classification |
| --- | --- | --- |
| `configs/data/legacy_bbb_dataset_with_features.yaml` | dataset path, column names, provisional version, source caveats | Likely safe after review. |
| `results/manifests/legacy_bbb_dummy_v01_manifest.json` | run metadata and artifact paths | Likely safe after review. |
| `results/manifests/legacy_bbb_lr_v01_manifest.json` | run metadata and artifact paths | Likely safe after review. |
| `results/manifests/legacy_bbb_rf_v01_manifest.json` | run metadata and artifact paths | Likely safe after review. |
| `results/sensitivity/combined_group_stratified_split_manifest.csv` | row_index, sequence_id, label, group_id, fold_id, group_size | Hold until source/license decision; row-level split manifest. |
| `results/sensitivity/group_assignments_combined.csv` | row_index, sequence_id, normalized_sequence, group_id, grouping metadata | Do not redistribute publicly without explicit permission. |
| `results/sensitivity/combined_group_stratified_split_summary.json` | aggregate fold/group summary | Likely safe after review. |
| `results/sensitivity/grouping_summary_combined.json` | aggregate group summary and caveats | Likely safe after review. |
| `docs/PROVENANCE.md` | provenance contract | Safe to expose now with caveats. |
| `docs/DATASET.md` | dataset status and caveats | Safe to expose now with caveats. |
| `docs/DATASET_PROVENANCE_AND_LABEL_SOURCE_CHECKLIST_V0_1.md` | provenance checklist | Safe to expose now with caveats. |

## 9. Result / Metric / Prediction Artifact Inventory

### Aggregate Metrics and Summaries

| Artifact | Content | Risk classification |
| --- | --- | --- |
| `results/tables/model_comparison_summary.csv` | aggregate model metrics | Likely safe after review. |
| `results/metrics/legacy_bbb_dummy_v01_metrics.json` | aggregate metrics | Likely safe after review. |
| `results/metrics/legacy_bbb_lr_v01_metrics.json` | aggregate metrics | Likely safe after review. |
| `results/metrics/legacy_bbb_rf_v01_metrics.json` | aggregate metrics | Likely safe after review. |
| `results/metrics/legacy_baseline_ml_results.csv` | aggregate legacy metrics | Likely safe after review. |
| `results/metrics/legacy_benchmark_ml_results.csv` | aggregate legacy metrics | Likely safe after review. |
| `results/sensitivity/leakage_aware_metrics_summary.json` | aggregate leakage-aware metric summary | Likely safe after review. |
| `results/sensitivity/leakage_aware_model_comparison_summary.csv` | aggregate model comparison | Likely safe after review. |
| `results/sensitivity/leakage_aware_model_comparison_per_fold.csv` | per-model/per-fold metrics; no sequence columns in header | Likely safe after review. |

### Row-Level Predictions and Rankings

| Artifact | Header / content | Risk classification |
| --- | --- | --- |
| `results/predictions/legacy_bbb_dummy_v01_predictions.csv` | sequence_id, true_label, predicted_label, predicted_score, fold | Hold until source/license decision. |
| `results/predictions/legacy_bbb_lr_v01_predictions.csv` | sequence_id, true_label, predicted_label, predicted_score, fold | Hold until source/license decision. |
| `results/predictions/legacy_bbb_rf_v01_predictions.csv` | sequence_id, true_label, predicted_label, predicted_score, fold | Hold until source/license decision. |
| `results/sensitivity/leakage_aware_predictions.csv` | model, sequence_id, true_label, predicted_label, predicted_score, fold_id, split_policy | Hold until source/license decision. |
| `results/tables/legacy_bbb_dummy_v01_ranking.csv` | sequence_id, predicted_score, rank | Hold until source/license decision. |
| `results/tables/legacy_bbb_lr_v01_ranking.csv` | sequence_id, predicted_score, rank | Hold until source/license decision. |
| `results/tables/legacy_bbb_rf_v01_ranking.csv` | sequence_id, predicted_score, rank | Hold until source/license decision. |

Reason:

- These files do not expose peptide sequences directly in their headers, but they expose row-level IDs, labels, scores, folds, or rankings derived from the processed dataset. They may be linkable to sequence rows if the dataset is present or later released.

## 10. Figure / Table Artifact Inventory

### Figures

Observed figure artifacts:

- `figures/dataset_distribution.png`
- `figures/benchmark_workflow_outputs.png`
- `figures/legacy_vs_rerun_metrics.png`
- `figures/legacy_rf_feature_importance.png`
- `figures/legacy_rf_feature_importance_chart.png`
- `figures/regenerated_rf_feature_importance.png`
- `figures/legacy_bbb_dummy_v01_score_distribution.png`
- `figures/legacy_bbb_lr_v01_score_distribution.png`
- `figures/legacy_bbb_rf_v01_score_distribution.png`
- `figures/smoke_test_rf_score_distribution.png`
- `figures/candidate_ranking_preview.png`

Risk classification:

- Aggregate/summary figures: likely safe after review.
- `candidate_ranking_preview.png`: hold until source/license and claim-boundary review because candidate ranking may expose or imply row-level prioritization.
- Dataset distribution figure: likely safe after review if it does not expose row-level sequences, but keep dataset caveats visible.

### Tables

| Table type | Files | Risk classification |
| --- | --- | --- |
| Aggregate comparison/summary tables | `results/tables/model_comparison_summary.csv`, `legacy_bbb_*_summary.csv`, `legacy_rf_feature_importance.csv`, `regenerated_rf_feature_importance.csv`, `smoke_test_rf_summary.csv` | Likely safe after review. |
| Row-level ranking tables | `results/tables/legacy_bbb_*_ranking.csv`, `smoke_test_rf_ranking.csv` | Hold until source/license decision. |

## 11. Leakage-Audit and Sensitivity Artifact Inventory

### Leakage Audit

| Artifact | Content | Risk classification |
| --- | --- | --- |
| `results/audits/leakage_audit_summary.json` | aggregate audit counts and output paths | Likely safe after review. |
| `results/audits/label_conflict_audit.csv` | empty/header-only in current audit | Likely safe after review. |
| `results/audits/source_group_leakage_summary.csv` | source-group summary | Likely safe after review. |
| `results/audits/sequence_duplicate_audit.csv` | normalized-sequence duplicate summary | Hold until source/license decision. |
| `results/audits/near_duplicate_pairs.csv` | explicit paired sequences | Do not redistribute publicly without explicit permission. |
| `results/audits/fold_similarity_leakage_summary.csv` | explicit paired sequences and folds | Do not redistribute publicly without explicit permission. |
| `results/audits/sequence_similarity_summary.csv` | sequence similarity summary | Hold until source/license decision. |

### Leakage-Aware Sensitivity

| Artifact | Content | Risk classification |
| --- | --- | --- |
| `results/sensitivity/group_assignments_combined.csv` | normalized_sequence, sequence_id, group IDs | Do not redistribute publicly without explicit permission. |
| `results/sensitivity/combined_group_stratified_split_manifest.csv` | sequence_id, label, group/fold assignments | Hold until source/license decision. |
| `results/sensitivity/leakage_aware_predictions.csv` | sequence_id, labels, scores, fold IDs | Hold until source/license decision. |
| `results/sensitivity/grouping_summary_combined.json` | aggregate grouping summary | Likely safe after review. |
| `results/sensitivity/combined_group_stratified_split_summary.json` | aggregate split summary | Likely safe after review. |
| `results/sensitivity/leakage_aware_metrics_summary.json` | aggregate metrics | Likely safe after review. |
| `results/sensitivity/leakage_aware_model_comparison_summary.csv` | aggregate metrics | Likely safe after review. |
| `results/sensitivity/leakage_aware_model_comparison_per_fold.csv` | per-fold metrics | Likely safe after review. |

## 12. Source / Attribution / License Metadata Observed

Observed:

- User-confirmed initial source URL: `https://webs.iiitd.edu.in/raghava/b3pred/`
- `references.bib` includes:
  - `b3pdb_2021`
  - `b3pred_2021`
- `configs/data/legacy_bbb_dataset_with_features.yaml` records:
  - dataset name: `legacy_bbb_dataset_with_features`
  - version: `pending_confirmation`
  - source column: `source`
  - notes that attribution and licensing must be confirmed
- `docs/BBB_PROVENANCE_RECOVERY.md` records legacy raw file names and label assignment direction.
- `docs/DATASET.md` and `docs/DATASET_PROVENANCE_AND_LABEL_SOURCE_CHECKLIST_V0_1.md` explicitly preserve unresolved source, license, and label-source caveats.

## 13. Source / Attribution / License Metadata Missing

Still missing:

- explicit local copy of raw upstream positive/negative source files
- exact upstream dataset version
- exact source terms or license for downloaded B3Pred data
- explicit redistribution permission for processed row-level data
- required attribution wording for the downloaded dataset
- original positive/negative inclusion criteria and label-source rationale
- whether row-level derived artifacts may be released
- whether split manifests, group assignments, predictions, or rankings may be released
- final public data availability route

## 14. Manuscript Dependency Mapping

| Manuscript dependency | Supporting local artifact(s) | Release-risk note |
| --- | --- | --- |
| Dataset row count and fields | `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`, `docs/DATASET.md` | Manuscript can cite row count/fields internally; row-level file redistribution remains unresolved. |
| Random-stratified metrics | `results/tables/model_comparison_summary.csv`, `results/metrics/legacy_bbb_*_metrics.json` | Aggregate metrics likely safe after review. |
| Leakage-aware sensitivity metrics | `results/sensitivity/leakage_aware_metrics_summary.json`, `leakage_aware_model_comparison_summary.csv` | Aggregate metrics likely safe after review. |
| Leakage audit findings | `results/audits/leakage_audit_summary.json`, audit docs | Aggregate audit summary likely safe after review; sequence-pair CSVs are high risk. |
| Split manifest description | `results/sensitivity/combined_group_stratified_split_manifest.csv`, summary JSON | Summary likely safe; row-level manifest should be held. |
| Grouping caveats | `results/sensitivity/grouping_summary_combined.json`, `group_assignments_combined.csv` | Summary likely safe; row-level group assignments should be held. |
| Feature importance | `results/tables/legacy_rf_feature_importance.csv`, `figures/*feature_importance*` | Likely safe after review if framed as model artifact only. |
| Candidate prioritization | `results/tables/legacy_bbb_*_ranking.csv`, `figures/candidate_ranking_preview.png` | Hold until source/license and claim-boundary review. |

## 15. Public-Release Risk Classification

### Safe to Expose Now

Subject to normal repo review:

- `.gitkeep` placeholders
- documentation that explicitly states unresolved limitations
- aggregate-ready caveat docs

### Likely Safe After Review

Likely safe after founder/manual and claim-boundary review:

- aggregate metric summaries
- aggregate leakage/sensitivity summary JSON files
- aggregate model-comparison CSVs
- model configuration YAMLs
- feature configuration YAMLs
- run manifest JSONs
- aggregate figures that do not expose row-level sequences or candidate identities
- synthetic smoke-test examples

### Hold Until Source / License Decision

Hold until source terms and legal/founder review:

- row-level prediction files
- row-level ranking files
- split manifests
- label/fold/group assignment files
- candidate ranking preview figure
- sequence duplicate/similarity summaries that may expose or reconstruct row-level data

### Do Not Redistribute Publicly Without Explicit Permission

Do not redistribute publicly without explicit permission:

- `data/processed/legacy_bbb_dataset_with_features.csv`
- `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`
- `results/audits/near_duplicate_pairs.csv`
- `results/audits/fold_similarity_leakage_summary.csv`
- `results/sensitivity/group_assignments_combined.csv`

Reason:

- These files contain peptide sequences directly or normalized sequence content, or they expose row-level sequence-derived artifacts tightly coupled to the processed dataset.

## 16. Recommended Safest Release Posture

Recommended current posture:

- No public row-level processed dataset redistribution.
- No public row-level prediction, ranking, split-manifest, group-assignment, or explicit sequence-pair artifact release.
- Code release may proceed only after repository release policy, software license, and founder/manual review.
- Aggregate metric summaries, aggregate audit summaries, aggregate sensitivity summaries, and selected figures may be considered after claim-boundary review.
- Public documentation should continue to state that dataset source, licensing, attribution, redistribution, and label-source criteria remain unresolved.

## 17. Data / Code Availability Wording Recommendation

Recommended conservative wording candidate:

```text
Code supporting the computational benchmark workflow is intended for release through the Permea repository after final release review, repository URL/tag confirmation, and software license approval. Processed row-level peptide datasets, row-level predictions, ranking tables, split manifests, group assignments, and sequence-pair leakage artifacts are not declared publicly available in this version because source attribution, source terms, redistribution permission, raw source paths, public dataset version, and original label-source criteria remain under manual review. Aggregate metric summaries and documentation may be released where approved, but such release does not imply permission to redistribute the underlying processed dataset.
```

Do not use wording that says row-level redistribution is permitted unless explicit source/legal documentation supports it.

## 18. Manual Founder / Legal Decision Checklist

Before public preprint, public repo release, or public artifact release:

- [ ] Confirm exact B3Pred download files used.
- [ ] Confirm source URL, source version, and download date if recoverable.
- [ ] Confirm B3Pred/B3Pdb attribution requirements.
- [ ] Confirm dataset source terms or license.
- [ ] Decide whether processed row-level data may be redistributed.
- [ ] Decide whether row-level prediction files may be released.
- [ ] Decide whether row-level ranking tables may be released.
- [ ] Decide whether split manifests and group assignments may be released.
- [ ] Decide whether sequence-pair leakage artifacts may be released.
- [ ] Decide whether aggregate metrics and figures may be released.
- [ ] Approve final data/code availability wording.
- [ ] Re-run final claim-boundary review after release set is chosen.

## 19. Recommended Next Task

Recommended next task:

**Task 145 - Commit Dataset Row-Level Provenance and Redistribution Risk Audit**

Suggested follow-up after commit:

- Prepare a public-release artifact allow/hold manifest that enumerates which files should be included, withheld, or redacted for any future public package.

## Required Posture

- Internal review only.
- Row-level processed dataset redistribution remains unresolved.
- Public bioRxiv remains **Hold / not submission-ready**.
- This report does not conclude that redistribution is allowed.
- This report separates observed repo facts from manual/legal decisions still required.

