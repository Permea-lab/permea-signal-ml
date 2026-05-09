# references.bib Conservative Cleanup Report - 2026-05-09

## 1. Purpose and Scope

This report documents a conservative `references.bib` metadata cleanup for the Permea first-paper internal draft package.

Scope:

- update only existing bibliography entries using already verified metadata from `docs/reports/2026-05-07-verified-comparator-bibtex-candidate-pack.md`
- preserve all citation keys exactly
- preserve all entries
- avoid invented DOI, URL, author, venue, page, article number, publication status, or year values
- leave `deepb3p3_2023` unchanged and unused

This task modified only `references.bib` and created this report. It did not modify manuscript v0.6, supplement v0.2, README, data, result, figure, model, split, prediction, ranking, or leakage-audit artifacts. It did not use web search, generate PDFs, export manuscript files, create DOCX files, stage, commit, or push.

## 2. references.bib Changes Made

Three existing entries were enriched from already verified candidate-pack metadata:

- `b3pred_2021`
- `bbppredict_2022`
- `augur_2024`

No citation key was renamed. No entry was removed. No new bibliography entry was added.

## 3. Citation Keys Preserved

All 26 `references.bib` citation keys were preserved:

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
- `deepb3p3_2023`
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

## 4. Entries Changed

### `b3pred_2021`

Changes:

- replaced abbreviated author field with verified full author list
- updated title to the verified candidate-pack title, including Blood--Brain hyphenation
- added `volume = {13}`
- added `number = {8}`
- added `pages = {1237}`

Reason:

- prior verified candidate pack recommended updating existing `b3pred_2021` metadata rather than adding a duplicate `kumar2021b3pred` key

### `bbppredict_2022`

Changes:

- replaced abbreviated author field with verified full author list
- added `volume = {13}`
- added `pages = {845747}`

Reason:

- prior verified candidate pack recommended updating existing `bbppredict_2022` metadata rather than adding a duplicate `chen2022bbppredict` key

### `augur_2024`

Changes:

- replaced abbreviated author field with verified full author list
- updated title casing and Blood--Brain hyphenation to match verified candidate-pack metadata
- added `volume = {22}`
- added `pages = {86}`

Reason:

- prior verified candidate pack recommended updating existing `augur_2024` metadata rather than adding a duplicate `gu2024augur` key

## 5. Entries Intentionally Left Unchanged

The following entries were intentionally left unchanged because they either require manual/source verification, were already added from verified metadata, or were outside the narrow safe cleanup scope:

- `brainpeps_2012`
- `b3pdb_2021`
- `bbppred_2021`
- `saito_rehmsmeier_2015_prauc`
- `chicco_jurman_2020_mcc`
- `scikit_learn_2011`
- `pandas_2010`
- `matplotlib_2007`
- `practicpp_2024`
- `bbb_shuttle_review_2016`
- `brainpeppass_2024`
- `deepb3p3_2023`
- `esm_bbb_pred_2025`
- `b3bpfn_2026`
- `perseucpp_2025`
- `naseem2023bbbpep`
- `tang2025deepb3p`
- `arif2025deepb3pred`
- `shaker2021lightbbb`
- `tang2022deepb3`
- `kumar2022deepredbbb`
- `parakkal2022deepbbbp`
- `oliveira2026titanbbb`

## 6. `deepb3p3_2023` Handling

`deepb3p3_2023` was left unchanged.

It remains unused by manuscript v0.6 and supplement v0.2.

It still requires manual/source verification before any citation, removal, rename, metadata enrichment, or public bibliography decision. Current repo evidence indicates it appears distinct from `tang2025deepb3p` and `arif2025deepb3pred`, but its exact manuscript role remains unresolved.

## 7. Metadata Still Requiring Manual / Source Verification

Author fields still requiring source verification or an approved abbreviated-author policy:

- `brainpeps_2012`
- `b3pdb_2021`
- `bbppred_2021`
- `scikit_learn_2011`
- `practicpp_2024`
- `brainpeppass_2024`
- `esm_bbb_pred_2025`
- `b3bpfn_2026`
- `perseucpp_2025`

DOI/URL:

- existing DOI fields still need final source verification before public export
- URL enrichment should not be performed without source verification or a style decision

Venue/status/year:

- recent and future-dated entries require publication-status verification before public use, especially 2025 and 2026 entries

Pages/article numbers:

- entries without volume, issue, pages, or article-number fields should not be enriched without verified metadata

Recent/future-dated entries requiring verification:

- `tang2025deepb3p`
- `arif2025deepb3pred`
- `esm_bbb_pred_2025`
- `perseucpp_2025`
- `b3bpfn_2026`
- `oliveira2026titanbbb`

Dataset/source metadata remains unresolved and is separate from bibliography metadata cleanup.

## 8. Duplicate Key Check Result

Validation command result:

- `ENTRY_COUNT 26`
- `DUPLICATE_KEYS NONE`

## 9. Brace / Syntax Check Result

Validation command result:

- `BRACE_BALANCE 0`

This is a lightweight syntax check, not a full BibTeX compiler/export check.

## 10. Internal Word Draft Readiness After Cleanup

`references.bib` is improved for internal Word draft preparation because three high-priority comparator entries now carry richer verified metadata while preserving stable keys.

It is still not fully internal Word draft-ready until remaining metadata verification, `deepb3p3_2023` handling/documentation, and citation rendering/export checks are complete.

## 11. Public bioRxiv Readiness

`references.bib` is not public bioRxiv-ready.

Public bioRxiv remains **Hold / not submission-ready**.

## 12. Remaining Blockers

Remaining blockers:

- `deepb3p3_2023` identity and role unresolved
- remaining abbreviated author fields
- final DOI/URL verification
- final venue/status/year verification
- final pages/article-number verification
- final citation formatting/export check
- final source-to-claim review
- dataset source/license/attribution/redistribution decision unresolved
- row-level artifacts blocked from public release
- supplement/export package incomplete
- founder/manual approval pending

Dataset redistribution remains unresolved.

Row-level artifacts remain blocked from public release.

## 13. Recommended Next Task

Recommended next task: run a citation rendering/export-readiness check for the current `references.bib` without generating public submission artifacts, then decide whether to verify remaining abbreviated-author and 2025/2026 entries with source lookup in a separate approved task.
