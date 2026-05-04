# Supplementary Materials Draft v0.1

## Status

Draft supplementary materials for a bioRxiv v0.1 manuscript candidate. Not final, not submission-ready, and not a public supplement.

This supplement is a computational evidence appendix. It does not add new results, modify artifacts, rerun models, or claim biological or wet-lab validation. Metric references in this supplement are random-stratified baseline references and should not be read as leakage-aware generalization estimates.

## Appendix A - Dataset Surface and Field Definitions

The current rerun-ready BBB-oriented processed dataset surface is documented as 2,959 rows in the manuscript and dataset docs. Confirmed benchmark-relevant fields are:

| Field | Role in current benchmark | Current caveat |
| --- | --- | --- |
| `sequence` | Peptide sequence input and row identity support. | Original upstream source path and source-chain metadata remain incomplete. |
| `label` | Supervised benchmark target. | Current label is not independently verified biological truth. |
| `length` | Sequence-derived physicochemical descriptor. | Feature-definition provenance remains a documentation item. |
| `charge` | Sequence-derived physicochemical descriptor. | Feature-definition provenance remains a documentation item. |
| `gravy` | Sequence-derived physicochemical descriptor. | Feature importance is model-level behavior, not mechanism. |
| `pI` | Sequence-derived physicochemical descriptor. | Feature-definition provenance remains a documentation item. |
| `aromaticity` | Sequence-derived physicochemical descriptor. | Feature importance is model-level behavior, not mechanism. |
| `sequence_id` | Operational row identity added for rerun traceability. | Operational metadata only. |
| `source` | Operational source label added for rerun traceability. | Current value `legacy_bbb_import` is too coarse for group-aware split control. |

## Appendix B - Feature Definitions

The current feature surface is intentionally narrow and sequence-derived: length, charge, gravy, pI, and aromaticity. It is used as an interpretable baseline surface, not as a complete representation of BBB transport chemistry, structure, or mechanism. No listed feature should be interpreted from this package as causal or as determining BBB transport.

No additional feature families, structural encodings, protein-language-model embeddings, assay-derived features, or model families are introduced by this supplement.

## Appendix C - Model and Evaluation Summary

The regenerated baseline reruns include:

- Dummy most-frequent classifier
- Logistic Regression
- Random Forest

The recovered evaluation policy is `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`. This is a random-stratified split policy, not a duplicate-aware or similarity-aware policy.

Reported metrics are ROC-AUC, PR-AUC, precision, recall, F1, and MCC. These metrics remain random-stratified baseline metrics and may be optimistic because the leakage audit found same-label duplicate and high-similarity pairs crossing reconstructed folds. They support benchmark-signal interpretation under the current split only, not leakage-aware or robust generalization.

## Appendix D - Metrics Table References

Main metric statements should be traced to:

- `results/tables/model_comparison_summary.csv`
- `results/metrics/legacy_bbb_dummy_v01_metrics.json`
- `results/metrics/legacy_bbb_lr_v01_metrics.json`
- `results/metrics/legacy_bbb_rf_v01_metrics.json`

Feature-importance statements should be traced to:

- `results/tables/regenerated_rf_feature_importance.csv`
- `figures/regenerated_rf_feature_importance.png`

Feature-importance statements are model-level summaries only. They should not be used as mechanistic proof, biological explanation, or evidence that any descriptor causally controls BBB transport.

This supplement does not restate or alter metric values.

## Appendix E - Leakage Audit Summary

The first leakage audit is documented in:

- `docs/LEAKAGE_AUDIT_REPORT_V0_1.md`
- `docs/LEAKAGE_AUDIT_FINDINGS_INVESTIGATION_V0_1.md`
- `results/audits/leakage_audit_summary.json`

Current documented findings:

- 4 exact duplicate sequence groups, all same-label, crossing reconstructed folds
- 0 normalized exact-sequence label-conflict groups
- 73 near-duplicate pairs, all same-label, 56 cross-fold
- 33 high k-mer Jaccard pairs, all same-label, 29 cross-fold
- source value `legacy_bbb_import` spans all 5 folds and is too coarse for group-aware split control
- overall benchmark optimism risk: Moderate

Interpretation boundary: these findings require conservative reporting. They do not prove the dataset is unusable, but they also do not support leakage-free, robust-generalization, or biological-validation claims.

## Appendix F - Artifact Inventory

### Main documents

- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/PREPRINT_ASSEMBLY_V0_1.md`
- `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`
- `docs/FINAL_ARTIFACT_TRACEABILITY_EXPORT_CHECK_V0_1.md`

### Tables

- `results/tables/model_comparison_summary.csv`
- `results/tables/regenerated_rf_feature_importance.csv`
- `results/tables/legacy_bbb_dummy_v01_summary.csv`
- `results/tables/legacy_bbb_lr_v01_summary.csv`
- `results/tables/legacy_bbb_rf_v01_summary.csv`
- `results/tables/legacy_bbb_dummy_v01_ranking.csv`
- `results/tables/legacy_bbb_lr_v01_ranking.csv`
- `results/tables/legacy_bbb_rf_v01_ranking.csv`

### Metrics and manifests

- `results/metrics/legacy_bbb_dummy_v01_metrics.json`
- `results/metrics/legacy_bbb_lr_v01_metrics.json`
- `results/metrics/legacy_bbb_rf_v01_metrics.json`
- `results/manifests/legacy_bbb_dummy_v01_manifest.json`
- `results/manifests/legacy_bbb_lr_v01_manifest.json`
- `results/manifests/legacy_bbb_rf_v01_manifest.json`

### Figures

- `figures/dataset_distribution.png`
- `figures/legacy_vs_rerun_metrics.png`
- `figures/regenerated_rf_feature_importance.png`
- `figures/benchmark_workflow_outputs.png`
- `figures/candidate_ranking_preview.png`

### Leakage audit outputs

- `results/audits/sequence_duplicate_audit.csv`
- `results/audits/label_conflict_audit.csv`
- `results/audits/near_duplicate_pairs.csv`
- `results/audits/sequence_similarity_summary.csv`
- `results/audits/fold_similarity_leakage_summary.csv`
- `results/audits/source_group_leakage_summary.csv`
- `results/audits/leakage_audit_summary.json`

## Appendix G - Provenance Caveats

The current dataset surface is not provenance-closed. The following remain unresolved before public submission:

- final upstream source-chain attribution
- dataset licensing and redistribution status
- raw source dataset path
- dataset version identifier beyond `pending_confirmation`
- original label-source criteria
- final public data availability statement

The label field is used as the current supervised benchmark target. It should not be described as independently verified biological truth.

## Appendix H - Reproducibility Commands

Existing repository commands and scripts referenced by current artifacts include:

```bash
python scripts/run_baseline.py
python scripts/export_metrics.py
python scripts/generate_figures.py
python scripts/rank_candidates.py
python scripts/audit_leakage.py
```

These commands are listed as repository anchors only. This supplement draft did not rerun them.

## Appendix I - Limitations and No-Wet-Lab Boundary

The current package is computational. It does not include biological validation, wet-lab validation, therapeutic efficacy evidence, clinical interpretation, or mechanism proof.

The current model family is baseline-oriented. The present package does not introduce new model families, does not rerun baselines, and does not add new benchmark results.

The public preprint remains not submission-ready until human metadata, legal, reference, disclosure, formatting, and approval blockers are resolved.
