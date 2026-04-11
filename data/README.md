# Data Notes

## Purpose of the data directory

This directory holds dataset inputs and dataset-layer notes for Permea Signal ML. It is structured to support a transition from synthetic smoke tests toward versioned real benchmark datasets.

## Example datasets

The file `data/examples/example_sequences.csv` is a tiny synthetic example dataset used only for smoke testing the v0.1 baseline workflow.

- it is synthetic
- it is not benchmark evidence
- it is not biologically validated

## Future benchmark datasets

Real benchmark datasets should be versioned and documented separately from example data.

- raw sources should be preserved or referenced explicitly
- processed benchmark tables should be versioned
- benchmark labels and split policy should be documented alongside the dataset version

## Provenance expectations

- raw data provenance should be recorded before modeling outputs are treated as meaningful
- interim transformations should remain inspectable and reversible where practical
- processed tables should be tied to a dataset version or manifest reference
- run outputs should reference the dataset version used

## Licensing and attribution expectations

- source licensing constraints should be respected
- attribution or citation requirements should be preserved
- restricted or unclear data should not be redistributed casually
