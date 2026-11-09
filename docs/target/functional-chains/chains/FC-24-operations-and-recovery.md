# FC-24 — Observability, incidents, continuity and owner-specific recovery

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-14](FC-14-identity-and-policy.md), [FC-16](FC-16-platform-lifecycle.md), [FC-18](FC-18-diagnostics-and-audit.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** A deployed or local product becomes degraded, a handoff fails, an import is disputed, or an operator initiates a controlled recover/replay action.

**Expected final outcome:** A bounded incident trace, legitimate owner intervention and independently verifiable recovered or explicitly degraded state without falsifying past effects.

**Owner(s) of state and decisions:** Every product for its own runtime/business data; kOA-Linux/host agents for platform-level recovery; diagnostic owners for proof; C0 for nonsecret coordination.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Detect | Owning product / admitted probes | health, error, lag, integrity signals → scoped incident | Differentiate UI uptime, API readiness, task completion and source correctness |
| 2 | Correlate | Owner systems | request IDs + receipts → owner-safe trace | No transfer of secret payloads to C0/public dashboard |
| 3 | Contain | Actual enforcing owner | risk classification → authorized pause/quarantine/deny | No diagnostic tool gets unrestricted emergency credentials |
| 4 | Diagnose | Independent diag / owner | pinned logs and subject → root-cause candidate and evidence | No change to operational state merely because a diagnosis exists |
| 5 | Recover | Correct state owner | rollback/replay/rebuild → measured recovered or degraded condition | Derived views rebuild; durable owner effects reconcile; platform rollback distinct |
| 6 | Close and learn | Owner + safe C0 projection | terminal state/evidence → dated closure and requirement updates | Retain traceability, avoid retroactive false success |

## Interfaces and authority gates

Each failure axis uses the lifecycle in 03. There is no single universal rollback: restoring a Koali surface must not mutate a Konnaxion vote, Moodle course or Orgo Case.

## Failure, privacy and forbidden shortcuts

Missing authoritative host observation, inconclusive async effects, broken key rotation, data loss or cross-tenant leakage require explicit escalation; never silently downgrade to optimistic status.

## Definition of done — acceptance and negative tests

Test crash/restart, lost network, log privacy, orphaned operations, idempotent replay, conflicting receipt, recovery with previous signed artifact, reader freshness after rebuild and public status truthfulness.

## Required code and contract alignment

Owner implementation: add correlation IDs and minimally sufficient event/receipt propagation at agreed boundaries; bind runbooks to actual owner recovery actions and independent verification.

## Product-specific notes

Cross-chain recovery is a coordination process among owners, not C0 commandeering their services.

## Source anchors and verification boundary

kOA-Linux operations/readiness docs, Orgo outbox behavior, Koali Spaces required probes, C0 incident and rollback references, owner diagnostics.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
