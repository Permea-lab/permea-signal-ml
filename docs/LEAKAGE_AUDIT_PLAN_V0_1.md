# Leakage Audit Plan v0.1

## Purpose

This document defines a future leakage audit plan for the current BBB-oriented benchmark dataset in `permea-signal-ml`.

This is a plan, not completed audit results. No leakage audit has been performed by this document. No leakage-free claim is made. No benchmark result is changed, no model rerun is performed, no metric value is changed, and no new scientific claim is added. The plan supports preprint-readiness planning by defining what must be checked before stronger public benchmark claims are made.

## Current dataset context

- Imported processed dataset path: `data/processed/legacy_bbb_dataset_with_features.csv`
- Rerun-ready processed dataset path: `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`
- Dataset config path: `configs/data/legacy_bbb_dataset_with_features.yaml`
- Raw source dataset path: unresolved in this repo; `data/raw/` has no raw source dataset file beyond `.gitkeep`
- Public/preprint dataset version: `pending_confirmation`
- Label-source criteria: unresolved beyond current benchmark-target usage
- Attribution/licensing: unconfirmed
- Current split policy: recovered random stratified folds using `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`

## Leakage risks to assess

### A. Exact duplicate sequence risk

Future audit should identify:

- repeated identical `sequence` values across the dataset
- repeated identical sequences with the same `label`
- repeated identical sequences with conflicting labels
- whether repeated sequences are assigned to different folds under the current split policy

### B. Near-duplicate risk

Future audit should identify:

- sequences differing by small edit distance
- short peptide variants where one or two edits may still represent a very similar candidate
- sequence variants that may share a source family, motif, or construction pattern
- whether near-duplicate pairs are split across train/test folds under the current split policy

### C. Sequence-similarity leakage risk

Future audit should assess whether high-similarity sequences appear across folds. In particular, it should test whether random `StratifiedKFold` may overestimate benchmark performance if highly similar, homologous, or motif-related sequences are distributed across train and test folds.

This audit should remain computational and dataset-structural. It should not be interpreted as biological validation.

### D. Label conflict risk

Future audit should identify:

- identical sequences with different labels
- highly similar sequences with conflicting labels
- source-dependent label inconsistency if source or family fields become available
- whether label conflicts are concentrated in particular sequence motifs or source groups

### E. Source/group leakage risk

Future audit should assess whether entries from the same source, family, motif group, or reconstructed origin are distributed across folds. The current `source` field is an operational rerun field and may be too coarse for group-aware leakage control. If future source or family identifiers are recovered, they should be considered candidate group labels for leakage-aware splitting.

## Proposed audit methods

These methods are proposed for a later implementation task. They are not run in this task.

- Exact sequence duplicate scan:
  - group by normalized `sequence`
  - count duplicate groups
  - report within-group label consistency
  - report whether duplicate groups cross current folds
- Duplicate label-conflict scan:
  - group by normalized `sequence`
  - flag groups containing both positive and negative labels
  - preserve `sequence_id`, `label`, and available source fields for later manual review
- Normalized sequence scan:
  - strip whitespace
  - standardize case
  - optionally flag noncanonical or ambiguous amino-acid characters
  - do not change source data in place
- Edit-distance or Levenshtein near-duplicate scan:
  - compute pairwise near-neighbor relationships within practical sequence-length bounds
  - prioritize short peptides because small edit counts may be meaningful
  - report near-duplicate pairs rather than editing or removing records
- k-mer Jaccard similarity scan:
  - compare sequence k-mer sets for configurable `k`
  - summarize high-similarity pairs and clusters
  - keep thresholds documented and adjustable
- Optional sequence identity thresholding:
  - compute aligned or simple identity where appropriate
  - evaluate thresholds such as 80%, 90%, and 95% identity as sensitivity settings
  - report results as audit evidence, not as biological interpretation
- Source-field group analysis:
  - evaluate whether the current `source` field is informative enough for grouping
  - if source labels are too coarse, document that limitation
  - if richer group labels are recovered later, rerun group analysis with those labels
- Fold-level leakage check against current `StratifiedKFold` setting:
  - reconstruct current folds with `n_splits=5`, `shuffle=True`, and `random_state=42`
  - determine whether duplicate, near-duplicate, or high-similarity groups cross folds
  - report fold-crossing counts and examples
- Alternative grouped split proposal:
  - define group-aware split options only if source, family, duplicate cluster, or similarity-cluster identifiers are sufficient
  - compare proposed split logic conceptually before any model rerun
- Future sensitivity analysis plan:
  - compare random stratified split against leakage-aware split only in a future benchmark task
  - treat any performance change as benchmark robustness evidence, not as biological validation

## Proposed future outputs

The following outputs are proposed for future audit tasks. They are not created by this plan and should not be treated as existing audit results unless a later task creates them.

- `results/audits/sequence_duplicate_audit.csv`
- `results/audits/label_conflict_audit.csv`
- `results/audits/near_duplicate_pairs.csv`
- `results/audits/sequence_similarity_summary.csv`
- `results/audits/fold_similarity_leakage_summary.csv`
- `results/audits/source_group_leakage_summary.csv`
- `docs/LEAKAGE_AUDIT_REPORT_V0_1.md`

## Impact on benchmark interpretation

Possible future audit outcomes should be interpreted as follows:

- If no major leakage risk is found, confidence in the current benchmark split improves, but biological validation is still not established.
- If exact duplicates with conflicting labels are found, dataset curation must be revised before public preprint claims are strengthened.
- If exact duplicates with the same label cross folds, current metrics may be optimistic and should be caveated or recomputed under duplicate-aware splitting.
- If near-duplicate or high-similarity sequences cross folds, current metrics should be treated as potentially optimistic until leakage-aware sensitivity analysis is performed.
- If grouped splits reduce performance, the manuscript should report leakage-aware results separately in a future benchmark update.
- If source grouping is insufficient, the limitation must remain explicit and public benchmark claims should remain conservative.
- If label conflicts are concentrated in specific sequence families or sources, label-source documentation and curation notes must be updated before public preprint use.

## Preprint-readiness decision rule

Before public preprint submission, the project should complete at least one of the following:

- run the leakage audit and document results in `docs/LEAKAGE_AUDIT_REPORT_V0_1.md`
- implement a leakage-aware split or sensitivity analysis if the audit identifies material leakage risk
- preserve a strong, explicit limitation if the audit cannot be completed before submission

The following block stronger public benchmark claims:

- unassessed duplicate or near-duplicate leakage presented as if controlled
- unassessed sequence-similarity leakage presented as if ruled out
- label conflicts left unexplained while reporting stronger benchmark claims
- source or group leakage ignored when source/family grouping is available

The following do not block trusted internal review:

- a clear plan for leakage audit
- explicit caveats that leakage has not yet been assessed
- use of current benchmark metrics as bounded computational evidence with limitations

## Suggested implementation sequence

| Task | Purpose | Expected output | What not to do |
|---|---|---|---|
| Task 030 — Commit Leakage Audit Plan | Close this plan artifact. | Committed leakage audit plan and index references. | Do not run audit checks. |
| Task 031 — Implement Leakage Audit Utilities | Add bounded scripts for duplicate, label-conflict, and similarity audit. | Audit utility scripts and dry-run documentation. | Do not change benchmark metrics or manuscript claims. |
| Task 032 — Run Leakage Audit and Generate Reports | Execute approved audit utilities. | Audit CSVs and `LEAKAGE_AUDIT_REPORT_V0_1.md`. | Do not rerun models unless separately approved. |
| Task 033 — Update Manuscript and Evidence Docs Based on Leakage Audit | Convert audit findings into claim-boundary and method updates. | Updated docs reflecting actual audit findings. | Do not overstate audit outcomes. |
| Task 034 — Reassess Preprint Readiness After Leakage Audit | Re-evaluate preprint status after audit closure. | Updated readiness memo or checklist. | Do not mark public preprint ready unless all blockers are addressed. |

## Non-goals

This plan is not:

- wet-lab validation
- a new biological claim
- a model performance improvement task
- a new benchmark result
- a completed leakage audit
- a public preprint submission package
- evidence that the dataset is leakage-free

