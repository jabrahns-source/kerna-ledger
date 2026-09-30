# Portfolio Health Audit — 2026-09-30

Owner: jabrahns-source  
Scope: all 25 repositories  
Method: recursive GitHub trees, size thresholds, CI/README/LICENSE/.gitignore, issue scan  
Principle: deterministic, no invented engines, no placeholders masquerading as production code

## Inventory (25)

| Repo | CI | LICENSE | README | Tests | Verdict |
|---|---|---|---|---|---|
| Q-Reg | Y | Y | Y | Y | Canonical engine. Formal Idris + Rust runtime + Python verifier. Healthy. |
| kerna-ledger | Y | Y | Y | Y | Umbrella. Intentional redirect stubs only. |
| kerna-ledger-vci | Y | Y | Y | Y | Hash + merkle + VERA packet. Healthy. |
| kerna-ledger-verified | Y | Y | Y | Y | Formal/Zig track (prior cycle). |
| vera-enterprise-engine | Y | Y | Y | Y | Production Python API + ledger. Healthy. |
| vera-packet-runtime | Y | Y | Y | thin | Packet + Stripe checkout. |
| phi-boundary-commitments | Y | Y | Y | Y | Verification suite present. |
| GridPulse | Y | Y | Y | Y | Scope-2 receipt demo. Healthy. |
| aethersound | Y | Y | Y | Y | Rust + Coq + UE5. Healthy. |
| psi-alpha-quantum | Y | Y | Y | Y | Process matrix. Healthy. |
| denali-kerna-psi-demo | pages+ci* | Y | Y | Y* | *CI + node tests added this cycle. |
| denali-whitepaper | pages | Y | Y | N | Docs-only. Acceptable. |
| kerna-denali | Y | Y | Y | Y | Receipt module. Healthy. |
| kerna-exact-matrix | Y | Y | Y | zig | Zero-FPU + Idris proofs. Healthy. |
| Kerna_Vera_VCI | thin | Y | ? | N | **Debt:** committed `.grok/` scaffold dump. Archive or pointer-rewrite. |
| qreg-scratch-ci-test | Y | Y | ? | ? | **Archive candidate.** Private scratch. |
| unignorable | Y | Y | Y | thin | 16 open issues. Do not spawn more. |
| pactkit | Y | Y | Y | Y | Engine present. |
| pactly | Y | Y | Y | N | Next.js; no unit tests. |
| aethersync | Y | Y | Y | Y | Thin but above placeholder threshold. |
| cyberpunk-web-daw | prior | | | | Not re-expanded. |
| gemma4-coder-gguf-runner | prior | | | | Not re-expanded. |
| deepsignal | Y | Y | Y | N | Static product page. |
| hq-bind | Y | Y | Y | Y | Commitment module. |
| siege-os | Y | Y | Y | Y | Minimal real `siege.py`. |

## Findings this cycle

1. **No committed `target/`, `node_modules/`, `__pycache__/`, `.pyc`, or `dist/`** in priority trees.
2. **Placeholder rule:** core-impact source files are either real implementations or *documented redirects* (`kerna-ledger/qreg_engine.py`, `api/gridpulse_hf_master.py`, `api/vercel_index.py`). Those redirects raise SystemExit with the canonical URL. Keep them; do not duplicate Q-Reg here.
3. **CI** present on all core-impact repos except the docs-only whitepaper (pages workflow only) and the demo (pages only — fixed this cycle).
4. **Kerna_Vera_VCI** remains the largest hygiene problem: a Grok game-scaffold dump, not a VCI runtime. Canonical VCI is `kerna-ledger-vci` + `vera-enterprise-engine`. Do not copy engines into it.
5. **Idris2 typecheck is still not in CI** for most formal trees. Python/Zig/Rust jobs run; Idris jobs do not. Tracked as remaining debt.

## Canonical map (do not fork)

- Engine: `Q-Reg`
- Umbrella + audits: `kerna-ledger`
- VCI / packet: `kerna-ledger-vci`, `vera-packet-runtime`
- Enterprise API: `vera-enterprise-engine`
- Formal + Zig: `kerna-ledger-verified`, `kerna-exact-matrix`
- Grid demo: `GridPulse`
- Phi: `phi-boundary-commitments`
- Psi: `psi-alpha-quantum`
- Denali receipt: `kerna-denali`

## Actions this cycle

- Published this audit.
- Added Node CI + deterministic receipt tests to `denali-kerna-psi-demo`.
- Updated tracking issue on `kerna-ledger`.
- Did **not** overwrite working engines. Did **not** invent a second Q-Reg.

## Remaining debt (ranked)

1. Strip or archive `Kerna_Vera_VCI` `.grok/` dump; leave a pointer README.
2. Archive `qreg-scratch-ci-test` after secret check.
3. Tests for `pactly` and `deepsignal` or mark demo-only in README.
4. Idris2 CI typecheck job on `Q-Reg/formal` and `kerna-exact-matrix/proofs`.
5. `unignorable` issue triage (16 open) — hygiene, not new features.

Deterministic close: core trust-boundary repos are populated, licensed, ignored correctly, and CI-wired. Remaining work is archive/hygiene, not missing engines.
