# Portfolio health audit 2026-10-01

Auditor: continuous repo health pass over all 25 repositories owned by jabrahns-source.
Scope: tree inspection, placeholder/size screen, committed artifact screen, CI/README/LICENSE/gitignore/tests/docs.
No committed `target/`, `node_modules/`, `__pycache__`, `.pyc`, or `dist/` trees were found in the inspected default-branch trees.

## Canonical map

| Concern | Canonical repo | Notes |
| --- | --- | --- |
| Q-Reg runtime | Q-Reg | Python engine + Rust runtime + Idris sketches. CI present. |
| Ledger umbrella | kerna-ledger | Spec, verifier, Rust sketch. `qreg_engine.py` is an intentional redirect stub to Q-Reg. |
| VCI packets | kerna-ledger-vci | Hash, Merkle, VERA packet, tests, CI. |
| Enterprise ledger | vera-enterprise-engine | SQLite ledger, Ed25519, tests, CI. |
| Phi commitments | phi-boundary-commitments | Python core + tests. Notebook `notebooks/phi_boundary_commitments.ipynb` is thin (1512 bytes). |
| Grid demo | GridPulse | HTML + receipt.py + tests. |
| Audio | aethersound | Rust lib, UE5 sources, Python verifier, CI. No committed Cargo target/. |
| Process matrices | psi-alpha-quantum | `src/process_matrix.py` + tests. |
| Denali | denali-kerna-psi-demo, denali-whitepaper, kerna-denali | Demo receipt canonicalizer fixed this pass. Whitepaper gained structural tests. |

## Debt left open

- qreg-scratch-ci-test and cyberpunk-web-daw already carry ARCHIVE.md. They should be archived in GitHub settings; automation cannot flip the archive bit from this pass.
- kerna-ledger LICENSE is NOASSERTION (35 KB, not a standard SPDX grant). Needs a human license decision.
- Idris/Coq files are sketches. CI does not typecheck them (no Idris2/Coq runner pinned).
- Q-Reg README claims 26k RPS / <7us p99. Those numbers are not reproduced by an in-repo benchmark harness.
- Duplicate VERA packet copies exist in kerna-ledger-vci and vera-packet-runtime. Keep vera-packet-runtime as the packet runtime; do not fork logic again.
