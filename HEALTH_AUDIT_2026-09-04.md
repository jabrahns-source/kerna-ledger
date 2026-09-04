# Portfolio health audit — 2026-09-04

Owner: jabrahns-source (Even The Odds Foundry). Scope: all 24 public repositories.
Method: recursive trees, size scan (<200 B), artifact scan, CI/README/LICENSE/.gitignore/tests.
Prior pass: HEALTH_AUDIT_2026-09-03.md. This pass re-verified every tree.

## Artifact scan

**Zero committed build artifacts** (`target/`, `node_modules/`, `__pycache__/`, `.pyc`, `dist/`) in any of the 24 trees.

## Classification (do not invert)

### Production / strategic cores (keep expanding here)

| Repo | Tree health | CI | LICENSE | Tests | Action this pass |
|------|-------------|----|---------|-------|------------------|
| Q-Reg | Real engine + formal/*.idr + rust runtime + python | 2 workflows | Apache-2.0 text (GitHub API still NOASSERTION; official text is abbreviated) | python + rust + verification/ | NOTICE + SPDX added |
| kerna-ledger | Umbrella + working `kerna_verify.py` | ci + narrative | AGPL-3.0-or-later (full text; API NOASSERTION) | test_kerna_verify | SPDX-LICENSE-IDENTIFIER + this audit |
| kerna-ledger-vci | Hash/merkle/VERA packet + 5 workflows | yes | MIT | hash + merkle | none required |
| kerna-ledger-verified | Idris2 examples + Zig receipt | yes | MIT | zig tests | none required |
| vera-enterprise-engine | FastAPI ledger package | yes | MIT | test_ledger | none required |
| vera-packet-runtime | Packet + checkout helper | yes | short custom | import test | none required |
| phi-boundary-commitments | src + 4 verifiers + paper | yes | MIT | test_phi | notebooks/README for Untitled62.ipynb |
| GridPulse | index.html + receipt.py | yes | MIT | test_receipt | none required |
| aethersound | Rust + Coq + UE5 | yes | MIT | verifier.py/rs | none required |
| psi-alpha-quantum | process_matrix | 5 wf | MIT | yes | none required |
| kerna-exact-matrix | Zig + Idris Matrix.idr | yes | MIT | examples | none required |
| kerna-denali | receipt module | yes | MIT | yes | none required |
| denali-whitepaper | paper + pages | pages/validate | MIT | n/a | docs-only OK |
| denali-kerna-psi-demo | static + pages API | pages | MIT | none | keep as demo |

### Adjacent product / operator

| Repo | Status |
|------|--------|
| unignorable | Outreach corpus + CLI + tests. Healthy. |
| pactkit | Python contract engine + tests. Healthy. |
| pactly | Next/Supabase/Stripe surface. No unit tests (tracked debt). |
| hq-bind | Small real commitment module + tests. |
| aethersync | sync_core + tests. Healthy enough. |
| siege-os | Thin operator CLI + tests. |
| deepsignal | Single HTML carousel. Acceptable. |
| gemma4-coder-gguf-runner | Docker/compose/systemd. No unit tests. |

### Archive / do not expand

| Repo | Decision |
|------|----------|
| cyberpunk-web-daw | No application source. ARCHIVE.md already present. GitHub-archive. |
| qreg-scratch-ci-test | Scratch CI sandbox. Pointers already refuse to act as verifier. GitHub-archive. |

## Placeholder policy (reconfirmed)

Files under 200 bytes that are **intentional sentinels** (redirects, config, SPDX stubs):

- kerna-ledger `qreg_engine.py`, `api/gridpulse_hf_master.py`, `KernaLedger.idr` — pointers to Q-Reg / GridPulse. Expanding them would fork the engine.
- qreg-scratch-ci-test `kerna_verify.py`, `build_vectors.py` — refuse-to-run sentinels.
- Tiny configs (`next.config.mjs`, `dependabot.yml`, `requirements.txt`) are not placeholders.

Do not replace sentinels with a second Q-Reg. Canonical runtime stays in Q-Reg.

## Remaining debt (honest)

1. Q-Reg Idris2 modules are specifications; GHA does not replay `idris2 --check`.
2. Q-Reg Apache LICENSE is abbreviated vs official Apache-2.0 blob; license API reports NOASSERTION.
3. kerna-ledger LICENSE is AGPL-3.0-or-later; GitHub license API reports NOASSERTION because of preamble wrapping.
4. Formal claims (F_83 primality, 200 ms finality, MEV resistance) are tracked, not CI-proved.
5. Live CAISO OASIS ingest is still a demo/fallback, not a verified production adapter.
6. `Untitled62.ipynb` in phi-boundary-commitments should be renamed (content kept; pointer added).
7. Archive the two empty/scratch repos on GitHub Settings (this automation cannot flip the archive bit).
8. pactly / gemma4 / deepsignal / denali demo lack unit tests.

Zero stochastic drift. Pointers stay pointers. Engines stay in Q-Reg / VERA / exact-matrix / verified.
