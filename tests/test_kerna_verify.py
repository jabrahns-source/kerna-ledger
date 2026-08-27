"""Deterministic tests for the umbrella verifier. No Z3 required."""

import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_verifier_exits_zero():
    r = subprocess.run(
        [sys.executable, str(ROOT / "kerna_verify.py")],
        capture_output=True,
        text=True,
        check=False,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "MASTER_HASH" in r.stdout
    assert "PASS" in r.stdout


def test_verifier_hash_is_deterministic():
    runs = []
    for _ in range(2):
        r = subprocess.run(
            [sys.executable, str(ROOT / "kerna_verify.py")],
            capture_output=True,
            text=True,
            check=True,
        )
        line = [ln for ln in r.stdout.splitlines() if ln.startswith("MASTER_HASH")][0]
        runs.append(line)
    assert runs[0] == runs[1]


def test_redirect_stubs_are_explicit():
    qreg = (ROOT / "qreg_engine.py").read_text(encoding="utf-8")
    assert "Q-Reg" in qreg
    assert "raise SystemExit" in qreg
