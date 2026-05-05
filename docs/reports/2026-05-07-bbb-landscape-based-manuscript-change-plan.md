# BBB Landscape-Based Manuscript Change Plan - 2026-05-07

## 1. Executive Summary

The BBB landscape review changes the recommended manuscript positioning for Permea's first paper.

Manuscript v0.2 is suitable for internal review, but it should be revised to v0.3 before broader review so the paper is explicitly positioned against direct BBB-penetrating peptide predictor work rather than generic BBB permeability prediction work.

Recommended positioning:

- Permea should be framed as a conservative, reproducible, peptide-focused baseline/evidence package.
- The closest lineage is B3Pdb/B3Pred and related BBB-penetrating peptide predictor work.
- The first paper should emphasize sequence-derived physicochemical signal, artifact traceability, leakage-aware sensitivity, and candidate prioritization before experimental validation.
- Permea should not claim to be a new state-of-the-art BBB permeability predictor, BBBP predictor, or validated BBB delivery system.

Public bioRxiv remains **Hold / not submission-ready**. Dataset redistribution remains unresolved.

## 2. Direct Peptide Predictor Landscape

Direct comparators are BBB-penetrating peptide resources or predictors. These are the primary manuscript comparator class because Permea's current task is peptide-focused and sequence-derived.

Direct peptide comparators identified by the landscape review:

- B3Pdb / B3Pred
- BBPpredict
- BBB-PEP-prediction
- Augur
- DeepB3P
- DeepB3Pred

Existing repo citation keys that appear aligned with this direct or near-direct lineage:

- `b3pdb_2021`
- `b3pred_2021`
- `bbppred_2021`
- `bbppredict_2022`
- `augur_2024`
- `deepb3p3_2023`
- `brainpeps_2012`
- `brainpeppass_2024`
- `esm_bbb_pred_2025`
- `b3bpfn_2026`

Important boundary:

- These references should be used to establish peptide/database/predictor context and lineage.
- They should not be used to claim Permea is superior, state-of-the-art, leakage-free, biologically validated, or experimentally confirmed.

## 3. Adjacent Compound BBB Predictor Landscape

Adjacent compound-level BBB predictors are relevant background only. They should not be treated as direct peptide benchmarks unless the manuscript explicitly explains the distinction.

Adjacent compound-level BBB permeability predictors identified by the landscape review:

- LightBBB
- Deep-B3
- DeePred-BBB
- DeepBBBP
- TITAN-BBB

Required distinction:

- TITAN-BBB and DeePred-BBB are adjacent compound-level BBB predictors.
- They are not direct peptide-focused comparators for the current Permea first paper.
- They may be mentioned only to clarify the broader computational BBB landscape and why the present work is restricted to a peptide-focused, sequence-derived baseline/evidence package.

Reference status:

- These adjacent compound-level references are not currently represented as explicit citation keys in `references.bib`.
- Do not add references or metadata until exact source details are verified.
- Mark any v0.3 citation need as source-required if no verified repo source exists.

## 4. Implications for Permea Positioning

The manuscript should be sharpened around a narrow, defensible position:

```text
Permea provides a reproducible, peptide-focused computational baseline/evidence package showing that BBB-related peptide classification signal is learnable from simple sequence-derived physicochemical features, with artifact traceability and leakage-aware sensitivity analysis.
```

The manuscript should avoid broader predictor competition language:

- not a SOTA BBB permeability predictor
- not a SOTA BBBP predictor
- not a benchmark claiming superiority over B3Pred, BBPpredict, Augur, DeepB3P, or DeepB3Pred
- not a compound-level BBB predictor comparison
- not a validated biological delivery paper

The strongest defensible contribution is not model novelty. It is reproducible evidence packaging, conservative claim discipline, and a transparent baseline/sensitivity workflow.

## 5. What Must Change in Manuscript v0.2

Manuscript v0.2 is already cautious, but v0.3 should make the landscape positioning more explicit.

Required changes:

1. Add a short "Related Work" section or subsection.
2. Separate direct peptide predictors from adjacent compound-level BBB predictors.
3. State that Permea's current work is not a SOTA predictor comparison.
4. Clarify that B3Pdb/B3Pred-like resources are the most relevant lineage.
5. Add a paragraph explaining why simple sequence-derived physicochemical baselines remain useful despite newer/deeper predictors.
6. Preserve leakage-aware sensitivity framing as a sensitivity estimate, not validation.
7. Keep data availability conservative because dataset redistribution remains unresolved.
8. Mark missing comparator citations as source-required instead of inventing references.

## 6. What Should Not Change

Do not change:

- metric values
- random-stratified baseline values
- leakage-aware sensitivity values
- confirmed metadata
- in-silico-only scope
- no wet-lab / no biological validation boundary
- dataset redistribution unresolved status
- source/legal TODOs
- references unless verified source metadata is available in a later reference task
- model family scope
- no-new-experiments status

Do not broaden the manuscript into:

- a SOTA benchmark paper
- a compound BBB predictor comparison
- a therapeutic/clinical relevance claim
- a biological mechanism paper
- a validation paper

## 7. Section-by-Section Change Checklist

### Title

Current title is conservative but long:

`Initial Computational Evidence for Learnable BBB-Related Peptide Permeability Signals from Sequence-Derived Physicochemical Features`

Recommended v0.3 title direction:

`A Reproducible Peptide-Focused Baseline for BBB-Related Permeability Signal from Sequence-Derived Physicochemical Features`

Rationale:

- Emphasizes reproducibility and peptide focus.
- Avoids sounding like a new SOTA predictor.
- Keeps "BBB-related" and "signal" language.

### Abstract

Required edits:

- Add one sentence placing the work in peptide-focused BBB predictor lineage.
- State that direct comparators are BBB-penetrating peptide predictors and resources.
- Avoid "new predictor" or "SOTA" framing.
- Preserve exact metrics.
- Preserve no-validation and public Hold statements.

Candidate wording:

```text
Rather than presenting a new state-of-the-art BBB permeability predictor, this work assembles a reproducible peptide-focused baseline/evidence package in the lineage of BBB-penetrating peptide database and predictor efforts.
```

### Introduction

Required edits:

- Expand the current predictor-context paragraph into direct peptide landscape plus adjacent compound landscape.
- Direct peptide context should mention B3Pdb/B3Pred, BBPpredict, BBB-PEP-prediction, Augur, DeepB3P, and DeepB3Pred where citations are available or marked source-required.
- Adjacent compound-level context should mention LightBBB, Deep-B3, DeePred-BBB, DeepBBBP, and TITAN-BBB only as broader BBB prediction context.
- Explicitly say Permea does not benchmark against compound-level BBB predictors.

Candidate wording:

```text
The closest context for the present study is BBB-penetrating peptide prediction rather than small-molecule or compound-level BBB permeability prediction. Compound-level BBB predictors are relevant to the broader computational BBB landscape, but they are adjacent rather than direct comparators for this peptide-focused baseline.
```

### Related Work

Recommended addition: create a dedicated `Related Work` section after the Introduction or as a subsection within it.

Suggested structure:

1. BBB-penetrating peptide resources and predictors.
2. Adjacent compound-level BBB predictors.
3. Permea's positioning as a reproducible baseline/evidence package.

Required boundary:

- Do not claim comparative superiority.
- Do not claim benchmark equivalence if datasets, labels, and tasks differ.
- Do not imply experimental validation.

### Methods

Required edits:

- Keep Methods largely unchanged.
- Add one clarifying sentence that model families are intentionally simple baseline families, not optimized SOTA architectures.
- In Feature Representation, add that the representation is deliberately simpler than deep sequence or structure models.

Candidate wording:

```text
The model and feature choices are deliberately baseline-oriented; the purpose is to test traceable sequence-derived signal under conservative audit conditions rather than to optimize a state-of-the-art predictor.
```

### Results

Required edits:

- Keep all metric values unchanged.
- Add a caution that results should not be compared as direct performance claims against published peptide predictors unless dataset/task comparability is established.
- Preserve leakage-aware sensitivity wording.

Candidate wording:

```text
These metrics are internal benchmark-surface estimates and should not be read as direct performance comparisons to prior BBB-penetrating peptide predictors without matched datasets, labels, splits, and evaluation policies.
```

### Discussion

Required edits:

- Add a paragraph explicitly defining the contribution:
  - reproducible baseline/evidence package
  - transparent artifact traceability
  - leakage-aware sensitivity
  - candidate prioritization before experimental validation
- State that the contribution is complementary to deeper/direct peptide predictor literature, not a replacement.
- State that v0.3 should not claim SOTA.

Candidate wording:

```text
The contribution is best understood as a reproducible baseline and evidence-traceability package for a peptide-focused BBB-related classification surface, complementary to more complex direct peptide predictors rather than a claim of state-of-the-art prediction.
```

### Limitations

Required edits:

- Add explicit limitation: no matched comparison against B3Pred, BBPpredict, BBB-PEP-prediction, Augur, DeepB3P, or DeepB3Pred.
- Add explicit limitation: adjacent compound-level predictors such as TITAN-BBB and DeePred-BBB address related but different prediction surfaces.
- Preserve current limitations around source, licensing, leakage sensitivity, feature simplicity, and no validation.

### Data Availability

Required edits:

- Keep current conservative stance.
- Add that dataset/source comparability to prior predictor datasets remains unresolved.
- Do not state that data can be redistributed.
- Keep `TODO(source-required)` for original dataset source/citation/license/label-source criteria.

Candidate wording:

```text
Dataset availability and comparability to prior BBB-penetrating peptide predictor datasets remain unresolved pending source attribution, licensing, label-source criteria, and manual review.
```

## 8. Required Claim-Boundary Updates

Add or strengthen these boundaries in v0.3:

- Permea is not claiming SOTA.
- Permea is not claiming direct performance superiority over BBB-penetrating peptide predictors.
- Permea is not claiming comparison to compound-level BBB predictors.
- Permea is not claiming dataset/task equivalence with prior published benchmarks.
- Permea is not claiming leakage-free status.
- Permea is not claiming robust generalization.
- Permea is not claiming biological, wet-lab, in-vivo, therapeutic, or clinical validation.

## 9. Required Data Availability Updates

v0.3 should preserve and slightly sharpen the current data availability stance:

- Processed dataset redistribution remains unresolved.
- Dataset source identity remains unresolved.
- Dataset license/terms remain unresolved.
- Original label-source criteria remain unresolved.
- Comparability to prior direct peptide predictor datasets remains unresolved.
- Any public release of row-level artifacts requires founder/legal and claim-boundary review.

Do not use wording that implies:

- redistribution permission
- licensing closure
- final attribution
- complete dataset comparability
- public release approval

## 10. Citation / Reference Action List

Existing keys that can support direct peptide predictor lineage after final cleanup:

- `brainpeps_2012`
- `b3pdb_2021`
- `b3pred_2021`
- `bbppred_2021`
- `bbppredict_2022`
- `augur_2024`
- `brainpeppass_2024`
- `deepb3p3_2023`
- `esm_bbb_pred_2025`
- `b3bpfn_2026`

Existing adjacent peptide / CPP context keys:

- `practicpp_2024`
- `perseucpp_2025`

Existing metric/software support keys:

- `saito_rehmsmeier_2015_prauc`
- `chicco_jurman_2020_mcc`
- `scikit_learn_2011`
- `pandas_2010`
- `matplotlib_2007`

Source-required references to verify before adding:

- BBB-PEP-prediction
- DeepB3P if not covered by existing `deepb3p3_2023`
- DeepB3Pred if distinct from existing keys
- LightBBB
- Deep-B3
- DeePred-BBB
- DeepBBBP
- TITAN-BBB
- Original dataset source/citation/license/label-source criteria

Important: do not add any of these references until exact metadata are verified. Do not invent DOI, URL, authors, venue, or publication status.

## 11. Recommended v0.3 Revision Plan

Recommended next manuscript revision sequence:

1. Create a manuscript v0.3 draft from v0.2.
2. Add a dedicated Related Work section distinguishing direct peptide predictors from adjacent compound-level predictors.
3. Revise title and abstract to emphasize reproducible peptide-focused baseline/evidence package.
4. Add explicit no-SOTA and no-direct-comparison boundaries.
5. Preserve all metrics exactly.
6. Preserve all dataset/source/legal TODOs.
7. Add source-required TODOs for missing landscape references.
8. Update limitations to include no matched comparison against direct peptide predictors.
9. Update data availability to note unresolved comparability with prior predictor datasets.
10. Run a claim-boundary and citation audit on v0.3 before broader review.

Recommended next task:

**Task 130 - Draft Manuscript v0.3 with BBB Landscape Positioning**

Scope should be limited to a new manuscript draft file unless the user explicitly asks to edit existing files.

## 12. Public-Readiness Status

Manuscript v0.2 is suitable for internal review but should be revised to v0.3 before broader review.

Permea should not claim SOTA.

Direct comparators are BBB-penetrating peptide predictors.

TITAN-BBB and DeePred-BBB are adjacent compound-level BBB predictors.

Dataset redistribution remains unresolved.

Public bioRxiv remains **Hold / not submission-ready**.

## No-Change Confirmation

This task did not modify:

- manuscript v0.2
- review snapshot
- `references.bib`
- data artifacts
- result artifacts
- figure artifacts
- model outputs
- split artifacts
- leakage audit artifacts

No references were added or removed. No models, leakage audits, or split generation were rerun. No public-readiness, SOTA, redistribution, leakage-free, robust-generalization, biological-validation, wet-lab-validation, in-vivo-validation, therapeutic, clinical, external-review, or peer-review claim was introduced.
