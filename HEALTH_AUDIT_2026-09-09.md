# Health Audit — 2026-09-09

Owner: `jabrahns-source` (Even The Odds Foundry).
Scope: all 24 public repositories. Method: GitHub Search + recursive trees + file-size classification.
Policy lock: no second Q-Reg engine; no invented formal claims; no committed build artifacts.

## Inventory (24)

| Repo | CI | LICENSE | Tests | Artifacts | Verdict |
|------|----|---------|-------|-----------|---------|
| Q-Reg | ci + gridpulse-verification | LICENSE present (API=other) | test_vectors.py + verification/ + formal/ | none | HEALTHY core |
| kerna-ledger | ci | AGPL file | tests/test_kerna_verify.py | none | HEALTHY umbrella |
| kerna-ledger-vci | ci/pages/release/security/validate | MIT | tests + vera/ | none | HEALTHY |
| kerna-ledger-verified | ci + security | MIT | zig tests + Idris sketches | none | HEALTHY; Idris not on GHA |
| vera-enterprise-engine | ci | MIT | tests/test_ledger.py | none | HEALTHY |
| vera-packet-runtime | (prior pass) | yes | import-level | none | HEALTHY small |
| phi-boundary-commitments | ci | MIT | tests + verification | none | HEALTHY; root Untitled62.ipynb |
| GridPulse | ci | MIT | tests/test_receipt.py | none | HEALTHY demo |
| psi-alpha-quantum | family workflows | MIT | tests | none | HEALTHY thin |
| aethersound | ci + determinism | MIT | rust + coq + verifier | none | HEALTHY |
| kerna-denali | ci | MIT | tests | none | HEALTHY small |
| denali-whitepaper | (docs) | MIT | paper | none | HEALTHY docs |
| denali-kerna-psi-demo | (pages) | MIT | html | none | HEALTHY demo |
| kerna-exact-matrix | ci | MIT | proofs + examples | none | HEALTHY |
| hq-bind | ci | MIT | tests | none | HEALTHY small |
| unignorable | (prior) | MIT | tests | none | HEALTHY ops |
| aethersync | (prior) | MIT | tests | none | HEALTHY small |
| pactkit | (prior) | MIT | tests | none | HEALTHY small |
| pactly | (prior) | MIT | app | none | HEALTHY scaffold |
| deepsignal | (prior) | MIT | static | none | HEALTHY static |
| gemma4-coder-gguf-runner | docker | MIT | docker | none | HEALTHY infra |
| siege-os | (prior) | MIT | tests | none | HEALTHY small |
| qreg-scratch-ci-test | scratch | MIT | ARCHIVE.md | none | ARCHIVE candidate |
| cyberpunk-web-daw | none | MIT | ARCHIVE.md only | none | ARCHIVE |

## Placeholders / size < 200 B

- `kerna-ledger/qreg_engine.py` — **intentional documented redirect** to canonical Q-Reg. Not expanded (drift lock).
- Identifier / config crumbs: `Q-Reg/SPDX-LICENSE-IDENTIFIER`, short `requirements.txt`, pactkit `__main__.py` entry.
- `cyberpunk-web-daw` is four files (README + ARCHIVE + LICENSE + .gitignore). Do not populate.

No silent "API spec" / "Full updated…" note-only files found in trees inspected this pass.

## Committed build artifacts

Trees inspected this pass (Q-Reg, kerna-ledger, kerna-ledger-vci, vera-enterprise-engine, phi-boundary-commitments, GridPulse, aethersound, psi-alpha-quantum, kerna-ledger-verified, cyberpunk-web-daw, hq-bind, kerna-exact-matrix, kerna-denali): **zero** `target/`, `node_modules/`, `__pycache__`, `.pyc`, `dist/`.
CI jobs on Q-Reg and kerna-ledger fail if those paths appear.

## Remaining debt (unchanged class, not new breakage)

1. GitHub License API `NOASSERTION` on Q-Reg and kerna-ledger despite LICENSE files.
2. Idris2 proof replay is not executed on GitHub Actions (no Idris2 toolchain job).
3. `phi-boundary-commitments/Untitled62.ipynb` still at repo root.
4. Archive UI action still needed for `cyberpunk-web-daw` and `qreg-scratch-ci-test`.
5. Q-Reg open-issue pile is mostly historical health-audit duplicates (this pass consolidates onto #36).
6. Formal modules are source specifications; do not advertise CI-checked totality until a toolchain job exists.

## Actions this pass

- Re-fetched recursive trees for 13 core/priority repos.
- Confirmed Q-Reg engine, Merkle verifier, test vectors, and CI path are real (not stubs).
- Confirmed kerna-ledger `qreg_engine.py` remains an explicit redirect, not a silent placeholder.
- Wrote this audit artifact.
- Updated tracking issue; marked older Q-Reg health-audit issues as duplicates.

## Drift lock

- Do not fork `Q-Reg/qreg_engine.py` into the umbrella repo.
- Do not claim Idris2 is CI-checked.
- Do not resurrect `cyberpunk-web-daw`.

Even The Odds Foundry — deterministic audit, 2026-09-09.
