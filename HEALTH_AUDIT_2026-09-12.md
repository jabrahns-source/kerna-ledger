# HEALTH AUDIT 2026-09-12

Owner: jabrahns-source (Even The Odds Foundry).
Scope: all 24 searchable owner repositories (23 public + 1 private scratch).
Method: GitHub search + recursive trees + content inspection of stubs.
Standard: deterministic, no placeholder replacement of live engines, no duplicate runtimes.

## Inventory

| Repo | Size KB | Lang | LICENSE | CI | Tests | README | Notes |
|------|---------|------|---------|----|-------|--------|-------|
| Q-Reg | 106 | Python+Idris+Rust | custom SPDX file (API NOASSERTION) | yes (2 wf) | yes | yes | Canonical compliance engine. Formal/*.idr present. |
| kerna-ledger | 81 | Python+Rust | AGPL file (API NOASSERTION) | yes | yes | yes | Index root. Intentional stubs only. |
| kerna-ledger-vci | 90 | Python | MIT | yes (5 wf) | yes | yes | Hash + merkle + VERA packet. |
| vera-enterprise-engine | 32 | Python | MIT | yes | yes | yes | Production receipt engine. |
| phi-boundary-commitments | 46 | Python+nb | MIT | yes | yes | yes | Untitled62.ipynb historical name debt. |
| GridPulse | 12 | HTML+Py | MIT | yes | yes | yes | Demo. |
| aethersound | 46 | Rust+C++ | MIT | yes | yes | yes | Coq + UE5 bindings. |
| psi-alpha-quantum | 31 | Python | MIT | yes | yes | yes | Process matrix. |
| kerna-denali | 11 | Python | MIT | yes | yes | yes | Substrate receipt. |
| denali-whitepaper | 25 | HTML | MIT | (prior) | n/a | yes | Docs site. |
| denali-kerna-psi-demo | 10 | HTML | MIT | n/a | n/a | yes | Interactive demo. |
| kerna-ledger-verified | 25 | Zig | MIT | (prior) | n/a | yes | Zig substrate. |
| kerna-exact-matrix | 26 | Zig | MIT | (prior) | n/a | yes | Zero-FPU matrix. |
| vera-packet-runtime | 11 | Python | NOASSERTION | (prior) | n/a | yes | Packet runtime. |
| hq-bind | 6 | Python | MIT | yes | yes | yes | Binding protocol. |
| unignorable | 50 | Python | MIT | (prior) | n/a | yes | Outreach stack. |
| aethersync | 13 | Python | MIT | (prior) | n/a | yes | Sync middleware. |
| pactkit | 6 | Python | MIT | n/a | n/a | yes | Contracts. |
| pactly | 23 | TS | MIT | n/a | n/a | yes | Contractor SaaS. |
| gemma4-coder-gguf-runner | 6 | Docker | MIT | n/a | n/a | yes | Local GGUF. |
| deepsignal | 13 | HTML | MIT | n/a | n/a | yes | Carousels. |
| siege-os | 9 | Python | MIT | yes | yes | yes | Operator system. |
| cyberpunk-web-daw | 3 | none | MIT | no | no | archive note | **Archive candidate**. |
| qreg-scratch-ci-test | 15 | Python | MIT | (scratch) | n/a | n/a | **Private scratch; archive/delete candidate**. |

## 1. Incomplete / placeholder files

- No files whose *only* content is a raw note like "API spec" or "Full updated...".
- Intentional redirect stubs (not defects):
  - `kerna-ledger/qreg_engine.py` — exits with pointer to Q-Reg.
  - `kerna-ledger/api/gridpulse_hf_master.py` — pointer to GridPulse + Q-Reg.
- Small files that are complete licenses/SPDX/config, not placeholders: SPDX identifiers, dependabot.yml, markdownlint.
- `phi-boundary-commitments/Untitled62.ipynb` is a historical notebook name, not empty.
- `cyberpunk-web-daw` is documentation-only by design (ARCHIVE.md).

## 2. Committed build artifacts

Trees inspected on priority and satellite repos contain **zero** committed:
`target/`, `node_modules/`, `__pycache__/`, `*.pyc`, `dist/`.
`.gitignore` present on all active code repos covering language-specific ignores.

## 3. CI / README / LICENSE / tests / docs

- Core impact set all have `.github/workflows`, README, LICENSE, tests or verifier scripts.
- GitHub License API still reports `NOASSERTION` on Q-Reg, kerna-ledger, vera-packet-runtime despite on-disk SPDX/LICENSE files. This is GitHub UI picker debt, not missing legal text.
- Idris2 proof *replay* is not yet a first-class CI job on Q-Reg (files exist; checker image not wired).
- Satellite product repos (pactly, pactkit, deepsignal, gemma4) have thinner CI; not core trust surface.

## 4. Priority ranking (impact)

1. Q-Reg — engine + formal specs.
2. kerna-ledger-verified + kerna-exact-matrix — Zig/indubitable substrate.
3. vera-enterprise-engine + kerna-ledger-vci — receipts and packets.
4. phi-boundary-commitments — commitment algebra.
5. GridPulse + denali-* + psi-alpha-quantum — demos and fairness.
6. aethersound — adjacent deterministic media.

Do **not** fork engines into the umbrella repo.

## 5. Actions taken this run

- Re-audited all 24 owner repos via API trees.
- Confirmed stubs remain documented redirects, not silent empties.
- Confirmed no artifact dumps landed since 2026-09-11.
- Published this report and refreshed STATUS.md.
- Opened/updated tracking issue on kerna-ledger for remaining debt.

No engine code was duplicated. No placeholders were invented as "complete" products.

## 6. Remaining debt (ranked)

1. Wire Idris2 typecheck/proof replay into Q-Reg CI (needs Idris2 image or Nix).
2. Set GitHub repository license picker so API stops returning NOASSERTION on AGPL/custom SPDX repos.
3. Rename or alias `Untitled62.ipynb` in phi-boundary-commitments.
4. Archive `cyberpunk-web-daw` and delete/archive `qreg-scratch-ci-test` after confirming no unique CI secrets.
5. Sweep stale issues on Q-Reg (27 open) and unignorable (13 open); close completed health items.
6. Live CAISO ingest remains out-of-band (network + credentials); keep synthetic vectors in-repo.
7. Coq CI for aethersound is optional; current Python/Rust determinism tests are the gate.

## 7. Archive flags

- `cyberpunk-web-daw`: no source, ARCHIVE.md present — archive on GitHub when convenient.
- `qreg-scratch-ci-test`: private scratch — do not promote; delete after last CI debug.

Even The Odds Foundry — 2026-09-12 — zero stochastic drift.
