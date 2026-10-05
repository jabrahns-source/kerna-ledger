# Estate health audit 2026-10-05

Scope: all 25 public repositories under `jabrahns-source`. Recursive default-branch trees. No committed `target/`, `node_modules/`, `__pycache__/`, `dist/`, or `*.pyc` blobs were present.

## Changes this pass

- `pactly`: added `tests/contract_rules.test.mjs` and wired `node --test` into CI. Locks paid-status (`active` only), free-document limit, price constant, and prompt rules (no invented tax IDs, counsel disclaimer, at least 8 clauses). Does not add a Stripe webhook; that remains open on pactly#1.
- No files deleted. No engine logic duplicated into this umbrella.

## Priority repos

| Repo | CI | LICENSE | README | Tests | Notes |
| --- | --- | --- | --- | --- | --- |
| Q-Reg | yes | yes (NOASSERTION SPDX file) | yes | yes | Canonical Python + Rust runtime. Idris modules are real, not one-line notes. |
| kerna-ledger | yes | yes, non-SPDX (35,314 bytes) | yes | yes | Umbrella map. Stubs redirect. |
| kerna-ledger-vci | yes | MIT | yes | yes | Packet, hash, Merkle present. |
| vera-enterprise-engine | yes | MIT | yes | yes | Ledger + API modules present. |
| phi-boundary-commitments | yes | MIT | yes | yes | `Untitled62.ipynb` retained; notebooks/ has a pointer. |
| GridPulse | yes | MIT | yes | yes | Demo HTML + receipt.py. |
| aethersound | yes | MIT | yes | yes | Rust core + UE5 scaffold. Coq proofs incomplete. |
| psi-alpha-quantum | yes | MIT | yes | yes | Process-matrix module present. |
| denali-whitepaper | yes | MIT | yes | yes | DOI metadata ready, not deposited. |
| denali-kerna-psi-demo | yes | MIT | yes | yes | Static demo + receipt module. |
| kerna-denali | yes | MIT | yes | yes | Receipt node. |

## Archive flags

- `cyberpunk-web-daw`: already archived. Leave archived.
- `qreg-scratch-ci-test`: scratch. README and ARCHIVE.md say not canonical. Issues #1-#5 already request archive. Do not treat as product.

## Remaining debt

- Zenodo DOI for denali-whitepaper is metadata-ready, not deposited.
- `kerna-ledger` LICENSE is long non-SPDX text. GitHub reports `NOASSERTION`. Human SPDX decision still required.
- `Kerna_Vera_VCI` commits `.grok/` skill files. Documented bloat, not a build artifact. Not deleted without an owner call. CI workflow exists.
- `aethersound` UE5 MetaSound graph and Coq proofs remain incomplete by README status.
- Formal Idris/Coq proofs across Q-Reg, phi-boundary, kerna-ledger-verified are not machine-checked in CI.
- `pactly` still lacks Stripe webhook route, auth gate, and draft persistence (issue #1). Tests now cover local contract rules only.
- `deepsignal` is a static carousel page with CI and no unit tests. Not a runtime.
