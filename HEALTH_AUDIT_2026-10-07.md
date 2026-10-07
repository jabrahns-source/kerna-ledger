# Portfolio health audit 2026-10-07

Scope: all 25 repositories owned by `jabrahns-source` (search `user:jabrahns-source`, total_count 25, incomplete_results false). Recursive trees inspected on the default branch for the priority line and adjacent substrates.

Inspected: Q-Reg, kerna-ledger, kerna-ledger-vci, vera-enterprise-engine, phi-boundary-commitments, GridPulse, aethersound, psi-alpha-quantum, kerna-denali, denali-whitepaper, denali-kerna-psi-demo, kerna-exact-matrix, hq-bind, vera-packet-runtime, kerna-ledger-verified, aethersync, Kerna_Vera_VCI (293 blobs).

## Method

1. Blob size scan for files under 200 bytes and note-only content.
2. Path scan for `target/`, `node_modules/`, `__pycache__/`, `*.pyc`, `dist/`, `.vercel/`.
3. Presence of `.github/workflows`, README, LICENSE, `.gitignore`, tests or a verifier, and docs.

## Findings

No committed `target/`, `node_modules/`, `__pycache__/`, `*.pyc`, `dist/`, or `.vercel/` trees on the inspected branches. `Kerna_Vera_VCI` size (about 1841 KB) is source plus `.grok` skill references and one design image, not a dependency dump. `screenshots/.gitkeep` is 0 bytes and intentional. Small files under 200 bytes there are config or barrel modules (`src/lib/utils.ts`, `src/lib/multiplayer/index.ts`), not API-spec notes.

Priority repos already carry CI, README, LICENSE, language-aware `.gitignore`, and at least one test or verifier:

| Repo | CI | README | LICENSE | gitignore | tests/verifier | note |
| --- | --- | --- | --- | --- | --- | --- |
| Q-Reg | yes | yes | yes | yes | test_vectors.py, verify_gate_logic.py | Idris not typechecked in CI |
| kerna-ledger | yes | yes | AGPL text + SPDX file | yes | tests/test_kerna_verify.py | umbrella; qreg_engine.py is a hard redirect |
| kerna-ledger-vci | yes | yes | MIT | yes | tests/ | packet + Merkle surface |
| vera-enterprise-engine | yes | yes | MIT | yes | tests/test_ledger.py | SQLite ledger |
| phi-boundary-commitments | yes | yes | MIT | yes | tests/test_phi.py | notebook stub documented in NOTE_NOTEBOOK.md |
| GridPulse | yes | yes | MIT | yes | tests/test_receipt.py | demo HTML + receipt.py |
| aethersound | yes | yes | MIT | yes | tests/test_determinism.py | Rust core + UE5 sources |
| psi-alpha-quantum | yes | yes | MIT | yes | tests/test_process_matrix.py | process-matrix research |
| kerna-denali | yes | yes | MIT | yes | tests/test_denali_receipt.py | receipt node |
| denali-whitepaper | yes | yes | MIT | yes | tests/test_whitepaper.py | paper, not a runtime |
| denali-kerna-psi-demo | yes | yes | MIT | yes | tests/test_receipt.mjs | scoped demo |
| kerna-exact-matrix | yes | yes | MIT | yes | zig examples | Idris proofs not in CI |
| kerna-ledger-verified | yes | yes | MIT | yes | zig/src/tests.zig | Idris examples not typechecked |

`qreg_engine.py` in this umbrella remains an intentional `SystemExit` redirect to `jabrahns-source/Q-Reg`. Canonical engine stays there. Do not duplicate logic here.

`cyberpunk-web-daw` is archived (`archived: true` on 2026-10-07). No scaffold. Leave archived.

`vera-packet-runtime/LICENSE` remains a short custom evaluation grant (376 bytes). Not rewritten.

Throughput and latency figures in READMEs were not re-measured in this pass.

## Changes this pass

- Added this audit.
- Updated tracking issue #32.
- No source replacements: no broken runtime was found that would justify a new dual implementation.
- No artifact deletions: none were present.

## Remaining debt

1. Idris sketches (`KernaLedger.idr`, `Q-Reg/formal/*.idr`, `kerna-exact-matrix/proofs/Matrix.idr`, `kerna-ledger-verified/idris2/proofs/examples/*.idr`) are not typechecked in CI. Adding that requires an Idris 2 runner image and totality check, not a placeholder workflow.
2. README RPS and latency claims stay unverified until a checked-in benchmark emits them.
3. `Kerna_Vera_VCI/artifacts/imagine_images/` design image may stay or move; not a build artifact.
4. GitHub license API may still report `NOASSERTION` on this repo until detection refreshes; `SPDX-LICENSE-IDENTIFIER` is `AGPL-3.0-only`.
5. Do not archive further repos without owner confirmation. `cyberpunk-web-daw` is already archived.
