# Initial Computational Evidence for Learnable BBB-Related Peptide Permeability Signals from Sequence-Derived Physicochemical Features

## Author and Affiliation

Albert Heekwan Kim

Permea Research

Corresponding author: a.kim@permea.us

## Abstract

Blood-brain barrier (BBB)-related peptide permeability remains a difficult early-stage prioritization problem, and computational benchmarks in this area require careful separation between reproducible in-silico signal, dataset provenance limits, and biological validation. This manuscript presents an initial computational evidence package for a BBB-related peptide classification task using sequence-derived physicochemical features: length, charge, gravy, pI, and aromaticity. Existing baseline artifacts compare a Dummy most-frequent classifier, Logistic Regression, and Random Forest. Under the recovered random-stratified baseline evaluation, Logistic Regression and Random Forest showed learnable permeability-related benchmark signal beyond the class-prior Dummy baseline. A leakage-aware group-stratified sensitivity rerun did not collapse the signal under the tested grouping strategy: Logistic Regression reached ROC-AUC 0.8587, PR-AUC 0.5024, and MCC 0.3747, while Random Forest reached ROC-AUC 0.8718, PR-AUC 0.5807, and MCC 0.5084. These results support cautious pre-experimental candidate prioritization, but they do not establish leakage-free status, robust generalization, biological validation, wet-lab validation, therapeutic efficacy, or clinical efficacy. Public preprint submission remains on Hold pending metadata, dataset licensing, data/code availability, reference cleanup, supplement/export formatting, and founder/manual approval.

## Keywords

- blood-brain barrier
- peptide permeability
- sequence-derived physicochemical features
- computational benchmark
- pre-experimental candidate prioritization
- leakage-aware sensitivity analysis
- reproducible evidence package

## Introduction

Biological delivery is a central bottleneck for many therapeutic modalities, and BBB-related peptide prioritization remains a particularly challenging setting. Computational models can support early hypothesis generation when their evidence is reproducible, bounded, and clearly separated from experimental validation. In this manuscript, "delivery" and "permeability" language refer to a computational BBB-related peptide classification task, not to experimentally validated BBB transport or therapeutic effect.

The present work assembles an initial in-silico evidence package from existing Permea repository materials. The target framing is deliberately narrow: determine whether BBB-related peptide permeability signals are learnable from a small set of sequence-derived physicochemical features and whether those signals can support candidate prioritization before experimental validation. Prior BBB peptide databases and predictors provide context for sequence-first benchmark work, while adjacent peptide-prediction literature motivates careful evaluation and claim boundaries. Citation keys used in the existing manuscript candidate include `bbb_shuttle_review_2016`, `brainpeps_2012`, `b3pdb_2021`, `b3pred_2021`, `bbppred_2021`, `bbppredict_2022`, `augur_2024`, `brainpeppass_2024`, `deepb3p3_2023`, `esm_bbb_pred_2025`, `b3bpfn_2026`, `practicpp_2024`, and `perseucpp_2025`.

This manuscript does not claim that the dataset is provenance-closed, that the benchmark is leakage-free, that the models robustly generalize, or that any candidate is biologically or clinically validated.

## Materials and Methods

### Study Design

This is an in-silico computational study. No wet-lab validation, in-vivo validation, therapeutic testing, clinical testing, or biological mechanism experiment was performed.

The study uses existing repository artifacts only. Models were not rerun for this draft, metrics were not recalculated for this draft, and no new split generation was performed. Metric values are copied from committed result artifacts and prior audit reports.

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

The `label` field is used as the supervised benchmark target. It is not treated as independently verified biological truth.

Dataset provenance and availability remain unresolved for public submission. The imported processed dataset and rerun-ready processed dataset may raise redistribution questions, and dataset availability depends on source terms and manual licensing review. This manuscript draft does not conclude that redistribution is permitted.

Unresolved submission blocker: finalize dataset source attribution, license, redistribution status, and data availability wording after manual legal/licensing review.

### Feature Representation

The feature representation is intentionally narrow and sequence-derived:

- length
- charge
- gravy
- pI
- aromaticity

This feature set is used as an interpretable baseline surface. It is not a complete representation of BBB transport chemistry, structure, biology, or mechanism.

### Baseline Models

The existing benchmark package uses only the following baseline model families:

- Dummy most-frequent classifier
- Logistic Regression
- Random Forest

No new model families are introduced in this manuscript draft.

The model configurations are stored under `configs/models/`:

| Model | Configuration used in existing artifacts |
| --- | --- |
| Dummy most-frequent | `strategy: most_frequent`; `class_weight: null` |
| Logistic Regression | `penalty: l2`; `C: 1.0`; `max_iter: 1000`; `class_weight: balanced`; `random_state: 42` |
| Random Forest | `n_estimators: 200`; `max_depth: null`; `min_samples_split: 2`; `class_weight: balanced`; `random_state: 42` |

### Random-Stratified Baseline Evaluation

The existing random-stratified baseline evaluation used a recovered `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` policy. Reported metrics include ROC-AUC, PR-AUC, precision, recall, F1, and MCC. PR-AUC is emphasized under class imbalance, and MCC is included as an additional binary-classification summary.

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

This manuscript revision did not rerun the script and did not regenerate these artifacts.

### Citation and Reference Status

The final post-sensitivity citation audit reported key-level consistency across 18 unique citation keys, with all checked keys present in `references.bib`. However, `references.bib` remains a draft and requires human cleanup before public posting.

Unresolved submission blocker: complete bibliography metadata cleanup, citation formatting, and sentence-level source-to-claim review.

## Results

### Random-Stratified Baseline Metrics

The random-stratified baseline metrics show class-prior behavior for the Dummy classifier and learnable benchmark signal for Logistic Regression and Random Forest:

| Model | ROC-AUC | PR-AUC | MCC | Interpretation |
| --- | ---: | ---: | ---: | --- |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 | Class-prior sanity baseline. |
| Logistic Regression | 0.8605 | 0.4903 | 0.3618 | Learnable benchmark signal under random-stratified split. |
| Random Forest | 0.8489 | 0.5002 | 0.4331 | Learnable benchmark signal under random-stratified split. |

These values are not leakage-aware generalization estimates. They remain bounded by documented duplicate and sequence-similarity findings.

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

### Leakage Audit Context

Prior leakage auditing found:

- 4 exact duplicate sequence groups, all same-label, crossing reconstructed folds
- 0 exact label conflicts
- 73 near-duplicate pairs, all same-label, including 56 cross-fold pairs
- 33 high k-mer Jaccard pairs, all same-label, including 29 cross-fold pairs
- a single coarse source value, `legacy_bbb_import`, spanning the dataset
- overall benchmark optimism risk: Moderate

The leakage-aware sensitivity result increases confidence relative to the initial leakage concern, but it does not establish leakage-free status or robust generalization.

### Feature-Importance Context

Existing Random Forest artifact summaries identify a feature-importance ordering in the committed rerun package. This is a model-level artifact, not mechanistic proof. Feature importance should not be used to claim causal biology or validated BBB transport mechanisms.

## Discussion

The assembled evidence supports a cautious computational interpretation: BBB-related peptide classification signal is learnable from a small sequence-derived physicochemical feature set in the current benchmark surface. The result is meaningful because it is accompanied by artifact traceability, leakage auditing, and leakage-aware sensitivity analysis rather than presented as an unconstrained performance claim.

The most important post-sensitivity observation is that the baseline signal did not collapse under the tested group-stratified sensitivity setting. Logistic Regression remained broadly similar to the random-stratified baseline, while Random Forest was comparable to or higher under the leakage-aware manifest. This supports continued use of the computational benchmark-signal claim and pre-experimental candidate-prioritization framing.

The result remains bounded. The dataset is not provenance-closed, source metadata are coarse, grouping may be incomplete due to the `max_pairs=10000` caveat, and only one non-singleton group appears under the current combined grouping output. No external validation, wet-lab validation, biological validation, in-vivo validation, therapeutic evaluation, or clinical evaluation has been performed.

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
- Random-stratified metrics may be optimistic under documented duplicate and sequence-similarity findings.
- Leakage-aware sensitivity analysis is a bounded sensitivity estimate under one manifest, not proof that leakage is fully controlled.
- `references.bib` requires human cleanup before public posting.
- Supplement/export formatting remains incomplete.

## Data and Code Availability

Code availability can be decided separately from data availability. Candidate wording from the current submission-readiness package states that code supporting the computational benchmark workflow is planned for release through an approved Permea repository or archive, pending final repository URL, commit, release tag, and software license confirmation.

Data availability remains unresolved. The processed peptide dataset used for the benchmark reruns is not approved for public redistribution in this draft because original source attribution, licensing, redistribution permission, raw source path, public dataset version, and label-source criteria remain pending confirmation. Derived benchmark artifacts, audit summaries, and code may be released where permitted and where they do not imply redistribution rights over the underlying dataset.

Unresolved submission blocker: finalize code availability statement after repository release policy is approved.

Unresolved submission blocker: finalize data availability statement only after source terms and manual licensing review are complete.

## Funding

No funding.

## Conflict of Interest

N/A

## Acknowledgements

N/A

## Ethics Statement

N/A

## References Placeholder and Citation-Key Notes

Draft bibliography source: `references.bib`.

Citation keys used by the existing manuscript package have passed key-level consistency checks, but final public submission requires human bibliography cleanup and source-to-claim review.

Reference-related unresolved submission blockers:

- Unresolved submission blocker: verify full author lists and remove or approve `and others` entries where needed.
- Unresolved submission blocker: verify title casing, journal or venue names, DOI, URL, volume, issue, page, and article-number fields.
- Unresolved submission blocker: confirm software citation policy for scikit-learn, pandas, and matplotlib.
- Unresolved submission blocker: confirm dataset/source citations after dataset legal and provenance review.

## Supplementary Materials Pointer

Supplementary materials draft:

- `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`

Supplement/export unresolved submission blockers:

- Unresolved submission blocker: finalize supplement section order and numbering.
- Unresolved submission blocker: finalize figure and table captions.
- Unresolved submission blocker: finalize file-path checks and export manifest.
- Unresolved submission blocker: rerun final claim-boundary and citation checks after formatting.

## Submission-Readiness Note

Public preprint submission remains **Hold / not submission-ready**.

Remaining blockers include:

- metadata and disclosures
- dataset legal/licensing and redistribution decision
- data/code availability wording
- `references.bib` cleanup
- final citation/source-claim review
- supplement/export formatting
- founder/manual approval
- final public posting decision

This manuscript draft is an internal first-paper assembly from existing materials. It does not declare public bioRxiv readiness and does not imply external expert review or peer review.
