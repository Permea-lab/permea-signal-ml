# Permea Reference Audit - 2026-05-05

## Purpose

This report summarizes the current reference and citation status for the Permea bioRxiv v0.1 manuscript candidate.

This is a documentation-only audit. It does not modify `references.bib`, add references, remove references, finalize bibliography metadata, or approve public posting.

## Materials Reviewed

- `references.bib`
- `docs/CITATION_CONSISTENCY_CHECK_V0_1.md`
- `docs/FINAL_POST_SENSITIVITY_CLAIM_AND_CITATION_AUDIT_V0_1.md`
- `docs/FINAL_REFERENCES_HUMAN_CLEANUP_CHECKLIST_V0_1.md`
- `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`

## Current Citation-Key Status

- Unique manuscript/supplement citation keys checked by the final post-sensitivity audit: 18.
- Missing keys: none reported.
- Deferred placeholder keys used: none reported.
- New post-sensitivity citation keys without `references.bib` entries: none reported.
- Verdict from existing audit: pass for key-level consistency.

## Current Bibliography Status

`references.bib` remains a draft bibliography. Human cleanup is still required before public posting.

High-priority cleanup items:

- Replace or explicitly approve `and others` author fields where required.
- Verify full author lists.
- Verify title casing, punctuation, accents, and exact typography.
- Verify journal or venue names.
- Verify DOI, URL, volume, issue, page, and article-number fields.
- Confirm publication status for newer entries.
- Confirm software citation policy for scikit-learn, pandas, and matplotlib.
- Confirm dataset/source citations align with the dataset attribution and legal decision.

## Entries Requiring Human Attention

Entries with `and others` noted in the cleanup checklist:

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

Entry without DOI in current draft:

- `scikit_learn_2011`

Entries with likely volume/issue/page/article-number cleanup needs:

- Most article entries, per `docs/FINAL_REFERENCES_HUMAN_CLEANUP_CHECKLIST_V0_1.md`.
- `pandas_2010` has a DOI but no page range in the draft.

## Citation-to-Claim Risk Areas

Before public posting, a human or reviewer should confirm:

- BBB/database/predictor citations support background and lineage only.
- Adjacent CPP citations remain adjacent context, not BBB validation.
- Metric citations support metric interpretation only.
- Software citations support tooling only.
- Dataset/source citations do not imply Permea dataset provenance, licensing, or redistribution closure.
- No citation is used to imply biological validation, wet-lab validation, validated delivery, therapeutic efficacy, clinical efficacy, leakage-free status, or robust generalization.

## Reference Audit Verdict

**Pass for key-level continuity; Hold for public submission.**

References remain a submission blocker until human bibliography cleanup, source-to-claim review, and final bibliography approval are complete.

## Recommended Next Actions

1. Complete human cleanup of `references.bib`.
2. Resolve deferred-reference decisions without adding unverified metadata.
3. Complete sentence-level citation/source-claim review.
4. Re-run a final citation consistency check after cleanup.

## No-Change Confirmation

- `references.bib` was not modified.
- No references were added.
- No reference metadata was invented.
- Manuscript scientific content was not modified.
- Public preprint remains **Hold / not submission-ready**.
