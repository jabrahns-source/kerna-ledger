# Portfolio Health Audit — 2026-09-24

Owner: jabrahns-source / Even The Odds Foundry  
Scope: all 25 repositories owned by jabrahns-source (`user:jabrahns-source`, total_count=25).  
Method: authenticated inventory + recursive trees on core protocol + file reads of umbrella redirects.  
Rule: no placeholder replacements that fork the canonical engine; no duplicate daily tracker issues.

## Executive verdict

Core protocol surface remains **operational**. Compared with 2026-09-23 there is **no tree drift** on:

| Repo | HEAD SHA (main tree) |
|---|---|
| kerna-ledger (pre-this-commit) | `1841bced` |
| Q-Reg | `646e0050` |
| kerna-ledger-vci | `fe098e26` |
| vera-enterprise-engine | `953fe04a` |
| phi-boundary-commitments | `a2f36721` |
| GridPulse | `eac7270d` |
| aethersound | `6799710d` |
| psi-alpha-quantum | `ebedd44b` |

Committed `node_modules/`, `target/`, `__pycache__/`, `.pyc`, and `dist/` were **not** found on core protocol repos.

Umbrella `qreg_engine.py` (664 B) and `api/gridpulse_hf_master.py` (573 B) were re-read: they are **intentional SystemExit redirects**, not incomplete notes. Expanding them would create a second engine. That is forbidden.

## Inventory (25)

| Repo | Role | CI | LICENSE | README | Tests | Artifact risk | Status |
|---|---|---|---|---|---|---|---|
| Q-Reg | Canonical engine + Idris formal + Rust runtime | yes | yes | yes | yes | none | healthy |
| kerna-ledger | Umbrella + health audits | yes | yes | yes | yes | none | healthy; redirects intentional |
| kerna-ledger-vci | Merkle + VERA packet + CAISO backtest | yes | yes | yes | yes | none | healthy |
| vera-enterprise-engine | Signed receipt API | yes | yes | yes | yes | none | healthy |
| phi-boundary-commitments | Phi / integer ALU commitments | yes | yes | yes | yes | Untitled62.ipynb name | healthy |
| GridPulse | Demo + receipt.py | yes | yes | yes | yes | none | healthy |
| aethersound | Rust oscillator + UE5 + Coq | yes | yes | yes | yes | none | healthy |
| psi-alpha-quantum | Process matrices | yes | yes | yes | yes | none | healthy |
| kerna-denali | Receipt node | yes | yes | yes | prior | none | satellite |
| vera-packet-runtime | Packet v0.3 runtime | yes | yes | yes | thin | none | thin twin of vci packet |
| Kerna_Vera_VCI | Web console | yes | MIT | yes | app | **`.vercel/` still tracked** | purge still required |
| qreg-scratch-ci-test | CI fixture (private) | yes | MIT | thin | thin | none | fixture, not product |
| cyberpunk-web-daw | Archive | no | yes | yes + ARCHIVE.md | no | none | archive candidate |
| denali-kerna-psi-demo | Static demo | pages | yes | yes | n/a | none | demo |
| denali-whitepaper | Paper HTML | pages | yes | yes | n/a | none | docs |
| hq-bind | Quantum binding | yes | yes | yes | yes | none | satellite |
| kerna-ledger-verified | Zig substrate | prior | yes | yes | prior | none | satellite |
| kerna-exact-matrix | Fixed-point Zig | prior | yes | yes | prior | none | satellite |
| aethersync | Tensor sync | prior | yes | yes | prior | none | satellite |
| unignorable | Receipt stack / outreach | prior | yes | yes | prior | none | satellite |
| pactkit / pactly | Product satellites | yes | yes | yes | yes | none | keep |
| deepsignal | Content | prior | yes | yes | n/a | none | keep |
| siege-os | Operator system | prior | yes | yes | prior | none | keep |
| gemma4-coder-gguf-runner | Local runner | yes | yes | yes | n/a | none | infra |

## Placeholders (<200B or note-only)

- `kerna-ledger/qreg_engine.py` (664B): **intentional redirect** to Q-Reg. Re-confirmed 2026-09-24. Do not expand.
- `kerna-ledger/api/gridpulse_hf_master.py` (573B): redirect to GridPulse. Leave.
- `EMPIRICAL_PROOF_REPORT.md` (595B): pointer to Q-Reg test vectors. Leave.
- No files whose entire content was only `API spec` or `Full updated...` on inspected core trees.
- Do **not** invent a second Q-Reg engine, a DAW, or packet fork this cycle.

## Committed build artifacts

| Path | Action |
|---|---|
| `Kerna_Vera_VCI/.vercel/` | Still present from prior audits. `.gitignore` already covers it. Operator must `git rm -r --cached .vercel` from a local clone. Contents API cannot cheaply delete the tree. |
| Core `target/`, `node_modules/`, `__pycache__/`, `dist/` | Not observed. |

## CI / docs / license

- Core protocol repos have `.github/workflows/*.yml`, LICENSE, README, language-aware `.gitignore`.
- Idris2 (`Q-Reg/formal/*.idr`) and Coq (`aethersound/coq`) are **not** type-checked on GitHub-hosted runners. Python/Rust tests remain the live gate.
- GitHub License API still reports `NOASSERTION` on Q-Reg, kerna-ledger, vera-packet-runtime despite LICENSE blobs + SPDX files.
- Q-Reg has 28 open issues, almost all historical daily health clones. Do not add another.

## Canonical map (no stochastic drift)

1. Engine / gates / Ed25519 / Merkle / Idris specs → **Q-Reg**
2. Packet schema + CAISO backtest → **kerna-ledger-vci** (+ thin twin **vera-packet-runtime**)
3. Enterprise signed ledger API → **vera-enterprise-engine**
4. Phi commitments → **phi-boundary-commitments**
5. Grid demo UI → **GridPulse**
6. Process matrices → **psi-alpha-quantum**
7. Umbrella + audits → **kerna-ledger**
8. Web console → **Kerna_Vera_VCI/src** (never `.vercel/output`)

## Changes this cycle (2026-09-24)

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
6. Triage stale issues on Q-Reg (28), cyberpunk-web-daw (16), psi-alpha-quantum (15), unignorable (14) — close bots, do not clone them.
7. Archive `cyberpunk-web-daw` when ready.
8. SPDX/license metadata so GitHub stops saying NOASSERTION on Q-Reg / kerna-ledger / vera-packet-runtime.

## Verification checklist

- [x] All 25 repos enumerated from `user:jabrahns-source` search (`total_count=25`).
- [x] Recursive trees inspected for Q-Reg, kerna-ledger, kerna-ledger-vci, vera-enterprise-engine, phi-boundary-commitments, GridPulse, aethersound, psi-alpha-quantum, hq-bind, cyberpunk-web-daw.
- [x] Redirect stubs in kerna-ledger confirmed by file read.
- [x] No new placeholder files written.
- [x] No stochastic fork of Q-Reg into the umbrella.
