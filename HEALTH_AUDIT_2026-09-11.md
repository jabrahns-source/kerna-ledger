# Health Audit — 2026-09-11

Owner: jabrahns-source (Even The Odds Foundry)
Auditor: continuous repo-health automation
Scope: all 24 owned repositories (23 public + 1 private scratch)
Method: GitHub search (user:jabrahns-source, total_count=24) + recursive trees on core and satellite repos + size classification + CI / LICENSE / README / tests scan
Principle: zero stochastic drift. Documented redirects are not silent placeholders. Do not fork Q-Reg into the umbrella.

## Artifact hygiene

Committed `target/`, `node_modules/`, `__pycache__/`, `*.pyc`, `dist/`: **none found** in any audited tree this cycle.

## Portfolio matrix (re-verified 2026-09-11)

| Repo | CI | LICENSE | README | Tests | Health |
|------|----|---------|--------|-------|--------|
| Q-Reg | ci + gridpulse-verification | yes | yes | vectors + verification + Idris sources | Canonical engine. Healthy. |
| kerna-ledger | ci + gridpulse-narrative | AGPL file present; API NOASSERTION | yes | pytest + cargo scaffold | Umbrella + documented redirects. |
| kerna-ledger-vci | ci/pages/release/security/validate | MIT | yes | hash + merkle | Healthy. |
| vera-enterprise-engine | ci | MIT | yes | ledger tests | Healthy production package. |
| phi-boundary-commitments | ci | MIT | yes | tests + verification/ | Untitled62.ipynb rename debt. |
| GridPulse | ci | MIT | yes | receipt tests | Demo surface healthy. |
| aethersound | ci + determinism | MIT | yes | python + rust verifier | Healthy. |
| psi-alpha-quantum | ci + pages + security | MIT | yes | process-matrix | Healthy. |
| denali-kerna-psi-demo | pages | MIT | short | static | Demo. |
| kerna-denali | ci | MIT | short | receipt tests | Healthy. |
| denali-whitepaper | pages/validate | MIT | yes | n/a | Docs. |
| kerna-ledger-verified | yes | MIT | yes | zig tests | Formal substrate. |
| kerna-exact-matrix | yes | MIT | yes | examples + proofs | Zero-FPU. |
| vera-packet-runtime | yes | commercial | yes | import-level | Packet surface. |
| hq-bind | ci | MIT | yes | commitment tests | Thin but functional. |
| aethersync | ci | MIT | short | sync_core tests | Functional. |
| siege-os | ci | MIT | long | siege tests | Functional. |
| unignorable | present historically | MIT | yes | — | 13 open issues; product surface. |
| pactkit / pactly | present | — | — | — | Adjacent products. |
| gemma4-coder-gguf-runner | — | — | — | — | Tooling. |
| deepsignal | — | — | — | — | Content. |
| cyberpunk-web-daw | none | MIT | ARCHIVE.md | none | **Archive candidate.** |
| qreg-scratch-ci-test | private | MIT | — | — | **Archive candidate.** |

## Placeholder classification

Size < 200 B that are **not** debt: SPDX files, dependabot.yml, one-line requirements, module `__init__` headers.

Intentional documented redirects in `kerna-ledger` (do not replace with a second engine):
- `qreg_engine.py` — SystemExit to Q-Reg
- `api/gridpulse_hf_master.py` — GridPulse
- `api/vercel_index.py` — vera-enterprise-engine

True remaining debt:
1. GitHub License API `NOASSERTION` on kerna-ledger (LICENSE starts with a copyright preamble; Linguist/licensee often wants the AGPL title as line 1). Fix is Settings → License picker or a LICENSE whose first line is the AGPL banner. Not rewritten this cycle to avoid a 35 kB churn commit.
2. `phi-boundary-commitments/Untitled62.ipynb` still at repo root. Canonical code is `src/phi_commitment.py`. Named notebook added this cycle under `notebooks/`.
3. Idris2 proof replay is not on GitHub-hosted runners.
4. CAISO live ingest remains offline-vector / demo.
5. Duplicate health issues #1 #2 #3 #24 #25 #26 #27 — collapse onto the latest issue.
6. Archive: `cyberpunk-web-daw`, `qreg-scratch-ci-test` (settings action; flagged only).
7. Q-Reg issue pile (27) and unignorable (13) need a human sweep, not more engines.

## Changes this cycle

- This audit file and STATUS.md date bump.
- phi-boundary-commitments: add `notebooks/phi_boundary_commitments.ipynb` as a real, executable notebook over `src.phi_commitment` (does not delete Untitled62).
- Close stale duplicate health issues on this repo as duplicates of the current tracking issue.

## What was not done (and why)

- No second Q-Reg engine written into kerna-ledger.
- No invented formal proofs.
- No archive API call (GitHub archive is a repository-settings action).
- LICENSE body not rewritten (risk of license-text drift).

Even The Odds Foundry — deterministic health pass.
