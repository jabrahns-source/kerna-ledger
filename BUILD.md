# Build & Run

The executable surface is the **Q-Reg** repository.

```bash
git clone https://github.com/jabrahns-source/Q-Reg.git
cd Q-Reg
python -m venv venv
source venv/bin/activate   # or Windows equivalent
pip install -r requirements.txt
python qreg_engine.py --demo
python kerna_verify.py --ledger ledger.jsonl --check-merkle --validate-signatures
python remediation_report_gen.py
```

Formal proofs (Idris 2) live under `Q-Reg/formal/`.

This umbrella repository (`kerna-ledger`) is the citation and navigation root only.
