# FC-02 — Durable source, snapshot and representation custody

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** Mediatheque / Mediatheque-blank.

**Initiator:** A permitted source provider deposits reviewed evidence into the selected library instance.

**Expected result:** Custody receipt and immutable source/snapshot/representation references under library ACL.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Authorize deposit | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | checksum source | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | preserve version | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | issue receiver receipt | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | serve permission-filtered references. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** B-KNOW-01, B-KNOW-02. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

Reject modified bytes, conflicting replay and cross-instance private reads; custody never validates epistemic truth.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Same-intent replay yields same receipt; divergent replay denied; permissioned recovery works.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Pin Skope sender and Mediatheque receiver schema and prove durable storage plus isolated library instance.

## Source anchors and verification boundary

See the [53-repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
