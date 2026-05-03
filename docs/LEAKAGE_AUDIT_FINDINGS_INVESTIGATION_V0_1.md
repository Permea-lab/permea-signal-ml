# Leakage Audit Findings Investigation v0.1

## Purpose

This memo investigates the first leakage audit outputs generated for the current rerun-ready processed BBB-oriented benchmark dataset.

This is not a new benchmark result, not model performance analysis, and not biological validation. It does not change existing metrics, does not claim leakage-free status, does not rerun baseline models, and does not add wet-lab, therapeutic, or clinical claims.

## Inputs

- `docs/LEAKAGE_AUDIT_REPORT_V0_1.md`
- `results/audits/sequence_duplicate_audit.csv`
- `results/audits/label_conflict_audit.csv`
- `results/audits/near_duplicate_pairs.csv`
- `results/audits/sequence_similarity_summary.csv`
- `results/audits/fold_similarity_leakage_summary.csv`
- `results/audits/source_group_leakage_summary.csv`
- `results/audits/leakage_audit_summary.json`
- `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`, inspected read-only for labels, source values, sequence IDs, sequence lengths, and reconstructed fold IDs

## Investigation summary

### Exact duplicates

The audit reported 4 exact duplicate sequence groups:

| Normalized sequence | Count | Labels | Reconstructed folds | Sequence IDs | Interpretation |
|---|---:|---|---|---|---|
| `NTGSPYE` | 2 | `1` only | 2, 3 | `legacy_bbb_000045`, `legacy_bbb_000052` | Same-label duplicate crossing folds. |
| `RGGRLSYSRRRFSTSTGR` | 2 | `1` only | 2, 4 | `legacy_bbb_000185`, `legacy_bbb_000190` | Same-label duplicate crossing folds. |
| `RQIKIWFQNRRMKWKK` | 2 | `1` only | 3, 4 | `legacy_bbb_000177`, `legacy_bbb_000179` | Same-label duplicate crossing folds. |
| `YGRKKRRQRRR` | 2 | `1` only | 2, 5 | `legacy_bbb_000115`, `legacy_bbb_000123` | Same-label duplicate crossing folds. |

These are not label contradictions. They are still possible fold leakage because identical sequences appear in different reconstructed folds. Future handling should either group duplicates before splitting, deduplicate them, or explicitly caveat that random stratified metrics may be optimistic.

### Label conflicts

The exact label-conflict audit reported 0 identical-sequence label-conflict groups. The audit groups normalized sequences, so this result applies after the implemented simple normalization step.

This lowers the severity of exact duplicate curation risk, but it does not validate the labels. The original label-source criteria remain partially unresolved, and near-duplicate label conflict is a separate question.

### Near-duplicates

The edit-distance audit reported 73 near-duplicate pairs at the configured threshold. Read-only investigation found:

- 73 of 73 near-duplicate pairs were same-label pairs.
- 0 of 73 near-duplicate pairs were mixed-label pairs.
- 56 of 73 near-duplicate pairs crossed reconstructed folds.
- 45 pairs had a shorter sequence length of 8 residues or fewer.
- 16 pairs had a shorter sequence length from 9 to 15 residues.
- 12 pairs had a shorter sequence length greater than 15 residues.

The near-duplicate pairs are not evidence of label disagreement. They are evidence that similar sequences, often short peptides where one edit can be proportionally large, are present across folds. This is enough to caveat random-stratified benchmark interpretation and motivate leakage-aware sensitivity analysis.

Frequently recurring near-duplicate sequence neighborhoods included variants around `YAFEVVG`, `VQIYK`, `VQIIYK`, `VQILYK`, `VQITYK`, `VQIVYK`, `YAGFL`, `YAFQVVG`, `YAFSVVG`, `YGGFL`, `YAGFLR`, and `YGGFLR`.

### High k-mer similarity

The k-mer Jaccard audit reported 33 high-similarity pairs at `k=3` and Jaccard threshold `0.8`. Read-only investigation found:

- 33 of 33 high-similarity pairs were same-label pairs.
- 0 of 33 high-similarity pairs were mixed-label pairs.
- 29 of 33 high-similarity pairs crossed reconstructed folds.
- 23 pairs overlapped with the near-duplicate pair set.
- 11 pairs had a shorter sequence length of 8 residues or fewer.
- 12 pairs had a shorter sequence length from 9 to 15 residues.
- 10 pairs had a shorter sequence length greater than 15 residues.

The high-similarity audit reinforces the near-duplicate finding. It does not show label conflict, but it shows that a random fold policy can place highly similar sequence records on both sides of a train/test boundary.

### Cross-fold high similarity

The fold-level audit reported 29 cross-fold high-similarity pairs. Read-only investigation found:

- 29 of 29 cross-fold high-similarity pairs were same-label pairs.
- 0 of 29 were mixed-label pairs.
- Fold-pair counts were: 3-4: 6, 2-5: 6, 2-4: 4, 2-3: 3, 4-5: 3, 1-4: 2, 1-2: 2, 3-5: 2, 1-3: 1.
- 19 of the cross-fold high-similarity pairs also appeared in the edit-distance near-duplicate set.

This is the strongest leakage-relevant finding in the current audit. It does not prove that reported model metrics are invalid, but it is sufficient to treat the current random-stratified metrics as potentially optimistic until a duplicate-aware or similarity-aware split sensitivity analysis is performed.

### Source/group leakage

The dataset contains one observed source value in the inspected field: `legacy_bbb_import`. That source value spans all 5 reconstructed folds:

- Fold 1: 592 rows
- Fold 2: 592 rows
- Fold 3: 592 rows
- Fold 4: 592 rows
- Fold 5: 591 rows

This source field is too coarse for meaningful source-aware group splitting. A useful group-aware split would require richer metadata such as original source, assay source, literature/source dataset identifier, peptide family, motif cluster, source accession, or a sequence-similarity cluster identifier. In the absence of richer metadata, sequence-similarity grouping can serve as a practical proxy for future sensitivity analysis.

## Severity assessment

| Area | Severity | Rationale |
|---|---|---|
| Exact duplicates | Moderate | Same-label only, but all 4 duplicate groups cross reconstructed folds. |
| Label conflicts | Low | No identical-sequence label-conflict groups detected under normalized exact matching. |
| Near-duplicates | Moderate | Same-label only, but 56 of 73 pairs cross reconstructed folds and many involve short peptides. |
| Cross-fold high similarity | Moderate | 29 same-label high-similarity pairs cross folds; this creates plausible random-split optimism risk. |
| Source/group leakage | Inconclusive | Current source field has only one coarse value and cannot support meaningful group leakage assessment. |
| Overall benchmark optimism risk | Moderate | Findings support caveated reporting and leakage-aware follow-up, not rejection of all current metrics. |

## Impact on manuscript claims

Current metrics can still be reported as random-stratified baseline metrics if the methods and limitations are explicit. They should not be presented as robust generalization evidence.

Recommended claim boundary:

- report current metrics as random-stratified baseline results
- state that duplicate and high-similarity sequence structure was detected
- caveat that current metrics may be optimistic under similarity-aware splitting
- avoid saying the dataset is leakage-free
- avoid treating this audit as biological validation
- reserve stronger benchmark robustness claims for a future leakage-aware split or sensitivity analysis

## Required next actions

### Before committing audit outputs

- No output schema refinement is required before committing the current audit outputs.
- Commit the generated audit outputs, leakage audit report, and this investigation memo together.
- Preserve the current conservative interpretation.

### Before updating manuscript

- Decide whether manuscript/evidence docs should mention the exact audit counts directly or cite the audit report only.
- Update leakage caveats to state that duplicate and sequence-similarity risks are measured rather than unassessed.
- Avoid adding new benchmark performance claims.

### Before public preprint

- Add clear leakage-audit limitations to the manuscript and supplement.
- Either run a leakage-aware split or similarity-aware sensitivity analysis, or explicitly state that random-stratified metrics may be optimistic.
- Resolve or continue disclosing dataset provenance, attribution/licensing, and label-source limitations.

### Before public deck/partner use

- Do not convert current metrics into delivery success probabilities.
- Avoid presenting current random-stratified metrics as robust generalization.
- Keep public material aligned with leakage-risk caveats and no-wet-lab-validation boundaries.

## Recommended next Codex task

Task 035 — Commit Leakage Audit Outputs and Investigation Report

Rationale: the generated outputs appear valid for the configured first-run audit, the interpretation is conservative, and the next step is repository hygiene closure before manuscript/evidence updates.
