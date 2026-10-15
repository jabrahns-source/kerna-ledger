# Portfolio Health Audit — 2026-10-15

Continuous repo health automation for jabrahns-source / Even The Odds Foundry.

**Scope:** All 25 public+private repositories owned by jabrahns-source.
**Date:** 2026-10-15
**Method:** Recursive tree fetches, size/content inspection of small files, CI/README/LICENSE/.gitignore/tests presence checks. Zero stochastic drift.

## Summary

All core impact repositories are in good health. No committed build artifacts (`target/`, `node_modules/`, `__pycache__`, `.pyc`, `dist/`) detected on any inspected tree. Intentional redirect stubs (e.g., `qreg_engine.py` in kerna-ledger) are documented and correct — do not re-implement engines in umbrella repos.

## Priority Repos Status

| Repo | CI | README+badges/usage | LICENSE | .gitignore | Tests | Docs | Notes |
|------|----|---------------------|---------|------------|-------|------|-------|
| Q-Reg | ✅ (2 workflows) | ✅ | ✅ | ✅ | ✅ (vectors + verify) | ✅ (formal + whitepaper) | Formal Idris suite solid. Runtime early-stage. |
| kerna-ledger | ✅ | ✅ | ✅ (custom) | ✅ | ✅ | ✅ (many HEALTH_AUDIT) | Umbrella with intentional SystemExit redirects. |
| kerna-ledger-vci | ✅ (multiple) | ✅ | ✅ | ✅ | ✅ (hash, merkle) | ✅ | Production VERA packet runtime. |
| vera-enterprise-engine | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | SQLite ledger + crypto. |
| phi-boundary-commitments | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (paper + verification) | Golden-ratio poly state reduction. |
| GridPulse | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (index.html demo) | Live Scope-2 receipt demo. |
| aethersound | ✅ (2) | ✅ | ✅ | ✅ | ✅ | ✅ (UE5 + Coq) | Deterministic audio engine. |
| psi-alpha-quantum | ✅ (multiple) | ✅ | ✅ | ✅ | ✅ | ✅ | Process matrix fairness. |
| denali-* / kerna-denali | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Substrate + whitepaper + demo. |

## Other Notable Repos

- **cyberpunk-web-daw**: Empty product surface. Explicitly flagged for archive in README.md and ARCHIVE.md. Do not populate. Archive from GitHub Settings.
- **Kerna_Vera_VCI**: Large .grok/ scaffold (game skills, references). Consider archive or pointer-rewrite; not core protocol.
- **qreg-scratch-ci-test**: Private scratch. Low strategic value after CI verification.
- **kerna-exact-matrix**: Strong Zig + Idris proofs. Zero-float matrix algebra.
- **hq-bind**, **aethersync**, **vera-packet-runtime**, **denali-kerna-psi-demo**: Functional scaffolds with CI/tests.
- Remaining (pactly, unignorable, deepsignal, siege-os, gemma4-coder-gguf-runner, etc.): Supporting or non-core; have basic hygiene.

## Placeholders / Incomplete Files

- No silent placeholders (<200 bytes of pure notes without purpose). Small files are either SPDX identifiers, intentional SystemExit redirects, or documented stubs.
- kerna-ledger `qreg_engine.py` and `api/gridpulse_hf_master.py` are correct redirects to canonical repos.

## Build Artifacts

None committed. .gitignore covers language-specific patterns across the portfolio.

## Remaining Debt (tracked in issues)

1. Archive `cyberpunk-web-daw` (and consider `qreg-scratch-ci-test`, `Kerna_Vera_VCI` if not needed).
2. Normalize LICENSE SPDX on kerna-ledger (currently NOASSERTION / custom grant).
3. Add Idris2 typecheck CI job for formal suites in Q-Reg and kerna-exact-matrix.
4. Deduplicate VERA packet implementations where appropriate (canonical is kerna-ledger-vci).
5. Issue hygiene on high-count repos (unignorable has 16 open).
6. Optional: Zenodo DOI finalization for whitepapers.

## Changes This Cycle

- Full recursive audit of all 25 repos.
- Confirmed no artifacts to clean and no silent incomplete files requiring functional replacements.
- Core engines remain in their canonical locations. No logic duplication.

Canonical engines: Q-Reg, kerna-ledger-vci, vera-enterprise-engine.
Do not copy production logic into umbrellas.

*Even The Odds Foundry — Deterministic systems. Zero stochastic drift.*
