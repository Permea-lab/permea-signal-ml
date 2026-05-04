# bioRxiv v0.1 Manuscript Candidate

## Candidate Status

Manuscript candidate prepared for human review. Not submission-ready. Do not post publicly until metadata, disclosure, dataset/legal, reference, formatting, and human approval blockers are resolved.

Computational evidence only. No biological validation, wet-lab validation, therapeutic efficacy, clinical interpretation, leakage-free status, or robust-generalization claim is made. Current metrics are random-stratified baseline metrics and may be optimistic under the documented same-label cross-fold duplicate and sequence-similarity findings.

## Title

Initial Computational Evidence for Permeability-Related Signal in a BBB-Oriented Peptide Benchmark

## Author and Affiliation Placeholders

Source placeholder blocks: `docs/PREPRINT_METADATA_BLOCKS_DRAFT_V0_1.md`.

- `[AUTHOR LIST PLACEHOLDER]`
- `[AFFILIATIONS PLACEHOLDER]`
- `[CORRESPONDING AUTHOR PLACEHOLDER]`
- `[ORCID PLACEHOLDER]`

## Abstract

Biological delivery remains a major bottleneck in the development of many next-generation therapeutic modalities, yet early computational work in this area is often difficult to compare because dataset provenance, benchmark definitions, and result artifacts are inconsistently documented. A sequence-first computational framing can support pre-experimental hypothesis generation only when its evidence is reproducible, benchmark-aware, and explicitly bounded. Here we present an initial BBB-oriented computational evidence package built from an imported legacy peptide dataset and regenerated under a current benchmark contract. The feature surface is intentionally narrow and limited to sequence-derived physicochemical descriptors: length, charge, gravy, pI, and aromaticity. Regenerated baseline reruns include a Dummy most-frequent classifier, Logistic Regression, and Random Forest under a recovered `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` evaluation policy. The resulting ROC-AUC, PR-AUC, and MCC values are random-stratified baseline metrics, not leakage-aware generalization estimates. Under strong class imbalance, the Dummy class-prior baseline has PR-AUC approximately 0.0909, while Logistic Regression and Random Forest show learnable benchmark signal under the current split, with ROC-AUC values of approximately 0.8605 and 0.8489 and PR-AUC values of approximately 0.4903 and 0.5002, respectively. A first leakage audit identified same-label duplicate and high-similarity sequence pairs crossing reconstructed folds, so these performance estimates may be optimistic under detected same-label cross-fold similarity. The cautious interpretation is therefore limited to benchmark signal under the present random-stratified split and to computational candidate-prioritization hypotheses before experimental validation. The contribution of the present work is not biological confirmation, validated delivery performance, or robust generalization, but a reproducible evidence package that distinguishes imported historical artifacts from regenerated current-contract benchmark artifacts.

## Keywords

- blood-brain barrier
- peptide benchmark
- permeability-related signal
- sequence-derived physicochemical features
- candidate prioritization
- benchmark-first evaluation
- reproducible evidence package

## Introduction

Biological delivery remains a persistent challenge in the development of many next-generation therapeutic approaches. Among these barriers, the blood-brain barrier remains especially important because it constrains access to the central nervous system and increases the cost of downstream experimental exploration [@bbb_shuttle_review_2016]. Computational delivery-adjacent benchmark work is often difficult to compare across projects because task definition, dataset handling, evaluation policy, and artifact packaging vary substantially. In this manuscript, delivery language refers to the broader problem context, not to validated delivery performance from the current benchmark.

A sequence-first framing remains worth studying because sequence is an inspectable and reusable starting surface. BBB peptide databases and early predictors provide useful context for this sequence-oriented benchmark lineage [@brainpeps_2012; @b3pdb_2021; @b3pred_2021; @bbppred_2021; @bbppredict_2022]. The present contribution is a bounded computational evidence package rather than a claim of validated biological delivery.

## Related Work

Prior BBB peptide resources and predictors define the immediate context for this manuscript. Brainpeps and B3Pdb provide database and archive context for BBB-related peptide records, while B3Pred, BBPpred, and BBPpredict represent earlier sequence-based BBB peptide predictor work [@brainpeps_2012; @b3pdb_2021; @b3pred_2021; @bbppred_2021; @bbppredict_2022]. More recent methods include data-augmentation, structure-aware, transformer, protein-language-model, and tabular-foundation-model style approaches [@augur_2024; @brainpeppass_2024; @deepb3p3_2023; @esm_bbb_pred_2025; @b3bpfn_2026]. Adjacent CPP work is useful for benchmark and descriptor context, but it is not direct evidence that the present BBB-oriented package is biologically validated [@practicpp_2024; @perseucpp_2025].

## Methods

### Dataset Surface

The current reruns are based on an imported legacy BBB-oriented processed dataset. In its rerun-ready form, the current dataset surface contains 2959 rows. Confirmed benchmark-relevant fields are `sequence`, `label`, `length`, `charge`, `gravy`, `pI`, and `aromaticity`, plus operational `sequence_id` and `source` fields. The dataset is not provenance-closed; attribution, licensing, source-level metadata, and original label-source criteria remain partially unresolved. The `label` field is treated as the supervised benchmark target, not as independently verified biological truth.

### Feature Representation

The present feature representation is intentionally narrow and sequence-derived. The benchmark surface uses length, charge, gravy, pI, and aromaticity. This feature set is an interpretable baseline surface, not a claim of mechanistic completeness, biological causality, or determinants of BBB transport [@b3pred_2021; @bbppred_2021; @augur_2024; @brainpeppass_2024; @deepb3p3_2023; @esm_bbb_pred_2025].

### Baseline Models and Evaluation

Three baseline model families were included: Dummy most-frequent classifier, Logistic Regression, and Random Forest. Recovered benchmark-style evaluation uses `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` via scikit-learn [@scikit_learn_2011]. ROC-AUC, PR-AUC, precision, recall, F1, and MCC are reported. PR-AUC is interpreted under class imbalance [@saito_rehmsmeier_2015_prauc], while MCC provides an additional bounded binary-classification summary [@chicco_jurman_2020_mcc].

### Output Artifacts

Current outputs include metrics summaries, row-level prediction files, ranking outputs, compact summary tables, and manifest-oriented provenance artifacts. Data processing, modeling, metric calculation, and figure generation are supported by pandas, scikit-learn, and matplotlib [@pandas_2010; @scikit_learn_2011; @matplotlib_2007].

## Results

Under the recovered `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` policy, the regenerated Dummy baseline yields a PR-AUC of approximately 0.0909, consistent with class-prior behavior under strong imbalance. Under that same random-stratified baseline policy, Logistic Regression reaches approximately 0.8605 ROC-AUC and 0.4903 PR-AUC, while Random Forest reaches approximately 0.8489 ROC-AUC and 0.5002 PR-AUC. The corresponding MCC values are approximately 0.3618 for Logistic Regression and 0.4331 for Random Forest. Because the leakage audit found same-label duplicate and high-similarity pairs crossing reconstructed folds, these values should be interpreted as potentially optimistic benchmark-signal estimates under the current split, not as robust generalization evidence.

Within the regenerated Random Forest artifact set, the current feature-importance ordering is `gravy`, `aromaticity`, `pI`, `length`, and `charge`. This is a model-level artifact summary within the current rerun contract, not a mechanistic explanation of BBB transport and not evidence that any listed descriptor causally determines delivery behavior.

## Leakage Audit and Benchmark Interpretation

The first leakage audit found 4 same-label exact duplicate sequence groups crossing reconstructed folds, 0 normalized exact-sequence label-conflict groups, 73 same-label near-duplicate pairs including 56 cross-fold pairs, 33 same-label high k-mer Jaccard pairs including 29 cross-fold pairs, and a coarse `legacy_bbb_import` source value spanning all 5 folds. Overall benchmark optimism risk is documented as Moderate.

The current metrics should therefore be interpreted as random-stratified baseline metrics that may be optimistic under measured sequence-similarity structure, not as leakage-aware generalization estimates. Any stronger benchmark claim would require leakage-aware or similarity-aware sensitivity follow-up. Adjacent CPP benchmark work reinforces the need for conservative imbalance, deduplication, and validation language in peptide-prediction settings [@practicpp_2024; @perseucpp_2025].

## Limitations

Dataset provenance is not fully closed. Attribution and licensing requirements still require confirmation. Original label-source criteria are partially unresolved. The feature surface is narrow. The model set is baseline-oriented. No wet-lab validation is included. The manuscript does not establish experimental transport confirmation, mechanism, broad delivery generalization, robust generalization, clinical interpretation, therapeutic relevance, or SOTA predictor status.

## Discussion

The present results are meaningful primarily because they are embedded in a benchmark-first and provenance-aware evidence surface. The repository distinguishes imported historical artifacts from regenerated current-contract artifacts and preserves caveats around dataset provenance, label-source criteria, leakage findings, and validation status. Within that framework, Logistic Regression and Random Forest exceeding the trivial class-prior baseline supports a cautious computational filtering interpretation on the present benchmark surface. It does not establish delivery performance, biological actionability, or leakage-aware generalization.

## Conclusion

The present work contributes an initial computational evidence package for a BBB-oriented peptide benchmark built around sequence-derived physicochemical features and reproducible baseline reruns. Its value lies in combining a bounded benchmark surface with explicit provenance boundaries and a clear imported-versus-regenerated distinction. Future progress depends on stronger provenance closure, leakage-aware or similarity-aware sensitivity analysis, final metadata/reference review, and eventual experimental validation pathways. Until then, this package should be read as benchmark documentation and hypothesis-generation support, not as validated biological delivery evidence.

## Data and Code Availability Placeholders

- Data availability: placeholder pending dataset attribution, licensing, redistribution, source-path, and version review.
- Code availability: placeholder pending repository URL, branch/tag, archive policy, and release-status review.

## Funding, Competing Interests, Acknowledgements, Ethics, and Contributions Placeholders

Source placeholder blocks: `docs/PREPRINT_METADATA_BLOCKS_DRAFT_V0_1.md`.

- Funding: placeholder.
- Competing interests: placeholder.
- Acknowledgements: placeholder.
- Ethics statement: placeholder.
- Author contributions: placeholder.

## Supplement Pointer

Supplementary materials draft: `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`.

## References Placeholder

Draft bibliography source: `references.bib`. Citation placeholders use keys from that file. Final references require human metadata and formatting review before public posting.
