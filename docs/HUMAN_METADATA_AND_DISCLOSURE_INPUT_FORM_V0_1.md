# Human Metadata and Disclosure Input Form v0.1

## Purpose

This form collects human-provided metadata, disclosure statements, legal decisions, availability decisions, and final approval inputs needed before any public bioRxiv v0.1 posting.

This form must be completed by the human operator. Codex must not invent values. Completing this form does not by itself make the preprint ready. Public preprint status remains **Hold / not submission-ready** until all required fields are filled, reviewed, checked against claim boundaries, and approved by the human operator.

## Completion Instructions

- Fill in bracketed placeholders only with human-provided values.
- Mark unavailable fields as `not provided` only when intentionally omitted or not applicable.
- Do not guess affiliations, author order, emails, funding, conflicts, acknowledgements, licences, permissions, or approval decisions.
- Dataset legal, licensing, redistribution, and public-release decisions require human confirmation.
- Unresolved items should remain explicitly unresolved rather than fabricated.
- If a field is uncertain, write `[HUMAN TO CONFIRM]` and describe the uncertainty.

## Author Metadata

| Field | Required for bioRxiv? | Internal Permea tracking? | Human-provided value | Notes / decision |
|---|---:|---:|---|---|
| Final author list | Yes | Yes | `[HUMAN TO PROVIDE]` | Do not infer names from repository history. |
| Author order | Yes | Yes | `[HUMAN TO PROVIDE]` | Must be approved by authors. |
| Full legal/preferred author names | Yes | Yes | `[HUMAN TO PROVIDE]` | Use exact spelling supplied by each author. |
| Affiliation for each author | Yes | Yes | `[HUMAN TO PROVIDE]` | Include department/institution/city/country only if supplied. |
| Corresponding author | Yes | Yes | `[HUMAN TO PROVIDE]` | Must match approved public contact. |
| Corresponding email | Yes | Yes | `[HUMAN TO PROVIDE]` | Do not infer from git config or commits. |
| ORCID IDs | Optional | Yes if used | `[HUMAN TO PROVIDE OR MARK NOT PROVIDED]` | Add only author-provided ORCIDs. |
| Author contribution statement | Usually yes | Yes | `[HUMAN TO PROVIDE]` | Use author-approved wording only. |
| Contribution taxonomy | Optional | Yes if used | `[HUMAN TO CHOOSE IF DESIRED]` | Example frameworks may be selected later by human operator. |
| Author approval confirmation | Yes before posting | Yes | `[HUMAN TO CONFIRM]` | Confirm every author has approved public posting. |

## Manuscript Administrative Metadata

| Field | Required for bioRxiv? | Internal Permea tracking? | Human-provided value / decision | Notes |
|---|---:|---:|---|---|
| Final title approval | Yes | Yes | `[HUMAN TO CONFIRM]` | Current title remains provisional until approved. |
| Short title / running title | If needed | Optional | `[HUMAN TO PROVIDE OR MARK NOT NEEDED]` | Do not invent. |
| Keywords | Yes | Yes | `[HUMAN TO CONFIRM OR EDIT]` | Draft keywords exist in manuscript docs. |
| Subject category | Yes | Yes | `[HUMAN TO SELECT]` | bioRxiv subject/category decision. |
| Version date | Yes at export | Yes | `[HUMAN TO PROVIDE AT FINAL EXPORT]` | Do not pre-fill. |
| Manuscript status | Yes | Yes | `Hold / not submission-ready until completed` | Status remains Hold until final approval. |
| Abstract approval | Yes | Yes | `[HUMAN TO CONFIRM]` | Confirm caveated abstract wording. |
| Supplement approval | Strongly recommended | Yes | `[HUMAN TO CONFIRM]` | Supplement draft is not final. |
| `references.bib` approval | Yes | Yes | `[HUMAN TO CONFIRM]` | Draft bibliography requires human cleanup. |

## Funding and Acknowledgements

| Field | Required for bioRxiv? | Human-provided value / decision | Notes |
|---|---:|---|---|
| Funding statement | Yes | `[HUMAN TO PROVIDE]` | Provide exact funder names or approved no-funding statement. |
| Grant numbers | If applicable | `[HUMAN TO PROVIDE OR MARK NOT APPLICABLE]` | Do not invent. |
| Institutional support | If applicable | `[HUMAN TO PROVIDE OR MARK NOT APPLICABLE]` | Include only approved support language. |
| Acknowledgements | If applicable | `[HUMAN TO PROVIDE OR MARK NOT APPLICABLE]` | Name people/tools only with approval. |
| People/tools to acknowledge | If applicable | `[HUMAN TO PROVIDE OR MARK NOT APPLICABLE]` | Separate acknowledgements from citations. |
| No-funding statement option | If applicable | `[HUMAN TO APPROVE IF TRUE]` | Do not choose automatically. |

## Competing Interests / Conflict of Interest

| Field | Required for bioRxiv? | Human-provided value / decision | Notes |
|---|---:|---|---|
| Competing interests statement | Yes | `[HUMAN TO PROVIDE]` | Must be exact human-approved wording. |
| Founder/company interest disclosure | If applicable | `[HUMAN TO PROVIDE OR MARK NOT APPLICABLE]` | Do not infer company role or equity. |
| Employment/equity/IP disclosure | If applicable | `[HUMAN TO PROVIDE OR MARK NOT APPLICABLE]` | Include only confirmed disclosures. |
| No competing interests statement option | If applicable | `[HUMAN TO APPROVE IF TRUE]` | Do not choose automatically. |

## Ethics Statement

| Field | Required decision | Human-provided value / decision | Notes |
|---|---:|---|---|
| Human subjects involved? | Yes | `[YES / NO / UNCERTAIN - HUMAN TO CONFIRM]` | Do not infer final ethics status. |
| Animal subjects involved? | Yes | `[YES / NO / UNCERTAIN - HUMAN TO CONFIRM]` | Do not infer final ethics status. |
| Wet-lab data included? | Yes | `[YES / NO / UNCERTAIN - HUMAN TO CONFIRM]` | Current docs state no new wet-lab validation, but final statement requires human confirmation. |
| Ethics approval required? | Yes | `[YES / NO / UNCERTAIN - HUMAN TO CONFIRM]` | Human operator must decide final wording. |
| Ethics statement text | Yes if required | `[HUMAN TO PROVIDE]` | Suggested non-final placeholder below may be adapted. |

Suggested placeholder for human review only:

`[HUMAN TO CONFIRM: This study uses computational analysis of an inherited peptide benchmark dataset and does not report new human-subject, animal-subject, or wet-lab experiments.]`

## Data Availability Decision

Known repository context:

- Imported processed dataset path: `data/processed/legacy_bbb_dataset_with_features.csv`
- Rerun-ready dataset path: `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`
- Dataset config path: `configs/data/legacy_bbb_dataset_with_features.yaml`
- Raw source path remains unresolved.
- Public/preprint dataset version remains `pending_confirmation`.
- Dataset attribution and licensing are unconfirmed.

| Field | Required for bioRxiv? | Human-provided value / decision | Notes |
|---|---:|---|---|
| Data availability statement | Yes | `[HUMAN TO PROVIDE]` | Must match legal and redistribution decision. |
| Raw source dataset availability | Yes or explicit caveat | `[HUMAN TO PROVIDE OR MARK UNRESOLVED]` | Current repo status: unresolved. |
| Processed dataset availability | Yes or explicit caveat | `[HUMAN TO DECIDE]` | Decide whether file can be public, referenced, or withheld. |
| Rerun-ready dataset availability | Yes or explicit caveat | `[HUMAN TO DECIDE]` | Decide whether file can be public, referenced, or withheld. |
| Dataset version | Yes or explicit caveat | `[HUMAN TO CONFIRM OR KEEP pending_confirmation]` | Current status: `pending_confirmation`. |
| Redistribution permission | Yes | `[HUMAN TO CONFIRM]` | Do not infer from repository license. |
| Dataset license | Yes | `[HUMAN TO PROVIDE OR MARK UNCONFIRMED]` | Code/docs license does not establish dataset license. |
| Unresolved dataset caveats | Yes if unresolved | `[HUMAN TO APPROVE FINAL CAVEAT]` | Preserve source/label/legal limits. |
| Public release approved? | Yes before posting | `[YES / NO / UNDECIDED - HUMAN TO CONFIRM]` | Required before public dataset release or supplement inclusion. |

## Code Availability Decision

| Field | Required for bioRxiv? | Human-provided value / decision | Notes |
|---|---:|---|---|
| Repository URL | Yes | `[HUMAN TO PROVIDE]` | Do not assume final public URL unless confirmed. |
| Branch/tag/commit to cite | Yes | `[HUMAN TO PROVIDE]` | Decide final tag/archive policy before posting. |
| Software license | Yes | `[HUMAN TO CONFIRM]` | Confirm how repository license should be stated. |
| Code availability statement | Yes | `[HUMAN TO PROVIDE]` | Must match actual public repository status. |
| GitHub repo public? | Yes | `[YES / NO / UNDECIDED - HUMAN TO CONFIRM]` | Do not infer from local remotes. |
| Release tag needed before bioRxiv? | Recommended decision | `[YES / NO / UNDECIDED - HUMAN TO CONFIRM]` | Coordinate with final export. |

## Bibliography / Reference Approval

| Field | Required before bioRxiv? | Human-provided value / decision | Notes |
|---|---:|---|---|
| `references.bib` reviewed by human? | Yes | `[YES / NO - HUMAN TO CONFIRM]` | Draft bibliography exists but is not final. |
| Incomplete author lists cleaned? | Yes | `[YES / NO - HUMAN TO CONFIRM]` | Several entries use `and others`. |
| Deferred references accepted? | Yes | `[YES / NO / N/A - HUMAN TO CONFIRM]` | Confirm whether deferred references remain omitted. |
| Software citations approved? | Yes | `[YES / NO - HUMAN TO CONFIRM]` | Confirm citation policy for software dependencies. |
| Dataset/source citations approved? | Yes | `[YES / NO - HUMAN TO CONFIRM]` | Must align with dataset attribution decision. |

## Public Posting Decision

| Decision | Human decision | Notes |
|---|---|---|
| Post to bioRxiv before leakage-aware split? | `[YES / NO / UNDECIDED - HUMAN TO CONFIRM]` | If yes, final caveat must explicitly disclose moderate optimism risk. |
| Post to Permea website before bioRxiv? | `[YES / NO / UNDECIDED - HUMAN TO CONFIRM]` | Requires separate website claim-boundary review. |
| Use manuscript candidate for trusted review? | `[YES / NO / UNDECIDED - HUMAN TO CONFIRM]` | Current status permits trusted review with caveats. |
| Use manuscript candidate for partner/deck? | `[YES / NO / UNDECIDED - HUMAN TO CONFIRM]` | Current review keeps partner/deck use on Hold. |

## Final Human Approval Checklist

- [ ] Author metadata confirmed.
- [ ] All authors approved.
- [ ] Funding statement reviewed.
- [ ] Competing interests / conflict statement reviewed.
- [ ] Ethics statement reviewed.
- [ ] Data availability statement reviewed.
- [ ] Code availability statement reviewed.
- [ ] Dataset legal/licensing/redistribution status reviewed.
- [ ] References reviewed.
- [ ] Supplement reviewed.
- [ ] Export package reviewed.
- [ ] Claim-boundary audit reviewed.
- [ ] Leakage caveat reviewed.
- [ ] Public posting approved.

## Remaining Blocker Summary

Until this form is completed and reviewed, public preprint status remains **Hold / not submission-ready**.

This form does not resolve dataset attribution, licensing, redistribution, source-chain, label-source, metadata, disclosure, bibliography, supplement/export, or public posting approval blockers by itself.
