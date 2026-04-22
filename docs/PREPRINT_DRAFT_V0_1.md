# Preprint Draft v0.1

## Working title

Initial Computational Evidence for Permeability-Related Signal in a BBB-Oriented Peptide Benchmark

## Abstract

Biological delivery remains a major bottleneck in the development of many next-generation therapeutic modalities, yet early computational work in this area is often difficult to compare because dataset provenance, benchmark definitions, and result artifacts are inconsistently documented. A sequence-first computational framing may help support earlier-stage candidate prioritization, but its value depends on evidence that is reproducible and benchmark-aware. Here we present an initial BBB-oriented evidence package built from an imported legacy peptide dataset and regenerated under a current benchmark contract. The feature surface is intentionally narrow and limited to sequence-derived physicochemical descriptors: length, charge, gravy, pI, and aromaticity. Regenerated baseline reruns include a Dummy most-frequent classifier, Logistic Regression, and Random Forest under a recovered `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` evaluation policy. Under strong class imbalance, the class-prior baseline behaves as expected, while Logistic Regression and Random Forest show non-trivial signal above that floor, with ROC-AUC values of approximately 0.8605 and 0.8489 and PR-AUC values of approximately 0.4903 and 0.5002, respectively. These results support a cautious interpretation: sequence-derived physicochemical features appear sufficient to support benchmark-oriented candidate prioritization on the present BBB-oriented wedge prior to experimental validation. The contribution of the present work is therefore not biological confirmation, but a reproducible evidence package that distinguishes imported historical artifacts from regenerated current-contract benchmark artifacts.

## Introduction

Biological delivery remains a persistent challenge in the development of many next-generation therapeutic approaches. Large molecules and biologically active payloads often encounter major transport barriers before they can reach the relevant intracellular or tissue context. Among these barriers, the blood-brain barrier remains especially important because it constrains access to the central nervous system and increases the cost of downstream experimental exploration. In practical terms, this creates a need for earlier-stage prioritization methods that can narrow candidate sets before more expensive validation work begins.

At the same time, computational work related to delivery signal is often difficult to compare across projects, groups, and repositories. Adjacent efforts may appear similar at the level of ambition while differing substantially in task definition, dataset handling, evaluation policy, or artifact packaging. In many cases, results are presented without a stable benchmark identifier, without a clear split policy, or without machine-readable outputs that allow outside reviewers to understand how a given number was produced. This fragmentation weakens comparability even when model families or biological framing appear related.

The problem is not only one of methodological variation but also one of provenance. Early computational outputs can be informative, but their interpretation depends on knowing what dataset surface was used, which features were computed, what baseline was compared, and how reruns relate to historical artifacts. Without that context, it becomes difficult to distinguish a reproducible benchmark result from an isolated analysis snapshot. For a field area that is already biologically complex, weak computational provenance adds another layer of ambiguity.

A sequence-first framing remains worth studying precisely because sequence is an inspectable and reusable starting surface. Even before richer structural, assay-derived, or multi-modal features are available, sequence-derived physicochemical descriptors can provide a narrow but disciplined basis for asking whether permeability-related signal is detectable at all. That question is useful not because it solves delivery, but because it can establish whether a benchmark-oriented prioritization surface exists for a constrained wedge of the broader problem.

For that reason, benchmark-first and provenance-aware public evidence become important. A benchmarked workflow does not establish biological truth on its own, but it does provide a more legible basis for comparison, reruns, and interpretation. In early-stage repository work, this structure is part of the contribution because it preserves the distinction between exploratory computation, current-contract benchmark artifacts, and claims that would require stronger validation tiers.

The present repository focuses on a deliberately narrow BBB-oriented wedge. It carries forward imported legacy dataset continuity while regenerating current-contract artifacts for a small sequence-derived physicochemical feature surface composed of length, charge, gravy, pI, and aromaticity. The baseline reruns use a Dummy most-frequent classifier, Logistic Regression, and Random Forest, and they emit metrics, predictions, ranking outputs, summary tables, and manifest-oriented artifacts under a reproducible repository structure.

Within this scope, the present work asks whether permeability-related signal can be detected strongly enough from sequence-derived physicochemical features to support candidate prioritization before experimental validation. The question is intentionally bounded. The aim is not to identify the final model family for delivery prediction, nor to claim biological mechanism, but to establish whether a transparent and reproducible baseline evidence surface can be defined for this BBB-oriented wedge.

Accordingly, the main contribution of the present work is a bounded computational evidence package. It combines imported historical continuity with regenerated benchmark artifacts, preserves an explicit imported-versus-regenerated distinction, and provides a reproducible baseline comparison surface grounded in current repository state. It should therefore be read as an initial benchmarked evidence layer that can support future refinement, stronger provenance closure, and eventual experimental linkage, rather than as a claim of validated biological performance.

## Methods

### Dataset surface

The current reruns are based on an imported legacy BBB-oriented processed dataset. In its rerun-ready form, the current dataset surface contains 2959 rows. Confirmed benchmark-relevant fields are `sequence`, `label`, `length`, `charge`, `gravy`, `pI`, and `aromaticity`. To support benchmark-contract compatibility, the rerun-ready dataset also includes operational metadata fields `sequence_id` and `source`. These additional fields were introduced to support stable row identity and explicit source labeling during reruns, but they did not alter the underlying labels or the precomputed feature values.

### Feature representation

The present feature representation is intentionally narrow and sequence-derived. The benchmark surface uses five physicochemical descriptors: length, charge, gravy, pI, and aromaticity. This feature set is not intended to exhaust the possible modeling surface for BBB-related signal. Instead, it provides an interpretable and reproducible starting point for asking whether non-trivial computational signal is detectable under a constrained benchmark framing.

### Baseline models

Three baseline model families were included in the regenerated reruns: a Dummy most-frequent classifier, Logistic Regression, and Random Forest. The Dummy classifier serves as a class-prior reference under the current imbalance profile. Logistic Regression and Random Forest provide non-trivial baseline comparisons without turning the present work into an optimization study. The purpose of this model set is to establish a stable baseline evidence surface rather than a frontier modeling benchmark.

### Evaluation policy

Recovered benchmark-style evaluation uses `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`. This split policy is important because the current dataset surface is strongly imbalanced, making trivial baseline behavior especially relevant to interpretation. The regenerated reruns report ROC-AUC, PR-AUC, precision, recall, F1, and MCC. Among these, ROC-AUC and PR-AUC help summarize ranking-sensitive behavior under imbalance, while MCC provides an additional bounded summary of binary classification performance.

### Output artifacts

The current-contract reruns emit a structured result package rather than isolated summary numbers. Current outputs include machine-readable metrics summaries, row-level prediction files, ranking outputs for candidate prioritization, compact summary tables, and manifest-oriented provenance artifacts. This packaging is intended to make the benchmark surface easier to inspect and compare, and it supports a clearer boundary between exploratory work and current-contract evidence.

### Imported versus regenerated evidence

An explicit distinction is maintained between imported historical artifacts and regenerated current-contract artifacts. Imported artifacts are retained for continuity and comparison, but they are not treated as the primary basis for current-tense interpretation. Regenerated artifacts define the current benchmark evidence surface because they are tied to the present repository contract, current output conventions, and reproducible rerun logic.

## Results

### Dataset and class balance

The current BBB-oriented benchmark surface is strongly imbalanced, which makes the behavior of the Dummy most-frequent classifier an important reference point. Under this setting, trivial behavior is expected to reflect the class prior rather than meaningful ranking or prioritization power. That floor is useful because it clarifies the minimum standard that non-trivial baseline models must exceed before any bounded prioritization interpretation is justified.

### Baseline comparison

The regenerated Dummy baseline yields a PR-AUC of approximately 0.0909, consistent with class-prior behavior under strong imbalance. Against that reference, Logistic Regression reaches approximately 0.8605 ROC-AUC and 0.4903 PR-AUC, while Random Forest reaches approximately 0.8489 ROC-AUC and 0.5002 PR-AUC. The corresponding MCC values are approximately 0.3618 for Logistic Regression and 0.4331 for Random Forest. These results indicate non-trivial signal above the trivial baseline on the present benchmark surface, while remaining firmly within a baseline-model regime rather than an optimized modeling program.

### Candidate-prioritization interpretation

The practical relevance of the current reruns lies in candidate prioritization rather than in stand-alone predictive claims. Because the repository emits ranking-oriented outputs alongside summary metrics, the benchmark results can support a filtering view in which higher-scoring candidates are organized for downstream consideration prior to experimental validation. Under this interpretation, the contribution of the baseline reruns is not universal prediction but a reproducible prioritization surface for the present BBB-oriented wedge.

### Regenerated feature-importance summary

Within the regenerated Random Forest artifact set, the current feature-importance ordering is `gravy`, `aromaticity`, `pI`, `length`, and `charge`. This ordering is useful as a compact summary of how the baseline Random Forest distributes emphasis across the present feature surface. It should not, however, be overread as a mechanistic explanation of BBB-related transport behavior. In the present manuscript, the feature-importance result is best understood as an internal summary of model behavior within the current rerun contract.

### Evidence-boundary interpretation

Taken together, the regenerated results support a bounded computational interpretation. On the present benchmark surface, sequence-derived physicochemical features appear sufficient to support non-trivial baseline comparison and candidate-prioritization analysis beyond a class-prior reference. These findings remain computational and benchmark-specific. They do not constitute experimental validation, mechanistic proof, or evidence of broad delivery behavior beyond the current BBB-oriented wedge.

## Discussion

The present results are meaningful primarily because they are embedded in a benchmark-first and provenance-aware evidence surface. In early-stage computational work, structure matters: a result that can be traced to a defined dataset surface, feature set, evaluation policy, and artifact package is easier to interpret than a result presented only as a detached summary number. The repository therefore contributes not only baseline metrics, but also a clearer basis for deciding what those metrics can reasonably support.

Provenance-aware packaging is especially important in this setting. The repository distinguishes dataset facts that are confirmed, operational metadata added for reruns, recovered benchmark details such as seed and split policy, and provenance elements that remain unresolved. That separation does not remove the limitations of the evidence package, but it does make those limitations easier to inspect and discuss directly.

The imported-versus-regenerated distinction is similarly important. Historical artifacts remain useful because they preserve continuity with prior work and help explain how the present wedge emerged. However, present-tense interpretation should be grounded in regenerated current-contract artifacts because those are the outputs that can be rerun and inspected under the repository's current evidence structure. This reduces the temptation to conflate historical continuity with current reproducibility.

Within that framework, the observed baseline results are useful without being overstated. Logistic Regression and Random Forest both exceed the trivial class-prior baseline on the benchmark surface, which supports a cautious argument that non-trivial permeability-related signal is detectable from the present feature set. At the same time, the feature surface is narrow, the model family is baseline-oriented, and the manuscript does not justify claims of validated biological prediction. The appropriate interpretation is therefore practical rather than expansive: the repository supports candidate prioritization before experimental validation under a BBB-oriented benchmark frame.

Within the broader Permea program, this wedge functions as the first concrete evidence layer for a sequence-first and benchmark-first approach. Its purpose is to show that a narrow but disciplined repository can preserve historical continuity, generate current-contract evidence, and provide a manuscript-ready computational surface without pretending to solve the broader delivery problem. That role is modest by design, but it provides a clearer base for later refinement, stronger provenance closure, and eventual validation linkage.

## Limitations

The present draft is subject to several clear limitations. Dataset provenance is not yet fully closed, and attribution and licensing requirements still require confirmation before the dataset surface can be treated as fully settled for broad public reference. The feature surface is narrow and limited to a small set of sequence-derived physicochemical descriptors, which constrains the representational scope of the analysis. The model family is baseline-oriented rather than exhaustive or heavily optimized, so the results should be read as an initial benchmark comparison rather than a mature modeling frontier. No wet-lab validation is included, which means the work does not establish experimental confirmation of transport behavior. Nor does the present wedge establish mechanistic proof, broad delivery generalization, clinical interpretation, or therapeutic relevance. These limitations define the boundary within which the manuscript should be read.

## Conclusion

The present work contributes an initial computational evidence package for a BBB-oriented peptide benchmark built around sequence-derived physicochemical features and reproducible baseline reruns. Within that bounded scope, the repository now provides a clearer benchmark surface for comparing trivial and non-trivial baselines and for supporting candidate-prioritization analysis prior to experimental validation.

This contribution remains intentionally narrow. Its value lies in combining a reproducible baseline benchmark surface with explicit provenance boundaries and a clear imported-versus-regenerated distinction. Future progress depends on stronger provenance closure, continued improvement of artifact packaging and figure support, and eventual linkage to experimental validation pathways. Until then, the current manuscript should be read as an early but structured computational wedge rather than as a claim of validated biological delivery performance.

## Draft figure placement notes

- Figure 1 — `dataset_distribution.png` — Results / Dataset and class balance
- Figure 2 — `legacy_vs_rerun_metrics.png` — Results / Baseline comparison
- Figure 3 — `regenerated_rf_feature_importance.png` — Results / Regenerated feature-importance summary
- Figure 4 — `benchmark_workflow_outputs.png` — Methods overview or Results overview
- Table 1 — `model_comparison_summary.csv` — Results / Baseline comparison
- Pending figure — regenerated-only comparison chart — Results / Baseline comparison, if later added

## Draft references / source anchors

- `docs/DATASET.md`
- `docs/FIRST_EVIDENCE_SUMMARY.md`
- `docs/V0_1_EVIDENCE_PACKAGE.md`
- `docs/PAPER_PACKAGE_V0_1.md`
- `docs/PREPRINT_SKELETON_V0_1.md`
- `results/tables/model_comparison_summary.csv`
- `results/tables/regenerated_rf_feature_importance.csv`
- `figures/regenerated_rf_feature_importance.png`
