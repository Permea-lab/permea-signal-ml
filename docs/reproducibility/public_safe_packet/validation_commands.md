# Validation Commands

This file distinguishes public packet validation instructions from prior public validation baselines.

## Public Packet Validation Commands

Working directory: `Permea-lab/permea-signal-ml`

```bash
test -d docs/reproducibility/public_safe_packet
test -f docs/reproducibility/public_safe_packet/README.md
test -f docs/reproducibility/public_safe_packet/public_artifact_manifest.md
test -f docs/reproducibility/public_safe_packet/validation_commands.md
test -f docs/reproducibility/public_safe_packet/expected_output_summary.md
test -f docs/reproducibility/public_safe_packet/aggregate_result_checksum_shape_summary.md
test -f docs/reproducibility/public_safe_packet/figure_manifest_summary.md
test -f docs/reproducibility/public_safe_packet/claim_boundary_checklist.md
test -f docs/reproducibility/public_safe_packet/public_private_boundary_checklist.md
test -f docs/reproducibility/public_safe_packet/reviewer_walkthrough.md
test -f docs/reproducibility/public_safe_packet/reproducibility_packet_manifest.json
test -f docs/reproducibility/public_safe_packet/correction_manifest.json
python3 -m json.tool docs/reproducibility/public_safe_packet/reproducibility_packet_manifest.json >/tmp/p_repro_packet_manifest_check.json
python3 -m json.tool docs/reproducibility/public_safe_packet/correction_manifest.json >/tmp/p_repro_correction_manifest_check.json
grep -R "not a merged release" docs/reproducibility/public_safe_packet/README.md
grep -R "public dataset availability" docs/reproducibility/public_safe_packet/claim_boundary_checklist.md
grep -R "independent validation" docs/reproducibility/public_safe_packet/claim_boundary_checklist.md
grep -R "experimental validation" docs/reproducibility/public_safe_packet/claim_boundary_checklist.md
git diff --check
```

Expected result: public packet files exist, manifest JSON parses, required boundary phrases are present, and public repo diff whitespace check passes.

Working directory: `Permea-lab/permea-signal-ml`

| Command | Purpose | Prior validation result |
| --- | --- | --- |
| `python3 -m pytest tests/test_p_figure_004_public_figures.py -q` | Verify public figure manifest, files, and claim/boundary guards. | `5 passed` |
| `python3 -m pytest tests/test_p_signal_001_public_artifacts.py -q` | Verify P-SIGNAL-001 public aggregate artifacts. | `4 passed` |
| `python3 -m pytest tests/test_p_signal_002_dry_run_gate.py -q` | Verify dry-run guard behavior for P-SIGNAL-002. | `11 passed` |
| `python3 -m pytest tests/test_p_signal_002_public_artifacts.py -q` | Verify P-SIGNAL-002 public aggregate artifacts. | `8 passed` |
| `python3 -m pytest tests/test_p_signal_003_public_artifacts.py -q` | Verify P-SIGNAL-003 public aggregate artifacts. | `8 passed` |
| `python3 -m pytest tests/test_p_signal_004_public_artifacts.py -q` | Verify P-SIGNAL-004 public calibration/threshold artifacts. | `6 passed` |
| `python3 -m pytest tests -q` | Verify the full current public suite. | `71 passed`, 3 known scikit-learn warnings |

## Commands Documented As Prior Public Baseline

Working directory: `Permea-lab/permea-signal-ml`

| Command | Purpose | Expected result | Candidate baseline status |
| --- | --- | --- | --- |
| `python3 -m pytest tests/test_p_figure_004_public_figures.py -q` | Verify public figure manifest, files, and claim/boundary guards. | P-FIGURE-004 public figures: `5 passed`. | Previously verified baseline: `5 passed`. |
| `python3 -m pytest tests/test_p_signal_001_public_artifacts.py -q` | Verify P-SIGNAL-001 public aggregate artifacts. | P-SIGNAL-001 public artifacts: `4 passed`. | Previously verified baseline: `4 passed`. |
| `python3 -m pytest tests/test_p_signal_002_dry_run_gate.py -q` | Verify dry-run guard behavior for P-SIGNAL-002. | P-SIGNAL-002 dry-run gate: `11 passed`. | Previously verified baseline: `11 passed`. |
| `python3 -m pytest tests/test_p_signal_002_public_artifacts.py -q` | Verify P-SIGNAL-002 public aggregate artifacts. | P-SIGNAL-002 public artifacts: `8 passed`. | Previously verified baseline: `8 passed`. |
| `python3 -m pytest tests/test_p_signal_003_public_artifacts.py -q` | Verify P-SIGNAL-003 public aggregate artifacts. | P-SIGNAL-003 public artifacts: `8 passed`. | Previously verified baseline: `8 passed`. |
| `python3 -m pytest tests/test_p_signal_004_public_artifacts.py -q` | Verify P-SIGNAL-004 public calibration/threshold artifacts. | P-SIGNAL-004 public artifacts: `6 passed`. | Previously verified baseline: `6 passed`. |
| `python3 -m pytest tests -q` | Verify the full current public suite. | Full public suite: `71 passed`, with 3 known scikit-learn warnings. | Previously verified baseline: `71 passed`, 3 known scikit-learn warnings. |

## Commands Not Run In This Candidate Task

No dataset downloads, model runs, accelerator jobs, prediction recomputation, calibration recomputation, or threshold sweep recomputation are part of this task. Any command that would require those actions is outside scope and must not be treated as public packet validation.
