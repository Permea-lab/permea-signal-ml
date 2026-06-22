"""Validate the P-SIGNAL-002 dry-run boundary without loading models or data."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ALLOWED_MODEL_IDS = {
    "facebook/esm2_t6_8M_UR50D",
    "facebook/esm2_t12_35M_UR50D",
    "facebook/esm2_t30_150M_UR50D",
    "facebook/esm2_t33_650M_UR50D",
}
PRIMARY_RECOMMENDED_MODEL = "facebook/esm2_t12_35M_UR50D"
EXPECTED_DATASET_SHA = "2e8d3fc30becfdd00ad7cd25eedd5e6c00df7698747ea358b4cc97f4268f8abf"

REQUIRED_PRIVATE_ARTIFACTS = {
    "row-level dataset",
    "raw sequences",
    "split manifests",
    "group assignments",
    "row-level embeddings",
    "per-row predictions",
    "sequence-pair leakage files",
    "model cache paths",
    "H100 paths",
}
REQUIRED_PUBLIC_SAFE_ARTIFACTS = {
    "aggregate model-comparison metrics",
    "aggregate per-fold metrics",
    "aggregate leakage summary",
    "no-private-path run manifest",
    "claim-bounded report",
    "public tests confirming no row-level leakage",
}
UNSAFE_PUBLIC_TERMS = {
    "row-level dataset",
    "raw sequences",
    "split manifests",
    "group assignments",
    "row-level embeddings",
    "per-row predictions",
    "sequence-pair leakage files",
    "model cache paths",
    "H100 paths",
    "/data/permea",
    "/Users/",
    "local_only",
    "private path",
}
REQUIRED_STOP_CONDITIONS = {
    "dataset SHA mismatch",
    "repo dirty state",
    "wrong repo HEAD",
    "package import failure",
    "model download failure",
    "OOM or GPU failure",
    "leakage audit failure",
    "public/private boundary risk",
    "claim discipline risk",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate P-SIGNAL-002 dry-run metadata without model download or inference."
    )
    parser.add_argument("--config", required=True, help="Path to a dry-run JSON config.")
    return parser.parse_args()


def load_config(path: str | Path) -> dict[str, Any]:
    with Path(path).open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError("Config must be a JSON object")
    return payload


def require_string(payload: dict[str, Any], field: str) -> str:
    value = payload.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Missing or empty string field: {field}")
    return value


def require_string_list(payload: dict[str, Any], field: str) -> list[str]:
    value = payload.get(field)
    if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
        raise ValueError(f"Missing or invalid string list field: {field}")
    return value


def require_mapping(payload: dict[str, Any], field: str) -> dict[str, Any]:
    value = payload.get(field)
    if not isinstance(value, dict):
        raise ValueError(f"Missing or invalid object field: {field}")
    return value


def validate_no_private_path_literals(config_text: str) -> None:
    forbidden = ["/data/permea", "/Users/", "local_only", "permea-private-doctrine"]
    found = [term for term in forbidden if term in config_text]
    if found:
        raise ValueError(f"Config contains forbidden private path literal(s): {found}")


def validate_model(payload: dict[str, Any]) -> str:
    model_id = require_string(payload, "model_id")
    if model_id not in ALLOWED_MODEL_IDS:
        raise ValueError(f"Model ID is not in allowed ESM-2 plan-only IDs: {model_id}")
    recommended = require_string(payload, "primary_recommended_model")
    if recommended != PRIMARY_RECOMMENDED_MODEL:
        raise ValueError(f"Primary recommended model must be {PRIMARY_RECOMMENDED_MODEL}")
    if model_id != recommended:
        raise ValueError("Example dry-run config must represent the primary recommended model")
    return model_id


def validate_dataset_metadata(payload: dict[str, Any]) -> None:
    dataset_sha = require_string(payload, "expected_dataset_sha256")
    if dataset_sha != EXPECTED_DATASET_SHA:
        raise ValueError("Expected dataset SHA does not match the P-SIGNAL-001/P-SIGNAL-002 plan")
    placeholder = require_string(payload, "private_input_path_placeholder")
    if not (placeholder.startswith("<") and placeholder.endswith(">")):
        raise ValueError("Private input path must be represented as a placeholder")


def validate_boundaries(payload: dict[str, Any]) -> tuple[list[str], list[str]]:
    outputs = require_mapping(payload, "planned_output_families")
    private_outputs = outputs.get("private_outputs")
    public_safe_outputs = outputs.get("public_safe_aggregate_candidates")
    if not isinstance(private_outputs, list) or not all(isinstance(item, str) for item in private_outputs):
        raise ValueError("planned_output_families.private_outputs must be a list of strings")
    if not isinstance(public_safe_outputs, list) or not all(isinstance(item, str) for item in public_safe_outputs):
        raise ValueError("planned_output_families.public_safe_aggregate_candidates must be a list of strings")

    private_set = set(private_outputs)
    public_set = set(public_safe_outputs)
    missing_private = sorted(REQUIRED_PRIVATE_ARTIFACTS - private_set)
    missing_public = sorted(REQUIRED_PUBLIC_SAFE_ARTIFACTS - public_set)
    if missing_private:
        raise ValueError(f"Missing private-only artifact boundary item(s): {missing_private}")
    if missing_public:
        raise ValueError(f"Missing public-safe aggregate candidate item(s): {missing_public}")

    unsafe_public = sorted(term for term in UNSAFE_PUBLIC_TERMS if term in public_set)
    if unsafe_public:
        raise ValueError(f"Public-safe candidates include private or row-level artifact(s): {unsafe_public}")
    return private_outputs, public_safe_outputs


def validate_stop_conditions(payload: dict[str, Any]) -> list[str]:
    stop_conditions = require_string_list(payload, "stop_conditions")
    missing = sorted(REQUIRED_STOP_CONDITIONS - set(stop_conditions))
    if missing:
        raise ValueError(f"Missing stop condition(s): {missing}")
    return stop_conditions


def validate_claim_boundaries(payload: dict[str, Any]) -> None:
    non_claims = require_string_list(payload, "non_claims")
    forbidden_claims = {
        "wet-lab validation",
        "in-vivo validation",
        "clinical relevance",
        "therapeutic efficacy",
        "solved delivery",
        "state-of-the-art status",
        "dataset redistribution rights",
    }
    missing = sorted(forbidden_claims - set(non_claims))
    if missing:
        raise ValueError(f"Missing non-claim boundary item(s): {missing}")


def build_summary(
    payload: dict[str, Any],
    model_id: str,
    private_outputs: list[str],
    public_safe_outputs: list[str],
    stop_conditions: list[str],
) -> dict[str, Any]:
    return {
        "status": "ok",
        "task_id": payload.get("task_id"),
        "dry_run_only": True,
        "model_id": model_id,
        "expected_dataset_sha256": payload.get("expected_dataset_sha256"),
        "private_input_path_is_placeholder": True,
        "private_output_count": len(private_outputs),
        "public_safe_candidate_count": len(public_safe_outputs),
        "stop_condition_count": len(stop_conditions),
        "no_model_download": True,
        "no_model_load": True,
        "no_inference": True,
        "no_embeddings": True,
        "no_dataset_read": True,
    }


def validate_config(config_path: str | Path) -> dict[str, Any]:
    path = Path(config_path)
    config_text = path.read_text(encoding="utf-8")
    validate_no_private_path_literals(config_text)
    payload = load_config(path)

    if require_string(payload, "task_id") != "P-SIGNAL-002D":
        raise ValueError("task_id must be P-SIGNAL-002D")
    if payload.get("dry_run_only") is not True:
        raise ValueError("dry_run_only must be true")
    if payload.get("no_model_download") is not True:
        raise ValueError("no_model_download must be true")
    if payload.get("no_model_load") is not True:
        raise ValueError("no_model_load must be true")
    if payload.get("no_inference") is not True:
        raise ValueError("no_inference must be true")
    if payload.get("no_embeddings") is not True:
        raise ValueError("no_embeddings must be true")

    model_id = validate_model(payload)
    validate_dataset_metadata(payload)
    validate_claim_boundaries(payload)
    private_outputs, public_safe_outputs = validate_boundaries(payload)
    stop_conditions = validate_stop_conditions(payload)
    return build_summary(payload, model_id, private_outputs, public_safe_outputs, stop_conditions)


def main() -> int:
    args = parse_args()
    try:
        summary = validate_config(args.config)
    except Exception as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, indent=2), file=sys.stderr)
        return 1
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
