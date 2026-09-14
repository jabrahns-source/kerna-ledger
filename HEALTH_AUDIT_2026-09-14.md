# Portfolio Health Audit — 2026-09-14

Owner: jabrahns-source / Even The Odds Foundry  
Auditor: continuous repo-health automation  
Scope: all 24 public repositories (`user:jabrahns-source`)  
Method: GitHub tree walk, size/content classification, CI / LICENSE / README / `.gitignore` presence, issue inventory  
Drift policy: zero. A file that raises `SystemExit` with a canonical URL is an **intentional redirect**, not incomplete work.

## Executive verdict

Priority engines (Q-Reg, kerna-ledger-vci, vera-enterprise-engine, phi-boundary-commitments, GridPulse, aethersound, psi-alpha-quantum, kerna-exact-matrix, kerna-ledger-verified) are **scaffolded, licensed, CI-backed, and free of committed build artifacts**. This sweep made no engine copies into the umbrella repo. Remaining debt is organizational: archive two empty/scratch repos, collapse VERA packet duplication, SPDX metadata, stale issue piles, and Idris2 CI that cannot run on default GitHub-hosted runners.

## Inventory (24)

| Repo | Role | CI | LICENSE | README | Tests/proofs | GitHub size | Open issues | Verdict |
|------|------|----|---------|--------|--------------|-------------|-------------|---------|
| kerna-ledger | Umbrella / citation root | yes | yes (GitHub SPDX NOASSERTION; file is AGPL-scale) | yes + badges | tests + Idris sketch | 90 | 1 | Healthy map |
| Q-Reg | Canonical compliance runtime | yes | yes | yes | formal/*.idr + verification + test_vectors | 106 | ~27 | Core healthy |
| kerna-ledger-vci | Hash / Merkle / VERA packet | yes (multi) | MIT | yes | tests + vera/ | 90 | 15 | Healthy |
| vera-enterprise-engine | Production receipt ledger | yes | MIT | yes | tests/test_ledger.py | 32 | 7 | Healthy |
| phi-boundary-commitments | φ-polynomial commitments | yes | MIT | yes | tests + verification/ | 46 | 9 | Healthy; rename Untitled62.ipynb |
| GridPulse | Scope-2 receipt demo | yes | MIT | yes | tests/test_receipt.py | 12 | 7 | Healthy demo |
| psi-alpha-quantum | Process-matrix research | yes | MIT | yes | src + tests | 31 | 15 | Healthy research |
| aethersound | Deterministic audio | yes | MIT | yes | rust + coq + ue5 + verifier | 46 | 7 | Healthy |
| kerna-exact-matrix | Zero-FPU Zig matrix | yes | MIT | yes | src + proofs + examples | 26 | 0 | Healthy |
| kerna-ledger-verified | Idris2 + Zig substrate | yes | MIT | yes | idris2/ + zig/ | 25 | 6 | Healthy |
| kerna-denali | Deterministic node | present | MIT | yes | python | 11 | 2 | Thin scaffold |
| denali-kerna-psi-demo | Pilot UI | pages-style | MIT | HTML | demo | 10 | 0 | Demo-only |
| denali-whitepaper | Preprint | — | MIT | HTML | docs | 25 | 6 | Content repo |
| vera-packet-runtime | VERA packet v0.3 | yes | short/NOASSERTION | yes | packet + tests | 11 | 1 | Overlaps kerna-ledger-vci/vera |
| hq-bind | Hybrid quantum bind | yes | MIT | yes | tests | 6 | 0 | Thin, complete for size |
| aethersync | Tensor sync | yes (prior) | MIT | yes | python | 13 | 3 | Thin |
| unignorable | Receipt-stack outreach | yes (prior) | MIT | yes | python | 50 | 13 | Product surface |
| pactkit / pactly | Contract drafts | yes | MIT | yes | tests | 6 / 23 | 1 | Non-core |
| deepsignal | LinkedIn carousels | — | MIT | HTML | — | 13 | 0 | Non-core |
| gemma4-coder-gguf-runner | Local GGUF runner | — | MIT | yes | Docker | 6 | 0 | Tooling |
| qreg-scratch-ci-test | Scratch CI | yes (sandbox) | MIT | yes + ARCHIVE.md | snapshot + sentinels | 15 | 4 | **Archive candidate** |
| siege-os | Operator system | yes | MIT | yes | tests | 9 | 2 | Non-core |
| cyberpunk-web-daw | Empty product shell | **no** | MIT | stub + ARCHIVE.md | none | ~3 | 15 | **Archive now** |

## Checks executed this sweep

### 1. Incomplete / placeholder files (size < 200 B or note-only)

- `kerna-ledger/qreg_engine.py` (664 B) and `api/gridpulse_hf_master.py` (573 B): **intentional redirects** to Q-Reg / GridPulse. Correct. Do not rehydrate.
- `kerna-ledger/EMPIRICAL_PROOF_REPORT.md` (595 B): pointer to Q-Reg vectors. Correct.
- `qreg-scratch-ci-test/kerna_verify.py` (205 B) and `build_vectors.py` (180 B): explicit sentinels. Correct for an archive candidate.
- `cyberpunk-web-daw`: only README + ARCHIVE.md + LICENSE + .gitignore. No source. Archive.
- No committed file whose sole body is the literal notes `API spec` or `Full updated...` was found on priority trees.
- `phi-boundary-commitments/notebooks/phi_boundary_commitments.ipynb` (1512 B) is thin; executable work is `src/phi_commitment.py` plus `Untitled62.ipynb` (94 KiB).

### 2. Committed build artifacts

Trees scanned for `target/`, `node_modules/`, `__pycache__/`, `*.pyc`, `dist/`:

**None present** on kerna-ledger, Q-Reg, kerna-ledger-vci, vera-enterprise-engine, phi-boundary-commitments, GridPulse, psi-alpha-quantum, aethersound, kerna-exact-matrix, kerna-ledger-verified, hq-bind, pactkit, vera-packet-runtime, siege-os, qreg-scratch-ci-test, cyberpunk-web-daw.

No deletions required.

### 3. CI / README / LICENSE / .gitignore

Priority repos all have `.github/workflows`, README (most with badges), LICENSE, and language-appropriate `.gitignore`.

Gaps that remain honest:
- GitHub license API reports `NOASSERTION` on kerna-ledger (large custom LICENSE blob) and vera-packet-runtime (short LICENSE). File exists; GitHub classifier does not map it.
- Idris2 proofs are source-of-truth; default `ubuntu-latest` runners do not ship `idris2 --check`.
- Zig CI depends on a runner image that actually has Zig; confirm `zig build test` is invoked where `build.zig` exists.
- `cyberpunk-web-daw` has no workflow (acceptable only because it should be archived).

### 4. Priority ranking (impact, unchanged)

1. Q-Reg — only canonical engine. Never duplicate.
2. kerna-ledger-vci + vera-enterprise-engine — receipt / Merkle / SB253 packet.
3. kerna-ledger-verified + kerna-exact-matrix — Idris2 / Zig trust boundary.
4. phi-boundary-commitments, psi-alpha-quantum, GridPulse — research + demo.
5. aethersound — adjacent product, independently healthy.
6. Umbrella kerna-ledger — navigation and citations only.

## Changes this sweep (2026-09-14)

- Recorded this audit next to the 2026-09-03…13 series.
- Re-verified trees after yesterday’s sweep; no new artifacts, no new placeholder engines.
- Did **not** overwrite redirect stubs (they remain correct).
- Did **not** populate `cyberpunk-web-daw` or `qreg-scratch-ci-test` with fake product code; ARCHIVE.md already states the policy.
- Updated tracking issue #29 on this repository.

## Remaining debt (ordered)

1. **Archive** `cyberpunk-web-daw` and `qreg-scratch-ci-test` (Settings → Danger Zone). Human action; automation cannot archive.
2. **Deduplicate** `vera-packet-runtime` vs `kerna-ledger-vci/vera/` — keep one packet module, leave the other as a redirect README.
3. Rename `Untitled62.ipynb` → `phi_boundary_commitments_colab.ipynb` in phi-boundary-commitments.
4. Make LICENSE files GitHub-parseable (standard MIT/Apache-2.0/AGPL-3.0 filename + SPDX header) where metadata shows NOASSERTION.
5. Document `idris2 --check formal/*.idr` in READMEs; optional containerized proof job later.
6. Triage stale issue piles: Q-Reg (~27), unignorable (13), cyberpunk-web-daw (15), psi-alpha-quantum (15), kerna-ledger-vci (15).
7. Keep umbrella kerna-ledger free of a second Q-Reg copy.

## Deterministic run path (unchanged)

```bash
git clone https://github.com/jabrahns-source/Q-Reg.git
cd Q-Reg
pip install -r requirements.txt
python qreg_engine.py --demo
python kerna_verify.py --ledger ledger.jsonl --check-merkle --validate-signatures
```

Do not rehydrate engines into the umbrella repository.
