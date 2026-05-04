# Preprint Manuscript Candidate Post-Fix Review v0.1

## Purpose

This document records an internal post-fix harsh review of the bioRxiv v0.1 manuscript candidate after the Task 060/061 abstract and claim-boundary fixes.

This is an internal virtual review only. It is not external expert review, not peer review, not public validation, and not new scientific evidence. The reviewer roles below are internal stress-test perspectives only and do not represent real people, institutions, affiliations, credentials, emails, ORCIDs, or external comments.

This review does not submit to bioRxiv, does not clear public posting, does not modify metric values, does not rerun models or leakage audits, and does not add biological, wet-lab, therapeutic, clinical, leakage-free, or robust-generalization claims.

## Materials Reviewed

- `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`
- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/PREPRINT_MANUSCRIPT_CANDIDATE_FIX_CHANGELOG_V0_1.md`
- `docs/PREPRINT_MANUSCRIPT_CANDIDATE_MAX_HARSH_REVIEW_V0_1.md`
- `docs/PREPRINT_CLAIM_BOUNDARY_AUDIT_V0_1.md`
- `docs/BIORXIV_V0_1_READINESS_REASSESSMENT_V0_1.md`
- `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`
- `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`
- `docs/BIORXIV_EXPORT_PACKAGE_DRAFT_V0_1.md`
- `docs/CITATION_CONSISTENCY_CHECK_V0_1.md`
- `references.bib`
- `docs/LEAKAGE_AUDIT_REPORT_V0_1.md`
- `docs/LEAKAGE_AUDIT_FINDINGS_INVESTIGATION_V0_1.md`
- `docs/DATASET.md`
- `results/audits/leakage_audit_summary.json`
- `results/tables/model_comparison_summary.csv`
- `results/tables/regenerated_rf_feature_importance.csv`
- `docs/REVIEW_OPERATIONS_INDEX_V0_1.md`

## Executive Verdict

Verdict: **Improved with required follow-up**

Task 060/061 materially reduced the highest-risk claim-boundary issues identified in the maximum-harsh review. The abstract now frames performance as random-stratified baseline metrics, explicitly says the estimates are not leakage-aware generalization estimates, places same-label cross-fold similarity caveats near the metric interpretation, and bounds candidate prioritization to computational hypothesis generation before experimental validation.

The manuscript candidate is now acceptable for the next internal draft stage. It is still not appropriate for public bioRxiv posting, website archive use, or partner/deck use without further readiness work. The remaining blockers are mostly P2 readiness and evidence-package issues: metadata/disclosure placeholders, dataset attribution and licensing, label-source criteria, human bibliography review, supplement/export formatting, human approval, and leakage-aware or similarity-aware sensitivity planning before any stronger benchmark claims.

## Reviewer A - Statistical Executioner

### Verdict

Improved with caveats

### Remaining Criticisms

- Metric interpretation is now much safer, but no leakage-aware sensitivity analysis exists.
- The candidate still reports point estimates without confidence intervals or fold-level dispersion.
- The current evidence remains tied to `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`, which is traceable but not duplicate-aware, similarity-aware, source-aware, or external validation.

### Issue Table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document | Recommended action | Required before next internal draft? | Required before public preprint? | Required before website/partner use? |
|---|---|---|---|---|---|---|---|---|---|
| A-01 | P2 | Leakage-aware evaluation | No duplicate-aware or similarity-aware sensitivity analysis is available. | `LEAKAGE_AUDIT_FINDINGS_INVESTIGATION_V0_1.md` reports 4 same-label duplicate groups crossing folds, 56 cross-fold near-duplicate pairs, and 29 cross-fold high-similarity pairs. | Manuscript candidate; supplement; roadmap | Keep as a visible limitation or plan a leakage-aware sensitivity task before stronger benchmark claims. | No | Yes, unless explicitly deferred and caveated | Yes |
| A-02 | P3 | Statistical uncertainty | Metrics are point estimates without interval or fold-dispersion context in the candidate package. | `results/tables/model_comparison_summary.csv` contains summary metrics only. | Manuscript candidate; supplement | Add fold-level or uncertainty context later if supported by artifacts; otherwise preserve point-estimate limitation. | No | Recommended | Recommended |
| A-03 | P4 | Future split policy | A richer future split policy is not yet specified. | Dataset docs state `source` is too coarse and recommend duplicate-aware, similarity-aware, or metadata-aware grouping. | Future analysis plan | Define a leakage-aware split/sensitivity plan in a future task. | No | No, if limitation remains explicit | Recommended |

### Upgrade Criteria

- Add leakage-aware or similarity-aware sensitivity analysis.
- Add uncertainty or fold-level context if artifacts support it.
- Keep every metric mention coupled to random-stratified and leakage-risk language.

## Reviewer B - Biological Skeptic

### Verdict

Improved and acceptable for internal draft

### Remaining Criticisms

- Biological and prioritization language is now bounded, but public summaries could still overread "candidate prioritization" if separated from the caveats.
- Label-source criteria and biological meaning of the positive class remain unresolved.
- Feature importance is safely framed in the manuscript and supplement, but figure reuse needs the same non-mechanistic caption discipline.

### Issue Table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document | Recommended action | Required before next internal draft? | Required before public preprint? | Required before website/partner use? |
|---|---|---|---|---|---|---|---|---|---|
| B-01 | P3 | Public-language carryover | "Permeability-related" and "candidate prioritization" are bounded in the candidate but could be overread in derivative summaries. | `PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md` defines the work as computational evidence and pre-experimental hypothesis generation. | Future public summaries; website/deck derivatives | Run a separate public-copy claim-boundary pass before website or deck use. | No | Recommended | Yes |
| B-02 | P2 | Label-source uncertainty | Original label-source criteria remain incomplete. | `DATASET.md` states the label field should not be treated as independently verified biological truth. | Dataset, Methods, Limitations | Resolve or keep the limitation highly visible. | No | Yes | Yes |
| B-03 | P4 | Experimental validation | No wet-lab or biological validation plan is executed in the current package. | Candidate and supplement explicitly state no biological or wet-lab validation exists. | Future work | Keep as future work without therapeutic, clinical, or delivery-performance claims. | No | No | Recommended |

### Upgrade Criteria

- Complete or explicitly disclose label-source criteria.
- Keep feature-importance captions model-level only.
- Review any public summary so computational filtering is not converted into delivery-performance language.

## Reviewer C - Literature Gatekeeper

### Verdict

Improved with caveats

### Remaining Criticisms

- The Related Work is safer because it avoids SOTA positioning, but it remains compressed.
- Citation consistency passed, but `references.bib` is still a draft requiring human bibliography review.
- Several bibliography entries use lead-author forms plus `and others`; that is acceptable for a draft but not final public posting.

### Issue Table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document | Recommended action | Required before next internal draft? | Required before public preprint? | Required before website/partner use? |
|---|---|---|---|---|---|---|---|---|---|
| C-01 | P2 | Related Work completeness | Related Work is adequate for candidate review but still thin for field-facing public use. | Candidate cites dataset lineage, early BBB predictors, modern predictors, and adjacent CPP benchmark context. | Related Work | Expand or polish the literature lineage before final public posting. | No | Recommended | Recommended |
| C-02 | P2 | Bibliography quality | Citation key consistency passed, but bibliography formatting and author completeness require human review. | `CITATION_CONSISTENCY_CHECK_V0_1.md` passes keys; `references.bib` includes several `and others` author lists. | `references.bib`; manuscript candidate | Complete human bibliography review before public posting. | No | Yes | Recommended |
| C-03 | P3 | Comparator framing | The manuscript says it is not a frontier/SOTA comparison, but the distinction could be sharper for non-specialists. | Candidate frames modern predictors as context rather than head-to-head comparators. | Related Work; Discussion | Add clearer direct-lineage versus contextual-method language in a later polish pass. | No | Recommended | Recommended |

### Upgrade Criteria

- Complete human bibliography cleanup.
- Sharpen lineage and comparator framing.
- Preserve no-SOTA positioning.

## Reviewer D - bioRxiv Screening Skeptic

### Verdict

Hold pending fixes

### Remaining Criticisms

- The manuscript candidate is internally coherent, but it is still explicitly not a submission package.
- Metadata, disclosure, data availability, code availability, licensing, and export items remain incomplete.
- The supplement and export manifest are drafts, not final formatted assets.

### Issue Table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document | Recommended action | Required before next internal draft? | Required before public preprint? | Required before website/partner use? |
|---|---|---|---|---|---|---|---|---|---|
| D-01 | P2 | Metadata and disclosures | Author metadata, affiliations, corresponding author, funding, conflicts, acknowledgements, contributions, ethics, and availability statements remain placeholders or pending human approval. | `BIORXIV_V0_1_READINESS_REASSESSMENT_V0_1.md` and `BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` list these blockers. | Metadata blocks; checklist; candidate package | Replace placeholders with human-approved metadata and disclosures. | No | Yes | Yes if public authoring is shown |
| D-02 | P2 | Dataset/legal status | Dataset attribution, licensing, redistribution, source-chain closure, and label-source criteria remain unresolved. | `DATASET.md` and readiness docs list provenance and legal blockers. | Dataset; Data Availability; supplement | Resolve or explicitly disclose final limitations before public posting. | No | Yes | Yes |
| D-03 | P2 | Supplement/export readiness | Supplement and export package are drafts only. | `SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md` says not final; `BIORXIV_EXPORT_PACKAGE_DRAFT_V0_1.md` says not export-ready. | Supplement; export manifest | Prepare final supplement, captions, table list, export format, and human approval checklist. | No | Yes | Recommended |
| D-04 | P3 | Formatting polish | Markdown candidate and draft package are not final submission-formatted assets. | Export draft confirms no final PDF, DOCX, submission bundle, website material, or public deployment was created. | Manuscript candidate; supplement; export package | Run final formatting/rendering pass after content and metadata closure. | No | Yes | No |

### Upgrade Criteria

- Complete metadata and disclosure blocks.
- Resolve or disclose dataset/legal issues.
- Prepare final supplement and export bundle.
- Obtain human approval before any public posting.

## Reviewer E - Adversarial Partner/Investor Reader

### Verdict

Improved with caveats

### Remaining Criticisms

- The paper is now more credible as a transparent versioned evidence release, but the metric values can still be misused outside the manuscript context.
- Website or deck reuse requires separate wording review because nontechnical audiences may drop the leakage and validation caveats.
- A leakage-aware sensitivity plan would strengthen credibility before stronger public benchmark messaging.

### Issue Table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document | Recommended action | Required before next internal draft? | Required before public preprint? | Required before website/partner use? |
|---|---|---|---|---|---|---|---|---|---|
| E-01 | P2 | Public-copy risk | The manuscript is caveated, but future public copy could turn metrics into unsupported performance claims. | Candidate explicitly states metrics are random-stratified baseline metrics and may be optimistic. | Future public summaries; website/deck derivatives | Require a separate public-facing claim-boundary pass before reuse. | No | Recommended | Yes |
| E-02 | P3 | Metric prominence | Metric values remain visible and attractive even with caveats. | Abstract reports LR and RF ROC-AUC/PR-AUC values alongside caveats. | Abstract; future public summaries | In public summaries, lead with transparent evidence-package positioning, not metric hype. | No | Recommended | Yes |
| E-03 | P4 | Strategic credibility | Leakage-aware sensitivity would convert the transparency story into stronger evidence discipline. | Leakage investigation recommends leakage-aware follow-up before stronger claims. | Roadmap; future analysis | Plan sensitivity analysis before stronger benchmark messaging. | No | No | Recommended |

### Upgrade Criteria

- Keep the package framed as disciplined computational transparency.
- Separate internal manuscript clearance from website and deck clearance.
- Plan leakage-aware sensitivity before stronger public benchmark claims.

## Before/After Comparison

| Area | Task 058/059 state | Post-fix state | Residual risk |
|---|---|---|---|
| Abstract caveat risk | Metrics were too easy to quote without caveats. | Abstract now states metrics are random-stratified baseline metrics, not leakage-aware generalization estimates, and may be optimistic under detected same-label cross-fold similarity. | Reduced to low for internal draft; still requires public-summary discipline. |
| Metric/leakage coupling | Split and leakage limits were present but not inseparable enough from performance interpretation. | Results, Discussion, Limitations, and supplement tie metrics to `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` and moderate optimism risk. | Remaining issue is lack of leakage-aware sensitivity analysis. |
| Biological/prioritization wording | Candidate prioritization and permeability-related signal could be overread. | Wording now limits prioritization to computational hypothesis generation/filtering before experimental validation. | Derivative public copy still needs review. |
| Feature-importance framing | Model-level framing existed but needed stronger non-mechanistic language. | Candidate, draft, and supplement state feature importance is model behavior, not mechanism, causality, or descriptor-determination proof. | Figure reuse must keep this caption boundary. |
| Readiness status | Public bioRxiv posting was Hold. | Public bioRxiv posting remains Hold; blockers are now clearer. | Readiness blockers remain P2/P3 rather than P1 claim-boundary blockers. |

## Consolidated P0-P4 Distribution

| Priority | Count | Interpretation |
|---|---:|---|
| P0 | 0 | No factual contradiction or broken evidence was found. |
| P1 | 0 | No remaining P1 claim-boundary blocker was identified after Task 060/061 fixes. |
| P2 | 8 | Main blockers are method sensitivity, bibliography, provenance/legal, supplement/export, metadata/disclosure, and public-copy control. |
| P3 | 5 | Readability, formatting, uncertainty visibility, and public-summary polish remain. |
| P4 | 3 | Future-work improvements would strengthen the evidence package but do not block internal continuation. |

## Remaining Blockers

### P0/P1 blockers

No P0 or P1 blockers were identified for the next internal draft stage. This does not clear public posting.

### Preprint blockers

- final author metadata, author order, affiliations, corresponding author, and email
- funding, competing interests, acknowledgements, author contributions, ethics, data availability, and code availability wording
- dataset attribution, licensing, redistribution rights, source-chain closure, and original label-source criteria
- final human bibliography review and reference formatting
- final supplement, captions, table list, export bundle, and formatting pass
- human approval
- leakage-aware or similarity-aware sensitivity analysis, or explicit final disclosure that current metrics may be optimistic

### Website/partner blockers

- separate public-facing claim-boundary review
- no conversion of metrics into delivery performance, therapeutic, clinical, or robust-generalization claims
- explicit leakage and no-biological-validation caveats in any derivative material
- final decision on whether candidate-ranking artifacts can be shown publicly

### Future-work blockers

- leakage-aware or similarity-aware split planning
- source metadata recovery if available
- biological validation only if separately designed and executed

## Go/No-Go Matrix

| Use case | Verdict | Rationale |
|---|---|---|
| Continue internal manuscript development | Go | Claim-boundary fixes reduced P1 risk and the remaining issues are tractable. |
| Public bioRxiv posting | Hold | Metadata, legal, bibliography, supplement/export, human approval, and sensitivity/disclosure blockers remain. |
| Permea website research archive | Hold | Public copy needs separate claim-boundary review and public-ready caveats. |
| Partner/deck use | Hold | Nontechnical reuse could overread metrics, candidate prioritization, or delivery language. |
| Trusted external reviewer circulation | Go with caveats | Suitable if framed as an internal candidate and not as public validation or submission clearance. |

## Recommended Next Codex Task

Task 063 - Commit Post-Fix Manuscript Candidate Re-Review

Rationale: the post-fix review report is a review artifact that should be committed before choosing the next active workstream. After that, the likely next substantive tracks are metadata/disclosure closure, bibliography cleanup, supplement/export formatting, or leakage-aware sensitivity planning.

## No-Change Confirmation

- Manuscript files were not modified by this review task.
- `references.bib` was not modified.
- Data files were not modified.
- Result artifacts were not modified.
- Figure artifacts were not modified.
- Metric values were not changed.
- Baseline models were not rerun.
- Leakage audit was not rerun.
