# A Reproducible Baseline Evidence Package for BBB-Related Peptide Permeability Signal from Sequence-Derived Features

## Manuscript Version Note

This v0.7 draft is an internal-preparation manuscript draft derived from manuscript v0.6 using the title/abstract positioning cleanup plan. It sharpens the framing around a reproducible baseline evidence package rather than a state-of-the-art predictor. It does not declare public preprint readiness. Public bioRxiv remains **Hold / not submission-ready** pending dataset/source licensing decisions, final data/code availability approval, final source-to-claim review, supplement/export completion, bibliography cleanup, and founder/manual approval.

## Author and Affiliation

Albert Heekwan Kim

Permea Research

Corresponding author: a.kim@permea.us

## Abstract

Blood-brain barrier (BBB)-related peptide permeability remains a difficult early-stage prioritization problem, and computational studies in this area require clear separation between benchmark signal, dataset provenance limits, and biological validation. This manuscript presents a reproducible baseline evidence package for a BBB-related peptide classification task using sequence-derived physicochemical features: length, charge, gravy, pI, and aromaticity. The work is positioned as a conservative peptide-focused benchmark package rather than a new state-of-the-art BBB permeability predictor or a matched comparison against prior BBB-penetrating peptide predictors. Existing aggregate artifacts compare a Dummy most-frequent classifier, Logistic Regression, and Random Forest under random-stratified baseline evaluation and a bounded leakage-aware group-stratified sensitivity setting. Under the leakage-aware sensitivity setting, Logistic Regression reached ROC-AUC 0.8587, PR-AUC 0.5024, and MCC 0.3747, while Random Forest reached ROC-AUC 0.8718, PR-AUC 0.5807, and MCC 0.5084. These aggregate results support a bounded computational benchmark-signal claim and cautious pre-experimental prioritization, but they do not establish leakage-free status, robust generalization, matched external predictor superiority, biological validation, wet-lab validation, therapeutic efficacy, or clinical efficacy. Dataset source, attribution, license, redistribution permission, label-source criteria, and public data/code availability remain unresolved; row-level processed datasets and row-level derived artifacts are not declared publicly available in this internal draft. Public bioRxiv submission remains Hold / not submission-ready pending source/license decisions, final data/code availability approval, figure/supplement/export completion, final source-to-claim review, bibliography verification, and founder/manual approval.

## Keywords

- blood-brain barrier
- peptide permeability
- sequence-derived physicochemical features
- computational benchmark
- candidate prioritization before experimental validation
- leakage-aware sensitivity analysis
- reproducible evidence package

## Introduction

Biological delivery is a central bottleneck for many therapeutic modalities, and BBB-related peptide prioritization remains a particularly challenging setting. BBB shuttle and peptide-delivery work motivates the search for sequence-associated permeability signals, but computational prioritization must remain distinct from experimentally demonstrated transport or efficacy [@bbb_shuttle_review_2016]. In this manuscript, "delivery" and "permeability" language refer to a computational BBB-related peptide classification task and supervised label surface, not to experimentally validated BBB transport or therapeutic effect.

The present work assembles an initial in-silico evidence package from existing Permea repository materials. The target framing is deliberately narrow: determine whether BBB-related peptide permeability-related signals are learnable from a small set of sequence-derived physicochemical features and whether those signals can support candidate prioritization before experimental validation. The closest context for the present study is BBB-penetrating peptide prediction rather than small-molecule or compound-level BBB permeability prediction. Prior BBB peptide resources and predictors provide context for sequence-first benchmark work [@brainpeps_2012; @b3pdb_2021; @b3pred_2021; @bbppred_2021; @bbppredict_2022]. Recent computational BBB-penetrating peptide predictor work provides direct related context for sequence-based prioritization, while not substituting for validation in this dataset or task [@naseem2023bbbpep; @augur_2024; @tang2025deepb3p; @arif2025deepb3pred; @brainpeppass_2024; @esm_bbb_pred_2025; @b3bpfn_2026]. Adjacent peptide-prediction work outside the direct BBBP comparator set is treated as broader sequence-modeling context only [@practicpp_2024; @perseucpp_2025].

This manuscript does not claim that the dataset is provenance-closed, that all leakage concerns are fully controlled, that the models robustly generalize, that Permea is state-of-the-art, or that any candidate is biologically or clinically validated.

## Related Work

### Direct BBB-Penetrating Peptide Predictor Context

The direct comparator landscape for this manuscript is BBB-penetrating peptide resources and predictors. This includes B3Pdb / B3Pred, BBPpredict, BBB-PEP-prediction, Augur, DeepB3P, and DeepB3Pred [@b3pdb_2021; @b3pred_2021; @bbppredict_2022; @naseem2023bbbpep; @augur_2024; @tang2025deepb3p; @arif2025deepb3pred]. Additional peptide database and predictor context is available through BrainPeps, BBPpred, BrainPepPass, ESM-BBB-Pred, and B3BPFN [@brainpeps_2012; @bbppred_2021; @brainpeppass_2024; @esm_bbb_pred_2025; @b3bpfn_2026].

These works are used as lineage and context for peptide-focused sequence modeling. B3Pdb and B3Pred support the closest database/predictor lineage framing, while BBPpredict, BBB-PEP-prediction, Augur, DeepB3P, and DeepB3Pred support direct peptide comparator context. They are not used here to claim that Permea is a state-of-the-art predictor, that Permea outperforms prior BBB-penetrating peptide predictors, or that datasets, labels, splits, and evaluation policies are matched across papers. Direct peptide predictor citations provide lineage and context only; they do not establish matched dataset, split, label, or metric comparability for the present benchmark.

The existing key `deepb3p3_2023` is intentionally not used as a DeepB3P or DeepB3Pred citation in this draft because its identity and citation role remain unresolved relative to the verified `tang2025deepb3p` and `arif2025deepb3pred` entries.

### Adjacent Compound-Level BBB Predictor Context

Adjacent compound-level BBB permeability predictors such as LightBBB, Deep-B3, DeePred-BBB, DeepBBBP, and TITAN-BBB address related but different prediction surfaces [@shaker2021lightbbb; @tang2022deepb3; @kumar2022deepredbbb; @parakkal2022deepbbbp; @oliveira2026titanbbb]. In particular, TITAN-BBB and DeePred-BBB are compound/SMILES BBB permeability work, not direct peptide predictors for the current Permea first paper.

These adjacent predictors may be useful for broader BBB computational context, but they should not be treated as direct benchmarks for this peptide-focused, sequence-derived baseline/evidence package.

### Permea Positioning

Permea's first paper is best positioned as a conservative and reproducible peptide-focused baseline/evidence package in the B3Pdb/B3Pred lineage. The contribution is not a new state-of-the-art architecture or a matched leaderboard comparison. The contribution is a traceable workflow showing that a BBB-related peptide classification signal is learnable from simple sequence-derived physicochemical features, with leakage-aware sensitivity analysis and explicit limitations.

## Materials and Methods

### Study Design

This is an in-silico computational study. No wet-lab validation, in-vivo validation, therapeutic testing, clinical testing, or biological mechanism experiment was performed.

The study uses existing repository artifacts only. Models were not rerun for this draft, metrics were not recalculated for this draft, and no new split generation was performed. Metric values are copied from committed result artifacts and prior audit reports. Version v0.7 is a title and abstract positioning revision over v0.6, not a new experiment.

### Dataset Surface

The current rerun-ready BBB-oriented processed dataset surface contains 2,959 rows. Confirmed benchmark-relevant fields include:

- `sequence`
- `label`
- `length`
- `charge`
- `gravy`
- `pI`
- `aromaticity`
- `sequence_id`
- `source`

The `label` field is used as the supervised benchmark target. It is treated as a benchmark label, not as independently verified biological truth.

Dataset provenance and availability remain unresolved for public submission. The imported processed dataset and rerun-ready processed dataset may raise redistribution questions, and dataset availability depends on source terms and manual licensing review. This manuscript draft does not conclude that redistribution is permitted. Row-level processed datasets, row-level predictions, rankings, split manifests, group assignments, and explicit sequence-pair leakage artifacts remain excluded from the public-facing package unless explicit permission and manual approval are documented.

Pre-export requirement: confirm the original dataset source citation, source license, and label-source criteria before any external circulation.

Pre-export requirement: finalize dataset source attribution, license, redistribution status, and data availability wording after manual legal/licensing review.

### Feature Representation

The feature representation is intentionally narrow and sequence-derived:

- length
- charge
- gravy
- pI
- aromaticity

This feature set is used as an interpretable baseline surface. It is not a complete representation of BBB transport chemistry, structure, biology, or mechanism.

The representation is deliberately simpler than deep sequence, structure, or compound-representation models. The purpose is to test traceable sequence-derived signal under conservative audit conditions rather than to optimize a state-of-the-art predictor.

### Baseline Models

The existing benchmark package uses only the following baseline model families:

- Dummy most-frequent classifier
- Logistic Regression
- Random Forest

No new model families are introduced in this manuscript draft.

The model choices are deliberately baseline-oriented. They support reproducible evidence packaging and sensitivity analysis rather than a claim of optimized predictor performance.

The model configurations are stored under `configs/models/`:

| Model | Configuration used in existing artifacts |
| --- | --- |
| Dummy most-frequent | `strategy: most_frequent`; `class_weight: null` |
| Logistic Regression | `penalty: l2`; `C: 1.0`; `max_iter: 1000`; `class_weight: balanced`; `random_state: 42` |
| Random Forest | `n_estimators: 200`; `max_depth: null`; `min_samples_split: 2`; `class_weight: balanced`; `random_state: 42` |

Model training and metric calculation used scikit-learn tooling in the existing repository workflow [@scikit_learn_2011]. Tabular data handling and plotting/reporting support in the repository use pandas and matplotlib where applicable [@pandas_2010; @matplotlib_2007].

### Random-Stratified Baseline Evaluation

The existing random-stratified baseline evaluation used a recovered `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` policy. Reported metrics include ROC-AUC, PR-AUC, precision, recall, F1, and MCC. PR-AUC is emphasized under class imbalance [@saito_rehmsmeier_2015_prauc], and MCC is included as an additional binary-classification summary [@chicco_jurman_2020_mcc].

Random-stratified metrics are interpreted as baseline benchmark-signal estimates. They may be optimistic because prior leakage analysis found same-label duplicate and sequence-similarity structure crossing reconstructed folds.

Random-stratified baseline artifacts were generated by the repository baseline workflow anchored at `scripts/run_baseline.py`, using:

- data config: `configs/data/legacy_bbb_dataset_with_features.yaml`
- feature config: `configs/features/physicochemical.yaml`
- model configs: `configs/models/dummy.yaml`, `configs/models/logistic_regression.yaml`, and `configs/models/random_forest.yaml`
- evaluation config: `configs/eval/default.yaml`

Committed random-stratified metric summaries are stored in:

- `results/tables/model_comparison_summary.csv`
- `results/metrics/legacy_bbb_dummy_v01_metrics.json`
- `results/metrics/legacy_bbb_lr_v01_metrics.json`
- `results/metrics/legacy_bbb_rf_v01_metrics.json`

These repository paths are internal result-artifact sources, not external bibliography citations. Any public-facing supplement should use aggregate summaries and path-level traceability only, without exposing row-level sequences, labels, predictions, rankings, split manifests, group assignments, or sequence-pair leakage tables.

### Leakage-Aware Sensitivity Analysis

The repository also contains a leakage-aware group-stratified sensitivity rerun using the committed split manifest:

- `results/sensitivity/combined_group_stratified_split_manifest.csv`

The split policy is `leakage_aware_group_stratified`. The manifest assigns 2,959 rows and 2,958 groups across 5 folds while keeping group identifiers together. This manifest is a sensitivity setting, not proof that all leakage or provenance concerns are fully controlled.

Known sensitivity limitations include the `max_pairs=10000` grouping caveat, only one non-singleton group under the current combined grouping output, and a `source` field that is too coarse for source-aware split control.

Leakage-aware baseline artifacts were generated by `scripts/run_leakage_aware_baselines.py` from existing model families only. The committed sensitivity outputs are stored in:

- `results/sensitivity/leakage_aware_model_comparison_summary.csv`
- `results/sensitivity/leakage_aware_model_comparison_per_fold.csv`
- `results/sensitivity/leakage_aware_predictions.csv`
- `results/sensitivity/leakage_aware_metrics_summary.json`

This manuscript revision did not rerun the script and did not regenerate these artifacts. Row-level sensitivity artifacts remain restricted from public-facing supplement/export until source/license and release-policy decisions are complete.

### Citation and Reference Status

The final post-sensitivity citation audit reported key-level consistency across 18 unique citation keys, with all checked keys present in `references.bib`. Task 114 completed conservative title-protection cleanup for existing keys only. However, `references.bib` remains a draft and requires human cleanup before public posting.

Pre-export requirement: verify the original dataset source citation, source license, and label-source criteria before external circulation.

Pre-export requirement: complete bibliography metadata cleanup, citation formatting review, and sentence-level source-to-claim review.

## Results

### Random-Stratified Baseline Metrics

The random-stratified baseline metrics show class-prior behavior for the Dummy classifier and learnable benchmark signal for Logistic Regression and Random Forest:

| Model | ROC-AUC | PR-AUC | MCC | Interpretation |
| --- | ---: | ---: | ---: | --- |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 | Class-prior sanity baseline. |
| Logistic Regression | 0.8605 | 0.4903 | 0.3618 | Learnable benchmark signal under random-stratified split. |
| Random Forest | 0.8489 | 0.5002 | 0.4331 | Learnable benchmark signal under random-stratified split. |

These values are not leakage-aware generalization estimates. They remain bounded by documented duplicate and sequence-similarity findings.

These metrics are internal benchmark-surface estimates and should not be read as direct performance comparisons to prior BBB-penetrating peptide predictors without matched datasets, labels, splits, and evaluation policies.

### Leakage-Aware Sensitivity Metrics

Under the leakage-aware group-stratified split manifest, the same baseline model families produced:

| Model | ROC-AUC | PR-AUC | MCC | Interpretation |
| --- | ---: | ---: | ---: | --- |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 | Class-prior sanity baseline. |
| Logistic Regression | 0.8587 | 0.5024 | 0.3747 | Broadly similar to random-stratified baseline under this manifest. |
| Random Forest | 0.8718 | 0.5807 | 0.5084 | Comparable to or higher than random-stratified baseline under this manifest. |

Relative to the random-stratified baseline:

| Model | ROC-AUC delta | PR-AUC delta | MCC delta |
| --- | ---: | ---: | ---: |
| Logistic Regression | -0.0018 | +0.0121 | +0.0130 |
| Random Forest | +0.0229 | +0.0805 | +0.0753 |

The sensitivity rerun did not collapse the baseline signal under the tested group-stratified sensitivity setting. Logistic Regression remained broadly similar, and Random Forest was comparable to or higher than the random-stratified baseline under this manifest.

These leakage-aware values are sensitivity estimates under the committed manifest. They are not direct comparisons to B3Pred, BBPpredict, BBB-PEP-prediction, Augur, DeepB3P, DeepB3Pred, or compound-level BBB predictors.

### Leakage Audit Context

Prior leakage auditing found:

- 4 exact duplicate sequence groups, all same-label, crossing reconstructed folds
- 0 exact label conflicts
- 73 near-duplicate pairs, all same-label, including 56 cross-fold pairs
- 33 high k-mer Jaccard pairs, all same-label, including 29 cross-fold pairs
- a single coarse source value, `legacy_bbb_import`, spanning the dataset
- overall benchmark optimism risk: Moderate

The leakage-aware sensitivity result increases confidence relative to the initial leakage concern, but it does not establish full leakage control or robust generalization.

### Feature-Importance Context

Existing Random Forest artifact summaries identify a feature-importance ordering in the committed rerun package. This is a model-level artifact, not mechanistic proof. Feature importance should not be used to claim causal biology or validated BBB transport mechanisms.

## Discussion

The assembled evidence supports a cautious computational interpretation: BBB-related peptide classification signal is learnable from a small sequence-derived physicochemical feature set in the current benchmark surface. The result is meaningful because it is accompanied by artifact traceability, leakage auditing, and leakage-aware sensitivity analysis rather than presented as an unconstrained performance claim.

The most important post-sensitivity observation is that the baseline signal did not collapse under the tested group-stratified sensitivity setting. Logistic Regression remained broadly similar to the random-stratified baseline, while Random Forest was comparable to or higher under the leakage-aware manifest. This supports continued use of the computational benchmark-signal claim and candidate-prioritization framing before experimental validation.

The contribution is best understood as a reproducible baseline and evidence-traceability package for a peptide-focused BBB-related classification surface, complementary to more complex direct peptide predictors rather than a claim of state-of-the-art prediction. Direct peptide predictor work provides the relevant lineage, while compound-level BBB predictors provide broader context only.

The result remains bounded. The dataset is not provenance-closed, source metadata are coarse, grouping may be incomplete due to the `max_pairs=10000` caveat, and only one non-singleton group appears under the current combined grouping output. The benchmark signal justifies continued internal prioritization and review, but it does not by itself justify biological, translational, or clinical claims. No external validation, wet-lab validation, biological validation, in-vivo validation, therapeutic evaluation, or clinical evaluation has been performed.

## Limitations

- This is an in-silico computational study only.
- No wet-lab validation was performed.
- No biological validation was performed.
- No in-vivo validation was performed.
- No therapeutic or clinical efficacy is claimed.
- Dataset source attribution, licensing, redistribution permission, and availability remain unresolved.
- Original label-source criteria remain unresolved.
- The `source` field is too coarse for source-aware split control.
- The leakage-aware grouping has a `max_pairs=10000` caveat and may be incomplete.
- The current combined grouping output contains only one non-singleton group.
- The feature set is limited to sequence-derived physicochemical descriptors.
- The model set is limited to baseline families.
- This manuscript does not provide a matched comparison against B3Pred, BBPpredict, BBB-PEP-prediction, Augur, DeepB3P, or DeepB3Pred.
- Adjacent compound-level predictors such as LightBBB, Deep-B3, DeePred-BBB, DeepBBBP, and TITAN-BBB address related but different prediction surfaces and are not direct peptide-focused comparators.
- Dataset/task comparability with prior published BBB-penetrating peptide predictor datasets remains unresolved.
- Random-stratified metrics may be optimistic under documented duplicate and sequence-similarity findings.
- Leakage-aware sensitivity analysis is a bounded sensitivity estimate under one manifest, not proof that leakage is fully controlled.
- `references.bib` requires human cleanup before public posting.
- Dataset/source citation and legal/availability decisions remain unresolved.
- Public reproducibility may remain aggregate-only if row-level dataset redistribution is not approved.
- Supplement/export formatting remains incomplete.

## Data and Code Availability

Code and data availability are currently under internal review. Processed row-level datasets and row-level derived artifacts are not publicly redistributed with this draft. The manuscript uses aggregate metric summaries and path-level artifact traceability only. Dataset source, attribution, license, redistribution permission, original label-source criteria, and final data availability wording remain pending manual review. Public posting remains on Hold until these decisions are complete.

Code availability is separable from data availability. Any public code release remains subject to final release review, repository URL confirmation, release/tag selection, software license confirmation, and founder/manual approval. Selected aggregate metrics, aggregate figures, non-row-level summaries, and reproducibility instructions may be considered only after founder/manual, source/legal, release-policy, and claim-boundary review.

For the current internal-preparation posture, row-level processed datasets, row-level labels, row-level predictions, rankings, split manifests, group assignments, sequence-pair leakage artifacts, upstream dataset mirrors, and row-level derived artifacts that can be linked back to restricted source rows are not declared publicly available.

No row-level processed dataset redistribution is declared for this version. Dataset availability and comparability to prior BBB-penetrating peptide predictor datasets remain unresolved pending source attribution, licensing, label-source criteria, and manual review.

Any future release of aggregate derived artifacts must avoid implying redistribution rights over the underlying processed dataset.

Pre-export requirement: confirm the original dataset source citation, source license, and label-source criteria.

Pre-export requirement: finalize the public data availability posture after verified source terms, attribution requirements, redistribution permission, and manual approval.

Pre-export requirement: finalize the code availability statement after repository release policy, software license, and archive/tag policy are approved.

## Funding

No funding.

## Conflict of Interest

N/A

## Acknowledgements

N/A

## Ethics Statement

N/A

## Reference and Export Note

Draft bibliography source: `references.bib`.

Sentence-level Pandoc citation keys have been integrated for background, predictor lineage, adjacent computational context, metric interpretation, and software tooling. The bibliography remains source-managed through `references.bib` and should be rendered during Word/PDF export with Pandoc citeproc or an equivalent bibliography workflow.

Reference-related pre-export requirements:

- Verify full author lists and remove or approve `and others` entries where needed.
- Verify title casing, journal or venue names, DOI, URL, volume, issue, page, and article-number fields.
- Confirm software citation policy for scikit-learn, pandas, and matplotlib.
- Confirm dataset/source citations after dataset legal and provenance review.
- Complete final sentence-level review after verified comparator citation integration.
- Resolve the identity and citation role of `deepb3p3_2023` relative to `tang2025deepb3p` and `arif2025deepb3pred`.

## Supplementary Materials Pointer

Current supplementary materials draft aligned to this manuscript version:

- `docs/supplement/permea-first-paper-supplement-v0-3.md`

The current supplement draft is internal-review only and uses aggregate summaries and path-level traceability; it is not a public supplement export. Supplement v0.3 relies on the manuscript bibliography/reference set unless a separate supplement bibliography is generated for standalone circulation.

Supplement/export unresolved submission blockers:

- Finalize supplement section order and numbering.
- Finalize figure and table captions.
- Finalize file-path checks and export manifest.
- Rerun final claim-boundary and citation checks after formatting.
- Confirm that any public-facing supplement excludes row-level sequences, labels, predictions, rankings, split manifests, group assignments, and sequence-pair leakage tables.

## Submission-Readiness Note

Public preprint submission remains **Hold / not submission-ready**.

Remaining blockers include:

- dataset legal/licensing and redistribution decision
- data/code availability wording
- final dataset/source citation
- final `references.bib` cleanup and source-to-claim review
- final citation/source-claim review
- supplement/export formatting
- founder/manual approval
- final public posting decision

This manuscript draft is an internal first-paper v0.7 preparation draft from existing materials. It does not declare public bioRxiv readiness and does not imply external expert review or peer review.
