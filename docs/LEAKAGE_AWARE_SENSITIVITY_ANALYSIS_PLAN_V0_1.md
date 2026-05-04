# Leakage-Aware Sensitivity Analysis Plan v0.1

## Purpose

This plan defines possible leakage-aware sensitivity analyses for future benchmark robustness assessment of the current BBB-oriented Permea Signal ML benchmark.

This is a plan only. No leakage-aware split has been run, no leakage-aware metric has been generated, no baseline model has been rerun, and no metric value is changed by this document. Current metrics remain random-stratified baseline metrics under the reconstructed `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` policy. Public preprint status remains **Hold / not submission-ready** unless the human operator chooses an explicit caveat path after reviewing the remaining metadata, legal, bibliography, export, and leakage-sensitivity blockers.

Implementation pointer: `docs/LEAKAGE_AWARE_GROUPING_UTILITIES_V0_1.md` describes grouping utilities now available for future sensitivity work. Those utilities support in-memory exact duplicate, near-duplicate, k-mer Jaccard, combined similarity, and source-feasibility grouping. They do not generate split manifests, rerun models, or produce leakage-aware metrics.

Output pointer: `docs/LEAKAGE_AWARE_GROUP_ASSIGNMENT_OUTPUTS_V0_1.md` summarizes the first combined group assignment outputs generated under `results/sensitivity/`. Split manifests, baseline model reruns, and leakage-aware metrics have still not been generated.

## Current Leakage Evidence Summary

Current leakage evidence comes from `docs/LEAKAGE_AUDIT_REPORT_V0_1.md`, `docs/LEAKAGE_AUDIT_FINDINGS_INVESTIGATION_V0_1.md`, and the committed audit outputs in `results/audits/`.

| Evidence area | Current finding | Interpretation boundary |
|---|---:|---|
| Same-label exact duplicate groups crossing reconstructed folds | 4 groups | Duplicates are not label conflicts, but identical sequences appear across random-stratified folds. |
| Exact normalized sequence label-conflict groups | 0 groups | This does not validate labels or rule out other leakage modes. |
| Same-label near-duplicate pairs | 73 pairs | Similar sequence neighborhoods exist in the benchmark surface. |
| Near-duplicate pairs crossing reconstructed folds | 56 pairs | Random-stratified folds may place related peptides on both sides of train/test boundaries. |
| Same-label high k-mer Jaccard pairs | 33 pairs | High sequence-similarity structure exists under the current `k=3`, Jaccard `>=0.8` screen. |
| High-similarity pairs crossing reconstructed folds | 29 pairs | This is a direct benchmark-optimism risk for random-stratified reporting. |
| Source/group limitation | `source=legacy_bbb_import` spans all 5 folds | The current source field is too coarse for source-aware group split control. |
| Overall benchmark optimism risk | Moderate | Current metrics may be optimistic and should not be framed as robust generalization. |

## Sensitivity Analysis Strategies

### Option A - Exact Duplicate Group-Aware Split

Group records by normalized sequence before assigning folds.

Planned rules:

- normalize sequence strings using the same conservative normalization used by the leakage audit
- assign all identical normalized sequences to the same fold
- prevent identical normalized sequences from crossing train/test boundaries
- if an exact duplicate group contains conflicting labels, quarantine that group for human curation before model reruns

Limitation: this controls exact duplicates only. It does not address near-duplicate or high-similarity sequence neighborhoods.

### Option B - Near-Duplicate Graph Grouping

Create a sequence graph where each node is a unique normalized sequence and each edge connects sequences within a selected edit-distance threshold. Connected components become split groups.

Candidate thresholds:

- edit distance `<= 1`
- edit distance `<= 2`

Limitation: for short peptides, one or two edits can be proportionally large. Thresholds should be interpreted as sensitivity settings, not definitive biological similarity.

### Option C - k-mer Jaccard Similarity Grouping

Create a graph where nodes are unique normalized sequences and edges connect sequences whose k-mer Jaccard similarity meets a selected threshold. Connected components become split groups.

Candidate settings:

- `k=3`, Jaccard threshold `>= 0.9`
- `k=3`, Jaccard threshold `>= 0.8`

Limitation: k-mer grouping is heuristic and threshold-dependent. It may cluster motif-similar peptides without proving shared biological behavior.

### Option D - Combined Duplicate + Near-Duplicate + k-mer Grouping

Combine exact duplicate, edit-distance, and k-mer similarity edges into one graph, then use connected components as groups.

This is the highest leakage-control option among the sequence-only strategies because it prevents multiple similarity definitions from crossing folds.

Limitation: combined grouping may reduce effective fold diversity, alter class balance, or make some folds unstable if large connected components exist.

### Option E - Source/Group Split

Use source, assay, peptide family, literature source, dataset source, or another provenance-aware grouping column to define folds.

Current feasibility: not feasible with the current `source` field because the only observed value is `legacy_bbb_import`, and it spans all 5 reconstructed folds. A meaningful source/group split requires richer source, assay, family, or provenance metadata.

### Option F - Holdout Stress Test

Reserve high-similarity clusters as a stress holdout and compare random-stratified baseline behavior against a similarity-aware holdout.

Potential use:

- identify high-similarity connected components
- hold out selected components or sequence neighborhoods
- train on the remaining benchmark surface
- compare performance against current random-stratified baselines

Limitation: this is best treated as future v0.2 robustness work unless a narrowly scoped v0.1 sensitivity pass is explicitly approved.

## Proposed Model Rerun Comparison

Future sensitivity analysis should rerun existing baseline model families only:

- Dummy most-frequent
- Logistic Regression
- Random Forest

Do not add new model families in the first leakage-aware sensitivity pass. The goal is to compare split policy sensitivity, not to improve model performance.

Metrics to compare:

- ROC-AUC
- PR-AUC
- MCC
- class prior / baseline PR-AUC
- optional confidence intervals or fold dispersion if implemented later

All future outputs should clearly label the split policy and should not overwrite the current random-stratified baseline artifacts.

## Proposed Future Outputs

The following outputs may be created by a later implementation task. They do not exist as leakage-aware sensitivity outputs at the time of this plan.

| Planned output | Purpose |
|---|---|
| `results/sensitivity/leakage_aware_split_manifest.json` | Records grouping policy, thresholds, fold counts, class balance, and random seed. |
| `results/sensitivity/group_assignments.csv` | Maps sequence records to duplicate/similarity groups and leakage-aware folds. |
| `results/sensitivity/model_comparison_leakage_aware.csv` | Reports baseline model metrics under leakage-aware split policies. |
| `results/sensitivity/random_vs_leakage_aware_delta.csv` | Compares random-stratified metrics against leakage-aware metrics. |
| `results/sensitivity/leakage_aware_summary.json` | Machine-readable summary of policy, metrics, deltas, and caveats. |
| `docs/LEAKAGE_AWARE_SENSITIVITY_REPORT_V0_1.md` | Human-readable report interpreting the sensitivity analysis. |

## Interpretation Decision Rules

These rules apply only after future sensitivity outputs exist.

| Future outcome | Interpretation rule | Manuscript/public-use consequence |
|---|---|---|
| Performance remains similar | Treat current benchmark signal as more robust to the tested split policy, but still computational and not biological validation. | Report both split policies and preserve no-wet-lab and no-robust-generalization boundaries. |
| Performance drops moderately | Treat current random-stratified metrics as optimistic but still informative as baseline signal. | Report both random-stratified and leakage-aware metrics; emphasize sensitivity to split policy. |
| Performance collapses | Reframe v0.1 as a leakage-exposed baseline and prioritize dataset reconstruction. | Avoid public benchmark-strength claims; consider delaying bioRxiv or making leakage exposure the main result. |
| Split cannot be built reliably | Keep strong limitation language and defer leakage-aware robustness to v0.2. | Do not imply robustness; explain why metadata or grouping structure blocks a reliable sensitivity estimate. |

None of these outcomes would establish biological validation, wet-lab validation, therapeutic efficacy, clinical efficacy, or validated BBB delivery performance.

## bioRxiv v0.1 Decision Options

### Option 1 - Include Leakage-Aware Sensitivity Before bioRxiv

Advantages:

- stronger scientific package
- lower benchmark optimism concern
- clearer random-vs-leakage-aware comparison

Costs:

- delays posting
- requires implementation, model reruns, artifact generation, and manuscript updates

### Option 2 - Post v0.1 With Explicit Leakage Limitation

Advantages:

- faster public evidence release
- keeps current manuscript focused on random-stratified baseline evidence

Requirements:

- avoid stronger benchmark claims
- state that current metrics may be optimistic
- position v0.2 as leakage-aware follow-up
- preserve explicit no-biological-validation and no-robust-generalization wording

### Option 3 - Website-Only Preview First

Advantages:

- allows an internal or public evidence archive preview before formal bioRxiv posting
- keeps bioRxiv on Hold until leakage-aware sensitivity and human/legal blockers are resolved

Requirements:

- separate website claim-boundary review
- no public framing that implies submission readiness, robust generalization, or validated delivery

No final option is selected by this plan.

## Recommended Future Task Sequence

| Task | Purpose | Output |
|---|---|---|
| Task 075 - Commit Leakage-Aware Sensitivity Analysis Plan | Commit this planning artifact. | Committed plan and index updates. |
| Task 076 - Implement Leakage-Aware Grouping Utilities | Add grouping/split utilities without changing current baseline artifacts. | Utility code and tests. |
| Task 077 - Generate Leakage-Aware Split Manifests | Create duplicate/similarity-aware fold manifests. | Split manifests and group assignments. |
| Task 078 - Rerun Baseline Models Under Leakage-Aware Splits | Rerun Dummy, Logistic Regression, and Random Forest under approved split policies. | Sensitivity metrics and predictions. |
| Task 079 - Compare Random-Stratified vs Leakage-Aware Metrics | Compare metric deltas and split-policy effects. | Comparison tables and sensitivity report. |
| Task 080 - Update Manuscript Based on Sensitivity Results | Update manuscript only after sensitivity results exist. | Claim-bounded manuscript and supplement updates. |

## Human Decision Point

The human operator must decide whether bioRxiv v0.1 requires leakage-aware sensitivity before posting or whether explicit caveat language is acceptable for a bounded v0.1 release.

Codex can plan and later implement leakage-aware utilities if instructed. Codex should not choose the public-posting strategy automatically, should not rerun models in this task, and should not represent future sensitivity outputs as already generated.

## No-Change Confirmation

- No leakage-aware split was run.
- No leakage-aware metric was generated.
- Baseline models were not rerun.
- Benchmark metric values were not changed.
- Manuscript files were not modified.
- `references.bib` was not modified.
- Data files were not modified.
- Result artifacts were not modified.
- Figure artifacts were not modified.
- No leakage-free, robust-generalization, biological-validation, wet-lab-validation, therapeutic, or clinical claim is made.
