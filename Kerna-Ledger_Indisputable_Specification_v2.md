# Kerna-Ledger Indisputable Specification v2.0

**Even The Odds Foundry · July 2026**

## 1. Purpose

This document defines the non-negotiable invariants of the Kerna-Ledger substrate. Any implementation claiming compatibility must satisfy every clause below. The specification is designed so that deviations are detectable by independent verification.

## 2. Core Invariants

### 2.1 Determinism
- All gate functions, hash functions, and sealing operations are pure and total.
- Given identical inputs and an identical cryptographic key, the output ledger is byte-for-byte identical across any conforming implementation.

### 2.2 Formal Gate Logic
- The compliance decision function maps a well-typed input record onto exactly one of {GREEN, YELLOW, BLACK, PIPELINE_ERROR}.
- The mapping is total and proven in dependent type theory (Idris 2 reference implementation in Q-Reg).

### 2.3 Cryptographic Sealing
- Every ledger record is signed with Ed25519 (RFC 8032).
- The public key is either published or included in the record in a verifiable manner.
- Signature verification must succeed for the record to be considered valid.

### 2.4 Merkle Provenance
- Records are ordered and hashed with SHA-256 under canonical JSON serialization (`ensure_ascii=True`, sorted keys).
- A Merkle root is computed over each contiguous batch; roots themselves may be chained.
- Any alteration of a leaf or reordering of records changes the root with overwhelming probability.

### 2.5 Independent Verifiability
- A clean-room verifier must be able to recompute every leaf hash and the final Merkle root from the published JSONL ledger and the public verification key.
- Failure of any recomputation renders the ledger invalid.

### 2.6 Linear Lifecycle (Delete Act / Erasure)
- Private keys and sensitive intermediate values obey linear typing discipline: they may be used exactly once and then erased.
- Erasure is proven; residual presence is a specification violation.

## 3. Interface Requirements

- Input: structured emissions / grid / consent events (JSON schema published in sibling repos).
- Output: JSONL audit ledger + optional PDF remediation report.
- Optional: StarkNet (or equivalent) ZK anchoring of daily Merkle roots.

## 4. Conformance Testing

A conforming implementation must pass the adversarial test suite published in Q-Reg (`test_vectors.jsonl`) and produce identical Merkle roots under the clean-room verifier.

## 5. Versioning

This is version 2.0. Breaking changes to any invariant require a new major version and explicit migration documentation.

---

Status: Normative. Implementations that claim Kerna-Ledger compatibility are measured against this document.
