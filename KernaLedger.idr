-- KernaLedger.idr (umbrella pointer)
-- The actual Idris 2 formal development (dependent types, totality,
-- gate logic, linear lifecycle, provenance, moat) lives in:
--
--   https://github.com/jabrahns-source/Q-Reg/tree/main/formal
--
-- Files: Compliance.idr, GateLogic.idr, LinearLifecycle.idr,
--        Provenance.idr, Moat.idr, Deadlines.idr, Erasure.idr,
--        RustBridge.idr, Tests.idr, Workflow.idr, Theory.md
--
-- This file exists only so the umbrella repository is not empty of
-- formal-surface references and to guide auditors to the verified source.

module KernaLedger

-- Intentionally minimal. See Q-Reg/formal for the real proofs.
-- Any expansion here would introduce duplication and risk divergence.
