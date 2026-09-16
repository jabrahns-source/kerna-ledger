# Portfolio Health Audit — 2026-09-16

Owner: jabrahns-source / Even The Odds Foundry  
Auditor: continuous repo-health automation  
Scope: all 24 repositories (`user:jabrahns-source`)  
Method: GitHub tree walk, size/content classification, CI / LICENSE / README / `.gitignore` presence, issue inventory  
Drift policy: zero. A file that raises `SystemExit` with a canonical URL is an **intentional redirect**, not incomplete work. Do not rehydrate engines into the umbrella.

## Executive verdict

Priority engines remain **scaffolded, licensed, CI-backed, and free of committed build artifacts**. This sweep made **no engine copies** into the umbrella repo. No `target/`, `node_modules/`, `__pycache__/`, `*.pyc`, or `dist/` blobs on any priority tree.

Delta vs 2026-09-15: tree SHAs unchanged for Q-Reg (`646e0050`), kerna-ledger-vci (`fe098e26`), vera-enterprise-engine (`953fe04a`), phi-boundary-commitments (`7d499b72`), GridPulse (`eac7270d`), aethersound (`6799710d`), psi-alpha-quantum (`ebedd44b`), kerna-exact-matrix (`cbc37251`), kerna-ledger-verified (`d36200aa`), kerna-denali (`bada1956`), cyberpunk-web-daw (`03ee0ce2`), qreg-scratch-ci-test (`71ab8a32`), vera-packet-runtime (`24635650`). Most recent product-surface push remains unignorable (2026-09-15T14:19Z). Umbrella last push before this audit: 2026-09-15T15:26Z.

## Inventory (24)

| Repo | Role | CI | LICENSE | README | Tests/proofs | Open issues | Verdict |
|------|------|----|---------|--------|--------------|-------------|---------|
| kerna-ledger | Umbrella / citation root | yes | yes (SPDX NOASSERTION; file present) | yes | tests + Idris sketch | 1 | Healthy map |
| Q-Reg | Canonical compliance runtime | yes (2 workflows) | yes | yes | formal/*.idr + verification + test_vectors | 28 | Core healthy |
| kerna-ledger-vci | Hash / Merkle / VERA packet | yes (multi) | MIT | yes | tests + vera/ | 15 | Healthy |
| vera-enterprise-engine | Production receipt ledger | yes | MIT | yes | tests/test_ledger.py | 7 | Healthy |
| phi-boundary-commitments | φ-polynomial commitments | yes | MIT | yes | tests + verification/ | 9 | Healthy; Untitled62.ipynb still untitled |
| GridPulse | Scope-2 receipt demo | yes | MIT | yes | tests/test_receipt.py | 7 | Healthy demo |
| psi-alpha-quantum | Process-matrix research | yes | MIT | yes | src + tests | 15 | Healthy research |
| aethersound | Deterministic audio | yes | MIT | yes | rust + coq + ue5 + verifier | 7 | Healthy |
| kerna-exact-matrix | Zero-FPU Zig matrix | yes | MIT | yes | src + proofs + examples | 0 | Healthy |
| kerna-ledger-verified | Idris2 + Zig substrate | yes | MIT | yes | idris2/ + zig/ | 6 | Healthy |
| kerna-denali | Deterministic node | yes | MIT | yes | src + tests | 2 | Thin but complete |
| denali-kerna-psi-demo | Pilot UI | pages-style | MIT | HTML | demo | 0 | Demo-only |
| denali-whitepaper | Preprint | — | MIT | HTML | docs | 6 | Content repo |
| vera-packet-runtime | VERA packet v0.3 | yes | short/NOASSERTION | yes | packet + tests + payment | 1 | Overlaps kerna-ledger-vci/vera |
| hq-bind | Hybrid quantum bind | yes | MIT | yes | tests | 0 | Thin, complete for size |
| aethersync | Tensor sync | yes | MIT | yes | python | 3 | Thin |
| unignorable | Receipt-stack outreach | yes | MIT | yes | python | 14 | Product surface |
| pactkit / pactly | Contract drafts | yes | MIT | yes | tests | 1 each | Non-core |
| deepsignal | LinkedIn carousels | — | MIT | HTML | — | 0 | Non-core |
| gemma4-coder-gguf-runner | Local GGUF runner | — | MIT | yes | Docker | 0 | Tooling |
| qreg-scratch-ci-test | Scratch CI | yes | MIT | yes + ARCHIVE.md | snapshot + sentinels | 4 | **Archive candidate** |
| siege-os | Operator system | yes | MIT | yes | tests | 2 | Non-core |
| cyberpunk-web-daw | Empty product shell | **no** | MIT | stub + ARCHIVE.md | none | 16 | **Archive now** |

## Checks executed this sweep

### 1. Incomplete / placeholder files (size < 200 B or note-only)

- `kerna-ledger/qreg_engine.py` (664 B) and `api/gridpulse_hf_master.py` (573 B): **intentional redirects** to Q-Reg / GridPulse. Correct. Do not rehydrate.
- `kerna-ledger/EMPIRICAL_PROOF_REPORT.md` (595 B): pointer to Q-Reg vectors. Correct.
- `qreg-scratch-ci-test/kerna_verify.py` (205 B) and `build_vectors.py` (180 B): explicit sentinels. Correct for an archive candidate.
- `cyberpunk-web-daw`: only README + ARCHIVE.md + LICENSE + .gitignore. No source. Archive.
- No committed file whose sole body is the literal notes `API spec` or `Full updated...` was found on priority trees.
- `phi-boundary-commitments/notebooks/phi_boundary_commitments.ipynb` (1512 B) is thin; executable Colab work remains in root `Untitled62.ipynb` (94 KiB). Not deleted.

### 2. Committed build artifacts

Trees scanned for `target/`, `node_modules/`, `__pycache__/`, `*.pyc`, `dist/`:

**None present** on kerna-ledger, Q-Reg, kerna-ledger-vci, vera-enterprise-engine, phi-boundary-commitments, GridPulse, psi-alpha-quantum, aethersound, kerna-exact-matrix, kerna-ledger-verified, kerna-denali, vera-packet-runtime, qreg-scratch-ci-test, cyberpunk-web-daw.

No deletions required.

### 3. CI / README / LICENSE / .gitignore

Priority repos all have `.github/workflows`, README, LICENSE, and language-appropriate `.gitignore`.

Honest gaps:
- GitHub license API reports `NOASSERTION` on kerna-ledger (large custom LICENSE) and vera-packet-runtime (short LICENSE).
- Idris2 proofs are source-of-truth; default `ubuntu-latest` runners do not ship `idris2 --check`.
- Zig CI depends on a runner image that actually has Zig.
- `cyberpunk-web-daw` has no workflow (acceptable only because it should be archived).

### 4. Priority ranking (impact, unchanged)

1. Q-Reg — only canonical engine. Never duplicate.
2. kerna-ledger-vci + vera-enterprise-engine — receipt / Merkle / SB253 packet.
3. kerna-ledger-verified + kerna-exact-matrix — Idris2 / Zig trust boundary.
4. phi-boundary-commitments, psi-alpha-quantum, GridPulse — research + demo.
5. aethersound — adjacent product, independently healthy.
6. Umbrella kerna-ledger — navigation and citations only.

## Changes this sweep (2026-09-16)

- Recorded this audit next to the 2026-09-03…15 series.
- Re-verified trees; no new artifacts, no new placeholder engines, no SHA drift on core trees.
- Did **not** overwrite redirect stubs.
- Did **not** populate `cyberpunk-web-daw` or `qreg-scratch-ci-test` with fake product code.
- Did **not** copy Q-Reg into the umbrella.
- Updated tracking issue #29 on this repository.

## Remaining debt (ordered)

1. **Archive** `cyberpunk-web-daw` and `qreg-scratch-ci-test` (Settings → Danger Zone). Human action; automation cannot archive.
2. **Deduplicate** `vera-packet-runtime` vs `kerna-ledger-vci/vera/` — keep one packet module; leave the other as a redirect README if citation URLs must survive.
3. Rename `Untitled62.ipynb` → `phi_boundary_commitments_colab.ipynb` in phi-boundary-commitments (94 KiB Colab notebook; git rename is a human/PR step to preserve SHA history cleanly).
4. Make LICENSE files GitHub-parseable (standard MIT/Apache-2.0/AGPL-3.0 + SPDX header) where metadata shows NOASSERTION.
5. Document `idris2 --check formal/*.idr` in READMEs; optional containerized proof job later.
6. Triage stale issue piles: Q-Reg (28), unignorable (14), cyberpunk-web-daw (16), psi-alpha-quantum (15), kerna-ledger-vci (15).
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
