# FC-21 — Licensed characters, palettes and educational media

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** Karacter / Kolor / UCKK-Assets.

**Initiator:** An author creates fictional narrative or visual assets for approved educational reuse.

**Expected result:** Versioned attributable media with reviewed rights and optional content-pack reference.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Draft story | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | produce palette/sheet | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | rights review | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | package asset | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | importer approval. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** TBD; no adopted cross-studio API. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

Fictional character authority is not Kristal semantic canon; private likeness or unlicensed media blocked.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Rights, locale, accessibility, version rollback and private-content rejection fixtures.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Agree creative manifest and safe content-pack import with Kontexte/Ekole owners.

## Source anchors and verification boundary

See the [53-repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
