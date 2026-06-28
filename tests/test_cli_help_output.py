from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_help(script_name: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / script_name), "--help"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def test_audit_leakage_help_output_is_available() -> None:
    result = run_help("audit_leakage.py")

    assert result.returncode == 0, result.stderr
    assert "Run leakage-audit utilities" in result.stdout
    assert "--input" in result.stdout
    assert "--dry-run" in result.stdout
