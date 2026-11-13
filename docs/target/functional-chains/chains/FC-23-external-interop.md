# FC-23 — Typed owner-to-owner and third-party exchange

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** Interaction-Kernel / Daat / two actual owner products.

**Initiator:** Two parties adopt an exact bounded contract for an identity-scoped exchange.

**Expected result:** Receiver-owned admission and terminal effect receipt, or an explicit rejection.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Agree profile | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | authenticate | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | map allowed fields | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | validate | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | execute owner effect | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 6 | reconcile. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** B-CIVIC-01, B-CIVIC-02, B-SEC-01. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

No global mandatory bus, unauthenticated mapping or sender direct-write to receiver database.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Golden/invalid envelope, downgrade, replay conflict and PEP denial fixtures.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Introduce adopted profile ID only after bilateral owner review and a passing consumer test.

## Source anchors and verification boundary

See the [repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
