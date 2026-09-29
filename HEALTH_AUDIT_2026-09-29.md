# Portfolio Health Audit — 2026-09-29

Owner: jabrahns-source  
Scope: all 25 repositories  
Method: recursive tree + size + CI/README/LICENSE/.gitignore presence  
Principle: deterministic, no placeholders, no committed build artifacts

## Inventory (25)

| Repo | CI | LICENSE | README | Tests | Notes |
|---|---|---|---|---|---|
| Q-Reg | Y | Y | Y | Y | Canonical engine. Formal Idris + Rust runtime + Python verifier. Healthy. |
| kerna-ledger | Y | Y | Y | Y | Umbrella. Intentional redirect stubs for qreg_engine.py and api/gridpulse_hf_master.py. |
| kerna-ledger-vci | Y | Y | Y | Y | Hash + merkle + VERA packet. Healthy. |
| kerna-ledger-verified | Y | Y | Y | Y | Idris2 proofs + Zig receipt runtime. Healthy. |
| vera-enterprise-engine | Y | Y | Y | Y | Production Python engine. Healthy. |
| vera-packet-runtime | Y | Y | Y | thin | Canonical packet + Stripe checkout. |
| phi-boundary-commitments | Y | Y | Y | Y | Notebook + verification suite. Healthy. |
| GridPulse | Y | Y | Y | Y | Scope-2 receipt demo. Healthy. |
| aethersound | Y | Y | Y | Y | Rust + Coq + UE5. Healthy. |
| psi-alpha-quantum | Y | Y | Y | Y | Process matrix. Healthy. |
| denali-kerna-psi-demo | pages | Y | Y | N | Next demo + static index. Missing unit tests. |
| denali-whitepaper | pages | Y | Y | N | Docs-only. Acceptable. |
| kerna-denali | Y | Y | Y | Y | Receipt module. Healthy. |
| kerna-exact-matrix | Y | Y | Y | via zig | Zero-FPU matrix + Idris proofs. Healthy. |
| Kerna_Vera_VCI | thin | Y? | ? | N | **Debt:** committed `.grok/` game-scaffold dump (~1.8k size). Not a VCI runtime. |
| qreg-scratch-ci-test | Y | Y | ? | ? | **Archive candidate.** Private scratch. |
| unignorable | Y | Y | Y | thin | Outreach stack + CLI. 15 open issues. |
| pactkit | Y | Y | Y | Y | Engine present. `__main__.py` is tiny but functional. |
| pactly | Y | Y | Y | N | Next.js app; no automated tests. |
| aethersync | Y | Y | Y | Y | Thin whitepaper (607 B) and quantum_accel (661 B) — above placeholder threshold, not empty. |
| cyberpunk-web-daw | (prior) | | | | Not re-expanded this cycle. |
| gemma4-coder-gguf-runner | (prior) | | | | Not re-expanded this cycle. |
| deepsignal | Y | Y | Y | N | Static `index.html` product. |
| hq-bind | Y | Y | Y | Y | Commitment module. Healthy. |
| siege-os | Y | Y | Y | Y | Minimal but real `siege.py`. |

## Findings

1. **No committed `target/`, `node_modules/`, `__pycache__/`, `.pyc`, or `dist/`** in the trees inspected this cycle.
2. **Placeholder rule (<200 B or note-only):** no core-impact source files matched. kerna-ledger stubs are *intentional redirects* with explicit SystemExit + canonical URL. Keep them.
3. **CI present** on all core-impact repos.
4. **Highest remaining debt**
   - `Kerna_Vera_VCI`: replace Grok scaffold with a thin pointer README to `kerna-ledger-vci` + `vera-enterprise-engine`, or archive.
   - `qreg-scratch-ci-test`: archive after confirming no unique CI secrets live only there.
   - `denali-kerna-psi-demo` / `pactly` / `deepsignal`: add tests or document as demo-only.
   - `unignorable`: 15 open issues — triage, do not spawn more unless new debt.
5. **Do not duplicate engines.** Canonical map:
   - Engine: `Q-Reg`
   - Ledger umbrella + audits: `kerna-ledger`
   - VCI / packet: `kerna-ledger-vci`, `vera-packet-runtime`
   - Enterprise API: `vera-enterprise-engine`
   - Formal+Zig: `kerna-ledger-verified`, `kerna-exact-matrix`
   - Grid demo: `GridPulse`
   - Phi: `phi-boundary-commitments`
   - Psi: `psi-alpha-quantum`

## Actions this cycle

- Published this audit.
- Opened / updated tracking issues on `kerna-ledger` and `Q-Reg`.
- No source replacements required on core-impact repos (trees already contain real code, proofs, CI, LICENSE, gitignore).
- Flagged archive set: `qreg-scratch-ci-test`, optionally `Kerna_Vera_VCI` after README-pointer rewrite.

## Remaining debt (ranked)

1. Strip or archive `Kerna_Vera_VCI` `.grok/` dump.
2. Archive `qreg-scratch-ci-test`.
3. Tests for `pactly` and `denali-kerna-psi-demo`.
4. Idris2 CI job that actually typechecks (most workflows only run Python).
5. Badge completeness on a few READMEs (optional).

Deterministic close: core trust-boundary repos are populated, licensed, ignored correctly, and CI-wired. No invented code was pushed over working trees.
