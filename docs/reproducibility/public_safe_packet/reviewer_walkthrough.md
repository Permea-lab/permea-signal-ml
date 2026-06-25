# Reviewer Walkthrough

This walkthrough is written for a scientifically serious outsider and remains public-safe. It describes how to inspect aggregate reproducibility surfaces without assuming access to private row-level material.

## Step 1: Identify Repos And Commits

Use the public repository paths and baseline commits in `public_artifact_manifest.md`. The relevant public aggregate evidence is in `permea-signal-ml` at commit `8ea31ddf3f5f70319b8a275753980ce11cfea3cc`; `permea-core` is a read-only public reference at commit `e6ed1b53c25103f73a82710cdb22d6f2bd65aa6c`.

## Step 2: Inspect Public Artifact Manifest

Review `public_artifact_manifest.md` to identify aggregate reports, aggregate CSV/JSON summaries, public-safe figures, figure manifests, and public validation tests.

## Step 3: Run Validation Commands

Use `validation_commands.md` to run public validation tests from the public repo if the local environment is prepared. Treat documented prior pass counts as historical baseline unless you personally rerun the command.

## Step 4: Compare Expected Output Summary

Use `expected_output_summary.md` to compare the aggregate counts and key metrics. Interpret these values as benchmark-label and aggregate evaluation summaries only.

## Step 5: Inspect Checksum/Shape Summaries

Use `aggregate_result_checksum_shape_summary.md` to verify file hashes, byte sizes, CSV shapes, CSV column names, and JSON top-level key summaries for already-public aggregate result files.

## Step 6: Inspect Public-Safe Figures

Use `figure_manifest_summary.md` and the public `figures/p_signal_figures/` directory to inspect the public-safe aggregate and metadata-level figures. Do not treat these as final publication figures.

## Step 7: Apply Claim Boundary Checklist

Use `claim_boundary_checklist.md` before citing or reviewing claims. The allowed claims are computational, aggregate, and bounded. The forbidden claims remain unsupported.

## Step 8: Understand Limitations Before Citing Or Reviewing Claims

This packet does not provide row-level data, sequences, labels, predictions, embeddings, split internals, new model outputs, calibration recomputation, threshold sweep recomputation, wet-lab validation, or independent validation. Cite it only as a public-safe aggregate reproducibility map.
