# Paper Package v0.1

## Purpose

This document organizes the current `permea-signal-ml` evidence surface into a paper-support structure for future preprint drafting. It is not a full paper. It is the first compact planning layer that ties the current evidence package, methods surface, and figure assets into a draft-ready scientific outline.

The first manuscript-facing draft built from this package is [PREPRINT_SKELETON_V0_1.md](./PREPRINT_SKELETON_V0_1.md). The first full prose manuscript draft is [PREPRINT_DRAFT_V0_1.md](./PREPRINT_DRAFT_V0_1.md). Assembly planning is documented in [PREPRINT_ASSEMBLY_V0_1.md](./PREPRINT_ASSEMBLY_V0_1.md), and supplementary planning is documented in [SUPPLEMENTARY_OUTLINE_V0_1.md](./SUPPLEMENTARY_OUTLINE_V0_1.md).

## Working paper framing

The current paper framing should remain narrow. The repository currently supports initial computational evidence that permeability-related signal is learnable from sequence-derived physicochemical features in a BBB-oriented peptide benchmark surface. The strongest supported interpretation is benchmark-oriented candidate prioritization before experimental validation.

## Candidate title options

- Initial Computational Evidence for Permeability-Related Signal in a BBB-Oriented Peptide Benchmark
- Benchmark-Oriented Candidate Prioritization for BBB-Related Peptide Delivery Signal
- Sequence-Derived Physicochemical Features as a Basis for BBB-Oriented Delivery-Signal Prioritization
- A BBB-Oriented Evidence Package for Permeability-Related Signal from Sequence-Derived Features

## Abstract skeleton

- background: Biological delivery remains difficult to compare across datasets, methods, and pipelines, especially when benchmark structure and provenance are weak.
- question: We asked whether permeability-related signal could be detected from sequence-derived physicochemical features in a BBB-oriented peptide benchmark surface.
- methods: We organized an imported legacy dataset into a current-contract rerun workflow and evaluated Dummy, Logistic Regression, and Random Forest baselines under recovered benchmark-style settings.
- results: Trivial baseline behavior was recovered as expected under class imbalance, while non-trivial baselines showed signal above that floor on the present benchmark surface.
- interpretation: These results support bounded computational candidate-prioritization utility before wet-lab validation.
- limitation: The current package does not establish experimental validation, mechanistic causality, or broad biological generalization.

## Introduction logic

1. biological delivery remains a major bottleneck
2. sequence-first framing is still underdeveloped in a standardized public benchmark form
3. benchmark-first computational evidence can help structure early delivery questions
4. the present work provides an initial bounded BBB-oriented evidence package

## Current evidence assets

- [Dataset documentation](./DATASET.md)
- [First evidence summary](./FIRST_EVIDENCE_SUMMARY.md)
- [v0.1 evidence package](./V0_1_EVIDENCE_PACKAGE.md)
- [Model comparison summary CSV](../results/tables/model_comparison_summary.csv)
- [Regenerated RF feature importance CSV](../results/tables/regenerated_rf_feature_importance.csv)
- [Regenerated RF feature importance figure](../figures/regenerated_rf_feature_importance.png)
- [Metrics export workflow](../scripts/export_metrics.py)
- [Figure generation workflow](../scripts/generate_figures.py)

## Methods / dataset references

- current dataset surface: [docs/DATASET.md](./DATASET.md)
- methods and repository workflow notes: [docs/METHODS.md](./METHODS.md)
- current reruns follow benchmark-contract-aligned outputs through metrics, predictions, ranking, summary, and manifest artifacts
- current feature surface: `length`, `charge`, `gravy`, `pI`, `aromaticity`
- recovered split policy and seed: `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`

## Figure package

Already available:

- [dataset_distribution.png](../figures/dataset_distribution.png)
- [legacy_vs_rerun_metrics.png](../figures/legacy_vs_rerun_metrics.png)
- [regenerated_rf_feature_importance.png](../figures/regenerated_rf_feature_importance.png)
- [candidate_ranking_preview.png](../figures/candidate_ranking_preview.png)
- [benchmark_workflow_outputs.png](../figures/benchmark_workflow_outputs.png)

Still pending or potentially useful:

- a compact regenerated-only model comparison figure
- appendix-ready legacy versus regenerated artifact mapping figure if later needed

## Imported vs regenerated appendix note

Any future paper, appendix, or supplementary package should preserve the distinction between imported historical artifacts and regenerated current-contract benchmark artifacts. Imported materials are useful for continuity and comparison, but regenerated artifacts define the current benchmark evidence surface.

## Limitations and claim boundary

The current package does not establish:

- experimental validation
- mechanistic causality
- universal BBB prediction
- broad delivery generalization

The current package does support:

- initial computational evidence
- bounded candidate-prioritization utility
- benchmark-oriented reproducible comparison

## Immediate next steps toward a preprint

- close remaining provenance gaps
- regenerate additional publication-support figures where needed
- align methods wording across docs and figure captions
- prepare appendix language for imported versus regenerated artifacts
- connect the benchmark surface to a future validation pathway without overstating current evidence
