# FC-08 — Governed operations, durable tasks and civic accountability

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-07](FC-07-civic-deliberation.md), [FC-14](FC-14-identity-and-policy.md), [FC-23](FC-23-external-interop.md), [FC-18](FC-18-diagnostics-and-audit.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** An authenticated civic/education/agent owner submits an approved intent that can legitimately create real work.

**Expected final outcome:** Accepted operational work reaches an observed terminal state, or remains explicitly pending/failed, with owner-scoped accountability.

**Owner(s) of state and decisions:** Orgo for Signals, Workflows, Cases, Tasks, outbox, IntegrationOperation and effect reconciliation; Konnaxion for returned civic impact.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Admit intent | Orgo | owner-authenticated typed request → accepted/rejected Signal | Exact tenant, actor, contract and effect permissions validated |
| 2 | Create work | Orgo | admitted Signal → Workflow/Case/Task with independent identities | No external direct writes to Orgo persistence |
| 3 | Execute and journal | Orgo | Tasks → scoped actions and durable outbox | Idempotent effect keys; state changes recorded before external side effects |
| 4 | Reconcile | Orgo | effect receipts → terminal succeeded/failed/pending state | Acceptance cannot masquerade as terminal success |
| 5 | Publish impact | Orgo → Konnaxion when applicable | terminal result → admitted impact record | IK accountability profile and Konnaxion-owned interpretation |

## Interfaces and authority gates

Konnaxion/Orgo IK `governance.decision.execute/1.0.0` and `accountability.impact.publish/1.0.0` are documented as selected qualified local boundaries. Education and agents need separately adopted profiles: do not reuse civic semantics by name alone.

## Failure, privacy and forbidden shortcuts

Failure mid-effect requires terminal reconciliation; timeout/unknown result must not cause double action. Consumer status and operator UI must show pending/degraded, not always green.

## Definition of done — acceptance and negative tests

Test duplicate acceptance, changed-intent replay, outbox crash/recovery, unauthorized tenant, partial fan-out, terminal failure, slow dependencies, and Konnaxion acknowledgement of the correct DecisionRecord.

## Required code and contract alignment

Owner implementation: retain Orgo sole Task/Case authority; add separately approved educational/agentic intents with scoped access and durable receipts.

## Product-specific notes

No additional exceptions. Refer to the global contract and lifecycle rules.

## Source anchors and verification boundary

Orgo and Konnaxion owner docs; targeted local IK contract evidence in `docs/2-Technical-Reference/40-integration/orgo-konnaxion/`.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
