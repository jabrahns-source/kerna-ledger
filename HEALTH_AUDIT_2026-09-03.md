# Portfolio health audit — 2026-09-03

Owner: jabrahns-source (Even The Odds Foundry). Scope: all 24 owned repositories.

## Method

1. Recursive trees on every public repo plus private `qreg-scratch-ci-test`.
2. Flag blobs < 200 bytes or note-only content.
3. Scan for committed `target/`, `node_modules/`, `__pycache__/`, `.pyc`, `dist/`.
4. Check CI, README, LICENSE, `.gitignore`, tests, docs.
5. Prioritize Q-Reg, kerna-ledger, kerna-ledger-vci, vera-enterprise-engine, phi-boundary-commitments, GridPulse, aethersound, psi-alpha-quantum, denali-*.

## Artifact scan

**Zero committed build artifacts** across the 24-repo set in this pass.

## Inventory (compressed)

| Repo | CI | LICENSE | Tests | Notes |
|------|----|---------|-------|-------|
| Q-Reg | yes (2 wf) | file present, GitHub NOASSERTION | python + rust + formal | Canonical engine. Cargo.lock is std-only complete. |
| kerna-ledger | yes | file present | kerna_verify | Umbrella. Pointer stubs by design. |
| kerna-ledger-vci | yes (5 wf) | MIT | hash/merkle | Production packet + pages. |
| kerna-ledger-verified | yes | MIT | zig tests | Idris2 examples + Zig receipt. |
| vera-enterprise-engine | yes | MIT | ledger | Real FastAPI/ledger package. |
| vera-packet-runtime | yes | SPDX-ish short | import test | Packet + stripe checkout helper. |
| phi-boundary-commitments | yes | MIT | test_phi + 4 verifiers | Notebook leftover `Untitled62.ipynb`. |
| GridPulse | yes | MIT | test_receipt | Demo HTML + receipt.py. |
| aethersound | yes | MIT | verifier.py/rs | Rust + Coq + UE5 bindings. |
| psi-alpha-quantum | yes (5 wf) | MIT | process_matrix | Real module. |
| denali-whitepaper | pages/validate | MIT | n/a (paper) | Docs-only, acceptable. |
| kerna-denali | yes | MIT | receipt tests | Functional. |
| denali-kerna-psi-demo | pages | MIT | none | Static demo; OASIS API now has fallback. |
| kerna-exact-matrix | yes | MIT | zig examples | Strong. |
| unignorable | yes | MIT | cli test | Outreach corpus + CLI. |
| pactkit | yes | MIT | engine | Python contract engine. |
| pactly | yes | MIT | none (Next app) | Full Next/Supabase/Stripe surface. |
| hq-bind | yes | MIT | commitment | Small but real. |
| aethersync | yes | MIT | sync_core (this pass) | JAX path optional; stdlib core added. |
| siege-os | yes | MIT | test_siege | Thin but real. |
| deepsignal | yes | MIT | n/a | Single HTML carousel. |
| gemma4-coder-gguf-runner | docker CI | MIT | n/a | Docker/compose/systemd. |
| cyberpunk-web-daw | no | MIT | no | **Archive candidate**. |
| qreg-scratch-ci-test | verify-regression | none | thin | **Private scratch — archive**. |

## Edits this pass

- aethersync: `sync_core.py`, `tests/test_sync_core.py`, `requirements.txt`, CI pytest.
- kerna-ledger: STATUS.md refresh + this file.
- denali-kerna-psi-demo: `pages/api/caiso.js` deterministic fallback.

## Remaining debt (do not paper over)

1. Q-Reg Idris2 files are specifications, not CI-replayed proofs (no Idris2 toolchain in GHA).
2. Q-Reg `runtime/Cargo.lock` is std-only; adding tonic/tokio requires regenerate.
3. kerna-ledger LICENSE file is huge / GitHub license API reports NOASSERTION.
4. `phi-boundary-commitments/Untitled62.ipynb` should be renamed or moved to `notebooks/`.
5. `cyberpunk-web-daw` and `qreg-scratch-ci-test` should be GitHub-archived.
6. pactly / gemma4 / deepsignal have no unit tests (product vs infra).
7. Live CAISO OASIS ingest is still not a verified production adapter.
8. Formal claims (F_83 primality, 200ms finality, MEV resistance) remain tracked debt, not proved in CI.

Zero stochastic drift. Pointers stay pointers. Engines stay in Q-Reg / VERA / exact-matrix.
