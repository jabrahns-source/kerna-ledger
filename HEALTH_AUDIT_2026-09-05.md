# Portfolio health audit — 2026-09-05

Owner: jabrahns-source (24 public repositories). Auditor: continuous repo-health automation.
Method: GitHub tree walk, size scan, artifact search (`node_modules`, `target/`, `__pycache__`, `.pyc`, `dist/`), CI/README/LICENSE/.gitignore presence.

## Artifact hygiene

Code search across `user:jabrahns-source` found **zero** committed `node_modules`, `target/`, `__pycache__`, `.pyc`, or `dist/` trees.

## Priority repos

| Repo | CI | LICENSE | README | tests/docs | Notes |
|------|----|---------|--------|------------|-------|
| Q-Reg | yes (2 workflows) | yes (custom/other) | yes | formal/ + python + rust runtime | Canonical engine. 31 open issues (historical). |
| kerna-ledger | yes | AGPL | yes | kerna_verify + cargo test | Citation root. Pointers documented. |
| kerna-ledger-vci | yes (5 workflows) | MIT | yes | hash/merkle/vera | Production packet path. |
| vera-enterprise-engine | yes | MIT | yes | src/vera_engine + tests | SaaS ledger. |
| phi-boundary-commitments | yes | MIT | yes | src + verification + paper | Untitled62.ipynb leftover name. |
| GridPulse | yes | MIT | yes | receipt.py + tests | Demo. |
| aethersound | yes | MIT | yes | rust + coq + ue5 + verifier | No Rust tests dir at crate root beyond lib. |
| psi-alpha-quantum | yes | MIT | yes | process_matrix + tests | |
| kerna-denali | yes | MIT | thin | receipt + tests | |
| denali-kerna-psi-demo | pages only | MIT | thin | static html + next pages | |
| kerna-ledger-verified | yes | MIT | yes | zig + idris examples | |

## Satellite / non-core

Healthy scaffolds: unignorable, pactkit, pactly (not re-walked in this pass beyond listing), hq-bind, siege-os, vera-packet-runtime, kerna-exact-matrix, aethersync, deepsignal, gemma4-coder-gguf-runner, denali-whitepaper, qreg-scratch-ci-test.

## Archive candidates

- **cyberpunk-web-daw**: empty product (README + LICENSE + ARCHIVE.md only). README now states archive recommendation. Audio work is aethersound.
- **qreg-scratch-ci-test**: scratch CI sandbox; keep private or archive after Q-Reg CI is trusted.

## Intentional stubs (not bugs)

`kerna-ledger` `qreg_engine.py` and `api/gridpulse_hf_master.py` are documented redirects to Q-Reg / GridPulse. Do not duplicate engines.

`KernaLedger.idr` is now a total Idris 2 *map* proving a unique compliance-engine role assignment. It is not a second GateLogic.

## Changes this pass

- `kerna-ledger`: typechecking umbrella Idris module; std-only FNV-1a daemon + tests.
- `cyberpunk-web-daw`: archive-forward README.
- This file.

## Remaining debt (do not inflate)

1. Idris 2 + Zig toolchains in GitHub-hosted CI (not present on ubuntu-latest by default).
2. License API still reports `NOASSERTION` on Q-Reg / kerna-ledger despite SPDX files.
3. Rename `Untitled62.ipynb` in phi-boundary-commitments.
4. Archive cyberpunk-web-daw and consider archiving qreg-scratch-ci-test.
5. Live CAISO ingest remains demo/stub across GridPulse / VCI.
6. Issue hygiene: Q-Reg (31) and kerna-ledger (22) have stale volume; close completed items.
