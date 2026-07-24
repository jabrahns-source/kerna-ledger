# Kerna-Ledger

**Deterministic Verifiable Compute Infrastructure for Grid Data, Emissions Integrity, and Sovereign Consent**

Even The Odds Foundry · Jacarri Sanders

---

## What this repository is

This is the high-level index and historical root for the Kerna-Ledger / VERA Substrata family.  
The **executable, formally-backed compliance engine** now lives in the dedicated sibling repository:

**→ https://github.com/jabrahns-source/Q-Reg**

Q-Reg contains:
- Fully functional deterministic gate engine (`qreg_engine.py`)
- Ed25519 sealing + SHA-256 Merkle chaining
- Clean-room verifier (`kerna_verify.py`)
- Adversarial test suite + remediation report generator
- Idris 2 formal proofs (Compliance, GateLogic, LinearLifecycle, Provenance, Moat, …)
- CI and Docker surface

## Related production surfaces

| Repo | Role |
|------|------|
| [Q-Reg](https://github.com/jabrahns-source/Q-Reg) | Core deterministic compliance runtime + formal proofs |
| [vera-enterprise-engine](https://github.com/jabrahns-source/vera-enterprise-engine) | Production-ready receipt ledger & metered SaaS engine |
| [phi-boundary-commitments](https://github.com/jabrahns-source/phi-boundary-commitments) | Golden-ratio polynomial state reduction + commitments |
| [kerna-ledger-vci](https://github.com/jabrahns-source/kerna-ledger-vci) | VCI / Denali / VERA protocol integration layer |
| [GridPulse](https://github.com/jabrahns-source/GridPulse) | Live Scope-2 receipt demo |
| [aethersound](https://github.com/jabrahns-source/aethersound) | Deterministic emotional audio engine |

## Design principles (non-negotiable)

- Deterministic, not probabilistic
- Formally verified decision procedures where possible (Idris 2 / dependent types)
- Cryptographic sealing (Ed25519) + tamper-evident Merkle provenance on every record
- Zero gatekeeping: runnable from a Chromebook, no credentials required to inspect or verify
- Built for SB 253 / CARB / CAISO realities and for pilot term-sheet readiness

## Status

- Core engine: **functional and testable** in Q-Reg (2026-07-24)
- This umbrella repo: cleaned of placeholders; acts as the stable entry point and citation root
- Continuous health automation runs daily across the entire foundry surface

## Contact / Foundry

Jacarri Sanders  
Even The Odds Foundry LLC  
GitHub: [@jabrahns-source](https://github.com/jabrahns-source)  
X: [@GirthyLengths95](https://x.com/GirthyLengths95)

---

Built under zero-budget, zero-gatekeeper constraints. The proofs and the ledger speak for themselves.
