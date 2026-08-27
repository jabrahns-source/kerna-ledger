//! Kerna-Ledger umbrella daemon skeleton.
//! Canonical compliance runtime lives in jabrahns-source/Q-Reg.
//! This binary exists so Cargo.toml is a real crate, not a dangling manifest.

fn main() {
    println!("kerna-ledger-daemon 0.1.0");
    println!("canonical engine: https://github.com/jabrahns-source/Q-Reg");
    println!("this crate is the umbrella map, not the production runtime");
}

#[cfg(test)]
mod tests {
    #[test]
    fn crate_name_is_stable() {
        assert_eq!(env!("CARGO_PKG_NAME"), "kerna-ledger-daemon");
    }
}
