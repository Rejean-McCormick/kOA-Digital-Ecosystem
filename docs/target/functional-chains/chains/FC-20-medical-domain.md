# FC-20 — Medical knowledge under separate safety governance

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** MediKristal / MediKristal-LevelUpDiag-.

**Initiator:** An authorized domain operator requests attributable medical-domain information.

**Expected result:** Scoped informational or domain pathway feature subject to clinical/privacy policies.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Admit purpose/actor | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | resolve permitted knowledge | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | apply owner domain logic | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | review | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | record. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** TBD; external clinical systems not adopted. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

Engineering PASS never equals clinical certification; missing consent or patient isolation blocks use.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Privacy/tenant/clinical safety and stale-evidence negative test expectations.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Demand independent clinical, institutional and regulatory approval before real patient effects.

## Source anchors and verification boundary

See the [repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
