# FC-15 — Bounded agentic planning and approved owner effects

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** Konductor / owner adapters.

**Initiator:** An operator submits a limited AI job with tools, purpose, budget and review checkpoints.

**Expected result:** Inspectible plan, approved typed external request and terminal owner receipt when relevant.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Define job | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | propose | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | reviewer checkpoint | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | owner-admitted action | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | reconcile | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 6 | resume/cancel. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** TBD; no general adopted Konductor→Orgo profile. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

Model text is a proposal; prompt-injection instructions cannot execute privileged actions.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Tool allowlists, spoofed resource, interrupted job, duplicate request and owner denial tests.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Implement a narrow job-state executor and one independently admitted owner adapter before generalization.

## Source anchors and verification boundary

See the [53-repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
