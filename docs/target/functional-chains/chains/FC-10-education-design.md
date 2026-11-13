# FC-10 — Pedagogical situations, plans and supervised missions

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** Kontexte / Kompose / Akor.

**Initiator:** A teacher selects a situation and drafts a lesson, preview or collaborative mission.

**Expected result:** Reviewed learning plan, simulated capsule or separately approved real-work intent.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Select scenario | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | compose plan | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | assign learning roles | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | preview | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | teacher approval | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 6 | optional Orgo request. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** B-EDU-01 to B-EDU-03. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

Simulation is not real work; underage privacy and mismatched teacher authority block effects.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

No Case/Task after preview; teacher denial and role isolation, accepted supervised intent.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Agree Kontexte→Kompose and Kompose/Akor→Orgo minimal schema and dry-run enforcement.

## Source anchors and verification boundary

See the [repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
