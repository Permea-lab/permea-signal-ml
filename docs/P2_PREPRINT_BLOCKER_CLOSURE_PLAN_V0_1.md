# P2 Preprint Blocker Closure Plan v0.1

## Purpose

This document classifies the remaining P2 blockers before any public bioRxiv v0.1 posting for the current Permea Signal ML manuscript candidate.

Public preprint status remains **Hold / not submission-ready**. This plan does not close blockers by itself, does not invent metadata or legal certainty, does not add scientific evidence, does not modify benchmark metrics, and does not make public posting safe without human approval.

## Current Readiness Summary

| Path | Current status | Reason |
|---|---|---|
| Internal development | Go | No P0/P1 blocker remains for the next internal draft stage. |
| Public bioRxiv | Hold | P2 readiness, metadata, legal, reference, supplement/export, and approval blockers remain. |
| Website archive | Hold | Public copy requires a separate claim-boundary review. |
| Partner/deck use | Hold | Nontechnical reuse could overread metrics or candidate prioritization. |
| Trusted reviewer circulation | Go with caveats | Suitable only if framed as an internal candidate, not public validation. |

Current review status from `docs/PREPRINT_MANUSCRIPT_CANDIDATE_POST_FIX_REVIEW_V0_1.md`:

- P0 blockers: 0
- P1 blockers: 0
- Remaining blockers: P2/P3/P4
- Current metrics remain random-stratified baseline metrics and may be optimistic under documented sequence-similarity leakage risk.

## Blocker Inventory

| Blocker ID | Blocker area | Description | Current status | Blocking level | Can Codex close? | Requires human input? | Can remain caveated in v0.1? | Recommended action | Target task |
|---|---|---|---|---|---|---|---|---|---|
| P2-001 | Metadata/disclosures | Metadata and disclosure placeholders remain incomplete. | Placeholder blocks exist in `PREPRINT_METADATA_BLOCKS_DRAFT_V0_1.md`. | Blocks bioRxiv | Partly | Yes | No for required fields | Prepare structured input form; human supplies final values. | Task 066 |
| P2-002 | Author/affiliation/corresponding author info | Final author list, order, affiliations, corresponding author, email, and optional ORCIDs are missing. | Placeholder only. | Blocks bioRxiv | No | Yes | No | Collect exact author metadata from human operator. | Task 066 |
| P2-003 | Funding/competing interests/acknowledgements | Funding, competing interests, acknowledgements, contributions, and ethics wording are not human-approved. | Placeholder only. | Blocks bioRxiv | Partly | Yes | No for required statements | Prepare options/form; human approves exact language. | Task 066 |
| P2-004 | Dataset attribution/licensing | Original dataset attribution, license, redistribution rights, and public data-release status remain unresolved. | Unconfirmed in dataset docs. | Blocks bioRxiv/data release | Partly | Yes | Only if final public language explicitly discloses limits and avoids redistribution claims | Prepare data/legal statement options without inventing certainty. | Task 068 |
| P2-005 | Source-chain/raw dataset path | Raw source path and source-chain closure remain unresolved. | `data/raw/` lacks source dataset beyond `.gitkeep`; dataset docs disclose unresolved status. | Blocks uncaveated public claims | Partly | Yes if source/legal confirmation is needed | Yes, if prominent and accepted by human operator | Draft final caveat options and source-chain checklist. | Task 068 |
| P2-006 | Label-source criteria | Original positive/negative label-source criteria remain partially unresolved. | Current labels are benchmark targets, not independently verified biological truth. | Blocks uncaveated public claims | Partly | Yes if source reconstruction is possible | Yes, if strongly disclosed | Prepare final limitation language and recovery checklist. | Task 068 |
| P2-007 | `references.bib` human cleanup | Draft bibliography exists but uses lead-author forms plus `and others` for multiple entries. | Citation consistency passed; formatting and author completeness need human review. | Blocks bioRxiv | Partly | Yes for final bibliography approval | No for final public posting | Prepare human reference cleanup checklist. | Task 069 |
| P2-008 | Citation/source claim review | Citation keys match, but final sentence-level source support still needs human review. | `CITATION_CONSISTENCY_CHECK_V0_1.md` passes with human-review caveat. | Blocks bioRxiv | Yes for checklist/report | Yes for final approval | No for final public posting | Prepare final citation/source-claim review checklist. | Task 069 |
| P2-009 | Supplement/export formatting | Supplement and export manifest are drafts, not final upload assets. | Draft supplement and draft export manifest exist. | Blocks bioRxiv | Yes | Human approval required | No for final public posting | Prepare supplement/export formatting checklist. | Task 067 |
| P2-010 | Final figure/table/caption review | Figure/table lists exist, but final captions, numbering, resolution, and claim alignment are pending. | Export draft flags figure/table caveats. | Blocks bioRxiv | Yes | Human approval required | No for final public posting | Prepare figure/table/caption checklist. | Task 067 |
| P2-011 | Leakage-aware sensitivity or explicit final disclosure | No duplicate-aware or similarity-aware sensitivity analysis exists. | Leakage audit found moderate optimism risk; metrics may be optimistic. | Blocks stronger benchmark claims | Partly | Yes for decision to defer or require before posting | Yes, if final disclosure is explicit and human-approved | Decide whether to run sensitivity before posting or defer with caveat. | Task 070 |
| P2-012 | Human approval | No final human approval for public posting exists. | All readiness docs keep public posting on Hold. | Blocks bioRxiv, website, partner use | No | Yes | No | Human operator must approve final package after blocker closure. | Human gate |

## Closure Categories

### A. Codex-closable now

Codex can prepare these without inventing values or changing scientific claims:

- supplement/export formatting checklist
- figure/table/caption checklist
- reference consistency and source-claim review checklist
- availability statement templates with unresolved placeholders
- final manuscript formatting checklist
- dataset/legal wording options that preserve uncertainty
- leakage-aware sensitivity analysis plan
- public-copy claim-boundary checklist for website/deck reuse

### B. Human-required

These require human-provided information, legal confirmation, or final approval:

- final author list
- author order
- affiliations
- corresponding author and approved email
- ORCID IDs, if used
- author contributions
- funding statement or approved no-funding statement
- competing interests statement
- acknowledgements
- ethics statement applicability and wording
- dataset attribution, licensing, redistribution permission, and public-release decision
- public repository URL, tag/archive policy, and code availability wording
- final human bibliography approval
- decision whether to post before leakage-aware sensitivity analysis
- final public posting approval

### C. Caveatable in v0.1

These can potentially remain as explicit v0.1 caveats if the human operator accepts the risk and final wording is conservative:

- raw source path unresolved
- label-source criteria partially unresolved
- dataset version remains `pending_confirmation`
- source field too coarse for group-aware split control
- no leakage-aware split yet, provided current metrics remain random-stratified baseline metrics and potentially optimistic
- point estimates without interval/fold-dispersion context
- Related Work compression, if the manuscript clearly avoids SOTA or robust-generalization claims

### D. Future v0.2 work

These should become future work rather than blockers for a bounded v0.1 candidate, unless the human operator wants stronger public claims:

- leakage-aware or similarity-aware split/sensitivity analysis
- stronger source-chain reconstruction
- richer metadata-aware grouping
- external validation
- expanded model baselines or new model families
- verified public dataset release
- broader delivery-barrier or therapeutic-context expansion

## Minimal Path to Public bioRxiv v0.1

A minimal safe route to public bioRxiv v0.1 requires:

1. Complete human metadata and disclosure placeholders.
2. Complete final human cleanup of `references.bib`, including author-list expansion and deferred-reference decisions.
3. Complete supplement/export formatting pass, including final figure/table/caption review.
4. Add final data and code availability statements that match actual dataset and repository status.
5. Decide dataset/legal wording: resolved attribution/licensing if available, or explicit final disclosure if unresolved.
6. Decide whether leakage-aware sensitivity is required before posting or can be explicitly deferred with strong caveats.
7. Run final claim-boundary and citation consistency checks.
8. Obtain explicit human approval for public posting.

This path does not require new benchmark results, new model families, biological validation, wet-lab validation, or stronger generalization claims.

## Conservative Alternative Path

If the human operator does not want to post publicly while legal, metadata, and sensitivity issues remain unresolved:

1. Keep bioRxiv status on Hold.
2. Continue internal manuscript development and trusted-review circulation with caveats.
3. Prepare a Permea website "internal candidate / evidence release preview" only after a dedicated website claim-boundary review.
4. Continue v0.2 leakage-aware sensitivity planning before public benchmark-strength claims.
5. Defer public dataset release until licensing and redistribution rights are confirmed.

## Recommended Next Codex Tasks

| Task | Purpose | Primary output |
|---|---|---|
| Task 065 - Commit P2 Preprint Blocker Closure Plan | Close this planning artifact. | Commit this plan and index update. |
| Task 066 - Prepare Human Metadata and Disclosure Input Form | Collect author, affiliation, disclosure, and availability inputs without inventing values. | Human input form/checklist. |
| Task 067 - Prepare Supplement and Export Formatting Checklist | Convert draft supplement/export issues into a final formatting checklist. | Supplement/export checklist. |
| Task 068 - Prepare Dataset Legal and Availability Statement Options | Draft safe options for unresolved attribution, licensing, redistribution, source, and label criteria. | Data/legal statement option set. |
| Task 069 - Prepare Final References Human Cleanup Checklist | Convert bibliography caveats into a human review checklist. | References cleanup checklist. |
| Task 070 - Plan Leakage-Aware Sensitivity Analysis | Scope duplicate-aware or similarity-aware sensitivity work without changing current metrics. | Sensitivity analysis plan. |

## Human Input Required

Exact human-provided information needed before final public posting:

- final author list
- author order
- affiliations
- corresponding author email
- ORCID IDs, if desired
- author contributions
- funding statement or approved no-funding statement
- competing interests statement
- acknowledgements
- ethics statement applicability and wording
- data availability decision
- code availability decision, including public repository URL and release/archive policy
- dataset attribution and citation decision
- dataset license and redistribution decision
- decision whether processed data can be included, referenced only, or withheld
- decision whether to post before leakage-aware sensitivity analysis
- decision whether to use a Permea website preview before bioRxiv
- final human approval for public posting

## Decision Recommendation

Codex can continue preparing forms, checklists, statement options, and formatting plans. Codex cannot finalize the public preprint without human metadata, disclosure, legal, dataset, bibliography, and approval decisions.

The next practical step is to collect human metadata/legal inputs, not to expand scientific claims or add new model results.

## Task 066 Status Note

The human metadata and disclosure input form has been prepared as `docs/HUMAN_METADATA_AND_DISCLOSURE_INPUT_FORM_V0_1.md`. It is a collection template only and does not fill, approve, or resolve any author, disclosure, dataset/legal, code/data availability, bibliography, leakage-sensitivity, or public-posting decision.

## Task 068 Status Note

The supplement and export formatting checklist has been prepared as `docs/SUPPLEMENT_EXPORT_FORMATTING_CHECKLIST_V0_1.md`. It is a formatting and packaging checklist only. It does not create final PDF, DOCX, submission-bundle, website, or archive files, and it does not resolve metadata, legal, bibliography, caption, or public-approval blockers.

## Task 070 Status Note

Dataset legal and availability statement options have been prepared as `docs/DATASET_LEGAL_AND_AVAILABILITY_STATEMENT_OPTIONS_V0_1.md`. The document provides conservative wording options and human decision checklists only. It does not confirm source attribution, licensing, redistribution permission, public dataset release, complete provenance, or public posting readiness.

## Task 072 Status Note

The final references human cleanup checklist has been prepared as `docs/FINAL_REFERENCES_HUMAN_CLEANUP_CHECKLIST_V0_1.md`. It inventories the draft `references.bib`, flags human cleanup needs, and preserves final bibliography approval as a blocker. It does not modify `references.bib`, add references, or mark references as final.

## No-Change Confirmation

- Manuscript content was not modified by this plan.
- `references.bib` was not modified.
- Data files were not modified.
- Result artifacts were not modified.
- Figure artifacts were not modified.
- Metric values were not changed.
- No public preprint-ready claim is made.
- No leakage-free, robust-generalization, biological-validation, wet-lab-validation, therapeutic, or clinical claim is made.
