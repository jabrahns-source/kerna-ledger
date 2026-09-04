# Kerna-Ledger Status (2026-09-04)

This repository is the **stable citation and index root** for the Kerna-Ledger / VERA family.

## Canonical locations

| Component | Repository |
|-----------|------------|
| Deterministic compliance engine + Idris 2 proofs | [Q-Reg](https://github.com/jabrahns-source/Q-Reg) |
| Formally verified Idris2 + Zig substrate | [kerna-ledger-verified](https://github.com/jabrahns-source/kerna-ledger-verified) |
| Production receipt ledger / SaaS engine | [vera-enterprise-engine](https://github.com/jabrahns-source/vera-enterprise-engine) |
| VCI / Denali / VERA packet integration | [kerna-ledger-vci](https://github.com/jabrahns-source/kerna-ledger-vci) |
| Zero-FPU exact matrix | [kerna-exact-matrix](https://github.com/jabrahns-source/kerna-exact-matrix) |
| Phi boundary commitments | [phi-boundary-commitments](https://github.com/jabrahns-source/phi-boundary-commitments) |
| Live demo | [GridPulse](https://github.com/jabrahns-source/GridPulse) |
| Process-matrix fairness | [psi-alpha-quantum](https://github.com/jabrahns-source/psi-alpha-quantum) |

## What is executable here

- `kerna_verify.py` + `tests/test_kerna_verify.py` — deterministic umbrella verifier (sampled integer checks only).
- `src/main.rs` — Cargo-valid umbrella daemon that prints the canonical map.
- CI: pytest + cargo check + artifact hygiene.
- License: AGPL-3.0-or-later (`LICENSE` + `SPDX-LICENSE-IDENTIFIER`).

## What is an intentional pointer (not a second engine)

- `qreg_engine.py`, `api/gridpulse_hf_master.py`, `KernaLedger.idr` redirect to Q-Reg / GridPulse.
- Duplicating the engine here would create divergence. Do not expand those files into a second runtime.

## Health notes (2026-09-04)

- No `target/`, `node_modules/`, `__pycache__/`, `.pyc`, or `dist/` committed.
- See `HEALTH_AUDIT_2026-09-04.md` for the 24-repo matrix.
- Remaining debt lives in sibling repos: Idris2 CI replay, license-API detection, CAISO live ingest, archive of scratch/empty repos.

Even The Odds Foundry — zero stochastic drift.
