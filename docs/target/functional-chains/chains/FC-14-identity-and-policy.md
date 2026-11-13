# FC-14 — Scoped identity, policy and actual enforcement

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** Konfid / Daat / each owner PEP.

**Initiator:** A workload requests a specific action on a resource within a tenant and purpose.

**Expected result:** Bound allow/deny decision and separate effect-point enforcement receipt.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Authenticate | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | bind actor/resource/digest | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | decide policy | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | enforce at PEP | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | journal result. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** B-SEC-01. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

Expired policy, missing identity/audit provider, wrong tenant and substituted digest fail closed.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Permission/denial and bypass tests prove no effect on a rejected request.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Connect Konfid/host-injected Daat rules to actual enforcing products, never a universal root permission.

## Source anchors and verification boundary

See the [repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
