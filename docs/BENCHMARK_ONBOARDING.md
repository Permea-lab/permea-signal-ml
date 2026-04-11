# Benchmark Onboarding

## Title

Permea Signal ML Benchmark Onboarding Guide

## Purpose

This document explains how to onboard a real benchmark dataset into `permea-signal-ml` in a way that remains benchmark-oriented, provenance-aware, and suitable for reproducible baseline runs.

## What counts as a benchmark-ready dataset

A dataset should be treated as benchmark-ready only when the repository can state clearly:

- what the records represent
- what the label means
- where the data came from
- which version of the dataset is being used
- how the split policy is defined
- what licensing or redistribution constraints apply

## Required columns

Minimum required columns:

- `sequence_id`
- `sequence`
- `label`
- `source`

## Recommended optional columns

Recommended optional columns:

- `metadata`
- `split`
- `dataset_version`
- `source_license`
- `notes`

These may be represented as explicit columns or as linked documentation, but the baseline run must remain auditable.

## Provenance requirements

Before a dataset is used as benchmark evidence, the following should be documented:

- source dataset or publication
- original acquisition path
- dataset version or dated snapshot
- transformation or filtering steps
- processed dataset location used for runs

## Label definition requirements

The label must be documented explicitly.

This includes:

- what positive and negative labels mean
- whether labels are binary, thresholded, or derived
- what assumptions or exclusions were applied during label construction

## Split-policy documentation requirements

The split policy should be stated before results are treated as benchmark evidence.

This includes:

- cross-validation or holdout strategy
- random seed
- stratification policy
- grouping or source-aware split rules if leakage is a concern

## Licensing and attribution requirements

Before onboarding a real benchmark dataset, confirm:

- whether redistribution is allowed
- whether attribution or citation is required
- whether source restrictions require keeping only references rather than raw copies

## Expected output artifacts after a benchmark run

After a benchmark run, the repository should contain:

- metrics JSON
- predictions CSV
- ranking CSV
- summary CSV
- manifest JSON
- figure PNGs where relevant

## Pre-run checklist

- dataset path defined
- dataset version documented
- required columns validated
- label meaning documented
- split policy documented
- config files set
- licensing constraints checked

## Post-run checklist

- metrics exported
- predictions exported
- ranking exported
- summary exported
- manifest exported
- figures exported if generated
- output paths recorded
- run interpretation reviewed against repository limitations
