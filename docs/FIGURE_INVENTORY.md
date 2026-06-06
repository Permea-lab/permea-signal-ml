# Figure Inventory

## Figure Classification

- **Aggregate-only**: Summary benchmark visualizations derived from aggregate metrics or benchmark outputs.
- **Workflow-only**: Figures describing repository workflows, processing pipelines, or artifact generation paths.
- **Row-derived**: Figures derived from row-level outputs or rankings that may require additional review before external reuse.

## Claim Boundaries

Figures in this repository are computational benchmark artifacts and support materials.

They should not be interpreted as:

- Wet-lab validation
- Clinical evidence
- Candidate efficacy proof
- Public release approval for row-level artifacts

Where provenance or generation context is uncertain, figures should be marked for review rather than interpreted beyond their documented source context.

| Figure filename | Purpose | Data source | Figure Type | Suitable use | Limitations / Non-Claims |
|---|---|---|---|---|---|
| `figures/dataset_distribution.png` | Show initial class balance of the onboarded BBB dataset | Documented dataset counts used for onboarding (`2959`, `269`, `2690`) | Aggregate-only | repo, docs, paper-support, deck | Does not demonstrate model performance, biological validation, or clinical relevance | 
| `figures/legacy_vs_rerun_metrics.png` | Compare imported legacy benchmark metrics against regenerated rerun metrics | `results/metrics/legacy_benchmark_ml_results.csv`, regenerated metrics JSON files |Aggregate-only | repo, docs, paper-support, deck | Comparison artifact only; does not imply biological validation, clinical relevance, or candidate efficacy |
| `figures/legacy_rf_feature_importance_chart.png` | Show imported RF feature-importance values in a clean chart | `results/tables/legacy_rf_feature_importance.csv` |Aggregate-only | repo, docs, paper-support, deck |Feature-importance visualization only; does not imply causality or biological validation| 
| `figures/candidate_ranking_preview.png` | Preview top-ranked candidates from regenerated RF ranking output | `results/tables/legacy_bbb_rf_v01_ranking.csv` | Row-derived | repo, docs, paper-support, deck | Ranking preview only; does not imply biological validation, efficacy, or release approval | 
| `figures/benchmark_workflow_outputs.png` | Show repository workflow from imported artifacts to benchmark outputs | Repository structure and current output contract | Workflow-only | repo, docs, paper-support, deck | Does not represent benchmark performance or biological validation | 
| `figures/legacy_bbb_dummy_v01_score_distribution.png` | Score distribution for imported legacy dummy baseline output | Legacy benchmark artifacts | Aggregate-only | repo, docs, paper-support, deck |Distribution summary only; does not imply model validity or biological validation | 
| `figures/legacy_bbb_lr_v01_score_distribution.png` | Score distribution for imported logistic-regression benchmark output | Legacy benchmark artifacts |Aggregate-only | repo, docs, paper-support, deck |Distribution summary only; does not imply model validity or biological validation | 
| `figures/legacy_bbb_rf_v01_score_distribution.png` | Score distribution for imported random-forest benchmark output | Legacy benchmark artifacts |Aggregate-only | repo, docs, paper-support, deck |Distribution summary only; does not imply model validity or biological validation | 
| `figures/legacy_rf_feature_importance.png` | Imported random-forest feature importance visualization | Legacy benchmark artifacts |Aggregate-only | repo, docs, paper-support, deck | Feature-importance visualization only; does not imply causality or biological validation | 
| `figures/regenerated_rf_feature_importance.png` | Regenerated random-forest feature importance visualization from rerun workflow | Regenerated benchmark outputs | Aggregate-only | repo, docs, paper-support, deck |Feature-importance visualization only; does not imply causality or biological validation | 
| `figures/smoke_test_rf_score_distribution.png` | Random-forest score distribution generated during smoke-test validation workflow | Smoke-test workflow outputs | Aggregate-only |repo, docs, paper-support, deck | Smoke-test artifact only; does not imply benchmark validity or biological validation |
