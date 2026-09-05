//! Kerna-Ledger umbrella daemon.
//! Canonical compliance runtime lives in jabrahns-source/Q-Reg.
//! This binary is a Cargo-valid citation map plus a std-only
//! deterministic checksum of the umbrella witness (no FPU, no time).

const WITNESS: &[u8] = b"KERNA_LEDGER_UMBRELLA_V3_DETERMINISTIC";
const F_83_ASCII: &[u8] = b"99194853094755497";

/// FNV-1a 64-bit. Stable across rustc versions; not a security hash.
fn fnv1a64(chunks: &[&[u8]]) -> u64 {
    const OFFSET: u64 = 0xcbf29ce484222325;
    const PRIME: u64 = 0x100000001b3;
    let mut h = OFFSET;
    for chunk in chunks {
        for b in *chunk {
            h ^= *b as u64;
            h = h.wrapping_mul(PRIME);
        }
    }
    h
}

fn main() {
    let digest = fnv1a64(&[WITNESS, F_83_ASCII]);
    println!("kerna-ledger-daemon 0.1.1");
    println!("canonical engine: https://github.com/jabrahns-source/Q-Reg");
    println!("umbrella_fnv1a64={digest:016x}");
    println!("this crate is the umbrella map, not the production runtime");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn crate_name_is_stable() {
        assert_eq!(env!("CARGO_PKG_NAME"), "kerna-ledger-daemon");
    }

    #[test]
    fn checksum_is_deterministic() {
        let a = fnv1a64(&[WITNESS, F_83_ASCII]);
        let b = fnv1a64(&[WITNESS, F_83_ASCII]);
        assert_eq!(a, b);
        assert_ne!(a, 0);
    }
}
