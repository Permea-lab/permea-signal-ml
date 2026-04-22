# Preprint Skeleton v0.1

## Purpose

This document is the first manuscript-facing draft structure for the current BBB-oriented Permea wedge. It is built from the existing v0.1 evidence package, the current regenerated benchmark artifacts, and the repository's current dataset and provenance documentation. Its purpose is to give future drafting work a concrete manuscript skeleton without overstating the maturity of the evidence.

## Current paper scope

The current paper scope is deliberately narrow. It is focused on BBB-oriented peptide / permeability-related signal, a sequence-derived physicochemical feature surface, baseline benchmark reruns, and candidate prioritization before experimental validation.

Out of scope for the present manuscript are experimental validation, broad delivery generalization, clinical interpretation, and mechanistic causality claims. The intended contribution is a bounded computational evidence package rather than a claim of validated biological performance.

## Candidate titles

- Initial Computational Evidence for Permeability-Related Signal in a BBB-Oriented Peptide Benchmark
- Benchmark-Oriented Candidate Prioritization for BBB-Related Peptide Delivery Signal
- Sequence-Derived Physicochemical Features for BBB-Oriented Delivery-Signal Prioritization
- A Benchmark-Oriented Evidence Package for BBB-Related Peptide Signal Prioritization
- Initial Benchmark Evidence for BBB-Oriented Peptide Candidate Prioritization from Sequence-Derived Features

## Draft abstract

Biological delivery remains a major bottleneck in the development of next-generation therapeutics, yet early computational work in this area is often difficult to compare because datasets, evaluation rules, and artifact standards are inconsistently documented. A sequence-first computational framing may help structure earlier-stage candidate prioritization, but its value depends on benchmark-aware and provenance-aware evidence surfaces. Here we present an initial BBB-oriented computational evidence package built from an imported legacy peptide dataset and regenerated under a current benchmark contract. The current feature surface is limited to sequence-derived physicochemical descriptors: length, charge, gravy, pI, and aromaticity. Baseline reruns include a Dummy most-frequent classifier, Logistic Regression, and Random Forest under recovered benchmark-style settings. The class-prior baseline behaves as expected under strong class imbalance, while Logistic Regression and Random Forest show non-trivial signal above that floor, with ROC-AUC values of approximately 0.8605 and 0.8489 and PR-AUC values of approximately 0.4903 and 0.5002, respectively. These results support a bounded interpretation: sequence-derived physicochemical features appear sufficient to support benchmark-oriented candidate prioritization before wet-lab validation on the current BBB-oriented wedge. The primary contribution of the present work is therefore not biological validation, but a reproducible and inspectable evidence package that separates imported historical artifacts from regenerated current-contract benchmark artifacts. The current package remains limited by incomplete provenance closure, a narrow feature surface, and the absence of experimental validation.

## Draft introduction

Biological delivery remains a central constraint in the development of many next-generation therapeutic modalities. Barriers such as the cell membrane and the blood-brain barrier continue to limit effective transport, and these constraints create a practical need for earlier-stage prioritization methods that can narrow candidate sets before more costly downstream evaluation.

Despite that need, computational work related to delivery signal is often difficult to compare across datasets, groups, and internal pipelines. Task definitions vary, provenance is frequently incomplete, and reported outputs are commonly detached from the exact dataset surface, split policy, and artifact package that produced them. This makes it difficult to judge whether adjacent results are genuinely comparable.

A sequence-first framing is worth studying because the sequence itself provides an inspectable and reusable starting surface for computational modeling. Even narrow feature families derived directly from sequence may be sufficient to detect bounded signal that is useful for prioritization, provided the resulting evidence is interpreted conservatively and tied to explicit benchmark conditions.

For that reason, benchmark-first and provenance-aware public evidence surfaces matter. A benchmarked workflow does not by itself establish biological truth, but it does make computational claims easier to inspect, rerun, and compare. In early-stage settings, this is a meaningful contribution because it reduces ambiguity about what the current evidence does and does not support.

The present BBB-oriented wedge is intentionally narrow. It studies an imported legacy processed peptide dataset using a small sequence-derived physicochemical feature surface consisting of length, charge, gravy, pI, and aromaticity. The current repository regenerates baseline reruns under a current-contract artifact structure that includes metrics, predictions, ranking outputs, summary tables, and manifests.

Within this scope, the present work asks whether permeability-related signal can be detected from these sequence-derived features strongly enough to support benchmark-oriented candidate prioritization before experimental validation. The focus is not on finding the best possible model family, but on establishing an interpretable and reproducible baseline evidence surface.

Accordingly, the main contribution of this paper is a bounded BBB-oriented evidence package rather than a final biological claim. It combines recovered legacy continuity with regenerated benchmark artifacts, separates imported from regenerated evidence, and provides a manuscript-ready computational wedge that can later be connected to stronger provenance closure and experimental follow-up.

## Draft methods skeleton

### Dataset surface

The current reruns use an imported legacy BBB-oriented processed dataset with `2959` rows. Confirmed benchmark-relevant fields are `sequence`, `label`, `length`, `charge`, `gravy`, `pI`, and `aromaticity`. For rerun compatibility, operational metadata fields `sequence_id` and `source` were added to the rerun-ready dataset surface. These additions support stable row identity and source labeling, but do not alter labels or feature values.

### Feature representation

The current feature surface is intentionally narrow and sequence-derived. The benchmarked feature set includes `length`, `charge`, `gravy`, `pI`, and `aromaticity`. This representation is intended to support an interpretable baseline surface rather than an exhaustive feature program.

### Baseline models

The regenerated benchmark reruns currently include three baseline models: a Dummy most-frequent classifier, Logistic Regression, and Random Forest. The purpose of this model set is to establish a comparison surface between trivial baseline behavior and non-trivial baseline classifiers under the same benchmark conditions.

### Evaluation policy

Recovered benchmark-style evaluation uses `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`. Class imbalance is substantial in the current dataset surface and is therefore relevant to interpretation, particularly for the Dummy baseline. Primary metrics include ROC-AUC, PR-AUC, precision, recall, F1, and MCC, with ROC-AUC, PR-AUC, and MCC serving as key summary signals for benchmark comparison.

### Output artifacts

Current-contract reruns emit machine-readable benchmark artifacts including metrics summaries, row-level predictions, ranking outputs, compact summary tables, and manifest-oriented provenance packaging. These outputs are treated as the current public benchmark evidence surface for the repository.

### Imported vs regenerated distinction

Imported historical artifacts are preserved for continuity and comparison. Regenerated current-contract artifacts define the present benchmark evidence surface and should be treated as the primary basis for interpretation in the manuscript body.

## Draft results skeleton

### Dataset and class balance

The current dataset surface is strongly imbalanced, which makes the Dummy most-frequent classifier an important reference point. In this setting, expected trivial behavior under the class prior helps define the floor that non-trivial baselines must exceed to support any bounded prioritization interpretation.

### Baseline comparison

The regenerated Dummy baseline shows PR-AUC of approximately `0.0909`, consistent with a class-prior reference under strong imbalance. Logistic Regression reaches approximately `0.8605` ROC-AUC and `0.4903` PR-AUC, while Random Forest reaches approximately `0.8489` ROC-AUC and `0.5002` PR-AUC. Taken together, these results indicate non-trivial signal above the trivial baseline on the present benchmark surface, while remaining within a baseline-model regime rather than an optimized modeling program.

### Candidate prioritization relevance

The ranking-oriented outputs matter because the practical near-term use of the current wedge is candidate filtering before wet-lab work. In this setting, the main question is not whether the repository establishes universal prediction, but whether the regenerated benchmark artifacts support a bounded and reproducible prioritization view over the current candidate surface.

### Regenerated feature-importance summary

The regenerated Random Forest feature-importance artifact orders the present feature set as `gravy`, `aromaticity`, `pI`, `length`, and `charge`. This ordering is useful as a compact summary of model emphasis within the current baseline rerun, but it should not be overinterpreted as mechanistic biological explanation.

### Evidence-boundary interpretation

Taken together, the current results support bounded computational prioritization and reproducible baseline comparison on a BBB-oriented wedge. They do not constitute biological validation, mechanistic proof, or evidence of general delivery behavior beyond the present benchmark surface.

## Draft discussion / interpretation skeleton

The main value of the current work is structural as well as empirical. A benchmark-first evidence surface makes it easier to understand what was run, what was measured, and what kind of interpretation is justified. In early-stage computational settings, that clarity is part of the contribution.

The separation between imported and regenerated artifacts also improves trust. Imported legacy materials remain useful for continuity, but regenerated current-contract artifacts provide a clearer basis for present-tense claims because they are tied to the current repository contract and output packaging.

The current baseline results are meaningful because they rise above a trivial class-prior reference while remaining narrow in interpretation. That is enough to support an initial candidate-prioritization framing, but not enough to justify broader claims about biological mechanism or validated transport performance.

Within the broader Permea program, this wedge functions as the first concrete evidence layer for a sequence-first and benchmark-first approach. Its role is to provide a reusable and inspectable starting surface that can later be extended through stronger provenance closure, richer artifact packaging, and eventual validation linkage.

## Draft limitations

The current evidence package has several important limitations. Dataset provenance is not yet fully closed, and attribution and licensing still require confirmation before the dataset surface can be treated as fully settled for broader public reference. The feature surface is narrow and limited to a small set of sequence-derived physicochemical descriptors. The model family is baseline-oriented rather than exhaustive, and the current results therefore reflect an initial benchmark comparison rather than a mature modeling frontier. No wet-lab validation is included, and the present wedge does not establish general delivery behavior, mechanistic causality, clinical interpretation, or therapeutic relevance. These limitations should remain explicit in any manuscript built from the current repository state.

## Figure-caption draft set

**Figure 1. Dataset distribution and class balance.** Distribution of positive and negative labels in the current BBB-oriented benchmark surface. The figure highlights strong class imbalance, which provides context for interpreting trivial baseline behavior and motivates the use of class-sensitive evaluation metrics.

**Figure 2. Baseline comparison across imported and regenerated benchmark evidence.** Comparison of key performance metrics for Dummy, Logistic Regression, and Random Forest baselines across imported legacy summaries and regenerated current-contract reruns. The figure is intended to show continuity and differences between historical artifacts and the present benchmark evidence surface without implying biological validation.

**Figure 3. Regenerated Random Forest feature importance.** Relative feature importance values from the regenerated Random Forest baseline trained on the current sequence-derived physicochemical feature surface. The caption should emphasize that the ordering summarizes model behavior within the current benchmark rerun and is not a mechanistic interpretation.

**Figure 4. Benchmark workflow and evidence-package surface.** Draft caption for the workflow figure showing the progression from imported legacy artifacts to an onboarded dataset, rerun-ready dataset, benchmark reruns, and current-contract outputs. This figure is intended to communicate how the evidence package is structured and why regenerated artifacts are treated as the current benchmark surface.

**Pending figure note.** If a regenerated-only model comparison figure is added later, its caption should explicitly state that it summarizes current-contract reruns only and serves as a compact benchmark comparison view rather than a claim of validated predictive performance.

## Immediate next steps

- close remaining provenance and attribution gaps
- refresh selected figures into more publication-ready layouts
- refine methods wording so manuscript text matches repository docs precisely
- draft appendix language for imported versus regenerated artifacts
- align the manuscript boundary with a future validation path without overstating current evidence
