# P-SIGNAL-002D Dry Run No-Model-Download Gate

Date: 2026-06-22

Task: P-SIGNAL-002D

## Purpose

This report records a public-safe dry-run gate for a future P-SIGNAL-002 ESM-2 / PLM representation comparison.

The gate validates config shape, planned model metadata, artifact boundaries, stop conditions, and public-safe output categories before any execution task is approved.

## Non-Execution Boundary

This task is a dry-run gate only.

- No model weights are downloaded.
- No model weight downloads occur.
- No PLM model is loaded.
- No model inference is run.
- No embeddings are generated.
- No training is run.
- No experiments are run.
- No row-level data is read by the dry-run script.

P-SIGNAL-002 execution still requires explicit approval in a separate future task.

## Public-Safe Files

- `scripts/p_signal_002_dry_run.py`
- `configs/p_signal_002_dry_run.example.json`
- `tests/test_p_signal_002_dry_run_gate.py`
- `docs/reports/p-signal-002d-dry-run-no-model-download-gate.md`

The example config uses placeholders only. It does not include private paths, raw sequences, row-level data, model cache locations, or private run directories.

## Gate Coverage

The dry-run script validates:

- expected dataset SHA metadata is present
- the model ID is one of the approved ESM-2 plan-only IDs
- the primary recommended model is represented as metadata
- private outputs and public-safe aggregate candidates are separated
- public-safe candidates do not include row-level artifacts
- private-only artifacts include row-level dataset, raw sequences, split manifests, group assignments, row-level embeddings, per-row predictions, sequence-pair leakage files, model cache paths, and private compute paths
- public-safe candidates are limited to aggregate model-comparison metrics, aggregate per-fold metrics, aggregate leakage summary, no-private-path run manifest, claim-bounded report, and public tests confirming no row-level leakage
- stop conditions are present

## Output Boundary

Private-only artifacts:

- row-level dataset
- raw sequences
- split manifests
- group assignments
- row-level embeddings
- per-row predictions
- sequence-pair leakage files
- model cache paths
- private compute paths

Public-safe candidates after review:

- aggregate model-comparison metrics
- aggregate per-fold metrics
- aggregate leakage summary
- no-private-path run manifest
- claim-bounded report
- public tests confirming no row-level leakage

Public artifacts must remain aggregate-only candidates until a separate review confirms they contain no row-level data, no private paths, and no unsupported claims.

## Claim Discipline

This gate does not claim:

- wet-lab validation
- in-vivo validation
- clinical relevance
- therapeutic efficacy
- solved delivery
- universal delivery prediction
- state-of-the-art status
- dataset redistribution rights

Any future public report must keep the framing to computational, aggregate, leakage-controlled candidate-prioritization evidence before experimental validation.

## Future Gate

Recommended next task:

`P-SIGNAL-002D Review / Merge Gate`.

Only after that review should a separate execution-gate task consider model weight download and embedding generation.
