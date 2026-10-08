# Portfolio health audit 2026-10-08

Scope: all 25 repositories owned by `jabrahns-source` (`user:jabrahns-source`, total_count 25, incomplete_results false).

Recursive default-branch trees inspected this pass: Q-Reg, kerna-ledger, kerna-ledger-vci, vera-enterprise-engine, phi-boundary-commitments, GridPulse, aethersound, psi-alpha-quantum, kerna-denali, denali-whitepaper, denali-kerna-psi-demo, kerna-exact-matrix, hq-bind, vera-packet-runtime, aethersync, pactkit, siege-os, gemma4-coder-gguf-runner, deepsignal, qreg-scratch-ci-test.

Prior pass (2026-10-07) already walked Kerna_Vera_VCI, kerna-ledger-verified, pactly, and unignorable. Code search for `placeholder`, `TODO` under 200 bytes, `.pyc`, `node_modules`, `__pycache__`, and `target` returned zero hits.

## Method

1. Blob size scan for files under 200 bytes and note-only content.
2. Path scan for `target/`, `node_modules/`, `__pycache__/`, `*.pyc`, `dist/`.
3. Presence of `.github/workflows`, README, LICENSE, `.gitignore`, tests or a verifier, and docs.

## Findings

No committed build-artifact trees on inspected branches. Small files under 200 bytes are config, SPDX identifiers, or intentional redirects, not API-spec placeholders.

Priority line still has CI, README, LICENSE, language-aware `.gitignore`, and at least one test or verifier. No dual implementation was justified.

| Repo | CI | README | LICENSE | gitignore | tests/verifier | note |
| --- | --- | --- | --- | --- | --- | --- |
| Q-Reg | yes | yes | yes | yes | test_vectors.py | Idris not typechecked in CI |
| kerna-ledger | yes | yes | AGPL text + SPDX file | yes | tests/test_kerna_verify.py | umbrella; qreg_engine.py redirects |
| kerna-ledger-vci | yes | yes | MIT | yes | tests/ | packet + Merkle |
| vera-enterprise-engine | yes | yes | MIT | yes | tests/test_ledger.py | SQLite ledger |
| phi-boundary-commitments | yes | yes | MIT | yes | tests/test_phi.py | notebook stub documented |
| GridPulse | yes | yes | MIT | yes | tests/test_receipt.py | demo |
| aethersound | yes | yes | MIT | yes | tests/test_determinism.py | Rust + UE5 |
| psi-alpha-quantum | yes | yes | MIT | yes | tests/test_process_matrix.py | research |
| kerna-denali | yes | yes | MIT | yes | tests/test_denali_receipt.py | receipt node |
| denali-whitepaper | yes | yes | MIT | yes (tightened) | tests/test_whitepaper.py | paper |
| denali-kerna-psi-demo | yes | yes | MIT | yes | tests/test_receipt.mjs | scoped demo |

`cyberpunk-web-daw` remains archived. Do not unarchive. `qreg-scratch-ci-test` is an explicit non-canonical fixture (`ARCHIVE.md`); it had no `.gitignore`.

Throughput and latency figures in READMEs were not re-measured.

## Changes this pass

- Added this audit and `scripts/portfolio_hygiene.py` (deterministic local contract, not a stub).
- Added `.gitignore` to `qreg-scratch-ci-test`.
- Extended `denali-whitepaper/.gitignore` with `target/`, `.vercel/`, venv, and pytest caches.
- Updated tracking issue #32.
- No source replacements. No artifact deletions (none present).

## Remaining debt

1. Idris sketches are not typechecked in CI. Do not add a workflow that pretends they are.
2. README RPS and latency claims stay unverified until a checked-in benchmark emits them.
3. `vera-packet-runtime/LICENSE` is a short custom evaluation grant (376 bytes). Not rewritten.
4. GitHub license API may still report `NOASSERTION` on kerna-ledger and Q-Reg until detection refreshes.
5. `qreg-scratch-ci-test` should be archived only after confirming no workflow still depends on it.
6. `deepsignal` is a static carousel site with CI and LICENSE; no tests beyond HTML presence. Acceptable for that scope.
