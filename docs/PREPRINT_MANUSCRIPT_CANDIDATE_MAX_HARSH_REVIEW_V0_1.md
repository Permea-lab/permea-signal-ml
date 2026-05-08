# Preprint Manuscript Candidate Maximum-Harsh Review v0.1

## Purpose

This document records an internal maximum-harsh virtual review of the bioRxiv v0.1 manuscript candidate package.

This is not external expert review, not peer review, not trusted reviewer feedback, not public validation, and not new scientific evidence. The reviewer roles below are internal stress-test perspectives only. They do not represent real people, institutions, affiliations, credentials, emails, ORCIDs, or external comments.

This review does not submit to bioRxiv, does not clear public posting, does not modify metric values, does not rerun models, and does not add biological, wet-lab, therapeutic, clinical, leakage-free, or robust-generalization claims.

## Materials Reviewed

- `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`
- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`
- `docs/PREPRINT_METADATA_BLOCKS_DRAFT_V0_1.md`
- `references.bib`
- `docs/PREPRINT_CLAIM_BOUNDARY_AUDIT_V0_1.md`
- `docs/CITATION_CONSISTENCY_CHECK_V0_1.md`
- `docs/BIORXIV_V0_1_READINESS_REASSESSMENT_V0_1.md`
- `docs/BIORXIV_EXPORT_PACKAGE_DRAFT_V0_1.md`
- `docs/OVERNIGHT_BATCH_046_057_REPORT_V0_1.md`
- `docs/LEAKAGE_AUDIT_REPORT_V0_1.md`
- `docs/LEAKAGE_AUDIT_FINDINGS_INVESTIGATION_V0_1.md`
- `docs/DATASET.md`
- `docs/DATASET_PROVENANCE_AND_LABEL_SOURCE_CHECKLIST_V0_1.md`
- `docs/FINAL_ARTIFACT_TRACEABILITY_EXPORT_CHECK_V0_1.md`
- `results/audits/leakage_audit_summary.json`
- `results/tables/model_comparison_summary.csv`
- `results/tables/regenerated_rf_feature_importance.csv`
- `figures/regenerated_rf_feature_importance.png`

## Executive Verdict

Verdict: **Candidate acceptable with required fixes**

The manuscript candidate is scientifically more honest than a typical early computational preprint because it explicitly acknowledges random-stratified metrics, moderate leakage optimism risk, missing biological validation, incomplete provenance, and placeholder metadata. However, the council would not clear the package for public bioRxiv posting, website publication, or partner-facing use in its current form. The current package is acceptable for continued internal manuscript development and can support carefully caveated trusted-review circulation.

The harshest summary is: the manuscript is directionally honest, but still too easy to overread. The abstract foregrounds attractive metrics before the leakage and provenance caveats. The title and conclusion are bounded but still use broad "permeability-related signal" language that could be read as stronger than the dataset supports. Related Work is adequate as a scaffold but not yet strong enough to survive a skeptical field reader. The supplement and bibliography are useful drafts, not submission assets.

## Reviewer A - Statistical Executioner

### Verdict

Hold pending fixes

### Top Criticisms

- The abstract still lets readers remember the ROC-AUC and PR-AUC values more strongly than the leakage caveat.
- The current split is reconstructed random-stratified `StratifiedKFold`, not duplicate-aware, similarity-aware, source-aware, or external validation.
- Moderate cross-fold sequence-similarity risk is enough to make any broad generalization reading unsafe.
- The manuscript reports useful baseline metrics, but does not yet supply confidence intervals, leakage-aware sensitivity, or a grouped split comparison.

### Issue Table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document | Recommended action | Required before public preprint? | Required before website publication? | Required before partner/deck use? |
|---|---|---|---|---|---|---|---|---|---|
| A-01 | P1 | Abstract / metric interpretation | The abstract foregrounds ROC-AUC and PR-AUC values before the reader has fully absorbed that they may be optimistic. | `PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md` reports LR ROC-AUC ~0.8605 / PR-AUC ~0.4903 and RF ROC-AUC ~0.8489 / PR-AUC ~0.5002, then caveats leakage. | `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md` | Move the leakage and random-stratified caveat closer to the metric sentence or make it impossible to quote metrics without caveat. | Yes | Yes | Yes |
| A-02 | P1 | Split policy | The evaluation policy is traceable but not leakage-aware. | `LEAKAGE_AUDIT_FINDINGS_INVESTIGATION_V0_1.md` reports 4 same-label exact duplicate groups crossing folds and 29 cross-fold high-similarity pairs. | Manuscript candidate; supplement | State more directly that the split is a baseline rerun policy, not an independence guarantee. | Yes | Yes | Yes |
| A-03 | P2 | Class imbalance | The class-prior baseline is present, but prevalence and PR-AUC interpretation could be made more visible for nontechnical readers. | `model_comparison_summary.csv` shows Dummy PR-AUC 0.0909086752 and zero precision/recall/F1/MCC. | Manuscript candidate; supplement | Add a concise class-prior explanation near the results table or supplement table. | Strongly recommended | Yes | Yes |
| A-04 | P2 | Missing sensitivity analysis | No leakage-aware, duplicate-aware, or similarity-aware split sensitivity is present. | `BIORXIV_V0_1_READINESS_REASSESSMENT_V0_1.md` keeps the package not submission-ready; leakage docs recommend follow-up. | Manuscript candidate; roadmap | Keep as explicit limitation or run a future sensitivity analysis before stronger benchmark claims. | Yes unless explicitly caveated | Yes | Yes |
| A-05 | P3 | Statistical uncertainty | Metrics are point estimates without intervals or fold-level dispersion in the candidate. | Main manuscript cites summary table only; no interval table inspected in package. | Manuscript candidate; supplement | Add fold-level or uncertainty context later if artifacts support it; otherwise state point-estimate limitation. | Recommended | Recommended | Recommended |

### Killer Questions

- What happens to Logistic Regression and Random Forest performance if exact duplicates and high-similarity sequence clusters cannot cross folds?
- Are the reported PR-AUC values still non-trivial under a similarity-aware split?
- Can the abstract metric sentence be quoted by a third party without dropping the caveat?
- Does the model improve over the dummy baseline because of general sequence signal or because related sequences cross fold boundaries?

### Upgrade Criteria

- Add or plan a leakage-aware sensitivity analysis, or make the current limitation stronger and more visible.
- Tie every metric mention to "random-stratified baseline" language.
- Add class-prior context in the result narrative or supplement.
- Avoid any phrase that implies current metrics are generalization estimates.

## Reviewer B - Biological Skeptic

### Verdict

Pass with severe caveats

### Top Criticisms

- "Permeability-related signal" is defensible only if repeatedly tied to the current benchmark labels, not real BBB transport.
- "Candidate prioritization" can be useful internally, but public readers may interpret it as biological actionability.
- Feature importance language is currently bounded, but figure captions and public reuse could easily turn it into mechanism.
- The label-source and dataset provenance gaps are still biologically serious, not merely administrative.

### Issue Table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document | Recommended action | Required before public preprint? | Required before website publication? | Required before partner/deck use? |
|---|---|---|---|---|---|---|---|---|---|
| B-01 | P1 | Biological claim boundary | The phrase "permeability-related signal" can be overread as biological transport evidence. | `DATASET.md` says labels are not independently verified biological truth; candidate says no wet-lab validation exists. | Title, abstract, conclusion | Define the phrase as benchmark-label signal under the current dataset, not confirmed BBB behavior. | Yes | Yes | Yes |
| B-02 | P1 | Candidate prioritization | Candidate-prioritization language could be mistaken for experimental prioritization readiness. | Candidate and supplement say ranking is pre-experimental; result artifacts include ranking outputs. | Results; Discussion; supplement | Add "computational filtering only" wherever ranking or prioritization is public-facing. | Yes | Yes | Yes |
| B-03 | P1 | Feature importance | The feature-importance result is easy to misuse as biological mechanism. | `regenerated_rf_feature_importance.csv` ranks `gravy`, `aromaticity`, `pI`, `length`, `charge`; candidate says model-level only. | Results; figures; captions | Keep feature importance out of mechanistic framing and caption it as model behavior only. | Yes | Yes | Yes |
| B-04 | P2 | Label-source uncertainty | Label provenance remains partially unresolved. | `DATASET_PROVENANCE_AND_LABEL_SOURCE_CHECKLIST_V0_1.md` lists original label assignment criteria, assay source, and source attribution as unresolved. | Dataset, Methods, Data Availability | Make label-source incompleteness prominent in dataset and limitations language. | Yes | Yes | Yes |
| B-05 | P4 | Future validation path | The manuscript lacks a concrete biological validation roadmap. | Candidate states no wet-lab validation and future validation linkage is needed. | Discussion; Future work | Add future-work language only if it remains non-promissory and non-therapeutic. | No | Recommended | Recommended |

### Killer Questions

- What exactly does the positive label mean, and can the original source criteria be reconstructed?
- Is the model predicting BBB penetration, inherited benchmark labels, or sequence similarity to labeled positives?
- Would any partner reader interpret ranking outputs as delivery success probabilities?
- Can feature importance be shown without inviting a mechanistic story?

### Upgrade Criteria

- Replace any ambiguous biological-language sentence with benchmark-target wording.
- Add a highly visible no-wet-lab and no-biological-validation boundary wherever public readers see metrics or rankings.
- Keep label-source incompleteness as a first-order limitation.

## Reviewer C - Literature Gatekeeper

### Verdict

Pass with severe caveats

### Top Criticisms

- Related Work names the right families, but it is still closer to a compressed citation scaffold than a fully argued field positioning.
- The manuscript avoids SOTA claims, which is correct, but it should more clearly say why it is not trying to compete with newer architecture-heavy predictors.
- Draft BibTeX entries use lead-author forms and need human bibliography cleanup before public use.
- Modern predictor citations make the work look field-aware, but the manuscript needs sharper separation between "context" and "direct comparator."

### Issue Table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document | Recommended action | Required before public preprint? | Required before website publication? | Required before partner/deck use? |
|---|---|---|---|---|---|---|---|---|---|
| C-01 | P2 | Related Work completeness | Related Work is adequate for a candidate, but too thin for a skeptical field reader. | Candidate lists Brainpeps, B3Pdb, B3Pred, BBPpred, BBPpredict, Augur, BrainPepPass, DeepB3P3, ESM-BBB-Pred, B3BPFN, PractiCPP, and PerseuCPP. | Related Work | Expand into a clearer lineage: dataset resources, early predictors, modern predictors, adjacent CPP benchmarks, benchmark hygiene. | Yes | Recommended | Recommended |
| C-02 | P2 | Comparator framing | The manuscript does not fully explain why there is no head-to-head SOTA-style comparison. | Candidate states this is not a frontier modeling benchmark, but Related Work is compressed. | Related Work; Discussion | State explicitly that modern predictors are context, not benchmarked comparators in v0.1. | Yes | Yes | Yes |
| C-03 | P2 | Bibliography quality | `references.bib` is useful but not final because several entries use `and others`. | `OVERNIGHT_BATCH_046_057_REPORT_V0_1.md` says human reference review required and author-list expansion remains. | `references.bib`; export package | Human review references before public posting; expand author lists and verify formatting. | Yes | Recommended | Recommended |
| C-04 | P1 | Positioning | The paper should not let "initial evidence" become an implicit novelty or superiority claim. | Candidate title and conclusion are bounded, but use broad "permeability-related signal" framing. | Title; abstract; conclusion | Preserve "baseline evidence package" positioning and avoid novelty language beyond reproducibility/discipline. | Yes | Yes | Yes |
| C-05 | P3 | Supplement structure | Related Work would benefit from a compact method-lineage table, but none is in the supplement draft. | `SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md` has artifact appendices but no related-work table. | Supplement | Add optional related-work or comparator-context table after bibliography cleanup. | No | Recommended | Recommended |

### Killer Questions

- Which cited methods are direct dataset-lineage references versus broad context?
- Does the manuscript fairly explain why Permea is not claiming to beat BBPpred, B3Pred, BBPpredict, Augur, BrainPepPass, DeepB3P3, ESM-BBB-Pred, or B3BPFN?
- Are all BibTeX entries publication-grade, or just citation-key consistent?
- Would a field reviewer see Related Work as complete enough to avoid the impression of cherry-picking?

### Upgrade Criteria

- Expand Related Work into a defensible lineage narrative.
- Add a clear "not a SOTA comparison" statement.
- Complete human bibliography cleanup.
- Separate direct comparator/dataset lineage from contextual modern methods.

## Reviewer D - bioRxiv Screening Skeptic

### Verdict

Hold pending fixes

### Top Criticisms

- The package is explicitly not submission-ready, and the unresolved blockers are not cosmetic.
- Metadata, disclosures, data availability, code availability, and legal/licensing statements are placeholders.
- The supplement is a draft appendix, not a final supplement.
- The export package is a draft manifest, not a submission bundle.

### Issue Table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document | Recommended action | Required before public preprint? | Required before website publication? | Required before partner/deck use? |
|---|---|---|---|---|---|---|---|---|---|
| D-01 | P1 | Metadata | Author list, affiliations, corresponding author, ORCIDs, funding, competing interests, acknowledgements, and contributions are placeholders. | `PREPRINT_METADATA_BLOCKS_DRAFT_V0_1.md` contains placeholder blocks only. | Metadata blocks; manuscript candidate | Replace placeholders with human-approved metadata before submission. | Yes | Yes if public authoring shown | Yes |
| D-02 | P1 | Data/legal availability | Dataset licensing, redistribution, attribution, source path, and label-source criteria remain unresolved. | `BIORXIV_V0_1_READINESS_REASSESSMENT_V0_1.md` and `DATASET_PROVENANCE_AND_LABEL_SOURCE_CHECKLIST_V0_1.md` list these as blockers. | Data Availability; Dataset; supplement | Resolve or explicitly disclose limitations in final public language. | Yes | Yes | Yes |
| D-03 | P2 | Bibliography | Citation consistency passed, but bibliography is still a draft requiring human review. | `CITATION_CONSISTENCY_CHECK_V0_1.md` passes key matching; `OVERNIGHT_BATCH_046_057_REPORT_V0_1.md` says human bibliography review required. | `references.bib`; manuscript | Complete human bibliography formatting and metadata review. | Yes | Recommended | Recommended |
| D-04 | P2 | Supplement/export | Supplement and export package are drafts, not final formatted assets. | `SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md` and `BIORXIV_EXPORT_PACKAGE_DRAFT_V0_1.md` both state not final or not export-ready. | Supplement; export package | Prepare final supplement, captions, table list, and export bundle. | Yes | Yes | Recommended |
| D-05 | P3 | Screening polish | Manuscript and supplement are Markdown candidates, not final submission formatting. | Export manifest says no final PDF, DOCX, submission bundle, or public deployment created. | Manuscript candidate; export package | Run final formatting and rendering pass after content fixes. | Yes | Recommended | No |

### Killer Questions

- Who are the authors, and who accepts responsibility for the manuscript?
- Can the dataset be redistributed or publicly referenced in its current form?
- Are references final enough for public posting?
- Is there a final supplement, or only a draft appendix?
- Has a human approved all placeholders, availability statements, and legal language?

### Upgrade Criteria

- Replace or explicitly approve all metadata and disclosure placeholders.
- Close or caveat data/legal availability in final text.
- Prepare a final supplement/export bundle.
- Complete final bibliography review.

## Reviewer E - Adversarial Partner/Investor Reader

### Verdict

Pass with severe caveats

### Top Criticisms

- The paper can strengthen Permea credibility if framed as disciplined transparency, but it will backfire if used as proof of delivery capability.
- The metric values are tempting public talking points; without immediate caveats, they are dangerous.
- The leakage audit is a trust-builder only if Permea owns the moderate optimism risk plainly.
- Website or deck reuse must be rewritten for nontechnical audiences without turning caveats into fine print.

### Issue Table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document | Recommended action | Required before public preprint? | Required before website publication? | Required before partner/deck use? |
|---|---|---|---|---|---|---|---|---|---|
| E-01 | P1 | Public metric risk | Public readers may quote ROC-AUC and PR-AUC without the leakage caveat. | Candidate abstract includes both metrics and caveat; readiness docs say not public-ready. | Abstract; website/deck derivatives | Make caveat inseparable from metric statements in any public or partner-facing version. | Yes | Yes | Yes |
| E-02 | P1 | Business overread | "Candidate prioritization" can be read as a practical delivery engine. | Candidate and supplement describe ranking outputs and prioritization before validation. | Results; Discussion; future website/deck | Rewrite public-facing phrasing as "computational triage hypothesis generation" or equivalent bounded language. | Yes | Yes | Yes |
| E-03 | P2 | Credibility framing | The strongest credibility story is process discipline, not predictive performance. | Package includes traceability, claim-boundary audit, citation check, leakage audit, and readiness reassessment. | Abstract; Discussion; public summary | Lead with reproducible evidence package and known limitations, not model performance. | Recommended | Yes | Yes |
| E-04 | P2 | Partner/deck separation | Partner or investor decks are absent and cannot inherit clearance from this manuscript review. | `FINAL_ARTIFACT_TRACEABILITY_EXPORT_CHECK_V0_1.md` says deck/pitch materials are absent and public deck traceability cannot be cleared. | Future decks; website | Run separate claim-boundary review for any public or partner deck. | No | Yes | Yes |
| E-05 | P4 | Strategic next step | A leakage-aware sensitivity plan would make the transparency story stronger. | Leakage docs recommend similarity-aware follow-up before stronger claims. | Roadmap; future work | Plan or run follow-up before stronger public benchmark claims. | No if caveated | Recommended | Recommended |

### Killer Questions

- Would a nontechnical reader conclude Permea has validated BBB delivery? If yes, the copy fails.
- Can the paper be summarized publicly without a metric hype cycle?
- Does the manuscript make caveats look like rigor or like excuses?
- Is the package better used as a transparent v0.1 evidence release than as a performance announcement?

### Upgrade Criteria

- Make public summaries lead with transparency, reproducibility, and boundaries.
- Keep metric statements coupled to random-stratified and leakage-risk language.
- Prepare separate public/partner claim-boundary materials before reuse.

## Consolidated P0-P4 Distribution

| Priority | Count | Interpretation |
|---|---:|---|
| P0 | 0 | No factual contradiction or broken evidence was found in the reviewed package. |
| P1 | 10 | Major claim-boundary, public-readiness, leakage, metadata, and public-overread risks require fixes before public use. |
| P2 | 10 | Method, citation, provenance, supplement, and artifact clarity issues require cleanup or explicit caveats. |
| P3 | 3 | Readability, formatting, and presentation polish issues remain. |
| P4 | 2 | Future-work improvements would strengthen the package but do not block internal continuation. |

## Top 10 Required Fixes

1. Strengthen the abstract so metric values cannot be quoted apart from random-stratified and leakage-risk caveats.
2. State more directly that the current split policy is not duplicate-aware, similarity-aware, source-aware, or external validation.
3. Reframe "permeability-related signal" as benchmark-label signal under the current dataset, not confirmed BBB transport.
4. Bound candidate-prioritization language as computational filtering before experimental validation.
5. Keep Random Forest feature importance explicitly non-mechanistic in text and captions.
6. Resolve or explicitly disclose dataset attribution, licensing, redistribution, source-path, and label-source gaps.
7. Replace or human-approve author, affiliation, funding, competing-interest, acknowledgement, contribution, ethics, data availability, and code availability placeholders.
8. Complete human bibliography review, including author-list expansion and final formatting.
9. Finalize supplement/export packaging with captions, table list, figure decisions, and artifact inventory.
10. Add or plan leakage-aware or similarity-aware split sensitivity before making stronger benchmark claims.

## Go/No-Go Matrix

| Use case | Decision | Rationale |
|---|---|---|
| Continue internal manuscript development | Go | The candidate is coherent, traceable, and scientifically bounded enough for continued editing. |
| Public bioRxiv posting | Hold | Metadata, legal, bibliography, supplement/export, and leakage-aware interpretation issues remain unresolved. |
| Permea website research archive | Hold | Public readers could overread metrics, candidate ranking, and biological relevance without a separate public-claims pass. |
| Partner/deck use | Hold | Deck materials are absent and would need separate claim-boundary review before use. |
| Trusted external reviewer circulation | Go with caveats | A carefully labeled human-review packet can be circulated if it states this is a computational candidate, not a public-ready submission. |

## Recommended Next Maintainer Task

Task 059 - Commit Maximum-Harsh Manuscript Candidate Review

Rationale: this review report is an internal planning artifact. It should be committed before any follow-on task applies fixes to the manuscript candidate, bibliography, metadata blocks, or export package.

## Safety Confirmation

- This review is internal and virtual only.
- No external reviewer feedback is represented.
- No manuscript files were modified by this review.
- `references.bib` was not modified by this review.
- No data files were modified.
- No result artifacts were modified.
- No figure artifacts were modified.
- No metric values were changed.
- No baseline models were rerun.
- Public preprint status remains not submission-ready.
- No leakage-free, robust-generalization, biological-validation, wet-lab-validation, therapeutic-efficacy, or clinical-efficacy claim is made.
