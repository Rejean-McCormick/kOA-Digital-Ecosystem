# FC-08 — Durable operational execution and accountability

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** Orgo / Konnaxion / Interaction-Kernel.

**Initiator:** A trusted owner submits a typed intent for real work under actual permission.

**Expected result:** Receiver-owned Case/Task and reconciled terminal effects; optional civic accountability.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Validate intent | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | create Signal/Case/Tasks | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | journal outbox | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | execute | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | reconcile | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 6 | publish terminal impact. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** B-CIVIC-01, B-CIVIC-02, B-EDU-02, B-EDU-03. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

Acceptance is not success; retries cannot duplicate external effects; unauthorized preview produces no Task.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Crash/replay, changed-intent conflict, owner PEP denial and terminal impact tests.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Preserve Orgo ownership and two-sided IK test fixtures; adopt separate educational intent only with owner approval.

## Source anchors and verification boundary

See the [53-repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
