# P-SIGNAL-002 ESM-2 Aggregate Representation Comparison

P-SIGNAL-002 reports an aggregate computational representation comparison using `facebook/esm2_t12_35M_UR50D` mean-pooled sequence representations. The public artifacts are summary-only benchmark evidence for model-comparison review; they do not release the underlying dataset.

## Public Boundary

The dataset is not redistributed. Row-level data, raw sequences, embeddings, predictions, split manifests, and group assignments are not public. Public files contain only aggregate model metrics, aggregate per-fold metrics, aggregate leakage-audit counts, and a public-safe run manifest.

This report does not claim wet-lab validation, in-vivo validation, clinical relevance, therapeutic efficacy, solved delivery, universal delivery prediction, state-of-the-art status, dataset public availability, or biological transport proof.

## Aggregate Model Comparison

| Model | ROC-AUC | PR-AUC | Balanced accuracy | Precision | Recall | F1 | MCC |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Dummy majority baseline | 0.5000 | 0.0909 | 0.5000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Logistic regression | 0.8843 | 0.5771 | 0.7962 | 0.4496 | 0.6768 | 0.5382 | 0.4954 |
| Random forest | 0.9027 | 0.6891 | 0.6361 | 0.8921 | 0.2752 | 0.4202 | 0.4734 |

The P-SIGNAL-001 aggregate physicochemical baseline random forest row reported ROC-AUC 0.8718, PR-AUC 0.5807, and MCC 0.5084 under the same leakage-aware group-stratified 5-fold policy. The P-SIGNAL-002 ESM-2 random forest aggregate result is ROC-AUC 0.9027, PR-AUC 0.6891, and MCC 0.4734. The P-SIGNAL-002 ESM-2 logistic regression aggregate result is ROC-AUC 0.8843, PR-AUC 0.5771, and MCC 0.4954. This is computational aggregate benchmark evidence only, not biological validation.

## Leakage Summary

The leakage audit is aggregate-only. It reports 4 duplicate-sequence groups, 0 label-conflict groups, 73 near-duplicate pair counts, 33 high k-mer/Jaccard pair counts, and 0 groups crossing execution folds.

Pairwise comparison stopped after `max_pairs=10000`; grouping may be incomplete. Source-aware biological interpretation is limited because source metadata is too coarse for source-aware split control.

## Public Artifacts

- `results/p_signal_002/esm2_embedding_model_comparison.csv`
- `results/p_signal_002/esm2_embedding_per_fold_metrics.csv`
- `results/p_signal_002/esm2_embedding_leakage_summary.json`
- `results/p_signal_002/esm2_embedding_run_manifest.json`

These files are intended for public review of aggregate model behavior only.
