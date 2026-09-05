module KernaLedger

-- Umbrella formal surface for the citation root.
-- Canonical proofs remain in Q-Reg/formal and kerna-ledger-verified/idris2.
-- This module is total and records the *map* so auditors can typecheck
-- the index without forking a second compliance engine.

%default total

public export
data CanonicalRepo
  = QReg
  | KernaVerified
  | VeraEnterprise
  | KernaVCI
  | ExactMatrix
  | PhiBoundary
  | GridPulse
  | PsiAlpha

public export
canonicalPath : CanonicalRepo -> String
canonicalPath QReg           = "jabrahns-source/Q-Reg"
canonicalPath KernaVerified  = "jabrahns-source/kerna-ledger-verified"
canonicalPath VeraEnterprise = "jabrahns-source/vera-enterprise-engine"
canonicalPath KernaVCI       = "jabrahns-source/kerna-ledger-vci"
canonicalPath ExactMatrix    = "jabrahns-source/kerna-exact-matrix"
canonicalPath PhiBoundary    = "jabrahns-source/phi-boundary-commitments"
canonicalPath GridPulse      = "jabrahns-source/GridPulse"
canonicalPath PsiAlpha       = "jabrahns-source/psi-alpha-quantum"

public export
data Role = ComplianceEngine | VerifiedSubstrate | ReceiptSaaS | PacketRuntime | ExactALU | Commitment | Demo | Fairness

public export
roleOf : CanonicalRepo -> Role
roleOf QReg           = ComplianceEngine
roleOf KernaVerified  = VerifiedSubstrate
roleOf VeraEnterprise = ReceiptSaaS
roleOf KernaVCI       = PacketRuntime
roleOf ExactMatrix    = ExactALU
roleOf PhiBoundary    = Commitment
roleOf GridPulse      = Demo
roleOf PsiAlpha       = Fairness

||| There is exactly one compliance engine in the family.
export
uniqueEngine : (r : CanonicalRepo) -> roleOf r = ComplianceEngine -> r = QReg
uniqueEngine QReg           Refl = Refl
uniqueEngine KernaVerified  prf  = absurd prf
uniqueEngine VeraEnterprise prf  = absurd prf
uniqueEngine KernaVCI       prf  = absurd prf
uniqueEngine ExactMatrix    prf  = absurd prf
uniqueEngine PhiBoundary    prf  = absurd prf
uniqueEngine GridPulse      prf  = absurd prf
uniqueEngine PsiAlpha       prf  = absurd prf
