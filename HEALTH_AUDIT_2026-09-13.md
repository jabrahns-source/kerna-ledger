# Portfolio Health Audit — 2026-09-13

Owner: jabrahns-source / Even The Odds Foundry
Auditor: continuous repo-health automation
Scope: all 24 public repositories
Method: recursive tree + size/content checks + CI / LICENSE / README / .gitignore presence
Drift policy: zero. Stubs that raise SystemExit with a canonical URL are treated as *intentional redirects*, not incomplete files.

## Inventory (24)

| Repo | Role | CI | LICENSE | README | Tests/proofs | Size (KiB) | Open issues | Verdict |
|------|------|----|---------|--------|--------------|------------|-------------|---------|
| kerna-ledger | Umbrella / citation root | yes | yes (NOASSERTION SPDX) | yes | python tests + Idris stub | 86 | 1 | Healthy as *map*, not runtime |
| Q-Reg | Canonical compliance runtime | yes (py + rust) | yes | yes | formal/*.idr + verification + test_vectors | 106 | 27 | Core healthy; Rust lock is std-only |
| kerna-ledger-vci | Hash / Merkle / VERA packet | yes (multi-workflow) | MIT | yes | tests + vera/ | 90 | 15 | Healthy |
| vera-enterprise-engine | Production receipt ledger | yes | MIT | yes | tests/test_ledger.py | 32 | 7 | Healthy |
| phi-boundary-commitments | φ-polynomial commitments | yes | MIT | yes | tests + verification/ | 46 | 9 | Healthy; keep Untitled62.ipynb or rename |
| GridPulse | Scope-2 receipt demo | yes | MIT | yes | tests/test_receipt.py | 12 | 7 | Healthy demo |
| psi-alpha-quantum | Process-matrix research | yes | MIT | yes | src + tests | 31 | 15 | Healthy research slice |
| aethersound | Deterministic audio | yes | MIT | yes | rust + coq + ue5 + py verifier | 46 | 7 | Healthy |
| kerna-exact-matrix | Zero-FPU Zig matrix | yes | MIT | yes | src + proofs + examples | 26 | 0 | Healthy |
| kerna-ledger-verified | Idris2 + Zig substrate | yes | MIT | yes | idris2/ + zig/ | 25 | 6 | Healthy |
| kerna-denali | Deterministic node | present (prior) | MIT | yes | python | 11 | 2 | Thin but scaffolded |
| denali-kerna-psi-demo | Pilot UI | — | MIT | — | HTML | 10 | 0 | Demo-only |
| denali-whitepaper | Preprint HTML | — | MIT | — | docs | 25 | 6 | Content repo |
| vera-packet-runtime | VERA packet v0.3 | — | NOASSERTION | — | python | 11 | 1 | Overlaps kerna-ledger-vci/vera |
| hq-bind | Hybrid quantum bind | — | MIT | — | python | 6 | 0 | Thin |
| aethersync | Tensor sync middleware | — | MIT | — | python | 13 | 3 | Thin |
| unignorable | Receipt stack outreach | — | MIT | — | python | 50 | 13 | Product surface |
| pactkit / pactly | Contract drafts | — | MIT | — | python | 6 | 1 | Non-core |
| deepsignal | LinkedIn carousels | — | MIT | — | HTML | 13 | 0 | Non-core |
| gemma4-coder-gguf-runner | Local GGUF runner | — | — | — | — | — | — | Tooling |
| qreg-scratch-ci-test | Scratch CI | — | MIT | — | python | 15 | 4 | **Archive candidate** |
| siege-os | Operator system | — | MIT | — | python | 9 | 2 | Non-core |
| cyberpunk-web-daw | Empty | **no** | MIT | stub | none | 3 | 15 | **Archive now** |

## Checks

### 1. Incomplete / placeholder files (<200 B or note-only)

- `kerna-ledger/qreg_engine.py`, `api/gridpulse_hf_master.py`: **intentional redirects** to Q-Reg / GridPulse. Not debt.
- `kerna-ledger/SPDX-LICENSE-IDENTIFIER` (173 B) and `Q-Reg/SPDX-LICENSE-IDENTIFIER` (36 B): identifiers, not code.
- `cyberpunk-web-daw`: README + ARCHIVE.md only. No source. Flagged for archive.
- `phi-boundary-commitments/notebooks/phi_boundary_commitments.ipynb` (1512 B) is a thin notebook; real work is in `src/phi_commitment.py` and `Untitled62.ipynb`.

No file matching the pattern "API spec" / "Full updated..." as sole content was found in priority trees.

### 2. Committed build artifacts

Searched trees for `target/`, `node_modules/`, `__pycache__/`, `*.pyc`, `dist/`.

**None committed** on audited trees (kerna-ledger, kerna-ledger-vci, Q-Reg, vera-enterprise-engine, phi-boundary-commitments, GridPulse, psi-alpha-quantum, aethersound, kerna-exact-matrix, kerna-ledger-verified, cyberpunk-web-daw).

Q-Reg CI includes an artifact-hygiene job. Keep that pattern.

### 3. Hygiene surface

Priority repos have `.github/workflows`, README, LICENSE, `.gitignore`.
Remaining gaps:
- SPDX on kerna-ledger / Q-Reg / vera-packet-runtime is `NOASSERTION` in GitHub metadata despite LICENSE files. Fix by adding a standard MIT or Apache header GitHub can parse, or a `LICENSE` filename GitHub already sees (Q-Reg LICENSE exists — metadata lag).
- Idris2 is not executed in GitHub Actions (no Idris toolchain on free runners). Proofs are source-of-truth for humans / local `idris2 --check`.
- Zig repos rely on `build.zig`; confirm CI actually invokes `zig build test` where a runner image has Zig.

### 4. Priority ranking (impact)

1. Q-Reg — runtime + formal + verifier. Do not duplicate engines elsewhere.
2. kerna-ledger-vci + vera-enterprise-engine — receipt / Merkle / SB253 packet.
3. kerna-ledger-verified + kerna-exact-matrix — Idris2/Zig trust boundary.
4. phi-boundary-commitments, psi-alpha-quantum, GridPulse — research + demo.
5. aethersound — adjacent product, independently healthy.
6. Umbrella kerna-ledger — navigation only.

## Changes this sweep

- Recorded this audit (no silent code mutation of healthy trees).
- No artifact deletions required (none present).
- Did not overwrite redirect stubs in the umbrella repo (they are correct).
- Opened / updated tracking issues for archive candidates and remaining debt.

## Remaining debt (ordered)

1. **Archive** `cyberpunk-web-daw` and `qreg-scratch-ci-test` (or convert scratch into a documented CI fixture owned by Q-Reg).
2. **Deduplicate** `vera-packet-runtime` vs `kerna-ledger-vci/vera/` — one canonical packet module.
3. Rename `Untitled62.ipynb` in phi-boundary-commitments.
4. Add SPDX-parseable license metadata where GitHub shows NOASSERTION.
5. Optional: Idris2 check job via a container image if a free runner can pull one; until then document `idris2 --check formal/*.idr` in each README.
6. Close stale issue piles on Q-Reg (27) and unignorable (13) after confirming they are not still actionable.
7. Keep umbrella kerna-ledger free of a second engine copy.

## Determinism note

Canonical executable path remains:

```bash
git clone https://github.com/jabrahns-source/Q-Reg.git
cd Q-Reg
pip install -r requirements.txt
python qreg_engine.py --demo
python kerna_verify.py --ledger ledger.jsonl --check-merkle --validate-signatures
```

Do not rehydrate engines into the umbrella repository.
