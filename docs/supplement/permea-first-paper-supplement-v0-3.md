> **SUPERSEDED (2026-06).** This draft predates Permea Signal ML's repositioning as a
> construct-validity audit of BBB peptide benchmarks. It is retained for history and link
> stability; it does not reflect the repository's current scope or claims. See the README
> for the current direction.

# Supplementary Information for Permea First Paper

Version: v0.3

Aligned manuscript: `permea-first-paper-manuscript-v0-7.md`

## 1. Status Note

This is a working supplementary draft aligned to manuscript v0.7. It supports internal review of the current first-paper package and updates the supplement framing from the earlier v0.6-aligned supplement.

Public submission remains on hold until data/code availability, figure/table, citation, and export checks are completed. Dataset source attribution is resolved to the B3Pred Dataset_3 benchmark surface; final data/code packaging and public release posture remain pending manual review.

This supplement supports computational evidence only. It does not report wet-lab validation, biological validation, in-vivo validation, therapeutic testing, clinical testing, public dataset redistribution permission, or public submission readiness.

Processed row-level datasets, row-level labels, row-level predictions, rankings, split manifests, group assignments, sequence-pair leakage artifacts, upstream dataset mirrors, and row-level derived artifacts remain excluded from public release unless explicit permission and manual approval are documented.

## 2. Supplement Overview

This supplement provides additional context for the manuscript v0.7 evidence package:

- dataset and task details for the BBB-related peptide classification surface
- sequence-derived physicochemical feature definitions
- baseline model and evaluation protocol details
- aggregate metric interpretation
- figure and table support notes
- data/code availability and reproducibility constraints
- limitations and pre-submission checks

The supplement is intended to support the manuscript's conservative framing: a reproducible baseline evidence package for BBB-related peptide permeability signal from sequence-derived features. It is not a state-of-the-art predictor claim, a matched leaderboard comparison, or a biological validation report.

## 3. Dataset and Task Definition

The current benchmark surface is a BBB-related peptide classification task following the B3Pred Dataset_3 benchmark surface. It is composed of 269 BBB-penetrating peptide positives and 2,690 randomly generated non-BBB negatives across 2,959 peptide sequences. The supervised target is treated as a benchmark label, not as independently verified biological truth.

Confirmed aggregate task details from current manuscript materials:

- row count: 2,959
- class composition: 269 BBB-positive peptides and 2,690 non-BBB negatives
- source: B3Pred Dataset_3 / B3Pred-derived public benchmark surface
- supervised target: `label`
- sequence-derived fields: `length`, `charge`, `gravy`, `pI`, `aromaticity`
- operational fields used for internal traceability: `sequence_id`, `source`

The task supports early computational evidence and cautious candidate prioritization before experimental validation. It does not establish physical BBB transport, biological mechanism, therapeutic effect, or clinical utility.

The current class distribution is imbalanced, and PR-AUC and MCC are therefore interpreted alongside ROC-AUC.

No row-level dataset redistribution is asserted in this supplement. Public reproducibility may remain aggregate-only if row-level artifact release is not approved.

## 4. Feature Extraction Details

The feature representation is intentionally narrow and sequence-derived. These descriptors support a transparent baseline surface and should not be interpreted as complete BBB transport chemistry or mechanism.

| Feature | Brief definition | Why it may be relevant | Interpretive caution |
| --- | --- | --- | --- |
| Length | Number of residues in the peptide sequence. | Peptide size may influence permeability-related benchmark signal and model separability. | Length alone does not establish transport mechanism or delivery potential. |
| Charge | Aggregate sequence charge under the implemented feature logic. | Charge can influence peptide interaction with membranes, proteins, and assay surfaces. | Charge effects are context-dependent and not direct evidence of BBB transport. |
| GRAVY / hydrophobicity | Grand average of hydropathy or related hydrophobicity summary. | Hydrophobicity may contribute to permeability-related signal in peptide benchmarks. | Hydrophobicity summaries are coarse and do not capture structure, stability, or assay context. |
| pI | Estimated isoelectric point. | pI may reflect charge-state behavior under different pH contexts. | pI is a derived descriptor and not a mechanistic BBB transport measurement. |
| Aromaticity | Fraction or summary of aromatic residue content. | Aromatic residues can influence interaction profiles and physicochemical behavior. | Model-level association should not be read as causal biological evidence. |

Feature importance, if shown in a figure or table, should be captioned as a model-level artifact only.

## 5. Model Training and Evaluation Protocol

The manuscript v0.7 evidence package uses baseline model families only:

- Dummy most-frequent classifier
- Logistic Regression
- Random Forest

The current supplement does not introduce new model families, rerun models, regenerate figures, or create new splits.

The random-stratified baseline evaluation uses aggregate metrics from committed result artifacts. The leakage-aware analysis is a bounded sensitivity setting using an existing group-stratified manifest. It is not proof that all leakage or provenance concerns are resolved.

Reported metrics include:

- ROC-AUC
- PR-AUC
- MCC

PR-AUC matters because the task is class-imbalanced and precision-recall behavior is more informative than ROC-AUC alone when positive examples are relatively sparse. ROC-AUC remains useful for ranking discrimination but can obscure practical behavior under imbalance. MCC is useful as a single binary-classification summary that accounts for all cells of the confusion matrix.

Implementation details not stated in manuscript v0.7 or committed configuration files should be marked as to be verified before submission rather than inferred.

## 6. Results Support and Interpretation

The supplement supports the manuscript's aggregate computational result interpretation.

Random-stratified aggregate metrics:

| Model | ROC-AUC | PR-AUC | MCC |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 |
| Logistic Regression | 0.8605 | 0.4903 | 0.3618 |
| Random Forest | 0.8489 | 0.5002 | 0.4331 |

Leakage-aware sensitivity aggregate metrics:

| Model | ROC-AUC | PR-AUC | MCC |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 |
| Logistic Regression | 0.8587 | 0.5024 | 0.3747 |
| Random Forest | 0.8718 | 0.5807 | 0.5084 |

Relative to the random-stratified baseline:

| Model | ROC-AUC delta | PR-AUC delta | MCC delta |
| --- | ---: | ---: | ---: |
| Logistic Regression | -0.0018 | +0.0121 | +0.0130 |
| Random Forest | +0.0229 | +0.0805 | +0.0753 |

These values support initial computational evidence for a learnable BBB-related peptide permeability signal under the documented benchmark settings. They support candidate prioritization before experimental validation, not wet-lab or clinical validation.

These values are not direct comparisons to B3Pred, BBPpredict, BBB-PEP-prediction, Augur, DeepB3P, DeepB3Pred, or compound-level BBB predictors. Dataset, split, label, and metric comparability with prior published predictors remains unresolved.

Numerical values should be verified against manuscript v0.7 and committed result artifacts before submission.

## 7. Supplementary Figures and Tables

Supplementary figures and tables are working references pending final source-file verification, caption approval, citation review, and export QA. All items support computational evidence only. No row-level dataset records, row-level labels, row-level predictions, rankings, split manifests, group assignments, sequence-pair leakage artifacts, or upstream dataset mirrors are included in this supplement.

Public submission remains on hold until final data/code availability, source-file, caption, numbering, citation, and export checks are completed.

### 7.1 Proposed Supplementary Figures

| Proposed figure | Working title | Candidate source | Current source status | Conservative caption draft | Required check |
| --- | --- | --- | --- | --- | --- |
| Supplementary Figure S1 | Benchmark workflow overview | `figures/benchmark_workflow_outputs.png` | Candidate source present; final caption/export QA pending. | Computational workflow overview for the BBB-related peptide benchmark package. The diagram summarizes the high-level path from processed benchmark inputs to aggregate model outputs and review artifacts; it does not report biological validation or approve public data release. | Confirm workflow is current and contains no restricted row-level content. |
| Supplementary Figure S2 | Aggregate benchmark performance summary | `figures/legacy_vs_rerun_metrics.png` | Candidate source present; final caption/export QA pending. | Aggregate benchmark performance summary for baseline model evaluation under documented computational settings. The figure should be interpreted as benchmark-surface evidence only and not as final biological or clinical performance evidence. | Confirm values, labels, and model names match manuscript v0.7 and aggregate result artifacts. |
| Supplementary Figure S3 | Regenerated Random Forest feature-importance summary | `figures/regenerated_rf_feature_importance.png` | Candidate source present; final caption/export QA pending. | Aggregate Random Forest feature-importance summary for the regenerated baseline. Feature importance is model- and dataset-dependent and should not be interpreted as a causal or mechanistic explanation of BBB transport. | Confirm source values and ensure caption remains model-level only. |
| Supplementary Figure S4 | Dataset distribution and class-imbalance surface | `figures/dataset_distribution.png` | Candidate source present; final caption/export QA pending. | Aggregate dataset distribution and class-imbalance summary for the benchmark surface. The figure provides metric-interpretation context and does not disclose row-level records or assert dataset redistribution permission. | Confirm the figure shows aggregate counts only and no row-level examples, identifiers, or labels. |

### 7.2 Proposed Supplementary Tables

| Proposed table | Working title | Contents | Current status | Conservative caption draft | Required check |
| --- | --- | --- | --- | --- | --- |
| Supplementary Table S1 | Feature definitions and interpretive cautions | Length, charge, GRAVY/hydrophobicity, pI, aromaticity. | Drafted from supplement v0.3 feature section. | Sequence-derived feature definitions used in the baseline benchmark surface, with interpretive cautions for each descriptor. These features support transparent computational modeling but do not fully represent BBB transport biology. | Verify definitions against implemented feature logic before submission. |
| Supplementary Table S2 | Model and evaluation protocol summary | Task framing, baseline model framing, metric set, class-imbalance handling, bounded sensitivity checks, and unverified implementation-specific details. | Draft concept. | Baseline model and evaluation protocol summary for the computational benchmark package. Implementation details not confirmed in manuscript v0.7 or committed configuration files should remain marked as to verify before submission. | Confirm model families, split/evaluation framing, metric names, and sensitivity wording against committed documentation. |
| Supplementary Table S3 | Aggregate metric interpretation guide | ROC-AUC, PR-AUC, MCC, dummy baseline interpretation, class-imbalance interpretation, and bounded sensitivity interpretation. | Draft concept using aggregate metric text above. | Aggregate metric interpretation guide for the BBB-related peptide benchmark surface. ROC-AUC, PR-AUC, and MCC are interpreted as computational benchmark summaries, not biological performance measures. | Confirm all metric definitions and examples match manuscript v0.7. |
| Supplementary Table S4 | Artifact allow/hold matrix | Aggregate figure/table candidates, aggregate metric summaries, feature definitions, protocol summaries, and blocked row-level or row-derived artifact classes. | Drafted below. | Artifact release-status matrix separating aggregate candidates, review-required files, and blocked row-level or row-derived artifacts. This table is a release-planning aid and does not approve public release. | Confirm final release posture after repository and manual approval decisions. |

### 7.3 Supplementary Table S1: Feature Definitions and Interpretive Cautions

| Feature | Concise definition | Interpretive caution |
| --- | --- | --- |
| Length | Number of residues in the peptide sequence. | Size can contribute to benchmark signal but does not establish transport mechanism. |
| Charge | Aggregate sequence charge under the implemented feature logic. | Charge effects are context-dependent and not direct evidence of BBB transport. |
| GRAVY / hydrophobicity | Grand average hydropathy or related hydrophobicity summary. | Hydrophobicity summaries are coarse and do not capture structure, stability, or assay context. |
| pI | Estimated isoelectric point. | pI is derived and should not be treated as a direct transport measurement. |
| Aromaticity | Fraction or summary of aromatic residue content. | Model association should not be read as causal biological evidence. |

### 7.4 Supplementary Table S2: Model and Evaluation Protocol Summary

| Protocol element | Current summary | Status |
| --- | --- | --- |
| Task framing | BBB-related peptide classification benchmark using sequence-derived physicochemical features. | Confirmed at manuscript level. |
| Baseline models | Dummy most-frequent classifier, Logistic Regression, Random Forest. | Confirmed at manuscript level. |
| Metric set | ROC-AUC, PR-AUC, MCC. | Confirmed at manuscript level. |
| Class-imbalance handling | PR-AUC and MCC are interpreted alongside ROC-AUC because the positive class is relatively sparse. | Confirm final prevalence wording before submission. |
| Random-stratified evaluation | Aggregate baseline evaluation setting. | Confirm artifact values before export. |
| Leakage-aware sensitivity | Bounded group-stratified sensitivity setting using aggregate summaries only. | Do not treat as proof of complete leakage control. |
| Implementation specifics | Hyperparameters, environment details, and exact split construction details. | To verify before submission unless already documented in committed configuration files. |

### 7.5 Supplementary Table S3: Aggregate Metric Interpretation Guide

| Metric or reference point | Interpretation in this supplement | Caution |
| --- | --- | --- |
| ROC-AUC | Ranking-discrimination summary under the documented benchmark setting. | Can be less informative under class imbalance if read alone. |
| PR-AUC | Precision-recall summary emphasized because positive examples are relatively sparse. | Sensitive to prevalence and benchmark definition. |
| MCC | Binary-classification summary accounting for all confusion-matrix cells. | Should be interpreted with the selected thresholding/evaluation context. |
| Dummy most-frequent baseline | Baseline reference point for non-informative majority-class behavior. | Does not represent a useful classifier. |
| Logistic Regression and Random Forest baselines | Transparent baseline model families for benchmark signal assessment. | Do not imply optimized predictor maturity or external superiority. |
| Leakage-aware sensitivity | Bounded aggregate sensitivity check. | Does not resolve all provenance, duplicate, or leakage concerns. |

### 7.6 Supplementary Table S4: Artifact Allow/Hold Matrix

| Artifact category | Example candidates or classes | Current posture | Reason | Future unlock condition |
| --- | --- | --- | --- | --- |
| Aggregate workflow figure | `figures/benchmark_workflow_outputs.png` | Public-safe candidate after review | Workflow-level artifact; expected to avoid row-level content. | Final source-file, caption, and manual approval. |
| Aggregate metric figures | `figures/legacy_vs_rerun_metrics.png` | Public-safe candidate after review | Aggregate performance visualization. | Confirm metric consistency and caption boundaries. |
| Aggregate feature-importance figure | `figures/regenerated_rf_feature_importance.png` | Public-safe candidate after review | Model-level aggregate interpretation. | Confirm values and non-mechanistic caption. |
| Aggregate metric summaries | `results/tables/model_comparison_summary.csv`; aggregate sensitivity summaries | Public-safe candidate after review | Aggregate model metrics. | Confirm values and exclude row-level derivatives. |
| Feature definitions | Feature definition table in this supplement | Public-safe candidate after review | Documentation-level content. | Confirm definitions against implemented feature logic. |
| Protocol summaries | Model/evaluation summary table | Public-safe candidate after review | Documentation-level content. | Confirm against committed configs and manuscript. |
| Candidate-ranking preview | Candidate-ranking figures or ranking outputs | Hold / blocked | Can expose row-level or row-derived prioritization. | Separate release approval and claim-boundary review. |
| Row-level predictions | Prediction CSV artifacts | Hold / blocked | Row-level derived artifact. | Separate documented release approval. |
| Split manifests | Split-manifest artifacts | Hold / blocked | May expose identifiers, labels, folds, groups, or row-derived structure. | Separate documented release approval. |
| Group assignments | Group-assignment artifacts | Hold / blocked | May expose row-derived grouping information. | Separate documented release approval. |
| Leakage-pair artifacts | Pair-level leakage or similarity CSVs | Hold / blocked | Can expose restricted row relationships. | Separate documented release approval. |
| Processed row-level datasets | Processed dataset files | Hold / blocked | Row-level dataset release is not included in the current public-facing package. | Separate row-level release decision and manual approval. |

### 7.7 Numbering and Cross-Reference Notes

Supplementary figures use `Supplementary Figure S1`, `Supplementary Figure S2`, and so on. Supplementary tables use `Supplementary Table S1`, `Supplementary Table S2`, and so on.

Manuscript v0.7 remains text-first at this stage. Any main-text figure or table insertion requires manual approval of the source artifact, caption, numbering, and claim boundary. Until numbering is finalized, manuscript references should use general language such as `see Supplementary Information` rather than unstable figure or table numbers.

Before Word/PDF export, verify that each callout has a matching item, every item has one caption, captions match the selected source files, blocked artifacts are absent, and no caption implies public release or evidence beyond the computational benchmark setting.

Caption verification should confirm:

- artifact type: workflow-only, aggregate-only, or documentation-only
- split/evaluation context
- dataset/source caveat where relevant
- no biological or therapeutic validation implication
- no dataset redistribution implication
- public release status if the material remains internal-only

## 8. Data/Code Availability and Reproducibility Constraints

Code and reproducibility logic may be shared where permitted after final release review, repository URL confirmation, software license approval, release tag selection, and restricted-path review.

Row-level artifacts are excluded or restricted unless a separate release decision and manual approval are documented. This includes processed row-level datasets, row-level labels, row-level predictions, rankings, split manifests, group assignments, sequence-pair leakage artifacts, upstream dataset mirrors, and row-level derived artifacts.

This supplement does not assert row-level dataset release. Public release posture must remain aligned with manuscript v0.7 and final repository policy.

Safe current posture:

- code and data availability remain under internal review
- processed row-level datasets are not publicly redistributed with this draft
- row-level derived artifacts are not publicly redistributed with this draft
- aggregate metric summaries and path-level traceability support the manuscript
- dataset source attribution is B3Pred Dataset_3 / B3Pred-derived public benchmark surface
- final data/code packaging and public release wording remain pending manual review
- public posting remains on hold until normal paper QA and approvals are complete

## 9. Citation and Source Note

This supplement is aligned to manuscript v0.7 and relies on the manuscript bibliography/reference set unless it is circulated as a standalone document. Separate supplement circulation requires citation and bibliography rendering, figure/table source verification, and final source-to-claim review.

No unsupported citation keys are added in this supplement draft. Dataset source attribution is resolved to the B3Pred Dataset_3 benchmark surface, with B3Pred and B3Pdb lineage handled through the manuscript bibliography. Final data/code packaging and public release wording remain pending manual review.

## 10. Limitations

- This is computational-only evidence.
- No wet-lab validation has been performed.
- No biological validation has been performed.
- No in-vivo validation has been performed.
- No therapeutic effect or clinical utility claim is made.
- No universal delivery prediction claim is made.
- Dataset source attribution is resolved to B3Pred Dataset_3; final data/code packaging and release wording remain under review.
- Class imbalance affects interpretation; PR-AUC and MCC should be reviewed alongside ROC-AUC.
- The feature set is narrow and sequence-derived.
- Feature-level associations are not mechanistic proof.
- Random-stratified metrics may be optimistic under duplicate and similarity structure.
- Leakage-aware sensitivity is bounded to the committed setting and is not proof of complete leakage control.
- External validation remains future work.
- A design-build-test-learn loop would be needed before any biological or translational claims.
- Figure/table numbering, captions, source files, citation rendering, and export checks remain incomplete.

## 11. Supplement-to-Manuscript Alignment Checklist

- [x] Manuscript version anchor updated to v0.7.
- [x] Claim level aligned to computational evidence only.
- [x] Data/code availability aligned to conservative pending-review posture.
- [ ] Figure/table references pending verification.
- [ ] Caption wording pending verification.
- [ ] Citation/reference consistency pending verification.
- [ ] Word/PDF export QA pending.
- [ ] Founder/manual approval pending.
- [x] Public submission remains on hold.

## 12. Pre-Submission Checklist

- [ ] Manual citation QA.
- [ ] Figure/table numbering QA.
- [ ] Caption QA.
- [ ] Word/PDF export QA.
- [ ] Data/code availability final approval.
- [ ] Row-level artifact release decision.
- [ ] Final data/code packaging decision.
- [ ] Bibliography/source verification.
- [ ] Founder/manual approval.
- [ ] Limited expert review feedback integration, if performed.
