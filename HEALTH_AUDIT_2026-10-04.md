# Estate health audit 2026-10-04

Scope: all 25 public repositories under `jabrahns-source`. Recursive trees. No build-artifact directories (`target/`, `node_modules/`, `__pycache__`, `dist/`, `*.pyc`) were present in any scanned default-branch tree.

## Changes this pass

- `denali-whitepaper`: replaced `.zenodo.json` description placeholder (`"..."`) with deposit-ready metadata. Structural test now rejects ellipsis and sub-80-character descriptions. Added `.github/workflows/ci.yml`.
- `gemma4-coder-gguf-runner`: added `tests/test_config.py` and `.github/workflows/ci.yml`. Weights stay out of git.

## Priority repos

| Repo | CI | LICENSE | README | Tests | Notes |
| --- | --- | --- | --- | --- | --- |
| Q-Reg | yes | yes (NOASSERTION SPDX file) | yes | yes | Canonical Python + Rust runtime. Idris skeletons are real modules, not one-line notes. |
| kerna-ledger | yes | yes, non-SPDX (35,314 bytes, license key other) | yes | yes | Umbrella. Do not duplicate engine logic. |
| kerna-ledger-vci | yes | MIT | yes | yes | Packet, hash, Merkle present. |
| vera-enterprise-engine | yes | MIT | yes | yes | Ledger + API modules present. |
| phi-boundary-commitments | yes | MIT | yes | yes | Notebook `Untitled62.ipynb` retained as source artifact; `notebooks/` has a pointer. |
| GridPulse | yes | MIT | yes | yes | Demo HTML + receipt.py. |
| aethersound | yes | MIT | yes | yes | Rust core + UE5 scaffold. Coq skeleton is a real file, proofs incomplete. |
| psi-alpha-quantum | yes | MIT | yes | yes | Process-matrix module present. |
| denali-whitepaper | yes (this pass) | MIT | yes | yes | DOI still not deposited. |
| denali-kerna-psi-demo | yes | MIT | yes | yes | Static demo + receipt module. |
| kerna-denali | yes | MIT | yes | yes | Receipt node. |

## Archive flags

- `cyberpunk-web-daw`: already archived. Leave archived.
- `qreg-scratch-ci-test`: scratch. `ARCHIVE.md` already says so. Flag for archive; do not treat as canonical. Engine lives in Q-Reg.

## Remaining debt

- Zenodo DOI for denali-whitepaper is metadata-ready, not deposited.
- `kerna-ledger` LICENSE is a long non-SPDX text. GitHub reports `NOASSERTION`. Needs a human SPDX decision (MIT vs custom).
- `Kerna_Vera_VCI` commits 126 `.grok/` skill files. Not a build artifact. Bloat, not deletion without an owner call.
- `aethersound` UE5 MetaSound graph and Coq proofs remain incomplete by README status.
- Formal Idris/Coq proofs across Q-Reg, phi-boundary, kerna-ledger-verified are skeletons with intent, not machine-checked in CI (Idris/Coq not installed in those workflows).
- `pactly` has no `tests/` directory. App code is present. Tests are debt, not a missing scaffold.
- No committed `node_modules`, `target`, or `__pycache__` found. Nothing deleted.
