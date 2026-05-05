# Permea Reference Cleanup and Citation Integration Plan - 2026-05-06

## Purpose

This report plans reference cleanup and sentence-level citation integration for the Permea first paper manuscript v0.1 before modifying `references.bib` or manuscript citations.

This is a documentation-only plan. It does not modify `references.bib`, revise the manuscript, add references, rerun models, rerun leakage audit, generate new splits, change metric values, approve dataset licensing, or approve public bioRxiv posting.

Public bioRxiv remains **Hold / not submission-ready**.

## Materials Reviewed

- `docs/paper/permea-first-paper-manuscript-v0-1.md`
- `docs/reports/2026-05-05-reference-audit.md`
- `references.bib`
- `README.md`
- `docs/reports/2026-05-05-manuscript-v0-1-audit.md`
- `docs/reports/2026-05-05-submission-readiness-audit.md`

## 1. Current Citation Readiness Status

Current status: **key-level pass; public citation integration not ready**.

Known status from prior audit:

- 18 unique manuscript/supplement citation keys were checked.
- All checked keys are present in `references.bib`.
- No missing keys were reported.
- No deferred placeholder keys were reported.
- `references.bib` remains a draft bibliography.

Current manuscript v0.1 status:

- The manuscript mostly lists citation keys in a reference note rather than integrating citations sentence by sentence.
- Public submission still requires human bibliography cleanup and source-to-claim review.
- No public bioRxiv readiness is implied by the current citation state.

## 2. Manuscript Sections Needing Citations

| Manuscript section | Citation need | Existing candidate keys | Status |
| --- | --- | --- | --- |
| Abstract | Usually citation-light; no mandatory inline citations unless target venue requires them. | None required at this stage. | Acceptable for internal review. |
| Introduction - BBB delivery challenge | Background source for BBB delivery/shuttle framing. | `bbb_shuttle_review_2016` | Usable after metadata verification. |
| Introduction - BBB peptide databases and predictors | Database and predictor lineage. | `brainpeps_2012`, `b3pdb_2021`, `b3pred_2021`, `bbppred_2021`, `bbppredict_2022` | Usable after metadata verification. |
| Introduction - adjacent peptide-prediction context | CPP or adjacent peptide benchmark context only; must not imply BBB validation. | `practicpp_2024`, `perseucpp_2025` | Usable with careful claim boundary. |
| Methods - feature representation | Prior BBB/peptide predictor context for sequence-derived features. | `b3pred_2021`, `bbppred_2021`, `augur_2024`, `brainpeppass_2024`, `deepb3p3_2023`, `esm_bbb_pred_2025` | Usable after source-to-claim review. |
| Methods - scikit-learn evaluation | Software citation for model/evaluation tooling. | `scikit_learn_2011` | Needs bibliography cleanup; no DOI in current draft. |
| Methods - pandas/matplotlib tooling | Software citations for data handling and plots if mentioned in final manuscript. | `pandas_2010`, `matplotlib_2007` | Usable after metadata check. |
| Methods/Results - PR-AUC under imbalance | Metric interpretation under class imbalance. | `saito_rehmsmeier_2015_prauc` | Usable. |
| Methods/Results - MCC | MCC metric interpretation. | `chicco_jurman_2020_mcc` | Usable. |
| Results - repository-generated metrics and leakage-aware rerun | Internal result artifacts, not external references. | Source should be repository artifact paths, not bibliography entries. | Artifact traceability required, not BibTeX citation. |
| Leakage audit context | Internal audit artifacts. | Source should be repository docs/results. | Artifact traceability required, not BibTeX citation. |
| Data/code availability | Dataset license/source terms. | None confirmed. | Source required/manual legal decision. |

## 3. Existing Citation Keys That Appear Usable

These keys are present in `references.bib` and appear directionally usable after metadata verification:

- `bbb_shuttle_review_2016` - BBB shuttle/delivery background.
- `brainpeps_2012` - BBB peptide database context.
- `b3pdb_2021` - BBB-penetrating peptide archive context.
- `b3pred_2021` - sequence-based BBB peptide predictor context.
- `bbppred_2021` - sequence-based BBB peptide predictor context.
- `bbppredict_2022` - BBB peptide predictor/web-service context.
- `augur_2024` - recent BBB peptide prediction context.
- `brainpeppass_2024` - recent BBB peptide prediction context.
- `deepb3p3_2023` - modern BBB peptide prediction context.
- `esm_bbb_pred_2025` - protein-language-model-style BBB peptide prediction context; needs publication-status verification because it is future/recent relative to earlier package materials.
- `b3bpfn_2026` - tabular/foundation-model-style BBB peptide prediction context; needs publication-status verification.
- `practicpp_2024` - adjacent CPP benchmark/predictor context only.
- `perseucpp_2025` - adjacent CPP predictor context only; needs publication-status verification.
- `saito_rehmsmeier_2015_prauc` - PR-AUC interpretation under class imbalance.
- `chicco_jurman_2020_mcc` - MCC interpretation.
- `scikit_learn_2011` - scikit-learn tooling.
- `pandas_2010` - pandas tooling.
- `matplotlib_2007` - matplotlib tooling.

## 4. Missing Reference Candidates

No missing citation key was detected from the current manuscript key list. However, several citation needs are not safely covered by the current bibliography and should be treated as source-required before public submission:

| Need | Status | Notes |
| --- | --- | --- |
| Original dataset source/publication | Source required | Dataset source attribution remains unresolved; do not invent source metadata. |
| Dataset license or terms-of-use source | Source required | Manual legal/licensing review required. |
| Original label-source criteria | Source required | Current docs say label-source criteria are unresolved. |
| Public data availability route | Source required/manual decision | Depends on source terms and founder/legal approval. |
| Software release/archive citation for this repository | Source required later | Requires final repository URL, commit/tag, license, and archive policy. |
| bioRxiv category or final submission metadata | Manual decision | Not a bibliography issue but needed before public posting. |

Do not add bibliography entries for these until a source exists and metadata are verified.

## 5. Bibliography Quality Issues

Known quality issues from `references.bib` and the reference audit:

### Author Fields With `and others`

The following entries need full author-list verification or explicit approval of abbreviated author handling:

- `brainpeps_2012`
- `b3pdb_2021`
- `b3pred_2021`
- `bbppred_2021`
- `bbppredict_2022`
- `scikit_learn_2011`
- `practicpp_2024`
- `augur_2024`
- `brainpeppass_2024`
- `esm_bbb_pred_2025`
- `b3bpfn_2026`
- `perseucpp_2025`

### Missing or Incomplete Bibliography Fields

- `scikit_learn_2011` has no DOI in the current draft.
- `pandas_2010` has a DOI but no page range in the current draft.
- Most article entries need human verification of volume, issue, pages or article numbers, title casing, journal names, DOI, and publication status.

### Recent/Future-Dated Entries Needing Publication-Status Verification

- `esm_bbb_pred_2025`
- `b3bpfn_2026`
- `perseucpp_2025`

These may be valid if already verified elsewhere, but the current plan should treat them as "needs verification" before public posting.

## 6. Sentence-Level Citation Integration Plan

Recommended integration targets for the manuscript v0.2 citation pass:

1. Introduction first paragraph:
   - Add `bbb_shuttle_review_2016` to BBB delivery/shuttle background.
   - Keep wording as background context only, not validation of Permea results.

2. Introduction sequence-first benchmark lineage:
   - Add `brainpeps_2012` and `b3pdb_2021` for database/archive context.
   - Add `b3pred_2021`, `bbppred_2021`, and `bbppredict_2022` for earlier sequence-based BBB peptide predictor work.

3. Introduction recent-method context:
   - Add `augur_2024`, `brainpeppass_2024`, `deepb3p3_2023`, `esm_bbb_pred_2025`, and `b3bpfn_2026` only after publication-status verification.
   - Present these as related predictor context, not evidence that Permea models are state-of-the-art or validated.

4. Adjacent CPP context:
   - Add `practicpp_2024` and `perseucpp_2025` only where discussing adjacent peptide-prediction or evaluation context.
   - Do not use CPP citations to support BBB validation claims.

5. Methods feature representation:
   - Cite prior BBB predictor papers only to show descriptor/predictor lineage.
   - Keep language clear that current features are a baseline surface, not mechanism.

6. Methods evaluation:
   - Add `scikit_learn_2011` where scikit-learn model/evaluation tooling is described.
   - Add `saito_rehmsmeier_2015_prauc` where PR-AUC under imbalance is discussed.
   - Add `chicco_jurman_2020_mcc` where MCC is introduced.

7. Methods/results tooling:
   - Add `pandas_2010` and `matplotlib_2007` only if final text explicitly mentions data handling or plotting libraries.

8. Results and leakage audit:
   - Use repository artifact references in text or supplement pointers, not external BibTeX citations.
   - Cite paths such as `results/tables/model_comparison_summary.csv`, `results/sensitivity/leakage_aware_metrics_summary.json`, and leakage audit docs/results.

9. Data/code availability:
   - Do not cite a dataset source until the original source and license are verified.
   - Mark the availability statement as unresolved until manual/legal review completes.

## 7. `references.bib` Cleanup Sequence

Recommended safe sequence:

1. Freeze manuscript citation scope for v0.2.
2. Extract all citation keys used by `docs/paper/permea-first-paper-manuscript-v0-1.md` after citation integration.
3. Verify each key exists in `references.bib`.
4. For each existing entry, verify:
   - full author list or approved abbreviated style
   - year
   - exact title
   - journal/venue
   - DOI
   - URL if needed
   - volume/issue/page/article number
   - publication status for 2025/2026 entries
5. Replace `and others` only with verified author lists.
6. Do not add source-dataset references until source identity and reuse terms are confirmed.
7. Re-run a key-level citation consistency check after edits.
8. Perform sentence-level source-to-claim review:
   - background citations support background only
   - adjacent CPP citations do not imply BBB validation
   - metric citations support metric interpretation only
   - software citations support tooling only
   - no citation implies leakage-free status, robust generalization, biological validation, wet-lab validation, therapeutic efficacy, clinical efficacy, or dataset licensing closure.

## 8. Risks and Manual Review Needs

### Citation Risks

- Citation keys are currently not integrated sentence by sentence in the new first-paper draft.
- Bibliography metadata are incomplete.
- Some entries are recent/future-dated and need publication-status verification.
- Dataset source and license citations remain unresolved.

### Claim Risks

- Predictor and database citations must not be used to imply that the current Permea evidence is biologically validated.
- Adjacent CPP citations must remain adjacent context only.
- Feature-related citations must not be used as mechanistic proof.
- Internal result artifacts should not be treated as external validation.

### Manual Review Needs

- Human bibliography cleanup.
- Dataset source/legal review.
- Final source-to-claim review.
- Founder/manual approval before public posting.

## 9. Recommended Next Task

Recommended next task:

**Task 114 - Clean `references.bib` Metadata for Existing Keys**

Scope should be limited to existing keys only. Do not add new dataset/source references until the dataset source and license are verified. Do not modify manuscript citations until the cleaned bibliography is reviewed, unless the task is explicitly scoped as a citation-integration pass.

## No-Change Confirmation

- `references.bib` was not modified.
- Manuscript files were not modified.
- Data files were not modified.
- Result artifacts were not modified.
- Figure artifacts were not modified.
- Models were not rerun.
- Leakage audit was not rerun.
- New split generation was not run.
- Public bioRxiv remains **Hold / not submission-ready**.
