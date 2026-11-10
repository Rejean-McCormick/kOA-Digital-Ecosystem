# FC-06 — Read-only knowledge consumers and context views

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** Kristal-Integration-Pack / Kompiler / EncyKlopedia / Konstellation / Konstellation-Light.

**Initiator:** A reader chooses an authorized immutable release revision and locale.

**Expected result:** Provenance-preserving rebuildable read view, context pack or encyclopedia navigation without canonical write.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Validate release index | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | derive view | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | apply permission filters | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | render locale coverage | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | rebuild when admitted. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** B-KNOW-10 to B-KNOW-13. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

No private/stale index, unknown digest, unapproved fallback or writeback; EncyKlopedia does not acquire sources.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Three independent consumer imports and negative privacy/fallback fixtures.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Align one derived read-view schema across Integration Pack and independently adopted clients.

## Source anchors and verification boundary

See the [53-repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
