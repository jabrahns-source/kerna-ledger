# Health Audit — 2026-09-08

Owner: `jabrahns-source` (Even The Odds Foundry).
Scope: all 24 repositories visible to the authenticated owner.
Method: recursive git trees + size/content classification. No stochastic rewrite of canonical engines.

## Inventory (24)

| Repo | Role | CI | LICENSE | README | Tests/docs | Artifacts in tree | Verdict |
|------|------|----|---------|--------|------------|-------------------|---------| 
| Q-Reg | Canonical compliance engine + Idris2 | yes (ci + gridpulse-verification) | yes (custom/NOASSERTION API) | yes | formal/, verification/, tests | none | HEALTHY core |
| kerna-ledger | Citation / umbrella index | yes | AGPL file present (API NOASSERTION) | yes | tests + STATUS | none | HEALTHY index; pointers intentional |
| kerna-ledger-vci | VCI + VERA packet | yes (ci/pages/release/security/validate) | MIT | yes | tests + vera/ | none | HEALTHY |
| kerna-ledger-verified | Idris2 + Zig substrate | yes + security | MIT | yes | zig tests + proofs | none | HEALTHY; Idris CI not executed on runner |
| vera-enterprise-engine | Production receipt engine | yes | MIT | yes | tests/test_ledger.py | none | HEALTHY |
| vera-packet-runtime | Packet v0.3 runtime | yes | SPDX-style short | yes | import test | none | HEALTHY small |
| phi-boundary-commitments | Phi / Galois commitments | yes | MIT | yes | tests + verification | none | HEALTHY; Untitled62.ipynb should move |
| GridPulse | Live Scope-2 receipt demo | yes | MIT | yes | tests/test_receipt.py | none | HEALTHY demo |
| psi-alpha-quantum | Process-matrix fairness | yes (family workflows) | MIT | yes | tests | none | HEALTHY thin |
| aethersound | Deterministic audio | yes + determinism | MIT | yes | coq + rust + verifier | none | HEALTHY |
| kerna-denali | Deterministic node | yes | MIT | thin | tests | none | HEALTHY small |
| denali-whitepaper | Architecture paper | pages/validate | MIT | yes | paper + index.html | none | HEALTHY docs |
| denali-kerna-psi-demo | Interactive demo | pages | MIT | thin | html + next stub | none | HEALTHY demo; Next.js incomplete vs static index |
| kerna-exact-matrix | Zero-FPU Zig matrix | yes | MIT | yes | proofs + examples | none | HEALTHY |
| hq-bind | Hybrid quantum bind | yes | MIT | yes | tests | none | HEALTHY small |
| unignorable | Outreach / receipt stack | yes | MIT | yes | tests + outreach corpus | none | HEALTHY ops |
| aethersync | Tensor sync middleware | yes | MIT | thin | tests | none | HEALTHY small |
| pactkit | Contract drafts CLI | yes | MIT | yes | tests | none | HEALTHY small |
| pactly | Contractor agreements app | yes | MIT | yes | app + lib | none | HEALTHY app scaffold |
| deepsignal | LinkedIn carousel site | yes | MIT | thin | index.html 30k | none | HEALTHY static |
| gemma4-coder-gguf-runner | Local GGUF runner | docker CI | MIT | yes | docker + config | none | HEALTHY infra |
| siege-os | Zero-budget operator | yes | MIT | large | tests | none | HEALTHY small |
| qreg-scratch-ci-test | Scratch CI | verify-regression | MIT | thin | ARCHIVE.md | none | ARCHIVE candidate (private) |
| cyberpunk-web-daw | Empty / archived | no | MIT | ARCHIVE.md | none | none | ARCHIVE |

## Placeholder / size < 200 B (non-license)

Intentional stubs (documented, not silent):
- `kerna-ledger/qreg_engine.py` — redirect to Q-Reg (664 B, SystemExit).
- `qreg-scratch-ci-test/build_vectors.py` (180 B), `kerna_verify.py` (205 B) — scratch, already ARCHIVE.md.
- `pactkit/src/pactkit/__main__.py` (79 B) — thin entry; engine.py is 3.3k and tested.
- `denali-kerna-psi-demo/next.config.mjs` (65 B) — config, not a spec note.
- `Q-Reg/SPDX-LICENSE-IDENTIFIER` (36 B) — identifier only.
- `Q-Reg/requirements.txt` (70 B) — expected.

No files found whose *only* content is "API spec" or "Full updated…".

## Committed build artifacts

Searched every tree for `target/`, `node_modules/`, `__pycache__`, `.pyc`, `dist/`.
**Zero matches across all 24 repos.**

## Hygiene gaps (remaining debt)

1. GitHub License API reports `NOASSERTION` for Q-Reg, kerna-ledger, vera-packet-runtime despite LICENSE files. Needs GitHub UI license picker or SPDX in LICENSE header GitHub recognizes.
2. Idris2 totality/proof checking is not executed in CI (no Idris2 toolchain on GHA). Proofs exist as source; replay is local/manual.
3. `phi-boundary-commitments/Untitled62.ipynb` is a large untitled notebook at repo root — should live under `notebooks/`.
4. `denali-kerna-psi-demo` mixes a complete static `index.html` with a thin Next.js `pages/` pair; pick one deploy path.
5. `cyberpunk-web-daw` and `qreg-scratch-ci-test` should be GitHub-archived when you next have UI access.
6. Several READMEs lack status badges (kerna-denali, aethersync, deepsignal, cyberpunk).
7. Formal proofs in Q-Reg / kerna-ledger-verified / kerna-exact-matrix are specifications + sketches; they are not claimed as machine-checked on CI in this audit.
8. Open issue counts are high on Q-Reg (31), psi-alpha (15), kerna-ledger-vci (15), cyberpunk (14), unignorable (11) — many likely stale from prior automations.

## Actions taken this pass

- Recorded this matrix (no invented second engines).
- Confirmed umbrella pointers remain intentional and must not be expanded into a fork of Q-Reg.
- Confirmed no committed build artifacts to delete.
- Opened / refreshed tracking issue on this repo for remaining debt.

## Do-not-do list (drift lock)

- Do not copy `Q-Reg/qreg_engine.py` into `kerna-ledger`.
- Do not claim Idris2 proofs are CI-checked until a toolchain job exists.
- Do not populate `cyberpunk-web-daw` — archive it.

Even The Odds Foundry — deterministic audit, 2026-09-08.
