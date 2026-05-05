# Permea Reference Cleanup Post-Audit - 2026-05-06

## Purpose

This report audits the conservative `references.bib` cleanup from Task 114 and prepares a sentence-level citation integration plan for a future manuscript v0.2 task.

This report does not modify `references.bib`, the manuscript draft, data, results, figures, models, leakage audit outputs, or split artifacts. It does not add or remove references and does not approve public bioRxiv posting.

Public bioRxiv remains **Hold / not submission-ready**.

## Materials Reviewed

- `references.bib`
- current `git diff -- references.bib`
- `docs/reports/2026-05-06-reference-cleanup-and-citation-plan.md`
- `docs/paper/permea-first-paper-manuscript-v0-1.md`
- `docs/reports/2026-05-05-reference-audit.md`
- `docs/reports/2026-05-05-manuscript-v0-1-audit.md`

## 1. `references.bib` Diff Audit Summary

Task 114 changed `references.bib` by adding BibTeX title-protection braces around existing terms that should not be downcased by bibliography styles.

The diff is limited to title fields. It does not:

- add references
- remove references
- rename citation keys
- add author names
- add DOI fields
- add URL fields
- add volume, issue, page, or article-number fields
- change years
- change journal or venue names
- change manuscript citations

Observed diff size:

- `references.bib`: 15 insertions and 15 deletions.

## 2. Whether Task 114 Changes Are Safe to Commit

Verdict: **safe to commit as a conservative cleanup**.

Rationale:

- Changes are limited to BibTeX capitalization/title-protection.
- No unverified metadata was introduced.
- Existing citation keys were preserved.
- Existing bibliography scope was preserved.
- No manuscript claims or citation placements were changed.

This does not make the bibliography public-ready. It only improves formatting safety for existing entries.

## 3. Citation Keys Touched by Task 114

Task 114 touched title fields for:

- `brainpeps_2012`
- `b3pdb_2021`
- `b3pred_2021`
- `bbppred_2021`
- `bbppredict_2022`
- `saito_rehmsmeier_2015_prauc`
- `chicco_jurman_2020_mcc`
- `scikit_learn_2011`
- `pandas_2010`
- `practicpp_2024`
- `augur_2024`
- `brainpeppass_2024`
- `esm_bbb_pred_2025`
- `b3bpfn_2026`
- `perseucpp_2025`

Keys not changed by Task 114:

- `matplotlib_2007`
- `bbb_shuttle_review_2016`
- `deepb3p3_2023`

## 4. Remaining Unresolved Bibliography Issues

The following issues remain unresolved and require human/source verification:

- `and others` remains in multiple author fields.
- Full author lists are not verified.
- `scikit_learn_2011` still lacks DOI in the current bibliography.
- `pandas_2010` still lacks a page range.
- Most article entries still need volume, issue, pages or article-number verification.
- Recent/future-dated entries still need publication-status verification:
  - `esm_bbb_pred_2025`
  - `b3bpfn_2026`
  - `perseucpp_2025`
- Dataset source, dataset license, source terms, and original label-source criteria still lack verified citation/source metadata.
- Repository release/archive citation remains pending final repository release policy.

No values should be filled without a verified source.

## 5. Manuscript Sections Needing Citation Integration

The manuscript currently has a `References Placeholder and Citation-Key Notes` section and does not yet place all citations sentence by sentence.

Sections needing citation integration:

| Manuscript section | Citation integration need |
| --- | --- |
| Introduction | BBB delivery background; BBB peptide database/predictor lineage; adjacent peptide-prediction context. |
| Materials and Methods - Feature Representation | Prior predictor context for sequence-derived features, without implying mechanism. |
| Materials and Methods - Random-Stratified Baseline Evaluation | scikit-learn tooling, PR-AUC under imbalance, MCC metric interpretation. |
| Materials and Methods - Leakage-Aware Sensitivity Analysis | Repository artifact paths rather than external bibliography citations. |
| Results | Artifact traceability for baseline and leakage-aware metrics. |
| Leakage Audit Context | Repository audit paths rather than external bibliography citations. |
| Data and Code Availability | No dataset source citation until source/legal review is complete. |

## 6. Sentence-Level Citation Integration Plan

Recommended future v0.2 insertion targets:

1. Introduction, BBB background:
   - Add `bbb_shuttle_review_2016`.
   - Use it only for BBB delivery/shuttle background.

2. Introduction, database/archive context:
   - Add `brainpeps_2012` and `b3pdb_2021`.
   - Use them to support BBB peptide database/archive lineage only.

3. Introduction, earlier predictor context:
   - Add `b3pred_2021`, `bbppred_2021`, and `bbppredict_2022`.
   - Use them for prior sequence-based BBB peptide predictor context, not validation of Permea results.

4. Introduction or Related Work paragraph, recent predictor context:
   - Add `augur_2024`, `brainpeppass_2024`, `deepb3p3_2023`, `esm_bbb_pred_2025`, and `b3bpfn_2026` only after publication-status verification.
   - Keep these as related-work context.

5. Adjacent peptide-prediction context:
   - Add `practicpp_2024` and `perseucpp_2025`.
   - Use only for adjacent CPP/peptide-prediction context; do not imply BBB validation.

6. Methods, evaluation tooling:
   - Add `scikit_learn_2011` for scikit-learn model/evaluation tooling.
   - Add `pandas_2010` and `matplotlib_2007` only if pandas or matplotlib are explicitly mentioned in final text.

7. Methods, metric interpretation:
   - Add `saito_rehmsmeier_2015_prauc` when discussing PR-AUC under class imbalance.
   - Add `chicco_jurman_2020_mcc` when discussing MCC.

8. Results and sensitivity:
   - Use repository artifact references rather than bibliography entries:
     - `results/tables/model_comparison_summary.csv`
     - `results/sensitivity/leakage_aware_model_comparison_summary.csv`
     - `results/sensitivity/leakage_aware_metrics_summary.json`
     - `results/sensitivity/combined_group_stratified_split_manifest.csv`

9. Leakage audit context:
   - Use repository audit docs/results rather than bibliography entries.
   - Keep language bounded: optimism risk, sensitivity estimate, no leakage-free claim.

10. Data/code availability:
   - Do not add a dataset source citation until source identity and license terms are verified.

## 7. Dataset/Source Citation Gaps

Dataset/source citation gaps remain unresolved:

- original dataset source/publication: source required
- dataset license or terms-of-use source: source required
- source attribution for imported legacy processed dataset: source required
- original label-source criteria: source required
- public data availability route: manual/legal decision required
- repository release/archive citation: pending release/tag/license policy

These gaps remain blockers for public submission and should not be filled with guessed metadata.

## 8. Recommended Next Task

Recommended next task:

**Task 116 - Commit Reference Cleanup and Citation Planning Reports**

Suggested commit scope:

- `references.bib`
- `docs/reports/2026-05-06-reference-cleanup-and-citation-plan.md`
- `docs/reports/2026-05-06-reference-cleanup-post-audit.md`

After that, a separate task can integrate sentence-level citations into manuscript v0.2, still without changing metric values or claim boundaries.

## 9. Public Submission Status Reminder

Public bioRxiv remains **Hold / not submission-ready**.

Reasons include:

- manuscript citation integration pending
- bibliography metadata cleanup still incomplete
- dataset/source/legal citation gaps unresolved
- supplement/export formatting pending
- founder/manual approval pending
- final public posting decision pending

The current reference cleanup is safe as a conservative internal step, but it does not make the bibliography final and does not approve public posting.

## No-Change Confirmation

- `references.bib` was read but not modified by this post-audit task.
- Manuscript draft was not modified.
- No references were added.
- No references were removed.
- Data files were not modified.
- Result artifacts were not modified.
- Figure artifacts were not modified.
- Models were not rerun.
- Leakage audit was not rerun.
- New split generation was not run.
