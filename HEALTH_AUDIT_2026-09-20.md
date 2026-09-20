# Portfolio Health Audit — 2026-09-20

Owner: jabrahns-source / Even The Odds Foundry  
Scope: all 25 repositories owned by jabrahns-source.  
Method: GitHub search inventory + recursive trees on core + satellite repos + prior-day audit delta.  
Rule: no placeholder replacements that fork the canonical engine; no duplicate issues.

## Executive verdict

Core protocol surface is **operational, not empty**. Q-Reg, kerna-ledger-vci, vera-enterprise-engine, phi-boundary-commitments, GridPulse, aethersound, psi-alpha-quantum, kerna-denali, vera-packet-runtime, and Kerna_Vera_VCI all have LICENSE + README + .gitignore + (except the web console historically) Actions. Committed `node_modules/`, `target/`, `__pycache__/`, and `.pyc` trees were **not** found on core protocol repos.

Largest remaining artifact is still **Kerna_Vera_VCI/.vercel/output** (already gitignored; still in history/index from the original scaffold). That is documentation + `git rm --cached` debt, not a missing engine.

## Inventory (25)

| Repo | Role | CI | LICENSE | README | Tests | Artifact risk | Status |
|---|---|---|---|---|---|---|---|
| Q-Reg | Canonical engine + Idris formal + Rust runtime | yes | yes | yes | yes | none | healthy |
| kerna-ledger | Umbrella + health audits | yes | yes | yes | yes | none | healthy; qreg_engine.py is an *intentional* redirect |
| kerna-ledger-vci | Merkle + VERA packet + CAISO backtest | yes | yes | yes | yes | none | healthy; packet also copied in vera-packet-runtime |
| vera-enterprise-engine | Signed receipt API | yes | yes | yes | yes | none | healthy |
| phi-boundary-commitments | Phi / integer ALU commitments | yes | yes | yes | yes | Untitled62.ipynb name | healthy |
| GridPulse | Demo + receipt.py | yes | yes | yes | yes | none | healthy |
| aethersound | Rust oscillator + UE5 + Coq | yes | yes | yes | yes | none | healthy |
| psi-alpha-quantum | Process matrices | yes | yes | yes | yes | none | healthy |
| kerna-denali | Receipt node | yes | yes | yes | yes | none | healthy |
| vera-packet-runtime | Packet v0.3 runtime | yes | yes | yes | yes | none | thin but real |
| Kerna_Vera_VCI | Web console (`src/`) | yes | yes | yes | app | **`.vercel/` still tracked** | hygiene OK; purge output |
| qreg-scratch-ci-test | CI fixture | yes | yes | thin | thin | none | fixture, not product |
| cyberpunk-web-daw | Archive | no | yes | yes | no | none | archive candidate |
| denali-kerna-psi-demo | Static + Next pages | pages.yml | yes | yes | n/a | tiny configs | demo |
| denali-whitepaper | Paper HTML | ? | yes | yes | n/a | none | docs |
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

- `kerna-ledger/qreg_engine.py` (664B): **intentional redirect** to Q-Reg. Do not expand.
- `kerna-ledger/api/*.py` (~573–714B): thin adapters. Leave unless they break imports.
- `denali-kerna-psi-demo/next.config.mjs` (65B), `tailwind.config.js` (143B): valid tiny configs, not notes.
- `qreg-scratch-ci-test/README.md` (206B), `test_regression.py` (391B): fixture-grade, already above stub threshold after 2026-09-19.
- `cyberpunk-web-daw`: four files including ARCHIVE.md. Flag archive. Do not invent a DAW.
- No files whose entire content was only `API spec` or `Full updated...` on inspected core trees.

## Committed build artifacts

| Path | Action |
|---|---|
| `Kerna_Vera_VCI/.vercel/` | Already in `.gitignore`. Still present in the tree from the first push. Operator must `git rm -r --cached .vercel` (see that repo `ARTIFACTS.md`). One-file GitHub API cannot cheaply delete hundreds of blobs. |
| `.grok/` in Kerna_Vera_VCI | Scaffold skill dump. Product source is `src/`. Do not treat `.grok` as protocol. |
| Core `target/`, `node_modules/`, `__pycache__/` | Not observed. |

## CI / docs / license

- Core protocol repos have `.github/workflows/*.yml`, LICENSE, README, language-aware `.gitignore`.
- Idris2 (`Q-Reg/formal/*.idr`) and Coq (`aethersound/coq`) are **not** type-checked on GitHub-hosted runners. Python/Rust tests are the live gate. That is remaining verification debt, not a missing file.
- Q-Reg LICENSE is large (custom/Apache-style 5768B); GitHub reports `NOASSERTION` on some repos despite a LICENSE blob. SPDX files exist on Q-Reg and kerna-ledger.

## Canonical map (no stochastic drift)

1. Engine / gates / Ed25519 / Merkle / Idris specs → **Q-Reg**
2. Packet schema + CAISO backtest → **kerna-ledger-vci** (+ thin twin **vera-packet-runtime**)
3. Enterprise signed ledger API → **vera-enterprise-engine**
4. Phi commitments → **phi-boundary-commitments**
5. Grid demo UI → **GridPulse**
6. Process matrices → **psi-alpha-quantum**
7. Umbrella + audits → **kerna-ledger**
8. Web console → **Kerna_Vera_VCI/src** (never `.vercel/output`)

## Changes this cycle (2026-09-20)

- This audit file.
- Tracker issue #30 updated (no new issue).
- No engine forks. No invented DAW. No mass issue spawn.

## Remaining debt (ordered)

1. `git rm --cached` Kerna_Vera_VCI `.vercel` (and optional filter-repo).
2. Stop treating `.grok/` as source; consider adding it to `.gitignore` if it is not the product.
3. Deduplicate VERA packet between kerna-ledger-vci and vera-packet-runtime (single module, other imports).
4. Rename `Untitled62.ipynb` in phi-boundary-commitments.
5. Idris2 + Coq CI image or nix flake.
6. Triage stale issues on Q-Reg (28), cyberpunk-web-daw (16), psi-alpha-quantum (15), unignorable (14) — close bots, do not clone them.
7. Archive `cyberpunk-web-daw` when ready.
8. SPDX/license metadata so GitHub stops saying NOASSERTION on Q-Reg / kerna-ledger / vera-packet-runtime.

## Verification checklist

- [x] All 25 repos enumerated from `user:jabrahns-source` search (`total_count=25`).
- [x] Recursive trees inspected for Q-Reg, kerna-ledger, kerna-ledger-vci, vera-enterprise-engine, phi-boundary-commitments, GridPulse, aethersound, psi-alpha-quantum, kerna-denali, denali-kerna-psi-demo, cyberpunk-web-daw, qreg-scratch-ci-test, Kerna_Vera_VCI (root + prior full tree).
- [x] Redirect stub in kerna-ledger confirmed by file read.
- [x] Kerna_Vera_VCI now has README + LICENSE + CI + ARTIFACTS.md + `.gitignore` covering `.vercel/` and `node_modules/`.
- [x] No new placeholder files written.
