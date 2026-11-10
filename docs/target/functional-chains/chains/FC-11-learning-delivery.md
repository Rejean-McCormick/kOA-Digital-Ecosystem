# FC-11 — Neutral education engine and institutional projections

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** Ekole / Ekole-Pastorale / UCKK-Assets / UCKK-Ops-Console.

**Initiator:** An educational authority approves a content pack and optional institutional projection.

**Expected result:** Rebuildable learning experience and permissioned Moodle/institution receipt.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Validate pack | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | import | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | class preview | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | institution consent | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | optional Moodle write | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 6 | reconcile. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** B-EDU-04. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

Preview never writes to Moodle; a media reference grants no private library access.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Idempotent approved import and denial of unapproved course/tenant operations.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Pin content-pack, media and institutional write/projection contracts with owner consent.

## Source anchors and verification boundary

See the [53-repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
