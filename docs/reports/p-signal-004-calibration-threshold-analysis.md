# P-SIGNAL-004 Aggregate Calibration / Threshold Analysis

P-SIGNAL-004 adds public-safe aggregate calibration and threshold analysis to the existing leakage-controlled computational benchmark. It is based on aggregate-compatible P-SIGNAL-001, P-SIGNAL-002, and P-SIGNAL-003 private out-of-fold prediction outputs, but this export includes only aggregate summaries.

No row-level predictions, row-level labels, raw sequences, embeddings, split manifests, or group assignments are public. The dataset is not redistributed, and no dataset public availability claim is made.

## Scope

This report summarizes aggregate calibration, threshold, prioritization-at-k, and fold-level behavior across the existing P-SIGNAL evidence packages:

- P-SIGNAL-001 physicochemical baseline.
- P-SIGNAL-002 ESM-2 t12/35M.
- P-SIGNAL-003 ESM-2 t30/150M.

The shared benchmark context is 2,959 rows with 269 positives and 2,690 negatives under the `leakage_aware_group_stratified` split policy. The source-aware limitation and `max_pairs=10000` caveat from the existing benchmark context still apply.

## Key Aggregate Findings

- Best Brier score: P-SIGNAL-002 random forest, `0.051176`.
- Best expected calibration error: P-SIGNAL-001 random forest, `0.021510`.
- Best aggregate MCC: P-SIGNAL-002 random forest at threshold `0.35`, MCC `0.620665`.
- Best aggregate F1: P-SIGNAL-002 random forest at threshold `0.20`, F1 `0.640569`.
- Best k=50 precision: P-SIGNAL-003 random forest, `0.940000`.
- Best k=269 recall: P-SIGNAL-002 random forest, `0.635688`.

P-SIGNAL-002 random forest is strongest as a general aggregate default and ranking-first candidate queue. P-SIGNAL-003 random forest is strongest for a high-precision shortlist. P-SIGNAL-003 logistic regression and P-SIGNAL-002 logistic regression remain relevant for recall-oriented screening.

Calibration-sensitive probability use remains cautious. These are aggregate benchmark scores for candidate prioritization before experimental validation, not deployment-grade probabilities.

## Interpretation

Preferred model/classifier choice depends on the operating point. Ranking-first selection, high-precision shortlisting, recall-oriented screening, and calibration-sensitive use do not all point to the same row.

This is computational candidate prioritization evidence before experimental validation. It is not biological validation, not wet-lab validation, not in-vivo validation, not clinical evidence, not therapeutic efficacy evidence, not solved delivery, not universal delivery prediction, not state-of-the-art status, and not biological transport proof.

## Public Boundary

This export is aggregate-only. It does not include private paths, private infrastructure references, row-level identifiers, row-level artifacts, raw sequences, embeddings, split manifests, or group assignments.
