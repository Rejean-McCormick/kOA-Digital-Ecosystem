# FC-19 — Portable integrity packages and static reading

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** Kontainer / Konstellation-Light / authoring owners.

**Initiator:** An authorized owner transfers a selected knowledge artifact without an online runtime.

**Expected result:** Verified offline package with manifest, read-only import and versioned rollback path.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Freeze permitted source | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | package with digest | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | transfer | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | verify/read | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | recover. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** B-KNOW-13. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

Possessing a package does not grant public release permission; corrupt bytes/wrong keys fail.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Offline repeatable import, tampered content denial and key/access-class tests.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Define optional Kontainer/export→Light reader schema; publisher rehearsal is not live deploy.

## Source anchors and verification boundary

See the [53-repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
