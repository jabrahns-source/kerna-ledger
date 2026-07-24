# Empirical Proof Report

The live, executable empirical validation for the deterministic gate + Merkle + Ed25519 pipeline is maintained inside the Q-Reg repository:

- `test_vectors.py` + `test_vectors.jsonl` (9-vector adversarial suite)
- `kerna_verify.py` (clean-room recomputation of Merkle roots and signature validation)
- `qreg_engine.py --demo` produces a sealed ledger that can be independently verified

Run the suite there. Results are deterministic and reproducible on any machine with the stated Python dependencies.

This file in the umbrella repo is intentionally a pointer only.
