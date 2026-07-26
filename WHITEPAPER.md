# Kerna-Ledger Whitepaper

**Deterministic Verifiable Compute Infrastructure for Grid-Arbitrage, Emissions Integrity and Sovereign Consent**

Even The Odds Foundry · 2026

## Executive Summary

Kerna-Ledger is the architectural substrate underlying the Q-Reg compliance runtime, the VERA enterprise engine, and the Denali gate logic. It provides a formally grounded, cryptographically sealed, and independently verifiable compute fabric optimised for California grid data (CAISO), SB 253 emissions reporting, and self-sovereign data governance.

This document is the stable citation root. Executable implementations and formal proofs live in the sibling repositories listed below.

## Design Invariants

1. **Determinism** — every decision is a pure function of its inputs; no stochastic components in the critical path.
2. **Formal verifiability** — where possible, properties are proven in Idris 2 (dependent types) so illegal states are unrepresentable.
3. **Cryptographic provenance** — every record is Ed25519-sealed and SHA-256 Merkle-chained.
4. **Zero-trust verification** — any third party can recompute the entire ledger from public data and the clean-room verifier.
5. **Regulatory grounding** — gate logic and report formats map directly onto CARB MRR, Title 17 CCR, SB 253, and Delete Act requirements.

## Repository Map

| Repository | Role |
|------------|------|
| Q-Reg | Core deterministic compliance engine + Idris proofs |
| vera-enterprise-engine | Production receipt ledger & metered SaaS runtime |
| kerna-ledger-vci | VCI / Denali / VERA protocol integration |
| phi-boundary-commitments | Golden-ratio polynomial state reduction |
| GridPulse | Live Scope-2 receipt demonstration |

## Status

The umbrella repository has been cleaned of placeholders. All production surfaces are maintained in the dedicated repositories above. Continuous health automation audits the entire foundry surface daily.

## Citation

When citing the Kerna-Ledger architecture, reference this whitepaper together with the formal proofs in Q-Reg and the empirical validation reports in the respective runtime repositories.

---

© 2026 Even The Odds Foundry. All rights reserved under the licenses of the individual component repositories.
