# FC-03 — Mapping, reviewed external alignment and lexicon

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** Daat / diK / Kristalizer / SenTient.

**Initiator:** An approved mapping reviewer selects admissible external and lexical evidence.

**Expected result:** Versioned reversible mapping proposal, lexical catalog and explicit approval state.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Validate external references | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | propose crosswalk | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | inspect homonyms | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | resolve locale coverage | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | stage reviewed import. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** B-KNOW-02 to B-KNOW-05, B-KNOW-14, B-SEC-01. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

Reject external Q/P as implicit KQ/KP, unknown actor, collision, wrong Framework draft and unreviewed machine-generated candidate.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Allowed/denied candidate, missing locale and namespace mismatch fixtures pass without canonical writes.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Adopt diK/Kristalizer/Daat Kit import schemas with review and rollback receipts.

## Source anchors and verification boundary

See the [repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
