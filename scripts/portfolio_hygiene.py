#!/usr/bin/env python3
"""Deterministic local hygiene contract for Even The Odds Foundry trees.

This does not call GitHub. It scans a checkout (or a path list) and fails
if committed build artifacts or note-only stubs are present.

Usage:
    python3 scripts/portfolio_hygiene.py /path/to/repo
"""

from __future__ import annotations

import sys
from pathlib import Path

ARTIFACT_PARTS = {
    "node_modules",
    "__pycache__",
    "target",
    "dist",
    ".vercel",
}
ARTIFACT_SUFFIXES = {".pyc", ".pyo"}
NOTE_MARKERS = (
    "api spec",
    "full updated",
    "todo: implement",
    "placeholder only",
)


def scan(root: Path) -> list[str]:
    failures: list[str] = []
    if not root.is_dir():
        return [f"not a directory: {root}"]
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        parts = set(rel.parts)
        if parts & ARTIFACT_PARTS or path.suffix in ARTIFACT_SUFFIXES:
            failures.append(f"artifact:{rel}")
            continue
        if path.stat().st_size >= 200:
            continue
        if path.name in {".gitignore", "SPDX-LICENSE-IDENTIFIER", "requirements.txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace").lower()
        if any(marker in text for marker in NOTE_MARKERS):
            failures.append(f"note-stub:{rel}")
    return failures


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: portfolio_hygiene.py <repo-root>", file=sys.stderr)
        return 2
    failures = scan(Path(argv[1]))
    if failures:
        for item in failures:
            print(item)
        return 1
    print("hygiene-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
