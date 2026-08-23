# Kerna-Ledger

[![CI](https://github.com/jabrahns-source/kerna-ledger/actions/workflows/gridpulse-narrative.yml/badge.svg)](https://github.com/jabrahns-source/kerna-ledger/actions)
[![License](https://img.shields.io/badge/license-AGPL--3.0-blue.svg)](LICENSE)
[![Even The Odds Foundry](https://img.shields.io/badge/Even%20The%20Odds-Foundry-black)](https://github.com/jabrahns-source)

**Deterministic Verifiable Compute Infrastructure for Grid-Arbitrage and SB 253 Compliance**

Author: Jacarri Sanders (Even The Odds Foundry)  
Canonical engines live in sibling repositories. This umbrella retains discoverability stubs and high-level specifications.

## Overview

Kerna-Ledger provides the mathematical and cryptographic substrate for deterministic, zero-stochastic-drift execution receipts on California grid data (CAISO), emissions integrity (SB 253 / CARB), and sovereign consent. It bridges algebraic polynomial reduction over the golden-ratio ring with integer-only ALU pipelines, formally verified gates, and Merkle-sealed ledgers.

Core guarantees:
- Zero floating-point drift
- Compile-time unrepresentable violations (via Idris 2 dependent types in formal siblings)
- Cryptographically sealed, auditable execution receipts
- Linear lifecycle + StarkNet-compatible ZK anchoring (see Q-Reg)

## Canonical Locations (Do Not Duplicate Logic Here)

| Component | Repository | Purpose |
|-----------|------------|---------|
| Q-Reg Engine | [jabrahns-source/Q-Reg](https://github.com/jabrahns-source/Q-Reg) | Formally verified deterministic compliance runtime, gate logic, Ed25519 + Merkle, CARB/SB 253 |
| GridPulse Demo | [jabrahns-source/GridPulse](https://github.com/jabrahns-source/GridPulse) | Live Scope-2 receipt + penalty clock demo |
| VERA Packet / Enterprise | [kerna-ledger-vci](https://github.com/jabrahns-source/kerna-ledger-vci), [vera-enterprise-engine](https://github.com/jabrahns-source/vera-enterprise-engine) | Verifiable Emission & Regulatory Artifact runtime + production ledger |
| Phi Boundary Commitments | [phi-boundary-commitments](https://github.com/jabrahns-source/phi-boundary-commitments) | Golden-ratio polynomial state reduction + formal verification |
| Denali Substrate | [kerna-denali](https://github.com/jabrahns-source/kerna-denali), [denali-whitepaper](https://github.com/jabrahns-source/denali-whitepaper) | Symbolic reasoning node + architecture whitepaper |

Stubs in this repo (`qreg_engine.py`, `api/gridpulse_hf_master.py`) intentionally redirect to the above. They exist solely for historical links and discoverability.

## Formal Verification

- `KernaLedger.idr` — core dependent-type sketch
- `kerna_verify.py` — Z3 / empirical proofs for golden-ratio ring exactness, Galois zero-divisor elimination, ICO Kraus cancellation, integer phase bounds
- Full Idris 2 proofs and Zig runtimes live in `kerna-ledger-verified` and related formal tracks

## Quick Start (Redirect)

```bash
# Preferred: clone the canonical engine
git clone https://github.com/jabrahns-source/Q-Reg.git
cd Q-Reg
python qreg_engine.py --demo
```

For GridPulse live demo:
```bash
git clone https://github.com/jabrahns-source/GridPulse.git
# open index.html or follow its README
```

## Repository Contents

- Specifications and whitepaper fragments
- Header / C bindings sketch (`kerna_ledger.h`)
- Cargo.toml scaffold for future Rust components
- Intentional redirect stubs
- STATUS.md and empirical reports

## Principles

- Deterministic only. No stochastic drift.
- Formal proofs first.
- Artifacts never committed (see `.gitignore`).
- Production-ready code or explicit, documented stubs — never silent placeholders.

## License

See LICENSE (AGPLv3 / dual where noted).

---

Even The Odds Foundry — continuous health automation keeps this map accurate.
