# Portfolio health audit — 2026-09-06

Owner: jabrahns-source (24 public repositories). Auditor: continuous repo-health automation.
Method: GitHub search + recursive tree walk of all 24 repos. Size scan for blobs <200 B and documented stubs. Artifact search for `target/`, `node_modules/`, `__pycache__/`, `.pyc`, `dist/`.

## Inventory (all 24)

| Repo | size (KB API) | CI | LICENSE | README | tests/docs | Verdict |
|------|---------------|----|---------|--------|------------|---------|
| Q-Reg | 106 | yes (2) | file present (API NOASSERTION) | yes | formal + py + rust | Canonical engine |
| kerna-ledger | 62 | yes | AGPL file | yes | verifier + cargo | Citation root |
| kerna-ledger-vci | 90 | yes (5) | MIT | yes | hash/merkle/vera | Production packet |
| vera-enterprise-engine | 32 | yes | MIT | yes | src + tests | SaaS ledger |
| phi-boundary-commitments | 44 | yes | MIT | yes | src + verification + paper | Notebook name debt |
| GridPulse | 12 | yes | MIT | yes | receipt + tests | Demo |
| aethersound | 44 | yes | MIT | yes | rust + coq + ue5 | Healthy |
| psi-alpha-quantum | 31 | yes | MIT | yes | process_matrix + tests | Healthy |
| kerna-denali | 11 | yes | MIT | thin | receipt + tests | Healthy scaffold |
| denali-kerna-psi-demo | 10 | pages | MIT | thin | html + next pages | Demo |
| denali-whitepaper | 25 | pages/validate | MIT | yes | whitepaper md | Docs |
| kerna-ledger-verified | 25 | yes | MIT | yes | zig + idris examples | Substrate |
| kerna-exact-matrix | 26 | yes | MIT | yes | zig + idris proofs | Healthy |
| vera-packet-runtime | 11 | yes | file (API NOASSERTION) | yes | packet + tests | Packet twin |
| unignorable | 41 | yes | MIT | yes | cli + tests + outreach | Product |
| aethersync | 13 | (prior) | MIT | yes | — | Satellite |
| pactkit | 6 | — | MIT | yes | — | Satellite |
| pactly | 23 | — | MIT | yes | — | Satellite |
| hq-bind | 6 | — | MIT | yes | — | Satellite |
| siege-os | 9 | — | MIT | yes | — | Satellite |
| deepsignal | 13 | — | MIT | yes | — | Satellite |
| gemma4-coder-gguf-runner | 6 | — | MIT | yes | — | Satellite |
| qreg-scratch-ci-test | 14 | yes | **missing** | archive note | scratch copies | Archive candidate |
| cyberpunk-web-daw | 3 | no | MIT | archive | none | Archive candidate |

## Artifact hygiene

Code search `user:jabrahns-source filename:package-lock.json` = 0.
No committed `node_modules/`, `target/`, `__pycache__/`, `.pyc`, or `dist/` trees observed in recursive trees of priority repos.

## Placeholders / stubs

**Intentional (do not expand into a second engine):**
- `kerna-ledger/qreg_engine.py` — documented redirect to Q-Reg
- `kerna-ledger/api/gridpulse_hf_master.py` — documented redirect to GridPulse
- `kerna-ledger/BUILD.md`, `EMPIRICAL_PROOF_REPORT.md` — pointers

**Real debt:**
- `phi-boundary-commitments/Untitled62.ipynb` still at repo root (notebooks/README already documents preferred name)
- `qreg-scratch-ci-test` has 180–205 B pointer scripts and no LICENSE
- `cyberpunk-web-daw` is empty product (README + LICENSE + ARCHIVE.md)
- GitHub license API still `NOASSERTION` on Q-Reg, kerna-ledger, vera-packet-runtime
- Idris 2 / Zig toolchains still not on default ubuntu-latest CI
- Live CAISO ingest remains demo-grade in GridPulse / VCI
- Issue hygiene: kerna-ledger has 23 open issues, almost all prior daily health audits

## Changes this pass (2026-09-06)

- Confirmed 24-repo tree inventory; no new committed build artifacts.
- Confirmed core engines (Q-Reg, VCI, VERA enterprise, phi, GridPulse, aethersound, psi-alpha, exact-matrix, verified substrate) already have CI + LICENSE + README + executable source. No placeholder replacement required on those surfaces.
- This file.
- New tracking issue; older daily health issues marked duplicate of the current tracker so the board stops accumulating identical debt lists.

## Remaining debt (same list, not inflated)

1. Idris 2 + Zig in GitHub-hosted CI (install from upstream releases or use a custom image).
2. Set GitHub license metadata (choose AGPL for kerna-ledger, MIT elsewhere) so API is not NOASSERTION.
3. Byte-identical copy of `Untitled62.ipynb` → `notebooks/phi_boundary_commitments.ipynb` then delete the root file.
4. Archive `cyberpunk-web-daw` and `qreg-scratch-ci-test` (or make scratch private).
5. Live CAISO ingest (GridPulse / VCI).
6. Close completed product issues in Q-Reg (31 open).

Even The Odds Foundry — deterministic, no engine duplication, no stochastic drift.
