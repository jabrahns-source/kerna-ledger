# Portfolio health audit 2026-10-03

Auditor: continuous repo health pass over all 25 repositories owned by jabrahns-source.
Method: GitHub repository search (total_count=25) plus recursive default-branch trees for every priority repo and every secondary repo except the already-archived cyberpunk-web-daw.
No committed `target/`, `node_modules/`, `__pycache__/`, `*.pyc`, or `dist/` trees were present in the inspected trees. `Kerna_Vera_VCI` commits `package-lock.json` (expected) and does not commit `node_modules/`.

## Inventory

Public non-fork count: 25. Archived: `cyberpunk-web-daw` only. Flagged for archive, not yet flipped: `qreg-scratch-ci-test` (ARCHIVE.md present; README is an explicit non-canonical pointer, 206 bytes).

## Priority repos

| Repo | CI | LICENSE | gitignore | tests | docs | Finding |
| --- | --- | --- | --- | --- | --- | --- |
| Q-Reg | ci.yml, gridpulse-verification.yml | AGPL-sized text present | yes | test_vectors.py, verification/ | docs/, formal/*.idr | Hygiene intact. Idris not in CI. Throughput claims still unreproduced. |
| kerna-ledger | ci.yml, gridpulse-narrative.yml | NOASSERTION, 35 KB | yes | tests/test_kerna_verify.py | spec + whitepaper | Umbrella only. `qreg_engine.py` (664 B) is an intentional redirect, not a silent placeholder. |
| kerna-ledger-vci | ci, pages, release, security, validate | MIT | yes | tests/test_hash.py, test_merkle.py | whitepaper | Audit-ready packet surface. |
| vera-enterprise-engine | ci.yml | MIT | yes | tests/test_ledger.py | README | Ledger, Ed25519, config, Dockerfile present. |
| phi-boundary-commitments | ci.yml | MIT | yes | tests/test_phi.py + verification/ | paper/PAPER.md | `notebooks/phi_boundary_commitments.ipynb` is 1512 bytes (thin wrapper). Untitled62.ipynb is the large notebook. |
| GridPulse | ci.yml | MIT | yes | tests/test_receipt.py | README + index.html | Demo complete for its scope. |
| aethersound | ci.yml, determinism.yml | MIT | yes | tests/test_determinism.py | BUILD_UE5.md, coq/ | UE5 MetaSound graph still incomplete by README status. |
| psi-alpha-quantum | ci, pages, release, security, validate | MIT | yes | tests/test_process_matrix.py | whitepaper | Process-matrix core present. |
| kerna-denali | ci.yml | MIT | yes | tests/test_denali_receipt.py | STATUS.md | Receipt node present. |
| denali-whitepaper | pages, release, security, validate | MIT | yes | tests/test_whitepaper.py | whitepaper md | No code CI (document repo). SECURITY.md is a short policy, not a stub. |
| denali-kerna-psi-demo | ci.yml, pages.yml | MIT | yes | tests/test_receipt.mjs | README + index.html | Demo + receipt canonicalizer present. |

## Secondary repos

| Repo | Status |
| --- | --- |
| Kerna_Vera_VCI | TypeScript app, LICENSE, README, lockfile, server/, src/, migrations/. Latest push 2026-10-02. No node_modules committed at repo root. |
| kerna-ledger-verified | Zig receipt + Idris sketches + CI. No zig-out/ committed. |
| kerna-exact-matrix | Zig matrix + Idris proof sketch + CI. No zig-out/. |
| vera-packet-runtime | Packet copy + tests. Duplicate of kerna-ledger-vci packet; CANONICAL.md must stay the pointer. |
| qreg-scratch-ci-test | Archive candidate. Keep only while a workflow still references it. |
| hq-bind | Commitment module + tests + CI. |
| aethersync | sync_core.py + tests + CI. Docs are short. |
| siege-os | siege.py + tests + long README + CI. |
| pactkit | engine.py + tests. `__main__.py` is a real entrypoint (79 B), not a placeholder. |
| pactly | Present in inventory (TypeScript, MIT, 1 open issue). Not re-scaffolded this pass. |
| gemma4-coder-gguf-runner | Docker + CI. No model weights committed. |
| deepsignal | Static HTML + CI. |
| unignorable | Present in inventory (Python, 16 open issues). Not re-scaffolded this pass. |
| cyberpunk-web-daw | Already archived. |

## Changes this pass

- Wrote this audit. Did not rewrite working engines. No artifact deletion was required because no build trees are committed.
- Did not invent formal proofs or performance numbers.

## Remaining debt

1. Human decision on kerna-ledger LICENSE (NOASSERTION vs AGPL-3.0-only / dual).
2. Archive `qreg-scratch-ci-test` in GitHub settings after confirming no external workflow still clones it.
3. Pin an Idris 2 and Coq job, or label `formal/` and `coq/` as non-machine-checked sketches in every README that mentions them.
4. Remove or reproduce the Q-Reg 26k RPS / <7 µs p99 claim with an in-repo harness.
5. Collapse VERA packet duplication: vera-packet-runtime should import or submodule kerna-ledger-vci rather than carry a second 8 KB copy.
6. aethersound UE5 MetaSound graph is still a scaffold.
7. phi notebook path is thin; point README at Untitled62.ipynb or regenerate the named notebook from src/phi_commitment.py.
