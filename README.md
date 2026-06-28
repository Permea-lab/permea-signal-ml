# Permea Signal ML

**A construct-validity audit of blood–brain barrier (BBB) peptide benchmarks.**

This repository asks a single question: *do published BBB-peptide predictors measure
BBB penetration, or do they measure how their benchmarks were built?* It provides a
fixed, reproducible evaluation harness, a cross-dataset provenance auditor, and the
aggregate findings that follow from them.

It is an **honest-evaluation** package, not a new predictor and not a wet-lab claim.
The model is CASP-style: the contribution is rigorous, shared evaluation infrastructure
for a problem where benchmark construction has not yet had that scrutiny.

> Repositioning note (2026-06): this repository previously framed itself as an early
> "evidence package" demonstrating that BBB signal is learnable from sequence features.
> It is being repositioned around the audit question above. Earlier manuscript drafts in
> `docs/` predate this direction and are being revised; treat this README as the current
> scope of record.

## Relationship to Permea Core

[Permea Core](https://github.com/Permea-lab/permea-core) defines the broader open
infrastructure for sequence-first delivery: benchmark contracts, dataset/evidence
conventions, run manifests, and claim boundaries. **Permea Signal ML** applies that
foundation to the first concrete audit surface — the standard BBB peptide benchmark —
and reports what an identity-controlled, provenance-aware re-evaluation finds.

## The audit question

Standard BBB peptide benchmarks pair a small set of curated positive peptides against
randomly chosen negatives, and predictors are scored with random train/test splits. Two
things follow that are rarely checked:

- **Shared-source provenance.** Different "datasets" draw their positives from the same
  few archives, so they are not independent.
- **Similarity leakage.** Random splits place near-duplicate peptides in both train and
  test, so a model can score well by memorizing rather than generalizing.

This repository measures these directly and reports the results as aggregate, reproducible
artifacts.

## First public finding: cross-dataset positive overlap

The standard B3Pred Dataset_3 positives and the independent Brainpeps archive are largely
the **same pool of peptides**:

- 54.0% of Brainpeps positives appear **verbatim** in B3Pred; 82.5% as near-duplicates
  (identity ≥ 0.9).
- 88.3% of B3Pred positives have a near-duplicate in Brainpeps.

These figures are stable across identity thresholds and comparator definitions. Full
tables, sensitivity sweeps, and provenance notes are in
[`results/cross_dataset_overlap/`](results/cross_dataset_overlap/); the tool is
[`scripts/cross_dataset_overlap.py`](scripts/cross_dataset_overlap.py). The leakage and
representation analyses are described in the accompanying manuscript (under revision).

## What this repository contains

- a fixed evaluation harness contrasting random-split vs identity-controlled grouped CV
- a cross-dataset positive-overlap / provenance auditor (aggregate-only)
- leakage-aware grouping and split-construction utilities
- sequence-derived physicochemical feature extraction and transparent baselines
  (Dummy, Logistic Regression, Random Forest)
- aggregate metrics, sensitivity outputs, and figures
- tests for data validation, leakage audits, grouping, split construction, and baselines
- manuscript and supplement support files (being revised to the audit framing)

## The benchmark under audit

The audited surface follows B3Pred Dataset_3:

- 269 BBB-positive peptides, 2,690 non-BBB negatives (2,959 total)
- sequence-derived fields: `length`, `charge`, `gravy`, `pI`, `aromaticity`
- the negatives are random Swiss-Prot proteins (keyword-filtered), not experimentally
  validated non-penetrators — itself one of the audit's points

The `label` is treated as a benchmark label with provenance and limitations, not as
independently verified biological truth.

## What this repository does NOT claim

- no new predictor and no state-of-the-art claim
- no claim that prior predictors are worthless — it characterizes *what the benchmark
  measures*, not whether the methods are well built
- no wet-lab validation, clinical, or therapeutic-effect claim
- no claim of complete leakage control or robust generalization
- no public release of row-level processed datasets, predictions, split manifests, or
  group assignments

## Suggested usage

Install dependencies:

```
python3 -m pip install -r requirements.txt
```

Run the tests:

```
python3 -m pytest tests -q
```

Validate the overlap tool, then run it on staged positive sets:

```
python3 scripts/cross_dataset_overlap.py --selftest
python3 scripts/cross_dataset_overlap.py \
  --dataset b3pred=<b3pred_positives.csv>:sequence \
  --dataset brainpeps=<brainpeps_positives.csv>:sequence \
  --tau 0.9 --out results/cross_dataset_overlap/overlap
```

Inspect the leakage-aware evaluation and baseline entrypoints under `scripts/`.

## Reproducibility framing

- dataset and label assumptions are documented before any modeling claim
- feature extraction is narrow and sequence-derived
- baselines are transparent and configurable
- aggregate metrics, audits, and sensitivity outputs are stored as reviewable artifacts
- identity conventions are stated explicitly (overlap uses LCS / shorter-length)
- limitations are explicit and repeated across public-facing docs

Row-level processed datasets, predictions, rankings, split manifests, and group
assignments may require separate release review before any redistribution.

## Status

Active early-stage open audit package. The first aggregate finding (cross-dataset
overlap) is in `results/`; the evaluation harness and leakage-aware utilities are in
`scripts/`; the manuscript is being revised to the audit framing. Public posting of any
result remains subject to source-to-claim review and release review.

## License

Apache-2.0. See [LICENSE](LICENSE).
