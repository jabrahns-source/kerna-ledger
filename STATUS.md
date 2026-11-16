# Kerna-Ledger Status (2026-11-16)

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

## Health notes (2026-11-16)

- 28 owner repos audited (`user:jabrahns-source`, total_count=28).
- Core protocol trees healthy: Q-Reg, kerna-ledger, kerna-ledger-vci, vera-enterprise-engine, phi-boundary-commitments, GridPulse, aethersound, psi-alpha-quantum, denali-* all have CI, LICENSE, README with usage, tests, .gitignore, no committed build artifacts (target/, node_modules/, __pycache__, .pyc, dist/).
- No incomplete/placeholder files <200B that are mere notes; small files are intentional (SPDX, redirects, LICENSE headers).
- Redirect stubs confirmed as SystemExit pointers.
- Archive candidates: `cyberpunk-web-daw` (ARCHIVE.md present, no source), `qreg-scratch-ci-test` (scratch with ARCHIVE.md).
- Residual debt: GitHub License API NOASSERTION on some repos despite on-disk LICENSE; optional Idris2 totality CI in Q-Reg; pin claims to benchmark harness; .vercel or .grok scaffolding in Kerna_Vera_VCI may need cleanup if not intentional.
- Zero stochastic drift. Portfolio green for deterministic Kerna/VERA principles.

Even The Odds Foundry — zero stochastic drift.
