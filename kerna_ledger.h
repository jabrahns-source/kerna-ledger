/*
 * kerna_ledger.h — C ABI surface for the Kerna-Ledger substrate
 *
 * This header is a stable declaration of the core types and functions
 * that any language binding (Rust, Zig, Python via cffi, etc.) must
 * honour. The actual implementations live in the production runtimes
 * (Q-Reg Rust core, vera-enterprise-engine, etc.).
 *
 * Even The Odds Foundry — 2026
 */

#ifndef KERNA_LEDGER_H
#define KERNA_LEDGER_H

#include <stdint.h>
#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Gate states — must match the Idris formalisation */
typedef enum {
    KERNA_GATE_GREEN          = 0,
    KERNA_GATE_YELLOW         = 1,
    KERNA_GATE_BLACK          = 2,
    KERNA_GATE_PIPELINE_ERROR = 3
} kerna_gate_t;

/* Opaque sealed record handle */
typedef struct kerna_record kerna_record_t;

/* Create a new sealed record from canonical JSON bytes.
 * Returns NULL on failure. Caller owns the returned pointer.
 */
kerna_record_t *kerna_record_create(const uint8_t *json, size_t len,
                                    const uint8_t *privkey_32);

/* Free a record */
void kerna_record_free(kerna_record_t *r);

/* Extract the gate decision (after successful creation) */
kerna_gate_t kerna_record_gate(const kerna_record_t *r);

/* Extract the 32-byte SHA-256 leaf hash */
int kerna_record_leaf_hash(const kerna_record_t *r, uint8_t out[32]);

/* Verify a signature against a public key. Returns 1 on success. */
int kerna_verify(const uint8_t *msg, size_t msg_len,
                 const uint8_t *sig_64, const uint8_t *pubkey_32);

#ifdef __cplusplus
}
#endif

#endif /* KERNA_LEDGER_H */
