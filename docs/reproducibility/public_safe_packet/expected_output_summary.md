# Expected Output Summary

This summary preserves the aggregate metric values from the Task 130 plan. It is public-safe because it contains aggregate metrics only.

## Dataset Counts

| Metric | Value |
| --- | ---: |
| Dataset rows | 2,959 |
| Positives | 269 |
| Negatives | 2,690 |

## Aggregate Performance Values

| Result | Value |
| --- | ---: |
| P-SIGNAL-001 RF ROC-AUC | 0.8718 |
| P-SIGNAL-001 RF PR-AUC | 0.5807 |
| P-SIGNAL-002 RF ROC-AUC | 0.9027 |
| P-SIGNAL-002 RF PR-AUC | 0.6891 |
| P-SIGNAL-003 LR MCC | 0.5143 |
| Best Brier | P-SIGNAL-002 RF `0.051176` |
| Best ECE | P-SIGNAL-001 RF `0.021510` |
| Best MCC | P-SIGNAL-002 RF threshold `0.35`, MCC `0.620665` |
| Best F1 | P-SIGNAL-002 RF threshold `0.20`, F1 `0.640569` |
| k=50 precision | P-SIGNAL-003 RF `0.940000`, 47 hits |
| k=269 recall | P-SIGNAL-002 RF `0.635688`, 171 hits |

## Interpretation

The public evidence supports aggregate benchmark-label evaluation, sequence-derived feature and representation comparison, aggregate calibration/threshold summaries, and candidate prioritization before experimental validation.

The evidence does not support claims of wet-lab, in-vivo, clinical, therapeutic, solved-delivery, universal-delivery, deployment-grade, independent-validation, or biological-transport-proof capability.

## Do Not Overclaim

- Do not describe aggregate benchmark labels as experimental validation.
- Do not describe source-card or lineage overlap context as independent validation.
- Do not state or imply public dataset availability.
- Do not infer wet-lab, in-vivo, clinical, therapeutic, solved-delivery, universal-delivery, SOTA, deployment-grade, or biological transport proof from these aggregate artifacts.
- Do not claim Permea is already AlphaFold for Delivery; that remains an ambition and infrastructure direction, not an achieved maturity claim.
