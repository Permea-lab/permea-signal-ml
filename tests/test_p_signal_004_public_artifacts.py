import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_FILES = [
    ROOT / "results/p_signal_004/calibration_summary.csv",
    ROOT / "results/p_signal_004/threshold_sweep_summary.csv",
    ROOT / "results/p_signal_004/prioritization_at_k_summary.csv",
    ROOT / "results/p_signal_004/fold_level_summary.csv",
    ROOT / "results/p_signal_004/calibration_threshold_run_manifest.json",
    ROOT / "docs/reports/p-signal-004-calibration-threshold-analysis.md",
]

CSV_FILES = EXPECTED_FILES[:4]

FORBIDDEN_COLUMNS = {
    "sequence",
    "sequence_id",
    "raw_sequence",
    "true_label",
    "label",
    "predicted_label",
    "prediction",
    "embedding",
    "group_id",
    "split_manifest",
    "private_path",
    "path",
}

PRIVATE_TERMS = [
    "/data/permea",
    "/Users/",
    "local_only",
    "permea-private-doctrine",
    "H100",
    "AI Champion",
    "K-EXAONE",
    "KORA",
    "model cache",
]

UNSUPPORTED_AFFIRMATIVE_CLAIMS = [
    "wet-lab validated",
    "in vivo validated",
    "clinical relevance",
    "therapeutic efficacy",
    "solved delivery",
    "universal delivery",
    "state-of-the-art",
    "SOTA",
    "dataset available",
    "download the dataset",
    "proves transport",
    "validated delivery",
    "biological transport proof",
]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_p_signal_004_expected_files_exist():
    for path in EXPECTED_FILES:
        assert path.is_file(), path


def test_p_signal_004_csv_files_parse_and_are_aggregate_only():
    for path in CSV_FILES:
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        assert rows, path
        assert not (FORBIDDEN_COLUMNS & set(rows[0])), path


def test_p_signal_004_manifest_boundary_flags():
    manifest = json.loads(
        (ROOT / "results/p_signal_004/calibration_threshold_run_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    assert manifest["row_level_public_release"] is False
    assert manifest["raw_sequences_public_release"] is False
    assert manifest["embeddings_public_release"] is False
    assert manifest["dataset_public_availability_claim"] is False
    assert manifest["public_export_scope"] == "aggregate_only"


def test_p_signal_004_public_files_have_no_private_paths_or_infra_terms():
    for path in EXPECTED_FILES:
        text = _read_text(path)
        for term in PRIVATE_TERMS:
            assert term not in text, (path, term)


def test_p_signal_004_report_has_required_values_and_boundary_language():
    report = _read_text(ROOT / "docs/reports/p-signal-004-calibration-threshold-analysis.md")
    for value in [
        "0.051176",
        "0.021510",
        "0.620665",
        "0.640569",
        "0.940000",
        "0.635688",
    ]:
        assert value in report

    lower = report.lower()
    for phrase in [
        "not biological validation",
        "before experimental validation",
        "aggregate",
        "candidate prioritization",
        "row-level predictions",
        "the dataset is not redistributed",
        "no dataset public availability claim",
    ]:
        assert phrase in lower


def test_p_signal_004_no_unsupported_affirmative_claims():
    combined = "\n".join(_read_text(path) for path in EXPECTED_FILES)
    lower = combined.lower()
    for claim in UNSUPPORTED_AFFIRMATIVE_CLAIMS:
        if claim in lower:
            assert f"not {claim}" in lower or f"no {claim}" in lower
