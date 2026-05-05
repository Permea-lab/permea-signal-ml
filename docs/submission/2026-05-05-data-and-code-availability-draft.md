# Data and Code Availability Draft - 2026-05-05

## Purpose

This draft proposes conservative candidate data and code availability wording for founder/manual review.

This is not a final availability statement. It does not make legal conclusions, approve public data release, authorize redistribution, finalize repository release policy, or make the public preprint submission-ready.

## Observed Repo Facts

- Remote URL in local repo: `https://github.com/Permea-lab/permea-signal-ml.git`.
- Branch: `master`.
- Latest local commit at SOD restore: `046b2d9 docs: add 2026-05-04 eod and 2026-05-05 sod handoff`.
- Dataset config: `configs/data/legacy_bbb_dataset_with_features.yaml`.
- Imported processed dataset path: `data/processed/legacy_bbb_dataset_with_features.csv`.
- Rerun-ready processed dataset path: `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`.
- Dataset version: `pending_confirmation`.
- Raw source dataset path: unresolved; `data/raw/` contains only `.gitkeep`.
- Dataset attribution, licensing, source terms, and redistribution permission remain unresolved in current docs.

## Separation of Code Availability and Data Availability

Code availability can be decided separately from data availability. A public code repository or code archive does not automatically grant permission to redistribute the processed dataset.

Data availability depends on source terms, attribution, licensing, redistribution permission, and founder/manual legal review. Do not state that processed dataset redistribution is permitted unless explicit documentation supports that decision.

## Conservative Candidate Wording - Code Availability

Candidate wording for founder/manual review:

```text
Code supporting the computational benchmark workflow is planned for release through an approved Permea repository or archive, pending final repository URL, commit, release tag, and license confirmation. The repository includes scripts, configuration files, documentation, and derived artifacts needed to inspect the benchmark package, subject to the dataset availability limitations described separately.
```

Required manual inputs:

- final repository URL
- final commit hash or release tag
- archive/DOI policy, if any
- software license statement
- repository visibility/public-release approval

## Conservative Candidate Wording - Data Availability

Candidate wording for founder/manual and legal review:

```text
The processed peptide dataset used for the current benchmark reruns is not approved for public redistribution in this draft because original source attribution, licensing, redistribution permission, raw source path, public dataset version, and label-source criteria remain pending confirmation. Derived benchmark artifacts, audit summaries, and code may be released where permitted and where they do not imply redistribution rights over the underlying dataset. Dataset provenance and label-source limitations are documented as limitations.
```

Required manual inputs:

- whether imported processed data can be public
- whether rerun-ready processed data can be public
- whether only derived artifacts can be public
- original dataset source and attribution
- dataset license or source terms
- final data availability route
- final contact route, if data will be available on request

## Alternative Data Availability Positions

### Option A - No Public Dataset Redistribution Yet

Use if licensing, source attribution, or redistribution permission remains unresolved. This is the current conservative default.

### Option B - Derived Artifacts Only

Use if processed dataset redistribution is not approved but figures, tables, audit summaries, and code can be shared without violating dataset restrictions.

### Option C - Data Available on Request

Use only if a founder/manual reviewer approves a contact route and sharing policy.

### Option D - Processed Dataset Public

Use only if source attribution, license, and redistribution permission are explicitly confirmed. This draft does not support choosing this option yet.

## Blockers Before Final Wording

- Dataset source attribution unresolved.
- Dataset license and source terms unresolved.
- Redistribution permission unresolved.
- Public dataset version unresolved.
- Label-source criteria unresolved.
- Final repository release tag/archive unresolved.
- Final code/data availability approval unresolved.

## Draft Verdict

**Hold / not submission-ready.**

The safest current availability path is code/derived-artifacts planning with processed-dataset redistribution withheld unless manual legal review explicitly approves redistribution.

## No-Change Confirmation

- No data files were modified.
- No result artifacts were modified.
- No figure artifacts were modified.
- `references.bib` was not modified.
- Manuscript scientific content was not modified.
- No legal certainty was invented.
- Public preprint remains **Hold / not submission-ready**.
