from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "p_signal_002_dry_run.py"
CONFIG = ROOT / "configs" / "p_signal_002_dry_run.example.json"


def run_gate(config_path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--config", str(config_path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def write_config(tmp_path: Path, updates: dict[str, object]) -> Path:
    payload = json.loads(CONFIG.read_text(encoding="utf-8"))
    for key, value in updates.items():
        if value is None:
            payload.pop(key, None)
        else:
            payload[key] = value
    path = tmp_path / "config.json"
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def test_dry_run_script_passes_with_example_config() -> None:
    result = run_gate(CONFIG)

    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["status"] == "ok"
    assert payload["dry_run_only"] is True
    assert payload["model_id"] == "facebook/esm2_t12_35M_UR50D"
    assert payload["no_model_download"] is True
    assert payload["no_model_load"] is True
    assert payload["no_inference"] is True
    assert payload["no_embeddings"] is True


def test_fails_if_model_id_is_missing(tmp_path: Path) -> None:
    result = run_gate(write_config(tmp_path, {"model_id": None}))

    assert result.returncode != 0
    assert "model_id" in result.stderr


def test_fails_if_model_id_is_not_allowed(tmp_path: Path) -> None:
    result = run_gate(write_config(tmp_path, {"model_id": "example/not-approved"}))

    assert result.returncode != 0
    assert "not in allowed" in result.stderr


def test_fails_if_private_artifact_boundary_is_missing(tmp_path: Path) -> None:
    payload = json.loads(CONFIG.read_text(encoding="utf-8"))
    payload["planned_output_families"]["private_outputs"].remove("row-level dataset")
    path = tmp_path / "config.json"
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    result = run_gate(path)

    assert result.returncode != 0
    assert "Missing private-only artifact" in result.stderr


def test_fails_if_public_safe_list_contains_row_level_embeddings(tmp_path: Path) -> None:
    payload = json.loads(CONFIG.read_text(encoding="utf-8"))
    payload["planned_output_families"]["public_safe_aggregate_candidates"].append("row-level embeddings")
    path = tmp_path / "config.json"
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    result = run_gate(path)

    assert result.returncode != 0
    assert "row-level embeddings" in result.stderr


def test_fails_if_public_safe_list_contains_raw_sequences(tmp_path: Path) -> None:
    payload = json.loads(CONFIG.read_text(encoding="utf-8"))
    payload["planned_output_families"]["public_safe_aggregate_candidates"].append("raw sequences")
    path = tmp_path / "config.json"
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    result = run_gate(path)

    assert result.returncode != 0
    assert "raw sequences" in result.stderr


def test_fails_if_public_safe_list_contains_private_path_surfaces(tmp_path: Path) -> None:
    payload = json.loads(CONFIG.read_text(encoding="utf-8"))
    payload["planned_output_families"]["public_safe_aggregate_candidates"].append("H100 paths")
    path = tmp_path / "config.json"
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    result = run_gate(path)

    assert result.returncode != 0
    assert "H100 paths" in result.stderr


def test_script_source_does_not_contain_model_loading_or_transformer_imports() -> None:
    text = SCRIPT.read_text(encoding="utf-8")

    assert "from_pretrained" not in text
    assert "import transformers" not in text
    assert "from transformers" not in text


def test_example_config_contains_no_concrete_private_paths_or_private_data() -> None:
    text = CONFIG.read_text(encoding="utf-8")

    assert "/data/permea" not in text
    assert "/Users/" not in text
    assert "local_only" not in text
    assert "permea-private-doctrine" not in text
    assert "<PRIVATE_DATASET_PATH>" in text
    assert "<PRIVATE_RUN_DIR>" in text


def test_example_config_preserves_split_caveats() -> None:
    payload = json.loads(CONFIG.read_text(encoding="utf-8"))
    split_policy = payload["split_policy"]

    assert split_policy["max_pairs"] == 10000
    assert "too coarse" in split_policy["source_aware_limitation"]


def test_example_config_contains_no_affirmative_unsupported_public_claims() -> None:
    text = CONFIG.read_text(encoding="utf-8")
    affirmative_claims = [
        "wet-lab validated",
        "in vivo",
        "clinically relevant",
        "therapeutically effective",
        "solved biological delivery",
        "universal delivery",
        "state-of-the-art performance",
        "SOTA",
        "dataset available",
        "download the dataset",
    ]

    for claim in affirmative_claims:
        assert claim not in text

    payload = json.loads(text)
    assert "clinical relevance" in payload["non_claims"]
    assert "therapeutic efficacy" in payload["non_claims"]
    assert "solved delivery" in payload["non_claims"]
    assert "state-of-the-art status" in payload["non_claims"]
