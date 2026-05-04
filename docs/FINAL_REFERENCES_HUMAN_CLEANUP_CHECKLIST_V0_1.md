# Final References Human Cleanup Checklist v0.1

## Purpose

This checklist supports human cleanup and approval of the draft `references.bib` file before any bioRxiv v0.1 public posting decision.

This checklist does not finalize references, does not modify `references.bib`, does not add new references, and does not make the public preprint ready. Public preprint status remains **Hold / not submission-ready** until reference cleanup, metadata/disclosure, dataset/legal, supplement/export, leakage-disclosure, and human approval blockers are closed.

## Current Bibliography Status

- `references.bib` exists.
- `references.bib` is a draft bibliography built from verified reference packs only.
- `docs/REFERENCE_BIBLIOGRAPHY_BUILD_LOG_V0_1.md` documents included and deferred entries.
- `docs/CITATION_CONSISTENCY_CHECK_V0_1.md` reports citation-key consistency as passing.
- Human cleanup remains required for author lists, formatting, optional fields, and sentence-level source support.
- Final bibliography approval has not been completed.

## Reference Inventory

| Citation key | Entry type | Title | Author field status | Year | Venue/journal status | DOI/URL status | Metadata completeness | Human cleanup needed? | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `brainpeps_2012` | article | Brainpeps: the blood-brain barrier peptide database | Lead-author form plus `and others` | 2012 | Journal present | DOI present | Draft-complete except full author list and optional volume/pages/issue | Yes | Verify full author list and journal formatting. |
| `b3pdb_2021` | article | B3Pdb: an archive of blood-brain barrier-penetrating peptides | Lead-author form plus `and others` | 2021 | Journal present | DOI present | Draft-complete except full author list and optional volume/pages/issue | Yes | Verify full author list and exact title typography. |
| `b3pred_2021` | article | B3Pred: A Random-Forest-Based Method for Predicting and Designing Blood-Brain Barrier Penetrating Peptides | Lead-author form plus `and others` | 2021 | Journal present | DOI present | Draft-complete except full author list and optional volume/pages/issue | Yes | Verify title casing and final journal style. |
| `bbppred_2021` | article | BBPpred: Sequence-Based Prediction of Blood-Brain Barrier Peptides with Feature Representation Learning and Logistic Regression | Lead-author form plus `and others` | 2021 | Journal present | DOI present | Draft-complete except full author list and optional volume/pages/issue | Yes | Verify full author list and final citation style. |
| `bbppredict_2022` | article | BBPpredict: A Web Service for Identifying Blood-Brain Barrier Penetrating Peptides | Lead-author form plus `and others` | 2022 | Journal present | DOI present | Draft-complete except full author list and optional volume/pages/issue | Yes | Verify full author list and final citation style. |
| `saito_rehmsmeier_2015_prauc` | article | The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets | Full supplied authors | 2015 | Journal present | DOI present | Metadata mostly complete; optional volume/pages/issue not present | Yes | Verify PLOS ONE volume/issue/article number if required by style. |
| `chicco_jurman_2020_mcc` | article | The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary classification evaluation | Full supplied authors | 2020 | Journal present | DOI present | Metadata mostly complete; optional volume/pages/issue not present | Yes | Verify BMC article number/volume if required by style. |
| `scikit_learn_2011` | article | Scikit-learn: Machine Learning in Python | Lead-author form plus `and others` | 2011 | Journal present | DOI not supplied; volume/pages present | Draft-complete for supplied pack; DOI/URL policy needs review | Yes | Verify full author list and whether a DOI or URL should be added. |
| `pandas_2010` | inproceedings | Data Structures for Statistical Computing in Python | Full supplied author | 2010 | Proceedings title present | DOI present | Metadata mostly complete; pages not present | Yes | Verify proceedings page range and formatting if required. |
| `matplotlib_2007` | article | Matplotlib: A 2D Graphics Environment | Full supplied author | 2007 | Journal present | DOI present | Metadata mostly complete; optional volume/pages/issue not present | Yes | Verify volume/issue/pages if required by style. |
| `practicpp_2024` | article | PractiCPP | Lead-author form plus `and others` | 2024 | Journal present | DOI present | Draft-complete for supplied pack; title may need expansion | Yes | Build log flags possible final full-title expansion. |
| `bbb_shuttle_review_2016` | article | Blood-brain barrier shuttle peptides: an emerging paradigm for brain delivery | Supplied author-name form, no initials | 2016 | Journal present | DOI present | Draft-complete except full author-name formatting and optional volume/pages/issue | Yes | Verify accents, initials, and journal style. |
| `augur_2024` | article | Prediction of blood-brain barrier penetrating peptides based on data augmentation with Augur | Lead-author form plus `and others` | 2024 | Journal present | DOI present | Draft-complete except full author list and optional volume/pages/issue | Yes | Verify full author list and final citation style. |
| `brainpeppass_2024` | article | BrainPepPass: A Framework Based on Supervised Dimensionality Reduction for Predicting Blood-Brain Barrier-Penetrating Peptides | Lead-author form plus `and others` | 2024 | Journal present | DOI present | Draft-complete except full author list and optional volume/pages/issue | Yes | Verify capitalization and full author list. |
| `deepb3p3_2023` | article | A prediction model for blood-brain barrier penetrating peptides based on masked peptide transformers with dynamic routing | Supplied author-name form | 2023 | Journal present | DOI present | Draft-complete except full author-name formatting and optional volume/pages/issue | Yes | Verify initials, author formatting, and final citation fields. |
| `esm_bbb_pred_2025` | article | ESM-BBB-Pred: a fine-tuned ESM 2.0 and deep neural networks for the identification of blood-brain barrier peptides | Lead-author form plus `and others` | 2025 | Journal present | DOI present | Draft-complete except full author list and optional volume/pages/issue | Yes | Verify publication status and final citation fields before public posting. |
| `b3bpfn_2026` | article | Prediction of Blood-Brain Barrier-Penetrating Peptides Using B3BPFN | Lead-author form plus `and others` | 2026 | Journal present | DOI present | Draft-complete except full author list and optional volume/pages/issue | Yes | Verify publication status and DOI before public posting. |
| `perseucpp_2025` | article | PerseuCPP: a machine learning strategy to predict cell-penetrating peptides and their uptake efficiency | Lead-author form plus `and others` | 2025 | Journal present | DOI present | Draft-complete except full author list and optional volume/pages/issue | Yes | Verify publication status and final citation fields before public posting. |

## Human Cleanup Checklist

- [ ] Verify full author lists for every entry.
- [ ] Replace `and others` where the final style or human reviewer requires complete author lists.
- [ ] Verify exact titles, including capitalization, punctuation, hyphenation, and Greek/special characters if present.
- [ ] Verify exact venue or journal names.
- [ ] Verify publication year.
- [ ] Verify DOI or stable URL.
- [ ] Verify volume, issue, pages, or article numbers where required by the final style.
- [ ] Verify software citation formats against package/project recommendations.
- [ ] Verify dataset/source citation formats against source attribution decisions.
- [ ] Verify citation keys match manuscript placeholders and remain stable.
- [ ] Verify no unverified references are included.
- [ ] Verify deferred references remain out of `references.bib` unless separately completed and approved.
- [ ] Verify every included reference supports the exact claim cited.

## High-Priority Entries to Review

### Entries with `and others`

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

### Entries without DOI in the draft BibTeX

- `scikit_learn_2011` - build log states no DOI was supplied in the verified pack.

### Entries without volume/pages/issue or article number in the draft BibTeX

- Most article entries omit one or more of volume, issue, pages, or article number. Human cleanup should decide which fields are required by the final bibliography style.
- `scikit_learn_2011` includes volume and pages but still needs author-list review.
- `pandas_2010` is a proceedings entry with DOI but no page range in the draft.

### Software/tool references

- `scikit_learn_2011`
- `pandas_2010`
- `matplotlib_2007`
- `REF_PROTPARAM_FEATURES` remains deferred pending canonical citation verification.

### Dataset/source lineage references

- `brainpeps_2012`
- `b3pdb_2021`
- `b3pred_2021`
- `bbppred_2021`
- `bbppredict_2022`

These support literature and dataset-lineage context only. They do not resolve Permea dataset attribution, licensing, redistribution, or novelty.

## Deferred or Partial References

Deferred references from the build log and consistency check:

| Placeholder key | Current status | Required action |
|---|---|---|
| `REF_DATASETS_FOR_DATASETS` | Deferred; DOI and final bibliographic details not supplied in verified pack. | Complete metadata before bibliography insertion. |
| `REF_PROTPARAM_FEATURES` | Deferred; canonical citation, year, venue, DOI/PMID/URL not supplied. | Verify canonical citation or approved tool-reference policy. |
| `REF_PEPBENCHMARK` | Deferred partial benchmark-standardization lead. | Verify exact citation type, stable URL/DOI if any, and PDF/supplement-supported claims before use. |
| `REF_CPP_COMPUTATIONAL_REVIEW` | Deferred; title, venue, year, DOI supplied but no author metadata. | Add only after author metadata is supplied or approved no-author convention is chosen. |
| `REF_CPP_CLINICAL_REVIEW` | Deferred/candidate-only; no second-pass metadata supplied. | Keep out unless later verified. |

Do not promote deferred references in this checklist.

## Citation-to-Claim Review Checklist

- [ ] Every citation supports the exact sentence where it appears.
- [ ] No citation is used to support stronger biological claims than the source provides.
- [ ] No citation is used to imply Permea biological validation, wet-lab validation, validated delivery, therapeutic efficacy, clinical efficacy, or robust generalization.
- [ ] BBB/background citations support background only.
- [ ] Dataset/source citations support lineage or background only and do not imply Permea dataset novelty or dataset licensing closure.
- [ ] Leakage/similarity citations support benchmark caution only.
- [ ] Software citations support implementation/tooling only.
- [ ] Metric citations support metric interpretation only, not benchmark generalization.
- [ ] Adjacent CPP citations are clearly presented as adjacent context, not direct BBB validation.
- [ ] Citation keys in `docs/PREPRINT_DRAFT_V0_1.md` and `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md` remain present in `references.bib`.

## Final Approval Checklist

- [ ] `references.bib` reviewed by human.
- [ ] Author lists cleaned or explicitly approved as abbreviated.
- [ ] Metadata verified.
- [ ] DOI/URL fields checked.
- [ ] Volume/issue/pages/article-number policy checked.
- [ ] Software citations approved.
- [ ] Dataset/source citations approved.
- [ ] Citation keys checked.
- [ ] Manuscript citations checked.
- [ ] Deferred-reference decisions approved.
- [ ] Final bibliography approved by human.

## Impact on Preprint Readiness

References remain a blocker until human cleanup and final approval are complete.

This checklist does not approve the bibliography, does not finalize reference metadata, and does not make the public preprint ready. Public preprint status remains **Hold / not submission-ready**.

## Recommended Next Codex Task

Recommended next task: Task 073 - Commit Final References Human Cleanup Checklist.

## No-Change Confirmation

- `references.bib` was not modified by this checklist.
- No new references were added.
- No missing metadata was invented.
- Manuscript files were not modified.
- Data, result, and figure artifacts were not modified.
