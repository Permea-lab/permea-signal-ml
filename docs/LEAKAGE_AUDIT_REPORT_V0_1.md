# Leakage Audit Report v0.1

## Purpose

This report summarizes the leakage audit run for the current rerun-ready processed BBB-oriented benchmark dataset.

This is a computational dataset audit only. It is not biological validation, does not prove the dataset is leakage-free, does not change benchmark metric values, and does not rerun baseline models. The audit outputs should be interpreted as dataset-structure evidence for review and preprint-readiness planning, not as new model-performance results.

## Inputs

- Input dataset path: `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`
- Audit output directory: `results/audits`
- Sequence column: `sequence`
- Label column: `label`
- Source column: `source`
- Split policy reconstructed for audit: `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`
- Random state: `42`
- k-mer size: `3`
- Jaccard threshold: `0.8`
- Maximum reported pairs per pairwise audit: `10000`

## Generated outputs

| Output file | Exists? | Notes |
|---|---:|---|
| `results/audits/sequence_duplicate_audit.csv` | yes | Exact duplicate sequence groups. |
| `results/audits/label_conflict_audit.csv` | yes | Header only; no label-conflict groups reported. |
| `results/audits/near_duplicate_pairs.csv` | yes | Edit-distance near-duplicate pairs. |
| `results/audits/sequence_similarity_summary.csv` | yes | High k-mer Jaccard pairs at configured threshold. |
| `results/audits/fold_similarity_leakage_summary.csv` | yes | High k-mer Jaccard pairs crossing reconstructed folds. |
| `results/audits/source_group_leakage_summary.csv` | yes | Source values distributed across reconstructed folds. |
| `results/audits/leakage_audit_summary.json` | yes | Machine-readable summary counts and output list. |

## Summary findings

| Check | Finding | Count | Conservative interpretation |
|---|---|---:|---|
| Exact duplicate sequences | Duplicate sequence groups were detected. | 4 groups | Duplicates exist and should be acknowledged or handled before stronger public benchmark claims. |
| Duplicate label conflicts | No identical-sequence label-conflict groups were reported. | 0 groups | This reduces one curation concern under this exact-sequence check, but does not validate labels. |
| Near-duplicate pairs | Near-duplicate pairs were reported by bounded edit-distance scan. | 73 pairs | Similar short peptides exist and may affect split-level independence. |
| High k-mer similarity pairs | High-similarity pairs were reported at `k=3`, Jaccard `>=0.8`. | 33 pairs | This heuristic screen identifies sequence-similarity structure that should be caveated. |
| Cross-fold high-similarity pairs | High-similarity pairs crossed reconstructed folds. | 29 pairs | Current random stratified folds may contain related sequences across train/test partitions. |
| Source/group distribution | The operational source value appears in all reconstructed folds. | 5 source/fold rows | The current `source` field is too coarse to resolve group leakage by itself. |

The reported pair counts are below the configured `max_pairs=10000` cap, so the reported outputs were not truncated by that cap in this run.

## Interpretation boundaries

- Absence of detected issue under one check does not prove absence of all leakage.
- Edit-distance and k-mer Jaccard methods are heuristic sequence-similarity screens.
- Threshold choices affect sensitivity and specificity.
- Cross-fold findings depend on reconstructed fold IDs using the current documented split policy.
- Source/group conclusions depend on the quality of the `source` field; the current field appears operational and coarse.
- This audit does not establish biological validation, wet-lab validation, therapeutic efficacy, clinical efficacy, or broad biological generalization.

## Impact on current benchmark interpretation

Impact: leakage risk detected; current metrics may be optimistic.

The audit did not find exact duplicate label conflicts, but it did identify exact duplicate sequence groups, near-duplicate pairs, high k-mer similarity pairs, and cross-fold high-similarity pairs. These findings do not invalidate the current benchmark outright, but they strengthen the need to present the current metrics as baseline-oriented computational evidence with leakage-risk caveats. A future leakage-aware split or sensitivity analysis would be needed before stronger public benchmark robustness claims.

## Impact on preprint readiness

Impact: still requires caveated reporting.

This audit improves preprint-readiness planning because leakage risks are now measured under documented checks rather than merely unassessed. Public preprint use still requires careful caveated reporting, and stronger benchmark claims should wait for either leakage-aware sensitivity analysis or explicit disclosure that sequence-similarity leakage may make current metrics optimistic.

## Post-audit investigation note

Follow-up investigation is documented in `docs/LEAKAGE_AUDIT_FINDINGS_INVESTIGATION_V0_1.md`.

The investigation found that the exact duplicates, near-duplicate pairs, and high-similarity pairs reported by the first audit were same-label pairs in the inspected dataset. However, all exact duplicate groups and many near-duplicate or high-similarity pairs crossed reconstructed folds. The conservative interpretation remains that current random-stratified metrics can be reported as baseline metrics, but they may be optimistic and should not be presented as robust generalization evidence without leakage-aware sensitivity follow-up.

## Recommended manuscript/document updates

The following documents may need later updates based on this audit:

- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/DATASET.md`
- `docs/FIRST_EVIDENCE_SUMMARY.md`
- `docs/V0_1_EVIDENCE_PACKAGE.md`
- `docs/SUPPLEMENTARY_OUTLINE_V0_1.md`
- `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`

Recommended update direction:

- Replace unresolved leakage-audit language with measured but conservative audit language.
- State that duplicate and similarity structure was detected under the current audit.
- Avoid saying the dataset is leakage-free.
- Avoid treating audit outputs as new benchmark results or biological validation.
- Preserve the need for leakage-aware sensitivity analysis before stronger public benchmark claims.

## Recommended next maintainer task

Task 034 — Investigate Leakage Audit Findings

Rationale: the audit produced real duplicate, near-duplicate, high-similarity, and cross-fold high-similarity findings. Before committing broader manuscript updates, the next task should inspect these findings and decide whether they require curation notes, leakage-aware sensitivity planning, or immediate claim-boundary edits.

## No-change confirmation

- Data files were not modified.
- Existing result artifacts outside `results/audits/` were not modified.
- Figure artifacts were not modified.
- Baseline models were not rerun.
- Benchmark metric values were not changed.
- No leakage-free claim is made.
