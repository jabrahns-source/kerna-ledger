# Kerna-Ledger Status (2026-09-17)

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
| Deterministic audio | [aethersound](https://github.com/jabrahns-source/aethersound) |
| Denali substrate node | [kerna-denali](https://github.com/jabrahns-source/kerna-denali) |

## What is executable here

- `kerna_verify.py` + `tests/test_kerna_verify.py` — deterministic umbrella verifier.
- `src/main.rs` — Cargo-valid umbrella daemon that prints the canonical map.
- CI: pytest + cargo check + artifact hygiene.
- License: AGPL-3.0-or-later on disk. GitHub License API still reports NOASSERTION — UI picker debt.

## What is an intentional pointer (not a second engine)

- `qreg_engine.py`, `api/gridpulse_hf_master.py` redirect to Q-Reg / GridPulse.
- Duplicating the engine here would create divergence. Do not expand those files into a second runtime.

## Health notes (2026-09-17)

- 24 owner repos audited. **Zero** committed `target/`, `node_modules/`, `__pycache__`, `.pyc`, or `dist/`.
- No raw placeholder notes ("API spec" / "Full updated...") remain as sole file content.
- See `HEALTH_AUDIT_2026-09-17.md` for the full matrix.
- Archive candidates unchanged: `cyberpunk-web-daw`, `qreg-scratch-ci-test`.
- Remaining debt: Idris2 CI replay, GitHub license-API detection, historical notebook name, stale issue sweep, CAISO live ingest.

Even The Odds Foundry — zero stochastic drift.
