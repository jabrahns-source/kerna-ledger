# Portfolio Health Audit — 2026-09-21

Owner: jabrahns-source / Even The Odds Foundry  
Scope: all 25 repositories owned by jabrahns-source (`user:jabrahns-source`, total_count=25).  
Method: authenticated inventory + recursive trees on core + denali + archive candidate + file reads of suspected stubs.  
Rule: no placeholder replacements that fork the canonical engine; no duplicate daily tracker issues.

## Executive verdict

Core protocol surface remains **operational**. Compared with 2026-09-20 there is **no tree drift** on Q-Reg (`646e0050`), kerna-ledger-vci (`fe098e26`), vera-enterprise-engine (`953fe04a`), phi-boundary-commitments (`a2f36721`), GridPulse (`eac7270d`), aethersound (`6799710d`), psi-alpha-quantum (`ebedd44b`), kerna-denali (`bada1956`). Umbrella HEAD before this commit: `90fe0a3b`.

Committed `node_modules/`, `target/`, `__pycache__/`, `.pyc`, and `dist/` were **not** found on core protocol repos. The only tracked build output remains `Kerna_Vera_VCI/.vercel/output` (gitignored, still in the index).

## Inventory (25)

| Repo | Role | CI | LICENSE | README | Tests | Artifact risk | Status |
|---|---|---|---|---|---|---|---|
| Q-Reg | Canonical engine + Idris formal + Rust runtime | yes | yes | yes | yes | none | healthy |
| kerna-ledger | Umbrella + health audits | yes | yes | yes | yes | none | healthy; qreg_engine.py is an *intentional* redirect |
| kerna-ledger-vci | Merkle + VERA packet + CAISO backtest | yes | yes | yes | yes | none | healthy |
| vera-enterprise-engine | Signed receipt API | yes | yes | yes | yes | none | healthy |
| phi-boundary-commitments | Phi / integer ALU commitments | yes | yes | yes | yes | Untitled62.ipynb name | healthy |
| GridPulse | Demo + receipt.py | yes | yes | yes | yes | none | healthy |
| aethersound | Rust oscillator + UE5 + Coq | yes | yes | yes | yes | none | healthy |
| psi-alpha-quantum | Process matrices | yes | yes | yes | yes | none | healthy |
| kerna-denali | Receipt node | yes | yes | yes | yes | none | healthy |
| vera-packet-runtime | Packet v0.3 runtime | yes | yes | yes | yes | none | thin twin of vci packet |
| Kerna_Vera_VCI | Web console (`src/`) | yes | yes | yes | app | **`.vercel/` still tracked** | purge still required |
| qreg-scratch-ci-test | CI fixture (private) | yes | MIT | thin | thin | none | fixture, not product |
| cyberpunk-web-daw | Archive | no | yes | yes + ARCHIVE.md | no | none | archive candidate |
| denali-kerna-psi-demo | Static + Next pages | pages.yml | yes | yes | n/a | tiny configs | demo |
| denali-whitepaper | Paper HTML | pages/validate | yes | yes | n/a | none | docs |
| hq-bind | Quantum binding | prior | yes | yes | prior | none | satellite |
| kerna-ledger-verified | Zig substrate | prior | yes | yes | prior | none | satellite |
| kerna-exact-matrix | Fixed-point Zig | prior | yes | yes | prior | none | satellite |
| aethersync | Tensor sync | prior | yes | yes | prior | none | satellite |
| unignorable | Receipt stack / outreach | prior | yes | yes | prior | none | satellite |
| pactkit / pactly | Product satellites | prior | yes | yes | prior | none | keep |
| deepsignal | Content | prior | yes | yes | n/a | none | keep |
| siege-os | Operator system | prior | yes | yes | prior | none | keep |
| gemma4-coder-gguf-runner | Local runner | yes | yes | yes | n/a | none | infra |

## Placeholders (<200B or note-only)

- `kerna-ledger/qreg_engine.py` (664B): **intentional redirect** to Q-Reg. Confirmed by file read 2026-09-21. Do not expand.
- `kerna-ledger/api/gridpulse_hf_master.py` (573B): same class of redirect to GridPulse. Leave.
- `denali-kerna-psi-demo/next.config.mjs` (65B), `tailwind.config.js` (143B): valid tiny configs.
- `cyberpunk-web-daw`: four files including ARCHIVE.md. Flag archive. Do not invent a DAW.
- `phi-boundary-commitments/notebooks/phi_boundary_commitments.ipynb` (1512B): named orientation notebook; historical dump remains `Untitled62.ipynb`.
- No files whose entire content was only `API spec` or `Full updated...` on inspected core trees.

## Committed build artifacts

| Path | Action |
|---|---|
| `Kerna_Vera_VCI/.vercel/` | Still present (config.json, functions/__server.func chunks, static assets). `.gitignore` already covers it. Operator must `git rm -r --cached .vercel`. One-file GitHub Contents API cannot cheaply delete the tree. |
| `.grok/` in Kerna_Vera_VCI | Scaffold skill dump. Product source is `src/`. |
| Core `target/`, `node_modules/`, `__pycache__/`, `dist/` | Not observed. |

## CI / docs / license

- Core protocol repos have `.github/workflows/*.yml`, LICENSE, README, language-aware `.gitignore`.
- Idris2 (`Q-Reg/formal/*.idr`) and Coq (`aethersound/coq`) are **not** type-checked on GitHub-hosted runners. Python/Rust tests remain the live gate.
- GitHub License API still reports `NOASSERTION` on Q-Reg, kerna-ledger, vera-packet-runtime despite LICENSE blobs + SPDX files.

## Canonical map (no stochastic drift)

1. Engine / gates / Ed25519 / Merkle / Idris specs → **Q-Reg**
2. Packet schema + CAISO backtest → **kerna-ledger-vci** (+ thin twin **vera-packet-runtime**)
3. Enterprise signed ledger API → **vera-enterprise-engine**
4. Phi commitments → **phi-boundary-commitments**
5. Grid demo UI → **GridPulse**
6. Process matrices → **psi-alpha-quantum**
7. Umbrella + audits → **kerna-ledger**
8. Web console → **Kerna_Vera_VCI/src** (never `.vercel/output`)

## Changes this cycle (2026-09-21)

- This audit file.
- `STATUS.md` date/health note refreshed.
- Tracker issue #30 updated (no new issue).
- No engine forks. No invented DAW. No mass issue spawn.
- Did **not** `git rm --cached` `.vercel` from this runner (too many blobs for Contents API).

## Remaining debt (ordered)

1. `git rm --cached` Kerna_Vera_VCI `.vercel` (and optional filter-repo).
2. Stop treating `.grok/` as source; consider adding it to `.gitignore` if it is not the product.
3. Deduplicate VERA packet between kerna-ledger-vci and vera-packet-runtime (single module, other imports).
4. Rename `Untitled62.ipynb` in phi-boundary-commitments (named notebook already exists).
5. Idris2 + Coq CI image or nix flake.
6. Triage stale issues on Q-Reg (28), cyberpunk-web-daw (16), psi-alpha-quantum (15), unignorable (14), kerna-ledger-vci (15) — close bots, do not clone them.
7. Archive `cyberpunk-web-daw` when ready.
8. SPDX/license metadata so GitHub stops saying NOASSERTION on Q-Reg / kerna-ledger / vera-packet-runtime.

## Verification checklist

- [x] All 25 repos enumerated from `user:jabrahns-source` search (`total_count=25`).
- [x] Recursive trees inspected for Q-Reg, kerna-ledger, kerna-ledger-vci, vera-enterprise-engine, phi-boundary-commitments, GridPulse, aethersound, psi-alpha-quantum, kerna-denali, denali-whitepaper, denali-kerna-psi-demo, cyberpunk-web-daw, Kerna_Vera_VCI `.vercel` prefix.
- [x] Redirect stub in kerna-ledger confirmed by file read.
- [x] No new placeholder files written.
