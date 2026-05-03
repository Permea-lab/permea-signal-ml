# Dataset Provenance and Label-Source Checklist v0.1

## Purpose

This checklist records dataset provenance, label-source, and licensing status for the current `permea-signal-ml` evidence package.

It does not add new data, validate biological labels, resolve unconfirmed provenance, add benchmark results, or expand scientific claims. It is intended to support trusted review and preprint-readiness planning by separating what is file-verified, what is documented, and what remains unresolved.

## Current dataset status summary

- Current evidence surface: `legacy_bbb_dataset_with_features`
- Raw dataset path status: no raw source dataset file is present in `data/raw/`; only `.gitkeep` is present there.
- Imported processed dataset path: `data/processed/legacy_bbb_dataset_with_features.csv`
- Current rerun-ready processed dataset path: `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`
- Dataset config path: `configs/data/legacy_bbb_dataset_with_features.yaml`
- Dataset version status: `pending_confirmation`
- Confirmed row count: 2,959 data rows in both processed CSV files, based on file line counts excluding the header row.
- Confirmed rerun-ready fields: `sequence_id`, `sequence`, `label`, `length`, `charge`, `gravy`, `pI`, `aromaticity`, `source`.
- Pending confirmation items: public dataset version identifier, source attribution, license or redistribution rights, original label-source criteria, and duplicate/near-duplicate/sequence-similarity leakage status.

## Confirmed fields table

| Field | Status | Evidence source | Notes |
|---|---|---|---|
| `sequence` | confirmed | `data/processed/legacy_bbb_dataset_with_features.csv`; `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`; `configs/data/legacy_bbb_dataset_with_features.yaml` | Sequence input field for current benchmark reruns. |
| `label` | confirmed | Processed CSV headers; dataset config; `scripts/run_baseline.py` | Current supervised benchmark target. Original label-source criteria remain unresolved. |
| `length` | confirmed | Processed CSV headers; `docs/BBB_PROVENANCE_RECOVERY.md`; feature config and rerun docs | Sequence-derived physicochemical feature. |
| `charge` | confirmed | Processed CSV headers; `docs/BBB_PROVENANCE_RECOVERY.md`; feature config and rerun docs | Sequence-derived physicochemical feature. |
| `gravy` | confirmed | Processed CSV headers; `docs/BBB_PROVENANCE_RECOVERY.md`; feature config and rerun docs | Sequence-derived physicochemical feature. |
| `pI` | confirmed | Processed CSV headers; `docs/BBB_PROVENANCE_RECOVERY.md`; feature config and rerun docs | Sequence-derived physicochemical feature. |
| `aromaticity` | confirmed | Processed CSV headers; `docs/BBB_PROVENANCE_RECOVERY.md`; feature config and rerun docs | Sequence-derived physicochemical feature. |
| `sequence_id` | confirmed | Rerun-ready CSV header; dataset config; `scripts/run_baseline.py` | Deterministic operational identifier added for rerun readiness. Not present in the imported processed CSV. |
| `source` | confirmed | Rerun-ready CSV header; dataset config; `scripts/run_baseline.py` | Operational source label added for rerun readiness. Current value documents imported legacy continuity, not original upstream attribution. |

## Provenance checklist

| Item | Current status | Evidence source | Preprint requirement | Required action | Blocking level |
|---|---|---|---|---|---|
| Raw dataset path | unresolved | `data/raw/` contains no source dataset file beyond `.gitkeep`; `docs/BBB_PROVENANCE_RECOVERY.md` references legacy raw paths from inspected legacy code | Raw source must be archived, referenced, or explicitly disclosed as unavailable | Locate source files or document absence and recovery basis | Blocks public preprint unless disclosed |
| Processed/current dataset path | confirmed | `data/processed/legacy_bbb_dataset_with_features.csv`; `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`; dataset config | Public docs should state both imported processed and rerun-ready paths | Keep paths visible in dataset docs and supplement | Does not block trusted review |
| Dataset version identifier | unresolved | Dataset config and manifests use `pending_confirmation` | Public version label must be confirmed or explicitly disclosed as pending | Resolve version naming or retain explicit limitation | Blocks public preprint |
| Original source attribution | unresolved | `docs/BBB_PROVENANCE_RECOVERY.md` recovers legacy filename hints but not publication metadata | Attribution or citation must be confirmed before public release | Recover upstream source or state unresolved status | Blocks public preprint |
| License / redistribution rights | unresolved | `data/README.md`; `docs/DATASET.md`; no license terms found for the dataset | Redistribution status must be confirmed before public dataset release | Confirm license or avoid redistributing beyond current repo scope | Blocks public preprint/data release |
| Dataset construction history | partially documented | `docs/BBB_PROVENANCE_RECOVERY.md` | Public docs should explain imported processed data and rerun-ready augmentation | Add concise construction summary and caveats | Blocks public preprint if omitted |
| Row count | confirmed | `wc -l` on processed CSV files gives 2,960 lines including header | State as 2,959 data rows | Keep row count tied to current files | Does not block trusted review |
| Feature fields | confirmed | CSV headers; feature recovery doc; scripts | State fields and source of feature recovery | Keep field table current | Does not block trusted review |
| Sequence ID policy | confirmed for rerun-ready file | Dataset config; rerun-ready CSV | Public docs should say this is operational metadata | Keep separate from original source metadata | Does not block trusted review |
| Source field definition | partially documented | Dataset config notes conservative `legacy_bbb_import` value | Public docs should not treat `source` as original upstream attribution | Clarify operational meaning | Blocks public preprint if overread |
| Imported vs regenerated distinction | documented | `docs/IMPORTED_VS_REGENERATED.md`; evidence package; artifact traceability report | Preserve distinction in public docs | Keep current wording | Does not block trusted review |

## Label-source checklist

| Item | Current status | Evidence source | Preprint requirement | Required action | Blocking level |
|---|---|---|---|---|---|
| Label field definition | partially documented | Dataset config; `docs/DATASET.md`; `scripts/run_baseline.py` | Define as current binary benchmark target, not independently verified truth | Keep benchmark-target wording | Does not block trusted review |
| Positive-class meaning | partially recovered | `docs/BBB_PROVENANCE_RECOVERY.md` reports legacy positive input file assignment to `label = 1` | Public docs need original source and meaning if recoverable | Recover original source criteria or disclose unresolved status | Blocks public preprint |
| Negative-class meaning | partially recovered | `docs/BBB_PROVENANCE_RECOVERY.md` reports legacy negative input file assignment to `label = 0` | Public docs need original source and meaning if recoverable | Recover original source criteria or disclose unresolved status | Blocks public preprint |
| Original label assignment criteria | unresolved | No current repo doc confirms assay, literature, or benchmark inclusion criteria | Criteria must be recovered or limitation must be prominent | Create label-source note after source recovery | Blocks public preprint |
| Original assay or benchmark source | unresolved | Legacy filenames suggest B3Pred dataset inputs, but current repo does not confirm upstream source metadata | Public docs need citation/source basis or explicit unresolved statement | Resolve attribution/source chain | Blocks public preprint |
| Label curation process | unresolved | No curation note found in current repo | Public docs should not imply independent curation | Document absence or recover curation details | Blocks public preprint if implied |
| Class imbalance context | documented | Manuscript, evidence docs, generated dataset distribution figure | Keep PR-AUC and baseline context visible | No immediate action | Does not block trusted review |
| Label limitation statement | documented | `docs/DATASET.md`; `docs/PREPRINT_DRAFT_V0_1.md` | Preserve in manuscript and supplement | No immediate action | Does not block trusted review |
| Biological validation boundary | documented | Manuscript and review-operation docs | Must remain explicit | No immediate action | Blocks public use if weakened |

## Licensing and redistribution status

Known:

- The project has a repository `LICENSE` file, but that does not establish dataset-specific licensing or redistribution rights.
- `data/README.md` states that source licensing constraints and attribution requirements should be respected.
- Current dataset config and docs explicitly keep dataset version, attribution, and licensing as pending or unresolved.

Unknown:

- Original upstream dataset license terms.
- Whether the processed dataset may be redistributed publicly.
- Required citation, attribution, or reuse conditions.
- Whether a public preprint supplement may include the current processed dataset tables directly.

What cannot be claimed:

- Complete provenance.
- Complete licensing.
- Unrestricted redistribution rights.
- Public dataset-release readiness.
- Biological validation of labels.

Before public preprint or public dataset release, the operator must either confirm source attribution and redistribution rights or keep dataset availability language constrained to what can be safely disclosed.

## Reviewer-facing caveat language

Suggested reusable language:

- "The current evidence package documents the recovered benchmark surface, while original dataset attribution and redistribution status remain pending confirmation."
- "The label field is used as the current benchmark target; the original label-source criteria require further documentation before public preprint finalization."
- "The rerun-ready dataset path is documented in the repository, but the public dataset version identifier remains `pending_confirmation`."
- "These limitations do not prevent trusted technical review, but they remain preprint-readiness blockers."

## Preprint-readiness decision

Status: Not yet.

Reason: the current repository now documents the processed dataset paths, rerun-ready path, row count, feature fields, operational `sequence_id`, and operational `source` field more clearly. However, public preprint readiness still requires either resolution or explicit final disclosure of dataset version, source attribution, license or redistribution status, original label-source criteria, and leakage-audit status.

## Recommended next action

Recommended next action: draft leakage audit plan.

The dataset path and field documentation is now clearer, but public preprint readiness still depends on leakage-risk handling in addition to provenance and label-source closure.

