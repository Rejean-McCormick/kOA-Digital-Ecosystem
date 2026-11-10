# FC-07 — Civic participation and finalized decisions

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** Konnaxion / Konnaxion-Worlds.

**Initiator:** An admitted participant proposes, deliberates and finalizes under a scoped World authority.

**Expected result:** Finalized owner DecisionRecord with legitimacy and accountable follow-up reference.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Admit civic context | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | deliberate | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | authorize finalization | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | emit bounded operation intent | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | observe impact. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** B-CIVIC-01, B-CIVIC-03. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

Wrong World, forged finalization or cross-tenant influence is rejected; an Orgo Task is not a civic DecisionRecord.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Authorized finalization plus denial, exact decision provenance and intact civic state.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Version-pin WorldRelease and Konnaxion IK intent/impact profiles with independent Orgo receiver.

## Source anchors and verification boundary

See the [53-repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
