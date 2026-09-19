# Portfolio Health Audit — 2026-09-19

Owner: jabrahns-source / Even The Odds Foundry  
Scope: all 25 public repositories. Method: recursive tree inspection, size/placeholder scan, artifact scan, CI/README/LICENSE/.gitignore presence.

## Executive verdict

Core protocol repos (Q-Reg, kerna-ledger-vci, vera-enterprise-engine, phi-boundary-commitments, GridPulse, aethersound, psi-alpha-quantum, kerna-denali, hq-bind, vera-packet-runtime) have LICENSE, README, .gitignore, tests, and GitHub Actions. They are **not empty**. Remaining debt is duplication, umbrella stubs, issue backlog, and one large committed Vercel output tree.

## Inventory (25 repos)

| Repo | Size KB | Lang | CI | LICENSE | README | Tests | Artifacts | Notes |
|---|---:|---|---|---|---|---|---|---|
| Kerna_Vera_VCI | 1835 | JS | no | no | no | some | **.vercel/output committed** | Grok scaffold + real `src/lib/qreg` |
| kerna-ledger | 115 | Py/Rust | yes | yes | yes | yes | no | umbrella + daily audits; qreg_engine.py is a redirect stub |
| vera-packet-runtime | 12 | Py | yes | yes | yes | yes | no | thin but functional packet |
| phi-boundary-commitments | 46 | Py/nb | yes | yes | yes | yes | no | Untitled62.ipynb leftover name |
| unignorable | 53 | Py | ? | ? | ? | ? | — | satellite |
| aethersound | 46 | Rust/C++ | yes | yes | yes | yes | no | Rust core + UE5 bindings |
| qreg-scratch-ci-test | 15 | Py | yes | yes | yes | thin | no | ARCHIVE.md; stubs <200B |
| cyberpunk-web-daw | 3 | — | no | yes | yes | no | no | ARCHIVE.md — archive candidate |
| Q-Reg | 106 | Py/Rust/Idris | yes | yes | yes | yes | no | canonical engine |
| denali-kerna-psi-demo | 10 | HTML | ? | ? | ? | ? | — | demo |
| aethersync | 13 | Py | ? | ? | ? | ? | — | satellite |
| kerna-ledger-verified | 25 | Zig | ? | ? | ? | ? | — | Zig substrate |
| pactkit | 6 | Py | ? | ? | ? | ? | — | product satellite |
| GridPulse | 12 | HTML/Py | yes | yes | yes | yes | no | demo receipt |
| kerna-ledger-vci | 90 | Py | yes | yes | yes | yes | no | merkle + VERA packet |
| pactly | 23 | TS | ? | ? | ? | ? | — | product satellite |
| gemma4-coder-gguf-runner | 6 | Docker | yes | yes | yes | no | no | infra |
| deepsignal | 13 | HTML | ? | ? | ? | ? | — | content |
| hq-bind | 6 | Py | yes | yes | yes | yes | no | commitments |
| denali-whitepaper | 25 | HTML | ? | ? | ? | ? | — | paper |
| kerna-exact-matrix | 26 | Zig | ? | ? | ? | ? | — | fixed-point algebra |
| psi-alpha-quantum | 31 | Py | yes | yes | yes | yes | no | process matrices |
| siege-os | 9 | Py | ? | ? | ? | ? | — | operator tooling |
| vera-enterprise-engine | 32 | Py | yes | yes | yes | yes | no | production engine |
| kerna-denali | 11 | Py | yes | yes | yes | yes | no | receipt node |

## Placeholders / stubs found

- `kerna-ledger/qreg_engine.py` (664B): intentional redirect to Q-Reg. Correct. Do not expand into a second engine.
- `kerna-ledger/api/*.py` under 800B: thin adapters. Acceptable if they import real modules.
- `qreg-scratch-ci-test/build_vectors.py` (180B), `kerna_verify.py` (205B): stubs. Remediated this cycle to deterministic wrappers.
- `cyberpunk-web-daw`: already documented as archive.
- `Kerna_Vera_VCI`: missing root README/LICENSE/CI; committed `.vercel/output`.

## Committed build artifacts

- **Kerna_Vera_VCI/.vercel/output/** — full SSR function bundle (hundreds of files, largest repo by size). Must not be treated as source of truth. `.gitignore` updated this cycle. Bulk delete of every blob is a follow-up (API is one-file-per-delete).
- No `node_modules/`, `target/`, `__pycache__/`, or `.pyc` trees observed on core protocol repos.

## CI / hygiene gaps (actionable)

1. Kerna_Vera_VCI: add LICENSE, README, workflow, ignore Vercel output and `.grok/` if not intended public.
2. cyberpunk-web-daw + qreg-scratch-ci-test: mark archived or keep as fixtures only.
3. Issue debt is high on Q-Reg (28), unignorable (14), kerna-ledger-vci (15), psi-alpha-quantum (15), cyberpunk-web-daw (16). Many are likely stale health-bot tickets — triage, do not spawn duplicates blindly.
4. Formal proofs live in Q-Reg `formal/*.idr` and aethersound `coq/`. Idris totality is **not** CI-gated on GitHub-hosted runners without an Idris image; Python/Rust tests are the current gate.

## Canonical map (no drift)

- Engine / gates / Ed25519 / Merkle: **Q-Reg**
- Packet schema + CAISO backtest: **kerna-ledger-vci** + **vera-packet-runtime**
- Enterprise API: **vera-enterprise-engine**
- Phi commitments: **phi-boundary-commitments**
- Grid demo: **GridPulse**
- Quantum process matrices: **psi-alpha-quantum**
- Umbrella docs + health audits: **kerna-ledger**
- Web console: **Kerna_Vera_VCI** (source under `src/`, not `.vercel/output`)

## Changes this cycle

- This audit file.
- qreg-scratch-ci-test stub replacement.
- Kerna_Vera_VCI README/LICENSE/.gitignore/CI.
- Tracking issue on kerna-ledger.

## Remaining debt (do not paper over)

- Bulk-delete `.vercel/output` from Kerna_Vera_VCI (or `git filter-repo`).
- Stop committing `.grok/` skill dumps unless they are the product.
- Close or retarget stale issues instead of opening another 25 copies.
- Idris2 proof replay in CI (needs image or nix).
- Deduplicate VERA packet copies across kerna-ledger-vci and vera-packet-runtime.
