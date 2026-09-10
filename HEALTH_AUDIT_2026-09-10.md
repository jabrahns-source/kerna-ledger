# Health Audit — 2026-09-10

Owner: jabrahns-source (Even The Odds Foundry)
Auditor: continuous repo-health automation
Scope: all 24 owned repositories (23 public + 1 private scratch)
Method: recursive git trees + size/content classification + CI presence + license/.gitignore/README scan
Principle: zero stochastic drift. Documented stubs are not treated as silent placeholders.

## Artifact hygiene (all repos)

Committed `target/`, `node_modules/`, `__pycache__/`, `*.pyc`, `dist/`: **none found**.

## Portfolio matrix

| Repo | Lang | CI | LICENSE | README | Tests | Notes |
|------|------|----|---------|--------|-------|-------|
| Q-Reg | Python + Rust + Idris | yes (ci + gridpulse-verification) | yes | yes + badges | yes (vectors + verification) | Canonical engine. Thin files: SPDX identifier, CONTRIBUTING. Not placeholders. |
| kerna-ledger | Python + Rust scaffold | yes | AGPL file present; GitHub API still NOASSERTION | yes + badges | yes | Umbrella. Intentional redirects: qreg_engine.py, api/*. |
| kerna-ledger-vci | Python | yes (ci/pages/release/security/validate) | MIT | yes | yes | VERA packet + merkle + hash |
| vera-enterprise-engine | Python | yes | MIT | yes | yes | Production ledger package |
| phi-boundary-commitments | Python + notebook | yes | MIT | yes | yes + verification/ | Rename debt: Untitled62.ipynb |
| GridPulse | HTML + Python | yes | MIT | yes | yes | Demo surface |
| aethersound | Rust + C++ + Coq | yes (ci + determinism) | MIT | yes | verifier.py/rs; adding pytest wrapper this cycle | UE5 bindings present |
| psi-alpha-quantum | Python | yes | MIT | yes | yes | Process-matrix core |
| denali-kerna-psi-demo | HTML + Next stub | pages.yml | MIT | short | no pytest (static demo) | next.config/package.json thin but functional |
| kerna-denali | Python | yes | MIT | short | yes | Receipt node |
| denali-whitepaper | Markdown + HTML | pages/validate | MIT | yes | n/a (docs) | |
| kerna-ledger-verified | Idris2 + Zig | yes | MIT | yes | zig/src/tests.zig | Formal substrate |
| kerna-exact-matrix | Zig + Idris | yes | MIT | yes | examples + proofs | Zero-FPU |
| vera-packet-runtime | Python | yes | custom commercial | yes | import test only | Packet + Stripe checkout |
| unignorable | Python | (not re-scored this pass) | MIT | — | — | Receipt stack; 13 open issues |
| pactkit / pactly | Python / TS | — | — | — | — | Adjacent product surface |
| gemma4-coder-gguf-runner | Dockerfile | — | — | — | — | Tooling |
| deepsignal | HTML | — | — | — | — | Content |
| hq-bind | Python | — | — | — | — | Protocol sketch |
| aethersync | Python | — | — | — | — | Tensor sync |
| siege-os | Python | — | — | — | — | Operator system |
| cyberpunk-web-daw | none | no | MIT | archive README | no | ARCHIVE.md present — archive candidate |
| qreg-scratch-ci-test | Python | (private) | MIT | — | — | Scratch; archive candidate |

## Incomplete / placeholder classification

Files with size < 200 bytes that are **not** debt:
- SPDX-LICENSE-IDENTIFIER, dependabot.yml, next.config.mjs, requirements one-liners, module headers.

Files that look thin but are **intentional documented redirects** (kerna-ledger):
- `qreg_engine.py` (664 B) — raises SystemExit pointing at Q-Reg
- `api/gridpulse_hf_master.py` — same for GridPulse
- `api/vercel_index.py` — 301 to vera-enterprise-engine
- `EMPIRICAL_PROOF_REPORT.md` — pointer to Q-Reg vectors

Do **not** fork Q-Reg into the umbrella. Divergence is worse than a stub.

True remaining debt:
1. GitHub License API reports `NOASSERTION` on kerna-ledger despite AGPL LICENSE file (needs UI license picker / SPDX header GitHub recognizes).
2. `phi-boundary-commitments/Untitled62.ipynb` still at repo root; notebooks/README documents preferred rename.
3. Idris2 CI replay is not installed on GitHub-hosted runners (proofs are source-of-truth, not CI-replayed).
4. CAISO live ingest remains demo/offline-vector; not a tree-health defect.
5. Open-issue pile on Q-Reg (27) and unignorable (13) needs a sweep, not more engines.
6. `cyberpunk-web-daw` and `qreg-scratch-ci-test` should be archived.
7. Duplicate health issues on kerna-ledger (#1, #2, #3, #24, #25, #26) should collapse onto the latest audit issue.

## Changes this cycle

- This audit file.
- STATUS.md date bump.
- aethersound: add `tests/test_verifier.py` so Python CI has an executable unit path beside the Rust crate.
- Tracking issue opened/updated on kerna-ledger.

## What was not done (and why)

- No second Q-Reg engine written into kerna-ledger.
- No deletion of documented stubs.
- No invented formal proofs.
- No archive API call (GitHub archive is a settings action; flagged only).

Even The Odds Foundry — deterministic health pass.
