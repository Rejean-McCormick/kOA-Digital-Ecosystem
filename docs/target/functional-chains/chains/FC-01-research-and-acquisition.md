# FC-01 — Bounded research and noncanonical acquisition

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** Skope / integrated EncyK.

**Initiator:** An authorized researcher selects a finite research profile and permitted providers.

**Expected result:** A reviewed source/candidate batch with provenance and exact export digest.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Skope selection | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | integrated EncyK extraction | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | reviewer acceptance | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | noncanonical export. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** B-KNOW-01, B-KNOW-14. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

Unapproved provider, unbounded import or corrupted digest is denied; research candidate never becomes canon automatically.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Repeatable synthetic export; source/licence trace; candidate rejected without downstream effect.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Adopt a source-evidence export profile with a named receiving library and receiver idempotency tests.

## Source anchors and verification boundary

See the [repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
