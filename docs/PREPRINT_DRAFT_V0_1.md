# Preprint Draft v0.1

## Title

Initial Computational Evidence for Permeability-Related Signal in a BBB-Oriented Peptide Benchmark

## Author and Affiliation Placeholders

- Author 1 — placeholder
- Author 2 — placeholder
- Affiliation 1 — placeholder
- Affiliation 2 — placeholder
- Corresponding author — placeholder

## Keywords

- blood-brain barrier
- peptide benchmark
- permeability-related signal
- sequence-derived physicochemical features
- candidate prioritization
- benchmark-first evaluation
- reproducible evidence package

## Manuscript status

bioRxiv v0.1 candidate draft, not submission-ready. Computational evidence only; no experimental validation included. Public preprint status remains Hold / candidate prepared for human review only. Current metrics are random-stratified baseline metrics and may be optimistic under documented same-label cross-fold duplicate and sequence-similarity findings.

## Abstract

Biological delivery remains a major bottleneck in the development of many next-generation therapeutic modalities, yet early computational work in this area is often difficult to compare because dataset provenance, benchmark definitions, and result artifacts are inconsistently documented. A sequence-first computational framing can support pre-experimental hypothesis generation only when its evidence is reproducible, benchmark-aware, and explicitly bounded. Here we present an initial BBB-oriented computational evidence package built from an imported legacy peptide dataset and regenerated under a current benchmark contract. The feature surface is intentionally narrow and limited to sequence-derived physicochemical descriptors: length, charge, gravy, pI, and aromaticity. Regenerated baseline reruns include a Dummy most-frequent classifier, Logistic Regression, and Random Forest under a recovered `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` evaluation policy. The resulting ROC-AUC, PR-AUC, and MCC values are random-stratified baseline metrics, not leakage-aware generalization estimates. Under strong class imbalance, the Dummy class-prior baseline has PR-AUC approximately 0.0909, while Logistic Regression and Random Forest show learnable benchmark signal under the current split, with ROC-AUC values of approximately 0.8605 and 0.8489 and PR-AUC values of approximately 0.4903 and 0.5002, respectively. A first leakage audit identified same-label duplicate and high-similarity sequence pairs crossing reconstructed folds, so these performance estimates may be optimistic under detected same-label cross-fold similarity. The cautious interpretation is therefore limited to benchmark signal under the present random-stratified split and to computational candidate-prioritization hypotheses before experimental validation. The contribution of the present work is not biological confirmation, validated delivery performance, or robust generalization, but a reproducible evidence package that distinguishes imported historical artifacts from regenerated current-contract benchmark artifacts.

## Introduction

Biological delivery remains a persistent challenge in the development of many next-generation therapeutic approaches. Large molecules and biologically active payloads often encounter major transport barriers before they can reach the relevant intracellular or tissue context. Among these barriers, the blood-brain barrier remains especially important because it constrains access to the central nervous system and increases the cost of downstream experimental exploration [@bbb_shuttle_review_2016]. In practical terms, this creates a need for earlier-stage computational triage methods that can organize candidate hypotheses before more expensive validation work begins.

At the same time, computational work related to delivery-adjacent benchmark signal is often difficult to compare across projects, groups, and repositories. Adjacent efforts may appear similar at the level of ambition while differing substantially in task definition, dataset handling, evaluation policy, or artifact packaging. In many cases, results are presented without a stable benchmark identifier, without a clear split policy, or without machine-readable outputs that allow outside reviewers to understand how a given number was produced. This fragmentation weakens comparability even when model families or biological framing appear related.

The problem is not only one of methodological variation but also one of provenance. Early computational outputs can be informative, but their interpretation depends on knowing what dataset surface was used, which features were computed, what baseline was compared, and how reruns relate to historical artifacts. Without that context, it becomes difficult to distinguish a reproducible benchmark result from an isolated analysis snapshot. For a field area that is already biologically complex, weak computational provenance adds another layer of ambiguity.

A sequence-first framing remains worth studying precisely because sequence is an inspectable and reusable starting surface. BBB peptide databases and early predictors provide useful context for this sequence-oriented benchmark lineage [@brainpeps_2012; @b3pdb_2021; @b3pred_2021; @bbppred_2021; @bbppredict_2022]. Even before richer structural, assay-derived, or multi-modal features are available, sequence-derived physicochemical descriptors can provide a narrow but disciplined basis for asking whether computational permeability-related benchmark signal is detectable on a bounded dataset surface. That question is useful not because it solves delivery, but because it can establish whether a benchmark-oriented computational triage surface exists for a constrained wedge of the broader problem.

For that reason, benchmark-first and provenance-aware public evidence become important. A benchmarked workflow does not establish biological truth on its own, but it does provide a more legible basis for comparison, reruns, and interpretation. In early-stage repository work, this structure is part of the contribution because it preserves the distinction between exploratory computation, current-contract benchmark artifacts, and claims that would require stronger validation tiers.

The present repository focuses on a deliberately narrow BBB-oriented wedge. It carries forward imported legacy dataset continuity while regenerating current-contract artifacts for a small sequence-derived physicochemical feature surface composed of length, charge, gravy, pI, and aromaticity. The baseline reruns use a Dummy most-frequent classifier, Logistic Regression, and Random Forest, and they emit metrics, predictions, ranking outputs, summary tables, and manifest-oriented artifacts under a reproducible repository structure.

Within this scope, the present work asks whether computational permeability-related benchmark signal can be detected from sequence-derived physicochemical features under the current random-stratified split. The question is intentionally bounded. The aim is not to identify the final model family for delivery prediction, nor to claim biological mechanism or delivery performance, but to establish whether a transparent and reproducible baseline evidence surface can be defined for this BBB-oriented wedge.

Accordingly, the main contribution of the present work is a bounded computational evidence package. It combines imported historical continuity with regenerated benchmark artifacts, preserves an explicit imported-versus-regenerated distinction, and provides a reproducible baseline comparison surface grounded in current repository state. It should therefore be read as an initial benchmarked evidence layer that can support future refinement, stronger provenance closure, and eventual experimental linkage, rather than as a claim of validated biological performance.

## Related Work

Prior BBB peptide resources and predictors define the immediate context for this manuscript. Brainpeps and B3Pdb provide database and archive context for BBB-related peptide records, while B3Pred, BBPpred, and BBPpredict represent earlier sequence-based BBB peptide predictor work [@brainpeps_2012; @b3pdb_2021; @b3pred_2021; @bbppred_2021; @bbppredict_2022]. More recent methods include data-augmentation, structure-aware, transformer, protein-language-model, and tabular-foundation-model style approaches [@augur_2024; @brainpeppass_2024; @deepb3p3_2023; @esm_bbb_pred_2025; @b3bpfn_2026]. Adjacent CPP work is useful for benchmark and descriptor context, but it is not direct evidence that the present BBB-oriented package is biologically validated [@practicpp_2024; @perseucpp_2025].

## Methods

### Dataset surface

The current reruns are based on an imported legacy BBB-oriented processed dataset. In its rerun-ready form, the current dataset surface contains 2959 rows. Confirmed benchmark-relevant fields are `sequence`, `label`, `length`, `charge`, `gravy`, `pI`, and `aromaticity`. To support benchmark-contract compatibility, the rerun-ready dataset also includes operational metadata fields `sequence_id` and `source`. These additional fields were introduced to support stable row identity and explicit source labeling during reruns, but they did not alter the underlying labels or the precomputed feature values.

The current dataset surface is sufficient for benchmark-oriented reruns, but it is not provenance-closed. Current manifests retain the dataset version as `pending_confirmation`, and attribution, licensing, source-level metadata, and original label-source criteria remain partially unresolved. The `label` field is therefore used as the current supervised benchmark target, not as independently verified biological truth or validated transport evidence.

### Feature representation

The present feature representation is intentionally narrow and sequence-derived. The benchmark surface uses five physicochemical descriptors: length, charge, gravy, pI, and aromaticity. This feature set is not intended to exhaust the possible modeling surface for BBB-related signal, and it should not be read as mechanistic completeness, biological causality, or a claim that these descriptors determine BBB transport. Instead, it provides an interpretable and reproducible starting point for asking whether non-trivial computational benchmark signal is detectable under a constrained framing, in contrast to broader contemporary BBB predictor families that incorporate richer data augmentation, structural, or deep representation strategies [@b3pred_2021; @bbppred_2021; @augur_2024; @brainpeppass_2024; @deepb3p3_2023; @esm_bbb_pred_2025].

### Baseline models

Three baseline model families were included in the regenerated reruns: a Dummy most-frequent classifier, Logistic Regression, and Random Forest. The Dummy classifier serves as a class-prior reference under the current imbalance profile. Logistic Regression and Random Forest provide non-trivial baseline comparisons without turning the present work into an optimization study. The purpose of this model set is to establish a stable baseline evidence surface rather than a frontier modeling benchmark.

### Evaluation policy

Recovered benchmark-style evaluation uses `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` via scikit-learn [@scikit_learn_2011]. This split policy is important because the current dataset surface is strongly imbalanced, making trivial baseline behavior especially relevant to interpretation. The regenerated reruns report ROC-AUC, PR-AUC, precision, recall, F1, and MCC. Among these, ROC-AUC and PR-AUC help summarize ranking-sensitive behavior under imbalance [@saito_rehmsmeier_2015_prauc], while MCC provides an additional bounded summary of binary classification performance [@chicco_jurman_2020_mcc].

A first leakage audit is now documented in `docs/LEAKAGE_AUDIT_REPORT_V0_1.md` and `docs/LEAKAGE_AUDIT_FINDINGS_INVESTIGATION_V0_1.md`. The audit found 4 same-label exact duplicate sequence groups, 0 normalized exact-sequence label-conflict groups, 73 same-label near-duplicate pairs, 33 same-label high k-mer Jaccard pairs, and 29 same-label high-similarity pairs crossing reconstructed folds. The recovered split policy should therefore be read as the current random-stratified rerun policy, not as a duplicate-aware or sequence-similarity-aware evaluation. Current metrics may be optimistic under similarity-aware splitting.

### Output artifacts

The current-contract reruns emit a structured result package rather than isolated summary numbers. Current outputs include machine-readable metrics summaries, row-level prediction files, ranking outputs for candidate prioritization, compact summary tables, and manifest-oriented provenance artifacts. This packaging is intended to make the benchmark surface easier to inspect and compare, and it supports a clearer boundary between exploratory work and current-contract evidence. Data processing, modeling, metric calculation, and figure generation are supported by the current Python tooling stack, including pandas, scikit-learn, and matplotlib [@pandas_2010; @scikit_learn_2011; @matplotlib_2007].

The main manuscript metric claims map to `results/tables/model_comparison_summary.csv` and the corresponding regenerated metrics JSON files under `results/metrics/`. The regenerated feature-importance statement maps to `results/tables/regenerated_rf_feature_importance.csv` and `figures/regenerated_rf_feature_importance.png`. The manifest files under `results/manifests/` provide run-level context, including the recovered seed, split policy label, and current `pending_confirmation` dataset-version status.

### Imported versus regenerated evidence

An explicit distinction is maintained between imported historical artifacts and regenerated current-contract artifacts. Imported artifacts are retained for continuity and comparison, but they are not treated as the primary basis for current-tense interpretation. Regenerated artifacts define the current benchmark evidence surface because they are tied to the present repository contract, current output conventions, and reproducible rerun logic.

## Results

### Dataset and class balance

The current BBB-oriented benchmark surface is strongly imbalanced, which makes the behavior of the Dummy most-frequent classifier an important reference point. Under this setting, trivial behavior is expected to reflect the class prior rather than meaningful ranking or prioritization power. That floor is useful because it clarifies the minimum standard that non-trivial baseline models must exceed before any bounded prioritization interpretation is justified.

### Baseline comparison

Under the recovered `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` policy, the regenerated Dummy baseline yields a PR-AUC of approximately 0.0909, consistent with class-prior behavior under strong imbalance. Against that reference and under the same random-stratified baseline policy, Logistic Regression reaches approximately 0.8605 ROC-AUC and 0.4903 PR-AUC, while Random Forest reaches approximately 0.8489 ROC-AUC and 0.5002 PR-AUC. The corresponding MCC values are approximately 0.3618 for Logistic Regression and 0.4331 for Random Forest. These results indicate non-trivial benchmark signal above the trivial baseline on the present computational surface, while remaining firmly within a random-stratified baseline-model regime rather than an optimized, leakage-aware, or robust-generalization modeling program. Because the leakage audit found same-label duplicate and high-similarity pairs crossing reconstructed folds, these values may be optimistic under similarity-aware splitting.

### Candidate-prioritization interpretation

The practical relevance of the current reruns lies in computational candidate-prioritization hypotheses rather than in stand-alone predictive or biological validation claims. Because the repository emits ranking-oriented outputs alongside summary metrics, the benchmark results can support a computational filtering view in which higher-scoring candidates are organized for downstream consideration prior to experimental validation. Under this interpretation, the contribution of the baseline reruns is not universal prediction, delivery performance, or evidence of biological activity, but a reproducible prioritization surface for the present BBB-oriented benchmark wedge.

### Regenerated model-level feature-importance summary

Within the regenerated Random Forest artifact set, the current feature-importance ordering is `gravy`, `aromaticity`, `pI`, `length`, and `charge`. This ordering is useful as a compact summary of how the baseline Random Forest distributes emphasis across the present feature surface. It should not, however, be overread as a mechanistic explanation of BBB-related transport behavior or as evidence that any listed descriptor causally determines delivery behavior. In the present manuscript, the feature-importance result is best understood as an internal summary of model behavior within the current rerun contract.

## Leakage Audit and Benchmark Interpretation

Taken together, the regenerated results support a bounded computational interpretation. On the present random-stratified benchmark surface, sequence-derived physicochemical features support non-trivial baseline comparison and computational candidate-prioritization hypotheses beyond a class-prior reference. Because same-label duplicate and high-similarity sequence pairs cross reconstructed folds, the current performance estimates may be optimistic and should be interpreted as evidence of learnable benchmark signal under the current split rather than leakage-aware or stronger generalization evidence. These findings remain computational and benchmark-specific. They do not constitute experimental validation, mechanistic proof, or evidence of broad delivery behavior beyond the current BBB-oriented wedge.

## Limitations

The present draft is subject to several clear limitations. Dataset provenance is not yet fully closed, and attribution and licensing requirements still require confirmation before the dataset surface can be treated as fully settled for broad public reference. The feature surface is narrow and limited to a small set of sequence-derived physicochemical descriptors, which constrains the representational scope of the analysis. The model family is baseline-oriented rather than exhaustive or heavily optimized, so the results should be read as an initial benchmark comparison rather than a mature modeling frontier. No wet-lab validation is included, which means the work does not establish experimental confirmation of transport behavior. Nor does the present wedge establish mechanistic proof, broad delivery generalization, robust generalization, clinical interpretation, or therapeutic relevance. These limitations define the boundary within which the manuscript should be read.

Additional benchmark-readiness limitations remain. Original label-source criteria are not yet fully reconstructed. The first leakage audit found no normalized exact-sequence label conflicts, but it did identify same-label exact duplicates, near-duplicate pairs, high-similarity pairs, and cross-fold high-similarity pairs under the reconstructed random-stratified split. These findings create a moderate benchmark optimism risk. Adjacent CPP benchmark work reinforces the need for conservative imbalance, deduplication, and validation language in peptide-prediction settings [@practicpp_2024; @perseucpp_2025]. The audit findings do not invalidate the current bounded computational benchmark surface for trusted review, but they require conservative reporting before public preprint use and motivate leakage-aware or similarity-aware sensitivity analysis before stronger benchmark claims.

## Discussion

The present results are meaningful primarily because they are embedded in a benchmark-first and provenance-aware evidence surface. In early-stage computational work, structure matters: a result that can be traced to a defined dataset surface, feature set, evaluation policy, and artifact package is easier to interpret than a result presented only as a detached summary number. The repository therefore contributes not only baseline metrics, but also a clearer basis for deciding what those metrics can reasonably support.

Provenance-aware packaging is especially important in this setting. The repository distinguishes dataset facts that are confirmed, operational metadata added for reruns, recovered benchmark details such as seed and split policy, and provenance elements that remain unresolved. That separation does not remove the limitations of the evidence package, but it does make those limitations easier to inspect and discuss directly.

The imported-versus-regenerated distinction is similarly important. Historical artifacts remain useful because they preserve continuity with prior work and help explain how the present wedge emerged. However, present-tense interpretation should be grounded in regenerated current-contract artifacts because those are the outputs that can be rerun and inspected under the repository's current evidence structure. This reduces the temptation to conflate historical continuity with current reproducibility.

Within that framework, the observed baseline results are useful without being overstated. Logistic Regression and Random Forest both exceed the trivial class-prior baseline on the benchmark surface, which supports a cautious argument that non-trivial computational permeability-related benchmark signal is detectable from the feature set used here under the current split. At the same time, the feature surface is narrow, the model family is baseline-oriented, and the manuscript does not justify claims of validated biological prediction or leakage-aware generalization. The appropriate interpretation is therefore practical rather than expansive: the repository supports computational candidate-prioritization hypotheses before experimental validation under a BBB-oriented benchmark frame.

Within the broader Permea program, this wedge functions as the first concrete evidence layer for a sequence-first and benchmark-first approach. Its purpose is to show that a narrow but disciplined repository can preserve historical continuity, generate current-contract evidence, and provide a manuscript-ready computational surface without pretending to solve the broader delivery problem. That role is modest by design, but it provides a clearer base for later refinement, stronger provenance closure, and eventual validation linkage.

## Conclusion

The present work contributes an initial computational evidence package for a BBB-oriented peptide benchmark built around sequence-derived physicochemical features and reproducible baseline reruns. Within that bounded scope, the repository now provides a clearer random-stratified benchmark surface for comparing trivial and non-trivial baselines and for supporting computational candidate-prioritization hypotheses prior to experimental validation.

This contribution remains intentionally narrow. Its value lies in combining a reproducible baseline benchmark surface with explicit provenance boundaries and a clear imported-versus-regenerated distinction. Future progress depends on stronger provenance closure, continued improvement of artifact packaging and figure support, and eventual linkage to experimental validation pathways. Until then, the current manuscript should be read as an early but structured computational wedge rather than as a claim of validated biological delivery performance.

## Data Availability Placeholder

Data availability statement pending human dataset/licensing review. Current processed dataset provenance, attribution, label-source criteria, and redistribution status remain incomplete and must not be represented as finalized.

## Code Availability Placeholder

Code availability statement pending human review of repository URL, branch/tag, archive policy, and release status.

## Funding, Competing Interests, and Acknowledgements Placeholders

- Funding: placeholder; no funding statement has been provided.
- Competing interests: placeholder; no competing-interest statement has been provided.
- Acknowledgements: placeholder; no acknowledgement text has been provided.
- Author contributions: placeholder; no final author metadata has been provided.
- Ethics statement: placeholder; computational evidence package only, final wording pending human review.
- Full placeholder block source: `docs/PREPRINT_METADATA_BLOCKS_DRAFT_V0_1.md`.

## References Placeholder

Draft bibliography source: `references.bib`. Citation placeholders in this draft use BibTeX keys from that file. Final references require human metadata and formatting review before public posting.

## Draft figure placement notes

- Figure 1 — `dataset_distribution.png` — Results / Dataset and class balance
- Figure 2 — `legacy_vs_rerun_metrics.png` — Results / Baseline comparison
- Figure 3 — `regenerated_rf_feature_importance.png` — Results / Regenerated model-level feature-importance summary
- Figure 4 — `benchmark_workflow_outputs.png` — Methods overview or Results overview
- Table 1 — `model_comparison_summary.csv` — Results / Baseline comparison
- Pending figure — regenerated-only comparison chart — Results / Baseline comparison, if later added

## Draft references / source anchors

- `docs/DATASET.md`
- `docs/FIRST_EVIDENCE_SUMMARY.md`
- `docs/V0_1_EVIDENCE_PACKAGE.md`
- `docs/PAPER_PACKAGE_V0_1.md`
- `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`
- `docs/PREPRINT_ASSEMBLY_V0_1.md`
- `docs/PREPRINT_SKELETON_V0_1.md`
- `docs/SUPPLEMENTARY_OUTLINE_V0_1.md`
- `results/tables/model_comparison_summary.csv`
- `results/tables/regenerated_rf_feature_importance.csv`
- `figures/regenerated_rf_feature_importance.png`
