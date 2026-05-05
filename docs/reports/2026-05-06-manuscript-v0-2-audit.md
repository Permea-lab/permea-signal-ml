# Permea Manuscript v0.2 Citation and Availability Wording Audit - 2026-05-06

## Purpose

This report audits `docs/paper/permea-first-paper-manuscript-v0-2.md` for citation integration, data/code availability caution, claim discipline, and friendly/internal-review readiness.

This is an audit only. It does not modify manuscript v0.2, manuscript v0.1, `references.bib`, data artifacts, result artifacts, figure artifacts, model outputs, split artifacts, or leakage audit artifacts. It does not add or remove references, rerun models, rerun leakage audit, generate new splits, approve dataset redistribution, make legal conclusions, or approve public bioRxiv posting.

Public bioRxiv remains **Hold / not submission-ready**. Dataset redistribution remains unresolved.

## Materials Reviewed

- `docs/paper/permea-first-paper-manuscript-v0-2.md`
- `docs/paper/permea-first-paper-manuscript-v0-1.md`
- `docs/reports/2026-05-06-reference-cleanup-and-citation-plan.md`
- `docs/reports/2026-05-06-reference-cleanup-post-audit.md`
- `docs/submission/2026-05-06-dataset-attribution-and-availability-decision-package.md`
- `docs/submission/2026-05-05-data-and-code-availability-draft.md`
- `docs/reports/2026-05-05-manuscript-v0-1-audit.md`
- `references.bib`

## Executive Verdict

Manuscript v0.2 is suitable for friendly/internal review after acknowledging one low-risk formatting issue: the file currently begins with `v#` rather than a clean Markdown H1. The issue is visible and should be fixed in the next manuscript revision before commit or public export, but it does not alter scientific meaning, citation content, metric values, or claim boundaries.

No high-risk claim-boundary issue was found. Citation keys integrated in v0.2 are present in `references.bib`. Data/code availability wording is conservative and aligned with the dataset attribution and availability decision package.

Public bioRxiv remains **Hold / not submission-ready**.

## 1. Metadata Consistency

Status: **Pass for internal review.**

Confirmed metadata in v0.2:

- Author: Albert Heekwan Kim
- Affiliation: Permea Research
- Corresponding author email: a.kim@permea.us
- Funding: No funding
- Conflict of Interest: N/A
- Acknowledgements: N/A
- Ethics Statement: N/A

No invented author metadata, affiliation, funding, acknowledgement, ethics, or conflict-of-interest detail was detected.

## 2. Citation Key Existence

Status: **Pass for key-level existence.**

The following citation keys are used in v0.2 and are present in `references.bib`:

- `bbb_shuttle_review_2016`
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
- `practicpp_2024`
- `perseucpp_2025`
- `scikit_learn_2011`
- `pandas_2010`
- `matplotlib_2007`
- `saito_rehmsmeier_2015_prauc`
- `chicco_jurman_2020_mcc`

No missing BibTeX key was found among the intended citation placeholders. The corresponding-author email contains `@permea.us`; this is not a citation key.

## 3. Sentence-Level Citation Integration Quality

Status: **Pass for internal review; not final public citation-ready.**

v0.2 improves on v0.1 by integrating sentence-level citation placeholders for:

- BBB shuttle/background context
- BBB peptide resource and predictor lineage
- adjacent computational peptide-prediction context
- scikit-learn tooling
- pandas and matplotlib tooling
- PR-AUC interpretation
- MCC interpretation

The citation placements are conservative. Background and adjacent predictor citations are used for context, not to claim validation of the Permea model, dataset, or candidates.

Remaining public-submission blocker: source-to-claim review is still required after final reference metadata cleanup.

## 4. Dataset/Source TODO Visibility

Status: **Pass.**

v0.2 clearly marks unresolved dataset/source issues with explicit TODOs:

- `TODO(source-required): original dataset source/citation/license/label-source criteria.`
- `TODO(source/legal): finalize dataset source attribution, license, redistribution status, and data availability wording after manual legal/licensing review.`
- `TODO(source-required): verify original dataset source citation, source license, and label-source criteria before public submission.`
- `TODO(source-required): confirm dataset/source citations after dataset legal and provenance review.`

These TODOs are visible and specific. They should remain unresolved until founder/legal/source review provides verified source details.

## 5. Data/Code Availability Caution

Status: **Pass.**

v0.2 aligns with the dataset attribution and availability decision package:

- Code availability is separated from data availability.
- Code release is described as intended through a public Permea repository, subject to final release review, URL/tag/license confirmation, and founder/manual approval.
- Processed dataset redistribution is not declared available.
- Dataset availability is explicitly dependent on source terms, attribution, and manual licensing review.
- Selected aggregate derived artifacts are described as releasable only after founder/legal and claim-boundary review.
- The draft does not conclude that dataset redistribution is permitted.

Dataset availability status remains: **unresolved**.

## 6. Results Traceability

Status: **Pass.**

v0.2 preserves traceability to committed repository artifacts:

- random-stratified summaries under `results/tables/` and `results/metrics/`
- leakage-aware split manifest under `results/sensitivity/combined_group_stratified_split_manifest.csv`
- leakage-aware rerun outputs under `results/sensitivity/`

The manuscript treats these as internal result-artifact sources rather than external bibliography references, matching the citation-integration plan.

No metric changes were detected in the audit.

## 7. Leakage-Aware Wording Discipline

Status: **Pass.**

v0.2 uses bounded leakage-aware language:

- "leakage-aware group-stratified sensitivity rerun"
- "did not collapse the signal under the tested grouping strategy"
- "sensitivity setting"
- "not proof that all leakage or provenance concerns are fully controlled"
- "does not establish full leakage control or robust generalization"

No leakage-free claim was found.

## 8. Candidate-Prioritization Qualifier Discipline

Status: **Pass.**

v0.2 qualifies candidate-prioritization language with pre-experimental or before-experimental-validation framing:

- "candidate prioritization before experimental validation"
- "computational prioritization must remain distinct from experimentally demonstrated transport or efficacy"
- "candidate-prioritization framing before experimental validation"

This preserves the internal review claim boundary.

## 9. Biological / Wet-Lab / Clinical Overclaim Risk

Status: **Pass.**

v0.2 explicitly states:

- this is an in-silico computational study
- no wet-lab validation was performed
- no biological validation was performed
- no in-vivo validation was performed
- no therapeutic or clinical efficacy is claimed
- no external validation, wet-lab validation, biological validation, in-vivo validation, therapeutic evaluation, or clinical evaluation has been performed

No biological, wet-lab, in-vivo, therapeutic, or clinical validation claim was found.

## 10. References / Bibliography Remaining Blockers

Status: **Medium-risk blocker for public submission; acceptable for internal review.**

Remaining reference blockers:

- Full author lists require verification.
- `and others` entries require human approval or cleanup.
- DOI, URL, volume, issue, page, article-number, venue, and publication-status fields require human review.
- Software citation policy requires confirmation.
- Dataset/source citation remains unresolved pending source/legal review.
- Final source-to-claim review remains pending.

These issues do not block friendly/internal review, but they block public submission.

## 11. Supplement / Export Blockers

Status: **Medium-risk blocker for public submission; acceptable for internal review.**

v0.2 retains explicit supplement/export TODOs:

- finalize supplement section order and numbering
- finalize figure and table captions
- finalize file-path checks and export manifest
- rerun final claim-boundary and citation checks after formatting

These blockers must close before any public preprint package is declared ready.

## 12. Friendly / Internal Review Readiness

Status: **Pass with minor formatting caveat.**

v0.2 is suitable for friendly/internal review because it:

- preserves confirmed metadata
- integrates existing citation keys without adding references
- separates code availability from data availability
- keeps processed dataset redistribution unresolved
- preserves metric values
- preserves leakage-aware sensitivity boundaries
- preserves biological/wet-lab/clinical claim boundaries
- keeps public bioRxiv status on Hold

Low-risk caveat: fix the leading `v#` heading typo before committing or sharing as a polished draft.

## 13. Public Submission Readiness Status

Status: **Hold / not submission-ready.**

Public bioRxiv remains blocked by:

- dataset legal/licensing and redistribution decision
- final data/code availability wording
- original dataset/source citation
- `references.bib` metadata cleanup
- final citation/source-claim review
- supplement/export formatting
- founder/manual approval
- final public posting decision

## Risk Summary

### High-Risk Issues

None found.

### Medium-Risk Issues

1. Dataset/source attribution, license, redistribution status, and label-source criteria remain unresolved.
2. `references.bib` metadata and final source-to-claim review remain incomplete.
3. Supplement/export formatting remains incomplete.

### Low-Risk Issues

1. The manuscript v0.2 file starts with `v#` instead of a clean Markdown H1. This should be corrected in the next revision task.
2. Public-facing citation formatting remains placeholder-style and should be polished after bibliography cleanup.

## Required Conclusions

- Manuscript v0.2 is suitable for friendly/internal review with the low-risk heading typo noted.
- Public bioRxiv remains **Hold / not submission-ready**.
- Dataset redistribution remains unresolved.

## Recommended Next Task

Recommended next task:

**Task 121 - Fix Manuscript v0.2 Heading Typo and Commit Manuscript v0.2 Audit Package**

Scope should be limited to:

- correcting the leading `v#` typo in `docs/paper/permea-first-paper-manuscript-v0-2.md`
- staging v0.2 and this audit report
- committing the internal-review manuscript v0.2 package

Do not modify `references.bib`, data artifacts, result artifacts, figure artifacts, model outputs, split artifacts, or leakage audit artifacts.

## No-Change Confirmation

This audit did not modify:

- manuscript v0.2
- manuscript v0.1
- `references.bib`
- data artifacts
- result artifacts
- figure artifacts
- model outputs
- split artifacts
- leakage audit artifacts

No models, leakage audits, or split generation were rerun.
