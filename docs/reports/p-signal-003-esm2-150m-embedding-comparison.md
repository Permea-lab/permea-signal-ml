# P-SIGNAL-003 ESM-2 150M Aggregate Representation Comparison

P-SIGNAL-003 reports an aggregate computational representation comparison using `facebook/esm2_t30_150M_UR50D` mean-pooled sequence representations. The public artifacts are summary-only benchmark evidence for model-comparison review; they do not release the underlying dataset.

## Public Boundary

The dataset is not redistributed. Row-level data, raw sequences, embeddings, predictions, split manifests, and group assignments are not public. Public files contain only aggregate model metrics, aggregate per-fold metrics, aggregate leakage-audit counts, and a public-safe run manifest.

Claim boundary: this report is limited to aggregate computational benchmarking and does not make experimental-validation, clinical, efficacy, delivery-solution, broad-prediction, best-in-field, dataset-availability, or biological-proof claims.

## Aggregate Model Comparison

| Model | ROC-AUC | PR-AUC | Balanced accuracy | Precision | Recall | F1 | MCC |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Dummy majority baseline | 0.5000 | 0.0909 | 0.5000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Logistic regression | 0.8811 | 0.5734 | 0.7937 | 0.4868 | 0.6577 | 0.5576 | 0.5143 |
| Random forest | 0.8956 | 0.6704 | 0.6201 | 0.9357 | 0.2416 | 0.3833 | 0.4551 |

The P-SIGNAL-001 aggregate physicochemical baseline random forest row reported ROC-AUC 0.8718, PR-AUC 0.5807, and MCC 0.5084 under the same leakage-aware group-stratified 5-fold policy.

The P-SIGNAL-002 ESM-2 35M logistic regression aggregate result reported ROC-AUC 0.8843, PR-AUC 0.5771, and MCC 0.4954. The P-SIGNAL-002 ESM-2 35M random forest aggregate result reported ROC-AUC 0.9027, PR-AUC 0.6891, and MCC 0.4734.

The P-SIGNAL-003 ESM-2 150M logistic regression aggregate result is ROC-AUC 0.8811, PR-AUC 0.5734, and MCC 0.5143. The P-SIGNAL-003 ESM-2 150M random forest aggregate result is ROC-AUC 0.8956, PR-AUC 0.6704, and MCC 0.4551.

P-SIGNAL-003 does not establish a monotonic model-scale improvement over P-SIGNAL-002. The 150M random forest result is lower than the 35M random forest result on ROC-AUC, PR-AUC, and MCC. The 150M logistic regression result has higher MCC than the 35M logistic regression result, but slightly lower ROC-AUC and PR-AUC. This is computational aggregate benchmark evidence only, not biological validation.

## Leakage Summary

The leakage audit is aggregate-only. It reports 4 duplicate-sequence groups, 0 label-conflict groups, 73 near-duplicate pair counts, 33 high k-mer/Jaccard pair counts, and 0 groups crossing execution folds.

Pairwise comparison stopped after `max_pairs=10000`; grouping may be incomplete. Source-aware biological interpretation is limited because source metadata is too coarse for source-aware split control.

## Public Artifacts

- `results/p_signal_003/esm2_t30_150m_model_comparison.csv`
- `results/p_signal_003/esm2_t30_150m_per_fold_metrics.csv`
- `results/p_signal_003/esm2_t30_150m_leakage_summary.json`
- `results/p_signal_003/esm2_t30_150m_run_manifest.json`

These files are intended for public review of aggregate model behavior only.
