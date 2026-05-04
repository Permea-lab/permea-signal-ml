# Supplementary Materials Draft v0.1

## Status

Draft supplementary materials for a bioRxiv v0.1 manuscript candidate. Not final, not submission-ready, and not a public supplement.

This supplement is a computational evidence appendix. It records committed artifacts but does not itself modify artifacts, rerun models, or claim biological or wet-lab validation. Metric references include random-stratified baseline metrics and committed leakage-aware sensitivity outputs; neither should be read as leakage-free or robust-generalization estimates.

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

Reported metrics are ROC-AUC, PR-AUC, precision, recall, F1, and MCC. The primary baseline metrics remain random-stratified baseline metrics and may be optimistic because the leakage audit found same-label duplicate and high-similarity pairs crossing reconstructed folds. The leakage-aware rerun metrics are bounded sensitivity estimates under one committed group-stratified manifest. Together, they support benchmark-signal interpretation under the documented split policies only, not leakage-free or robust generalization.

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

Values below are copied from committed sensitivity outputs for manuscript traceability; this supplement does not alter metric values.

## Appendix D2 - Leakage-Aware Sensitivity Metrics

Leakage-aware sensitivity outputs are documented in:

- `docs/LEAKAGE_AWARE_BASELINE_RERUN_REPORT_V0_1.md`
- `docs/LEAKAGE_AWARE_BASELINE_RERUN_FINDINGS_INVESTIGATION_V0_1.md`
- `results/sensitivity/combined_group_stratified_split_manifest.csv`
- `results/sensitivity/leakage_aware_model_comparison_summary.csv`
- `results/sensitivity/leakage_aware_model_comparison_per_fold.csv`
- `results/sensitivity/leakage_aware_metrics_summary.json`

The split manifest uses `leakage_aware_group_stratified` policy with 2,959 rows, 2,958 groups, and 5 folds. Group identifiers are kept together across folds. This is a sensitivity manifest, not model validation or proof that leakage is fully controlled.

### Leakage-aware rerun metrics

| Model | ROC-AUC | PR-AUC | MCC | Interpretation boundary |
| --- | ---: | ---: | ---: | --- |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 | Class-prior sanity baseline. |
| Logistic Regression | 0.8587 | 0.5024 | 0.3747 | Broadly similar to random-stratified baseline under this manifest. |
| Random Forest | 0.8718 | 0.5807 | 0.5084 | Comparable to or higher than random-stratified baseline under this manifest. |

### Random-stratified versus leakage-aware comparison

| Model | Random ROC-AUC | Leakage-aware ROC-AUC | Delta | Random PR-AUC | Leakage-aware PR-AUC | Delta | Random MCC | Leakage-aware MCC | Delta |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Dummy most-frequent | 0.5000 | 0.5000 | 0.0000 | 0.0909 | 0.0909 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Logistic Regression | 0.8605 | 0.8587 | -0.0018 | 0.4903 | 0.5024 | +0.0121 | 0.3618 | 0.3747 | +0.0130 |
| Random Forest | 0.8489 | 0.8718 | +0.0229 | 0.5002 | 0.5807 | +0.0805 | 0.4331 | 0.5084 | +0.0753 |

Conservative interpretation: the leakage-aware sensitivity rerun did not collapse the baseline signal under this specific grouping strategy. Logistic Regression remained broadly similar, and Random Forest was comparable to or higher than its random-stratified baseline under this manifest. These results increase confidence relative to the initial leakage concern, but they do not establish leakage-free status, robust generalization, biological validation, wet-lab validation, or true BBB performance.

Remaining sensitivity limitations:

- The combined grouping retained the `max_pairs=10000` caveat, so grouping may be incomplete.
- Only one non-singleton group appears under the current combined grouping output.
- The `source` field remains too coarse for source-aware grouping or split control.
- Raw source path, provenance, attribution, licensing, redistribution, and source-chain status remain unresolved.
- Original positive/negative label-source criteria remain unresolved.
- Feature inputs remain limited to sequence-derived physicochemical descriptors.
- No external validation, wet-lab validation, or biological validation was performed.

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
- `results/sensitivity/combined_group_stratified_split_manifest.csv`
- `results/sensitivity/combined_group_stratified_split_summary.json`
- `results/sensitivity/leakage_aware_model_comparison_summary.csv`
- `results/sensitivity/leakage_aware_model_comparison_per_fold.csv`
- `results/sensitivity/leakage_aware_predictions.csv`
- `results/sensitivity/leakage_aware_metrics_summary.json`

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

The current model family is baseline-oriented. The leakage-aware rerun uses only the same existing baseline model families and does not add new model families.

The public preprint remains not submission-ready until human metadata, legal, reference, disclosure, formatting, and approval blockers are resolved.
