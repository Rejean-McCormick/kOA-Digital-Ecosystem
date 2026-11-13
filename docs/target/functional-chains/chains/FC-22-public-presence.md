# FC-22 — Public discovery, docs portal and explanatory scenarios

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** HomePage-initkoa.org / initkoa-docs / Koali-Scenario-Mosaic / C0.

**Initiator:** A visitor requests a public explanation of the ecosystem or a functional capability.

**Expected result:** Accessible dated public page linking to canonical owner and accurately classified functional requirements.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Select approved C0 projection | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | build local site | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | label status | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | publish with site owner consent. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** TBD; read-only public export. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

A public editorial example is not evidence of production operation; no private source or secrets.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Navigation, bilingual routes, source pin, stale manifest and false-green status tests.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Use a safe generated public architecture manifest in all three independent presentation products.

## Source anchors and verification boundary

See the [repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
