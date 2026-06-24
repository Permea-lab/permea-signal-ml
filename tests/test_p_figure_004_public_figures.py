import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURE_DIR = ROOT / "figures/p_signal_figures"

EXPECTED_FILES = [
    FIGURE_DIR / "README.md",
    FIGURE_DIR / "figure_01_workflow_release_boundary.svg",
    FIGURE_DIR / "figure_01_workflow_release_boundary.png",
    FIGURE_DIR / "figure_02_aggregate_performance_comparison.svg",
    FIGURE_DIR / "figure_02_aggregate_performance_comparison.png",
    FIGURE_DIR / "figure_03_non_monotonic_classifier_interaction.svg",
    FIGURE_DIR / "figure_03_non_monotonic_classifier_interaction.png",
    FIGURE_DIR / "figure_04_calibration_threshold_operating_summary.svg",
    FIGURE_DIR / "figure_04_calibration_threshold_operating_summary.png",
    FIGURE_DIR / "figure_05_prioritization_at_k_summary.svg",
    FIGURE_DIR / "figure_05_prioritization_at_k_summary.png",
    FIGURE_DIR / "figure_06_source_lineage_overlap_risk.svg",
    FIGURE_DIR / "figure_06_source_lineage_overlap_risk.png",
    FIGURE_DIR / "figure_manifest.json",
    ROOT / "docs/reports/p-figure-004-public-safe-figure-export.md",
]

TEXT_FILES = [
    path
    for path in EXPECTED_FILES
    if path.suffix in {".md", ".svg", ".json"}
]

PRIVATE_TERMS = [
    "/Users/albertkim",
    "/data/permea",
    "local_only",
    "permea-private-doctrine",
    "H100",
    "AI Champion",
    "K-EXAONE",
    "KORA",
    "model cache",
]

ROW_LEVEL_TERMS = [
    "sequence_id",
    "raw_sequence",
    "true_label",
    "predicted_label",
    "embedding_vector",
    "group_id",
    "split_manifest",
    "private_path",
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
    "downloadable benchmark",
    "proves transport",
    "validated delivery",
    "biological transport proof",
    "deployment-grade",
    "independent validation achieved",
    "external validation achieved",
]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_p_figure_004_expected_files_exist_and_are_non_empty():
    for path in EXPECTED_FILES:
        assert path.is_file(), path
        assert path.stat().st_size > 0, path


def test_p_figure_004_manifest_parses_and_records_boundaries():
    manifest = json.loads((FIGURE_DIR / "figure_manifest.json").read_text(encoding="utf-8"))
    assert manifest["task_id"] == "P-FIGURE-004"
    assert manifest["not_final_publication_figures"] is True
    assert manifest["row_level_public_release"] is False
    assert manifest["raw_peptide_records_included"] is False
    assert manifest["row_level_labels_included"] is False
    assert manifest["row_level_predictions_included"] is False
    assert manifest["representation_matrices_included"] is False
    assert manifest["fold_assignment_records_included"] is False
    assert manifest["group_assignments_included"] is False
    assert manifest["public_dataset_availability_claim"] is False
    assert manifest["independent_validation_claim"] is False
    assert manifest["experimental_validation_claim"] is False
    assert len(manifest["exported_files"]) == 12


def test_p_figure_004_no_private_paths_or_row_level_terms():
    combined = "\n".join(_read_text(path) for path in TEXT_FILES)
    for term in PRIVATE_TERMS + ROW_LEVEL_TERMS:
        assert term not in combined, term


def test_p_figure_004_no_unsupported_affirmative_claims():
    combined = "\n".join(_read_text(path) for path in TEXT_FILES)
    lower = combined.lower()
    for claim in UNSUPPORTED_AFFIRMATIVE_CLAIMS:
        assert claim.lower() not in lower, claim


def test_p_figure_004_required_public_safe_boundary_language_present():
    combined = "\n".join(_read_text(path) for path in TEXT_FILES).lower()
    for phrase in [
        "aggregate benchmark-label evaluation",
        "aggregate-only",
        "candidate prioritization before experimental validation",
        "metadata-level source context",
        "no public dataset availability claim",
        "no experimental validation claim",
        "no independent validation claim",
        "not final publication figures",
    ]:
        assert phrase in combined
