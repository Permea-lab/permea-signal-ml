# Public Artifact Manifest

Status: public export candidate manifest for aggregate artifacts only.

## Public Repositories

| Repo | Public-safe repository reference | Baseline commit | Read/write status in Task 133 |
| --- | --- | --- | --- |
| permea-core | `Permea-lab/permea-core` | `e6ed1b53c25103f73a82710cdb22d6f2bd65aa6c` | Read-only; no edits. |
| permea-signal-ml | `Permea-lab/permea-signal-ml` | `8ea31ddf3f5f70319b8a275753980ce11cfea3cc` | Read-only; no edits. |

## Artifact Classes

- Aggregate result reports
- Aggregate CSV/JSON summaries
- Public-safe figures
- Figure manifests
- Validation tests

## Discovered Artifacts

| Path | Repo | Purpose | Public/private safety status | Aggregate data only |
| --- | --- | --- | --- | --- |
| `docs/reports/p-signal-001-leakage-controlled-physchem-baseline.md` | permea-signal-ml | P-SIGNAL-001 aggregate report. | Public-safe report. | Yes. |
| `results/p_signal_001/physchem_baseline_model_comparison.csv` | permea-signal-ml | Aggregate model comparison. | Public-safe aggregate CSV. | Yes. |
| `results/p_signal_001/physchem_baseline_per_fold_metrics.csv` | permea-signal-ml | Aggregate fold metrics. | Public-safe aggregate CSV. | Yes. |
| `results/p_signal_001/physchem_baseline_leakage_summary.json` | permea-signal-ml | Aggregate leakage summary. | Public-safe aggregate JSON. | Yes. |
| `results/p_signal_001/physchem_baseline_run_manifest.json` | permea-signal-ml | Public-safe run metadata. | Public-safe manifest. | Yes. |
| `docs/reports/p-signal-002-esm2-embedding-comparison.md` | permea-signal-ml | P-SIGNAL-002 aggregate report. | Public-safe report. | Yes. |
| `results/p_signal_002/esm2_embedding_model_comparison.csv` | permea-signal-ml | Aggregate model comparison. | Public-safe aggregate CSV. | Yes. |
| `results/p_signal_002/esm2_embedding_per_fold_metrics.csv` | permea-signal-ml | Aggregate fold metrics. | Public-safe aggregate CSV. | Yes. |
| `results/p_signal_002/esm2_embedding_leakage_summary.json` | permea-signal-ml | Aggregate leakage summary. | Public-safe aggregate JSON. | Yes. |
| `results/p_signal_002/esm2_embedding_run_manifest.json` | permea-signal-ml | Public-safe run metadata. | Public-safe manifest. | Yes. |
| `docs/reports/p-signal-003-esm2-150m-embedding-comparison.md` | permea-signal-ml | P-SIGNAL-003 aggregate report. | Public-safe report. | Yes. |
| `results/p_signal_003/esm2_t30_150m_model_comparison.csv` | permea-signal-ml | Aggregate model comparison. | Public-safe aggregate CSV. | Yes. |
| `results/p_signal_003/esm2_t30_150m_per_fold_metrics.csv` | permea-signal-ml | Aggregate fold metrics. | Public-safe aggregate CSV. | Yes. |
| `results/p_signal_003/esm2_t30_150m_leakage_summary.json` | permea-signal-ml | Aggregate leakage summary. | Public-safe aggregate JSON. | Yes. |
| `results/p_signal_003/esm2_t30_150m_run_manifest.json` | permea-signal-ml | Public-safe run metadata. | Public-safe manifest. | Yes. |
| `docs/reports/p-signal-004-calibration-threshold-analysis.md` | permea-signal-ml | P-SIGNAL-004 aggregate report. | Public-safe report. | Yes. |
| `results/p_signal_004/calibration_summary.csv` | permea-signal-ml | Aggregate calibration summary. | Public-safe aggregate CSV. | Yes. |
| `results/p_signal_004/threshold_sweep_summary.csv` | permea-signal-ml | Aggregate threshold summary. | Public-safe aggregate CSV. | Yes. |
| `results/p_signal_004/prioritization_at_k_summary.csv` | permea-signal-ml | Aggregate prioritization summary. | Public-safe aggregate CSV. | Yes. |
| `results/p_signal_004/fold_level_summary.csv` | permea-signal-ml | Aggregate fold calibration summary. | Public-safe aggregate CSV. | Yes. |
| `results/p_signal_004/calibration_threshold_run_manifest.json` | permea-signal-ml | Public-safe calibration and threshold manifest. | Public-safe manifest. | Yes. |
| `docs/reports/p-figure-004-public-safe-figure-export.md` | permea-signal-ml | Public-safe figure export report. | Public-safe report. | Yes. |
| `figures/p_signal_figures/README.md` | permea-signal-ml | Public figure README. | Public-safe figure documentation. | Yes. |
| `figures/p_signal_figures/figure_manifest.json` | permea-signal-ml | Public figure manifest. | Public-safe manifest. | Yes. |
| `figures/p_signal_figures/figure_01_workflow_release_boundary.svg` | permea-signal-ml | Workflow and release-boundary figure, SVG. | Public-safe figure. | Yes. |
| `figures/p_signal_figures/figure_01_workflow_release_boundary.png` | permea-signal-ml | Workflow and release-boundary figure, PNG. | Public-safe figure. | Yes. |
| `figures/p_signal_figures/figure_02_aggregate_performance_comparison.svg` | permea-signal-ml | Aggregate performance figure, SVG. | Public-safe figure. | Yes. |
| `figures/p_signal_figures/figure_02_aggregate_performance_comparison.png` | permea-signal-ml | Aggregate performance figure, PNG. | Public-safe figure. | Yes. |
| `figures/p_signal_figures/figure_03_non_monotonic_classifier_interaction.svg` | permea-signal-ml | Aggregate representation/classifier interaction figure, SVG. | Public-safe figure. | Yes. |
| `figures/p_signal_figures/figure_03_non_monotonic_classifier_interaction.png` | permea-signal-ml | Aggregate representation/classifier interaction figure, PNG. | Public-safe figure. | Yes. |
| `figures/p_signal_figures/figure_04_calibration_threshold_operating_summary.svg` | permea-signal-ml | Aggregate calibration and threshold figure, SVG. | Public-safe figure. | Yes. |
| `figures/p_signal_figures/figure_04_calibration_threshold_operating_summary.png` | permea-signal-ml | Aggregate calibration and threshold figure, PNG. | Public-safe figure. | Yes. |
| `figures/p_signal_figures/figure_05_prioritization_at_k_summary.svg` | permea-signal-ml | Aggregate top-k prioritization figure, SVG. | Public-safe figure. | Yes. |
| `figures/p_signal_figures/figure_05_prioritization_at_k_summary.png` | permea-signal-ml | Aggregate top-k prioritization figure, PNG. | Public-safe figure. | Yes. |
| `figures/p_signal_figures/figure_06_source_lineage_overlap_risk.svg` | permea-signal-ml | Metadata-level source lineage figure, SVG. | Public-safe figure. | Yes. |
| `figures/p_signal_figures/figure_06_source_lineage_overlap_risk.png` | permea-signal-ml | Metadata-level source lineage figure, PNG. | Public-safe figure. | Yes. |
| `tests/test_p_signal_001_public_artifacts.py` | permea-signal-ml | P-SIGNAL-001 public artifact tests. | Public-safe validation code. | N/A. |
| `tests/test_p_signal_002_dry_run_gate.py` | permea-signal-ml | P-SIGNAL-002 dry-run boundary tests. | Public-safe validation code. | N/A. |
| `tests/test_p_signal_002_public_artifacts.py` | permea-signal-ml | P-SIGNAL-002 public artifact tests. | Public-safe validation code. | N/A. |
| `tests/test_p_signal_003_public_artifacts.py` | permea-signal-ml | P-SIGNAL-003 public artifact tests. | Public-safe validation code. | N/A. |
| `tests/test_p_signal_004_public_artifacts.py` | permea-signal-ml | P-SIGNAL-004 public artifact tests. | Public-safe validation code. | N/A. |
| `tests/test_p_figure_004_public_figures.py` | permea-signal-ml | P-FIGURE-004 public figure tests. | Public-safe validation code. | N/A. |

## Unresolved / Not Found

None for the controlling public aggregate inventory. No new paths were invented for this corrected candidate.
