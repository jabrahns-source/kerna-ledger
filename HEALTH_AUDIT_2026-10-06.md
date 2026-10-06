# Portfolio health audit 2026-10-06

Scope: all public and private repositories owned by `jabrahns-source` (25). Priority line inspected with recursive trees: Q-Reg, kerna-ledger, kerna-ledger-vci, vera-enterprise-engine, phi-boundary-commitments, GridPulse, aethersound, psi-alpha-quantum, denali-whitepaper, kerna-denali, denali-kerna-psi-demo, vera-packet-runtime, Kerna_Vera_VCI, cyberpunk-web-daw.

## Method

- Tree walk for blobs under 200 bytes and note-only files.
- Path search for `target/`, `node_modules/`, `__pycache__/`, `*.pyc`, `dist/`.
- Presence check: `.github/workflows`, README, LICENSE, `.gitignore`, tests, docs.

## Findings

No committed `target/`, `node_modules/`, `__pycache__/`, `*.pyc`, or `dist/` trees were found on the inspected default branches. Code search for `filename:.pyc` and `path:target` under the user returned zero hits.

`kerna-ledger/LICENSE` is the GNU AGPL v3 full text (about 35 KB), not a placeholder. GitHub reports SPDX `NOASSERTION` because the file has no machine identifier. This commit adds `SPDX-LICENSE-IDENTIFIER` with `AGPL-3.0-only`. The grant was not rewritten.

`qreg_engine.py` is an intentional `SystemExit` redirect to `jabrahns-source/Q-Reg`. `tests/test_kerna_verify.py` asserts that redirect. It is not a silent stub. Canonical engine stays in Q-Reg to avoid dual sources of truth.

`Kerna_Vera_VCI/ARTIFACTS.md` claimed committed `.vercel/output/**`. Recursive tree filter on `.vercel` returned empty on 2026-10-06. Remaining non-source blob: `artifacts/imagine_images/f5454902-eeba-4470-9beb-6c79b4aab3d4.jpg` (209350 bytes). `package-lock.json` is a lockfile, not a build artifact.

`cyberpunk-web-daw` has README, LICENSE, `.gitignore`, and `ARCHIVE.md`, and no application source. Flag for archive. Do not scaffold.

`vera-packet-runtime/LICENSE` is a short custom evaluation grant (376 bytes), not MIT. Leave it; do not silently relicense.

Priority repos already have CI workflows, README, LICENSE, gitignore, and at least one test or verifier. Idris files are not typechecked in CI. Throughput claims in READMEs are not reproduced by this audit.

## Changes this pass

- Added `SPDX-LICENSE-IDENTIFIER` (`AGPL-3.0-only`).
- Added this audit.
- Updated issue #32.
- Corrected stale artifact note in `Kerna_Vera_VCI`.

## Remaining debt

1. GitHub license detection may still say NOASSERTION until a license API refresh; the SPDX file is the machine marker.
2. Idris sketches (`KernaLedger.idr`, `Q-Reg/formal/*.idr`) are not in CI.
3. Do not treat README latency or RPS figures as measured until a checked-in benchmark emits them.
4. Archive `cyberpunk-web-daw` when the owner confirms.
5. Decide whether `artifacts/imagine_images/` in `Kerna_Vera_VCI` stays as design source or moves out of the repo.
