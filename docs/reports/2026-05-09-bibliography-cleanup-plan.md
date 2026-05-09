# Bibliography Cleanup Plan - 2026-05-09

## 1. Purpose and Scope

This report plans a later `references.bib` cleanup pass for the Permea first-paper internal draft package. It identifies exact reference keys, cleanup categories, risk levels, `deepb3p3_2023` handling options, and safe next edits.

Reviewed materials:

- `references.bib`
- `docs/paper/permea-first-paper-manuscript-v0-6.md`
- `docs/supplement/permea-first-paper-supplement-v0-2.md`
- `docs/reports/2026-05-09-bibliography-and-export-readiness-audit.md`
- `docs/reports/2026-05-08-manuscript-v0-6-source-to-claim-audit.md`
- `docs/reports/2026-05-08-supplement-v0-2-audit.md`
- `docs/reports/2026-05-07-verified-comparator-bibtex-candidate-pack.md`
- `docs/reports/2026-05-07-updated-references-bib-post-audit.md`
- `docs/reports/2026-05-07-deepb3p3-identity-review.md`
- `docs/reports/2026-05-07-comparator-reference-and-source-metadata-plan.md`
- `docs/submission/2026-05-07-biorxiv-readiness-blocker-checklist.md`

This planning task does not modify `references.bib`, manuscript v0.6, supplement v0.2, README, data, result, figure, model, split, prediction, ranking, or leakage-audit artifacts. It does not use web search and does not approve public bioRxiv submission.

## 2. Current Bibliography Status

`references.bib` is key-complete for manuscript v0.6. No missing manuscript citation keys were found.

The bibliography is not ready for internal Word draft today because metadata cleanup, `deepb3p3_2023` resolution/documentation, and citation rendering checks remain pending.

The bibliography is not public bioRxiv-ready. Public use still requires source verification, final metadata cleanup, final source-to-claim review, citation formatting/export check, dataset/source decisions, and founder/manual approval.

## 3. Citation Keys Used by Manuscript v0.6

Manuscript v0.6 uses 25 citation keys:

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

The corresponding-author email address contains `@permea.us`; this is not a citation key.

## 4. Citation Keys Used by Supplement v0.2

No bracketed citation keys were found in supplement v0.2.

Current implication:

- supplement v0.2 has no missing-key issue
- any future supplement/export citation additions should be checked against `references.bib`
- supplement v0.2 currently relies on manuscript v0.6 for formal bibliography integration

## 5. references.bib Inventory Summary

`references.bib` contains 26 entries:

- direct BBB peptide database / predictor / related context: `brainpeps_2012`, `b3pdb_2021`, `b3pred_2021`, `bbppred_2021`, `bbppredict_2022`, `augur_2024`, `brainpeppass_2024`, `deepb3p3_2023`, `esm_bbb_pred_2025`, `b3bpfn_2026`, `naseem2023bbbpep`, `tang2025deepb3p`, `arif2025deepb3pred`
- adjacent compound BBB predictor context: `shaker2021lightbbb`, `tang2022deepb3`, `kumar2022deepredbbb`, `parakkal2022deepbbbp`, `oliveira2026titanbbb`
- broader peptide-prediction context: `practicpp_2024`, `perseucpp_2025`
- metric interpretation: `saito_rehmsmeier_2015_prauc`, `chicco_jurman_2020_mcc`
- software/tooling: `scikit_learn_2011`, `pandas_2010`, `matplotlib_2007`
- BBB shuttle background: `bbb_shuttle_review_2016`

Current inventory risk:

- one unused/confusing entry remains: `deepb3p3_2023`
- several older entries use abbreviated author fields with `and others`
- several entries lack volume, issue, page, or article-number fields
- recent/future-dated entries require status verification before public use

## 6. Missing Citation Key Check

No missing citation keys were found for manuscript v0.6.

No citation keys were found in supplement v0.2, so no supplement missing-key issue was found.

## 7. Unused Entry Inventory

Unused by manuscript v0.6:

- `deepb3p3_2023`

All other `references.bib` entries are used by manuscript v0.6.

Future supplement/export may need formal citations for comparator context if supplement text is converted from narrative placeholders into citation-bearing sections. No future supplement citation should be added without a new key-level audit.

## 8. `deepb3p3_2023` Resolution Options

Current entry:

- key: `deepb3p3_2023`
- authors: Ma and Wolfinger
- title: prediction model for BBB-penetrating peptides based on masked peptide transformers with dynamic routing
- journal: Briefings in Bioinformatics
- year: 2023
- DOI: `10.1093/bib/bbad399`

Prior identity review concluded that `deepb3p3_2023` appears distinct from both `tang2025deepb3p` and `arif2025deepb3pred` based on current repo evidence. It should not be used as the DeepB3P citation and should not be used as the DeepB3Pred citation.

Resolution options:

1. Keep unused with note
   - safest immediate option
   - preserves the entry while avoiding unsupported citation use
   - should be documented in the cleanup report or future bibliography notes

2. Move to future-use section if format supports it
   - acceptable only if the project adopts an explicit unused/future-use section convention in `references.bib`
   - must not affect citation rendering or create nonstandard BibTeX problems

3. Remove later only after manual approval
   - do not remove automatically
   - requires confirmation that the key is unused by all manuscript/supplement/export paths and that manual bibliography scope approval is documented

4. Verify identity and role later
   - required before citing it as an additional direct BBB-penetrating peptide predictor
   - must include source verification for full metadata, model name, and safe sentence-level claim role

Recommended current handling:

- keep `deepb3p3_2023` unchanged and unused in the next `references.bib` edit
- add no manuscript citation to it until source identity and role are manually verified
- do not rename or remove it in the next edit task

`deepb3p3_2023` cannot be resolved automatically from current repo evidence.

## 9. Metadata Cleanup Categories

### Author fields

Replace or approve abbreviated `and others` author fields only after source verification or an approved bibliography style decision.

Current abbreviated-author keys:

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

### Title protection

Protect acronyms, model names, database names, and software names where needed. Do not change title wording without source verification.

Priority title-protection targets:

- BBB / blood-brain barrier abbreviations
- B3Pdb, B3Pred, BBPpred, BBPpredict
- BBB-PEP-prediction
- BrainPepPass
- DeepB3P, DeepB3Pred, ESM-BBB-Pred, B3BPFN
- PractiCPP, PerseuCPP
- ROC, PR-AUC, MCC, F1
- Python, LightGBM, BiGRU, GAN
- TITAN-BBB

### DOI

Every current entry has a DOI. Later DOI work should verify existing DOI values rather than invent or change values.

### URL

No URL enrichment should be performed without source verification or a style decision. Add URLs only where DOI is absent, where preprint/source policy requires it, or where dataset/source attribution requires a URL.

### Venue / journal / conference / preprint server

Verify exact venue names and whether entries should use `journal`, `booktitle`, or preprint metadata. Do not change venue fields without source verification.

### Year / status

Recent or future-dated entries require status verification before public use:

- `tang2025deepb3p`
- `arif2025deepb3pred`
- `esm_bbb_pred_2025`
- `perseucpp_2025`
- `b3bpfn_2026`
- `oliveira2026titanbbb`

### Pages / article numbers

Entries missing volume, issue, pages, or article-number fields should be enriched only from verified sources. Do not infer article numbers from DOI strings.

### Access / publication status

Confirm whether preprint entries require `note = {Preprint}` or server-specific metadata. Current `oliveira2026titanbbb` already carries `note = {Preprint}` and should not be changed without source verification.

## 10. High-Priority Keys for Cleanup

High priority means the entry is used in manuscript v0.6 and affects direct comparator, source lineage, or confusing identity risk.

High-priority keys:

- `deepb3p3_2023`: unused/confusing; identity and role need manual/source verification before any citation, removal, or rename
- `b3pdb_2021`: dataset/source-lineage sensitivity; full metadata and source/attribution boundary need verification
- `b3pred_2021`: dataset/source-lineage sensitivity; verified candidate pack contains richer metadata; do not imply redistribution rights
- `brainpeps_2012`: database lineage; abbreviated authors and missing volume/pages likely need verification
- `bbppred_2021`: direct peptide predictor context; abbreviated authors and possible volume/pages cleanup
- `bbppredict_2022`: direct peptide predictor context; verified candidate pack contains richer metadata
- `augur_2024`: direct peptide predictor context; verified candidate pack contains richer metadata
- `naseem2023bbbpep`: direct BBB-PEP-prediction comparator; retain exact role and metadata
- `tang2025deepb3p`: verified DeepB3P comparator; keep distinct from `deepb3p3_2023`
- `arif2025deepb3pred`: verified DeepB3Pred comparator; keep distinct from `deepb3p3_2023`

## 11. Medium-Priority Keys for Cleanup

Medium priority means used by manuscript v0.6 and important for related-work, adjacent context, metrics, or software, but less likely to drive dataset/source confusion.

Medium-priority keys:

- `brainpeppass_2024`
- `esm_bbb_pred_2025`
- `b3bpfn_2026`
- `practicpp_2024`
- `perseucpp_2025`
- `shaker2021lightbbb`
- `tang2022deepb3`
- `kumar2022deepredbbb`
- `parakkal2022deepbbbp`
- `oliveira2026titanbbb`
- `saito_rehmsmeier_2015_prauc`
- `chicco_jurman_2020_mcc`
- `scikit_learn_2011`
- `pandas_2010`
- `matplotlib_2007`
- `bbb_shuttle_review_2016`

## 12. Low-Priority Keys for Cleanup

No current `references.bib` entry is low priority for the first cleanup pass because every entry is either used by manuscript v0.6 or is the known unused/confusing `deepb3p3_2023`.

If a later export path does not include adjacent or broader context, some adjacent-context entries may become lower priority for that specific export, but they remain relevant to the current manuscript v0.6 citation surface.

## 13. Entries Requiring Manual / Source Verification

Manual/source verification is required before metadata enrichment for:

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
- `perseucpp_2025`
- `practicpp_2024`
- `tang2025deepb3p`
- `arif2025deepb3pred`
- `oliveira2026titanbbb`

Dataset/source verification is separately required for any claim about:

- exact upstream dataset files/version
- B3Pred/B3Pdb source terms and license
- required attribution wording
- original label-source criteria
- processed row-level dataset redistribution
- row-level derived artifact release

## 14. Entries That Should Not Be Changed Without Web / Source Lookup

Do not change the following without web/source lookup or manually supplied verified source metadata:

- `deepb3p3_2023`: identity, title, full authors, volume/issue/pages/article number, and role
- `b3pdb_2021`: source-lineage-sensitive metadata
- `b3pred_2021`: source-lineage-sensitive metadata and richer candidate metadata
- `bbppredict_2022`: richer candidate metadata exists in prior report but should still be applied deliberately
- `augur_2024`: richer candidate metadata exists in prior report but should still be applied deliberately
- all 2025/2026 entries: publication status, year, venue, pages, article numbers, and preprint status
- all entries with `and others`: full author lists
- any dataset/source/download/license/terms citation that is not already represented as a verified bibliography entry

Do not invent DOI, URL, author list, venue, page, article number, publication status, or year values.

## 15. Proposed Safe Next `references.bib` Edit Task

Recommended next edit task:

**Draft conservative `references.bib` metadata cleanup patch without removing or renaming keys.**

Allowed scope for that later task:

- update only fields supported by already verified metadata in prior reports or manually supplied source metadata
- normalize existing keys without adding duplicate entries
- keep all current keys stable
- keep `deepb3p3_2023` unchanged unless manual source verification and approval are provided
- preserve manuscript v0.6 citation keys
- run a key-level citation audit after edits
- run a lightweight BibTeX syntax/brace-balance check after edits
- do not modify manuscript/supplement text unless a separate task explicitly allows it

Suggested first patch candidates if using only repo-verified candidate-pack metadata:

- enrich `b3pred_2021` from the verified B3Pred candidate metadata
- enrich `bbppredict_2022` from the verified BBPpredict candidate metadata
- enrich `augur_2024` from the verified Augur candidate metadata

Do not change `deepb3p3_2023` in that first patch.

## 16. Public-Readiness Warning

Public bioRxiv remains **Hold / not submission-ready**.

Bibliography cleanup alone will not make the paper public-ready. Public submission still requires dataset/source/legal decisions, data/code availability approval, final source-to-claim review, supplement/export readiness, artifact release decisions, and founder/manual approval.

Do not use bibliography cleanup to imply:

- dataset redistribution permission
- row-level artifact release permission
- wet-lab validation
- biological validation
- therapeutic efficacy
- clinical efficacy
- state-of-the-art performance
- AlphaFold-level performance, adoption, maturity, or validation

## 17. Remaining Blockers

Remaining blockers:

- `references.bib` metadata cleanup incomplete
- `deepb3p3_2023` identity/role unresolved
- final citation formatting/export check incomplete
- final sentence-level source-to-claim review incomplete
- exact upstream dataset files/version unresolved
- B3Pred/B3Pdb source terms/license unresolved
- required attribution wording unresolved
- original label-source criteria unresolved
- dataset redistribution unresolved
- row-level artifacts blocked from public release
- supplement/export package incomplete
- founder/manual approval pending
- final public posting decision pending

## Required Conclusions

`references.bib` is not safe for internal Word draft today. It is key-complete for manuscript v0.6, but metadata cleanup, `deepb3p3_2023` handling, and citation rendering checks remain pending.

`references.bib` is not public bioRxiv-ready.

`deepb3p3_2023` cannot be resolved automatically from current repo evidence.

Web/source verification or manually supplied verified metadata is needed before metadata enrichment beyond already documented candidate-pack fields.

Public bioRxiv remains **Hold / not submission-ready**.
