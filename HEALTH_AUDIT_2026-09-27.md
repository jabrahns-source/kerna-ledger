# Portfolio Health Audit — 2026-09-27

Owner: jabrahns-source / Even The Odds Foundry  
Scope: all 25 repositories owned by jabrahns-source (`user:jabrahns-source`, total_count=25).  
Method: authenticated inventory + recursive trees on all priority and satellite repos + file reads of umbrella redirects.  
Rule: no placeholder replacements that fork the canonical engine; no duplicate daily tracker issues.

## Executive verdict

Core protocol surface remains **operational**. Compared with 2026-09-26 there is **no tree drift** on:

| Repo | HEAD SHA (main tree) |
|---|---|
| Q-Reg | `646e0050` |
| kerna-ledger-vci | `fe098e26` |
| vera-enterprise-engine | `953fe04a` |
| phi-boundary-commitments | `a2f36721` |
| GridPulse | `eac7270d` |
| aethersound | `6799710d` |
| psi-alpha-quantum | `ebedd44b` |
| kerna-denali | `bada1956` |
| vera-packet-runtime | `5deec540` |
| hq-bind | `b8b07e35` |
| kerna-exact-matrix | `cbc37251` |
| kerna-ledger-verified | `d36200aa` |
| denali-whitepaper | `343032ed` |
| denali-kerna-psi-demo | `3c0a786e` |
| unignorable | `f30e240e` |
| siege-os | `43c2f274` |
| pactkit | `10471f2e` |
| pactly | `4dc4334d` |
| aethersync | `edda6403` |
| Kerna_Vera_VCI | `97e818f0` |

Committed `target/`, `node_modules/`, `__pycache__/`, `.pyc`, and `dist/` were **not** found on core protocol repos.

Umbrella `qreg_engine.py` and `api/gridpulse_hf_master.py` were re-read: they are **intentional SystemExit redirects**, not incomplete notes. Expanding them would create a second engine. That is forbidden.

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
| kerna-denali | Receipt node | yes | yes | yes | yes | none | satellite |
| vera-packet-runtime | Packet v0.3 runtime | yes | yes | yes | thin | none | thin twin of vci packet |
| Kerna_Vera_VCI | Web console | scaffold | MIT | yes | app | **`.vercel/` still tracked** | purge still required |
| qreg-scratch-ci-test | CI fixture (private) | yes | MIT | thin | thin | none | fixture, not product |
| cyberpunk-web-daw | Archive | no | yes | yes + ARCHIVE.md | no | none | archive candidate |
| denali-kerna-psi-demo | Static demo | pages | yes | yes | n/a | none | demo |
| denali-whitepaper | Paper HTML | pages | yes | yes | n/a | none | docs |
| hq-bind | Quantum binding | yes | yes | yes | yes | none | satellite |
| kerna-ledger-verified | Zig substrate | yes | yes | yes | zig tests | none | satellite |
| kerna-exact-matrix | Fixed-point Zig | yes | yes | yes | zig | none | satellite |
| aethersync | Tensor sync | yes | yes | yes | yes | none | satellite |
| unignorable | Receipt stack / outreach | yes | yes | yes | yes | none | satellite |
| pactkit / pactly | Product satellites | yes | yes | yes | yes | none | keep |
| deepsignal | Content | yes | yes | yes | n/a | none | keep |
| siege-os | Operator system | yes | yes | yes | yes | none | keep |
| gemma4-coder-gguf-runner | Local runner | yes | yes | yes | n/a | none | infra |

## Placeholders (<200B or note-only)

- `kerna-ledger/qreg_engine.py` (664B): **intentional redirect** to Q-Reg. Re-confirmed 2026-09-27. Do not expand.
- `kerna-ledger/api/gridpulse_hf_master.py` (573B): redirect to GridPulse. Leave.
- `EMPIRICAL_PROOF_REPORT.md` (595B): pointer to Q-Reg test vectors. Leave.
- `Kerna_Vera_VCI/.node_modules.lock`: empty marker (0 B). Not a vendor tree.
- `cyberpunk-web-daw`: ARCHIVE.md + thin README only. Flagged for archive; do not invent a DAW.
- No files whose entire content was only `API spec` or `Full updated...` on inspected core trees.
- Do **not** invent a second Q-Reg engine, a DAW, or packet fork this cycle.

## Committed build artifacts

| Path | Count | Action |
|---|---|---|
| `Kerna_Vera_VCI/.vercel/**` | tracked from prior scaffold | `.gitignore` already covers `.vercel/`. Contents API cannot cheaply delete the tree. Local `git rm -r --cached .vercel` remains required. |
| `Kerna_Vera_VCI/.node_modules.lock` | 1 empty blob | Lock marker only. |
| Core `target/`, `node_modules/`, `__pycache__/`, `dist/` | 0 | Clean. |

## CI / docs / license

- Core protocol repos have `.github/workflows/*.yml`, LICENSE, README, language-aware `.gitignore`.
- Idris2 (`Q-Reg/formal/*.idr`) and Coq (`aethersound/coq`) are **not** type-checked on GitHub-hosted runners. Python/Rust/Zig tests remain the live gate.
- GitHub License API still reports `NOASSERTION` on kerna-ledger / vera-packet-runtime despite LICENSE blobs + SPDX files.
- Q-Reg historically accumulated daily health clones. Do not add another there.
- kerna-ledger has a single open tracker (#30). Update in place.

## Canonical map (no stochastic drift)

1. Engine / gates / Ed25519 / Merkle / Idris specs → **Q-Reg**
2. Packet schema + CAISO backtest → **kerna-ledger-vci** (+ thin twin **vera-packet-runtime**)
3. Enterprise signed ledger API → **vera-enterprise-engine**
4. Phi commitments → **phi-boundary-commitments**
5. Grid demo UI → **GridPulse**
6. Process matrices → **psi-alpha-quantum**
7. Umbrella + audits → **kerna-ledger**
8. Web console → **Kerna_Vera_VCI/src** (never `.vercel/output`)

## Changes this cycle (2026-09-27)

- This audit file.
- `STATUS.md` date/health note refreshed.
- Tracker issue #30 updated (no new issue).
- Re-walked all 25 trees including satellites not re-listed every prior day (pactkit, pactly, siege-os, aethersync, gemma4, deepsignal, unignorable).
- No engine forks. No invented DAW. No mass issue spawn.
- Did **not** `git rm --cached` `.vercel` from this runner (Contents delete is one-file-per-commit and would thrash history without removing ancestor objects).

## Remaining debt (ordered)

1. `git rm --cached` Kerna_Vera_VCI `.vercel` (and optional filter-repo).
2. Deduplicate VERA packet between kerna-ledger-vci and vera-packet-runtime (single module, other imports).
3. Rename `Untitled62.ipynb` in phi-boundary-commitments (named notebook already exists).
4. Idris2 + Coq CI image or nix flake.
5. Triage stale issues on Q-Reg, cyberpunk-web-daw, psi-alpha-quantum, unignorable — close bots, do not clone them.
6. Archive `cyberpunk-web-daw` and consider archiving `qreg-scratch-ci-test` when ready.
7. SPDX/license metadata so GitHub stops saying NOASSERTION on kerna-ledger / vera-packet-runtime.
8. CAISO live ingest (beyond recorded backtest vectors).

## Verification checklist

- [x] All 25 repos enumerated from `user:jabrahns-source` search (`total_count=25`).
- [x] Recursive trees inspected for priority + satellite set listed above.
- [x] Redirect stubs in kerna-ledger confirmed by file read.
- [x] No new placeholder files written.
- [x] No stochastic fork of Q-Reg into the umbrella.
