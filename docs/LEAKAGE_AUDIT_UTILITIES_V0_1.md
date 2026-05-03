# Leakage Audit Utilities v0.1

## Purpose

This document describes the leakage-audit utilities implemented for `permea-signal-ml`.

The utilities support future duplicate, label-conflict, near-duplicate, sequence-similarity, fold-leakage, and source/group leakage audits. Implementing these utilities is not the same as completing the leakage audit. No leakage-free claim is made by this document, and no benchmark metric or manuscript claim is changed by the utility implementation.

## Implemented components

- `src/permea_signal_ml/audits/leakage.py` — reusable audit functions
- `scripts/audit_leakage.py` — CLI wrapper with dry-run support
- `tests/test_leakage_audit.py` — small fixture-based unit tests

## What the utilities do

- load and validate a CSV dataset with at least `sequence` and `label`
- normalize sequences conservatively by stripping whitespace and uppercasing
- identify exact duplicate sequence groups
- identify identical sequence groups with conflicting labels
- identify near-duplicate sequence pairs using bounded edit distance
- identify high-similarity pairs with k-mer Jaccard similarity
- reconstruct random stratified fold IDs for audit purposes only
- summarize high-similarity pairs that cross folds
- summarize source/group distribution across folds when a source column is present
- write audit outputs only when the CLI is run without `--dry-run`

## What the utilities do not do

- they do not run baseline models
- they do not change metric values
- they do not modify input data files
- they do not modify existing result or figure artifacts
- they do not establish biological validation
- they do not establish that the dataset is leakage-free
- they do not make the public preprint ready

## Dry-run command

Use dry-run mode to validate inputs and preview planned outputs without writing audit files:

```bash
python scripts/audit_leakage.py \
  --input data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv \
  --output-dir results/audits \
  --dry-run
```

Dry-run mode reports the input row count, input columns, and planned output paths. It does not create `results/audits` and does not write audit CSV or JSON files.

## Full audit command for a future task

A future approved audit task can run:

```bash
python scripts/audit_leakage.py \
  --input data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv \
  --output-dir results/audits \
  --sequence-col sequence \
  --label-col label \
  --source-col source \
  --n-splits 5 \
  --random-state 42 \
  --kmer-size 3 \
  --jaccard-threshold 0.8 \
  --max-pairs 10000
```

That future run would create audit outputs. It should be paired with a review task that interprets outputs conservatively and updates documentation only after inspecting the generated files.

## Planned output files

When the full audit is explicitly run, the utility writes:

- `results/audits/sequence_duplicate_audit.csv`
- `results/audits/label_conflict_audit.csv`
- `results/audits/near_duplicate_pairs.csv`
- `results/audits/sequence_similarity_summary.csv`
- `results/audits/fold_similarity_leakage_summary.csv`
- `results/audits/source_group_leakage_summary.csv`
- `results/audits/leakage_audit_summary.json`

These files are not created by utility implementation alone.

## First audit run status

A first approved audit run has generated outputs under `results/audits/` and a conservative report at `docs/LEAKAGE_AUDIT_REPORT_V0_1.md`.

The existence of these outputs does not establish that the dataset is leakage-free and does not change benchmark metric values. The report should be read before making manuscript, preprint-readiness, or benchmark-interpretation updates.

## Limitations

- Edit-distance and k-mer Jaccard checks are heuristic sequence-similarity screens.
- Pairwise scans can be expensive on larger datasets; `--max-pairs` limits output rows but does not replace careful scaling review.
- The current `source` field is operational metadata and may be too coarse for source-aware split control.
- Fold reconstruction uses the current random stratified split policy for audit only; it does not train models.
- Any future audit findings must be reviewed before changing manuscript or preprint-readiness status.

## Claim boundary

These utilities are infrastructure for future audit work. They are not completed audit results, not biological validation, not a new benchmark result, and not evidence that leakage has been ruled out.
