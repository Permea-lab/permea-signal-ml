# Citation Rendering and Export-Readiness Check - 2026-05-09

## 1. Purpose and Scope

This report documents a local, non-destructive citation rendering and export-readiness check for `references.bib` and manuscript v0.6.

Reviewed materials:

- `references.bib`
- `docs/paper/permea-first-paper-manuscript-v0-6.md`
- `docs/supplement/permea-first-paper-supplement-v0-2.md`
- `docs/reports/2026-05-09-bibliography-and-export-readiness-audit.md`
- `docs/reports/2026-05-09-bibliography-cleanup-plan.md`
- `docs/reports/2026-05-09-references-bib-conservative-cleanup-report.md`
- `docs/reports/2026-05-08-manuscript-v0-6-source-to-claim-audit.md`
- `docs/reports/2026-05-08-supplement-v0-2-audit.md`

This task did not modify manuscript v0.6, supplement v0.2, `references.bib`, README, data, result, figure, model, split, prediction, ranking, or leakage-audit artifacts. It did not generate a public submission PDF, final manuscript export, DOCX, or public release artifact. It did not stage, commit, or push.

## 2. Current Bibliography State

`references.bib` currently contains 26 BibTeX entries.

Task 105 conservatively enriched only:

- `b3pred_2021`
- `bbppredict_2022`
- `augur_2024`

No citation keys were renamed. No entries were removed. No new entries were added. `deepb3p3_2023` remains unchanged and unused.

## 3. Manuscript v0.6 Citation Key Check

Bracketed citation keys found in manuscript v0.6:

- `arif2025deepb3pred`
- `augur_2024`
- `b3bpfn_2026`
- `b3pdb_2021`
- `b3pred_2021`
- `bbb_shuttle_review_2016`
- `bbppred_2021`
- `bbppredict_2022`
- `brainpeppass_2024`
- `brainpeps_2012`
- `chicco_jurman_2020_mcc`
- `esm_bbb_pred_2025`
- `kumar2022deepredbbb`
- `matplotlib_2007`
- `naseem2023bbbpep`
- `oliveira2026titanbbb`
- `pandas_2010`
- `parakkal2022deepbbbp`
- `perseucpp_2025`
- `practicpp_2024`
- `saito_rehmsmeier_2015_prauc`
- `scikit_learn_2011`
- `shaker2021lightbbb`
- `tang2022deepb3`
- `tang2025deepb3p`

Result:

- actual bracketed manuscript citation keys: 25
- missing manuscript citation keys: none

A broad raw `@...` scan also detects `permea` from the corresponding-author email address `a.kim@permea.us`. This is not a citation key and should be ignored in citation-key checks.

## 4. Supplement v0.2 Citation Key Check

No bracketed citation keys were found in supplement v0.2.

Result:

- supplement citation keys: none
- missing supplement citation keys: none

## 5. references.bib Duplicate / Syntax Check

Local validation result:

- `BIB_ENTRY_COUNT 26`
- `BIB_DUPLICATE_KEYS NONE`
- `BIB_BRACE_BALANCE 0`

Unused bibliography entries relative to manuscript v0.6 and supplement v0.2 bracketed citations:

- `deepb3p3_2023`

This is expected based on Task 103, Task 104, and Task 105. It remains unchanged and unused pending manual/source verification.

This check is a lightweight structural check, not a full bibliography compiler/export validation.

## 6. Tool Availability Check

Local tool availability:

- `pandoc`: available, version `3.9.0.2`
- `bibtex`: not available in this shell
- `biber`: not available in this shell

Implication:

- Pandoc-based internal conversion may be possible in a later export task.
- BibTeX/Biber-based rendering cannot be validated locally in the current shell without installing or enabling those tools.
- No export was generated in this task.

## 7. Citation Rendering Risk Assessment

Risk level for internal citation rendering: low-to-moderate.

Low-risk findings:

- all actual manuscript v0.6 citation keys resolve to `references.bib`
- supplement v0.2 has no citation keys
- no duplicate BibTeX keys were detected
- brace balance is zero
- key stability was preserved during Task 105 cleanup
- Pandoc is available

Remaining rendering risks:

- BibTeX and Biber are unavailable, so those paths were not checked
- no actual citation-rendering export was generated in this task
- remaining abbreviated author fields may render less polished than desired
- `deepb3p3_2023` remains unused/confusing and should be documented or resolved before public export
- final style-specific formatting may reveal title-case, author-list, or venue formatting issues

## 8. Internal Word Draft Readiness Assessment

`references.bib` is ready enough for a controlled internal Word draft generation attempt, provided the draft is clearly marked internal-only and the export task does not claim public readiness.

Rationale:

- manuscript v0.6 citation keys resolve
- no supplement citation keys are missing
- duplicate-key and brace-balance checks pass
- Pandoc is available
- Task 105 improved three high-priority comparator entries with verified metadata

Internal Word draft generation should still include a post-export citation rendering review for:

- unresolved or malformed rendered citations
- title capitalization
- author-list rendering
- bibliography ordering/style
- unused `deepb3p3_2023` behavior
- any missing citation processor configuration

## 9. Public bioRxiv Readiness Assessment

`references.bib` is not public bioRxiv-ready.

Public bioRxiv remains **Hold / not submission-ready**.

Bibliography checks alone do not close public submission blockers. Public readiness still requires source verification, final metadata cleanup, final citation formatting/export check, final source-to-claim review, data/code availability approval, supplement/export completion, artifact release decisions, and founder/manual approval.

## 10. Remaining Bibliography Metadata Blockers

Remaining bibliography blockers:

- `deepb3p3_2023` identity and citation role unresolved
- `deepb3p3_2023` remains unused and should not be cited automatically
- abbreviated author fields remain in several entries
- DOI/URL fields still need final source verification before public export
- venue/status/year fields still need verification
- pages/article numbers still need verification for entries not enriched from verified metadata
- recent/future-dated 2025/2026 entries need publication-status verification
- style-specific citation rendering has not been visually reviewed

## 11. Remaining Export Blockers

Remaining export blockers:

- no DOCX or final manuscript export has been generated or checked
- supplement/export figure and table numbering remain incomplete
- final captions remain incomplete
- export manifest remains incomplete
- row-level artifact blocklist and aggregate allowlist require final review
- BibTeX/Biber export paths are unavailable in the current shell
- final source-to-claim review after formatting remains pending
- founder/manual approval remains pending

Dataset redistribution remains unresolved.

Row-level artifacts remain blocked from public release.

## 12. Recommended Next Task

Recommended next task: generate an internal-only Word draft package in a controlled export task using Pandoc, if that task explicitly permits DOCX creation, then perform a post-export citation and layout review. Keep the output internal-only and preserve public bioRxiv **Hold / not submission-ready** status.

## Required Conclusions

`references.bib` is ready enough for internal Word draft generation attempt.

`references.bib` is not public bioRxiv-ready.

Manuscript v0.6 can proceed to internal Word draft generation in a later task that explicitly permits creating a DOCX or other internal export artifact.

Public bioRxiv remains **Hold / not submission-ready**.

Dataset redistribution remains unresolved.

Row-level artifacts remain blocked from public release.
