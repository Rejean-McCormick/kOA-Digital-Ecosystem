# FC-05 — Independent qualification and immutable knowledge publication

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** KristalDiag / Kristal-Manager / kristal-public / Konstellation-Publisher.

**Initiator:** An owner submits an exact local build for independent checks and a separate scoped release decision.

**Expected result:** Immutable authorized release reference or an explicit denial, with qualification and publication receipts separate.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Register candidate | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | independent verify | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | request permission | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | publish atomically | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | reconcile or withdraw. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** B-KNOW-07 to B-KNOW-09. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

Green build/diagnostic never grants public permission; private bytes and wrong revision block release.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Exact-subject approval, no-grant rejection, idempotent publication and recovery fixtures.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Implement verified build→authorization→publisher boundaries with no automatic Git remote write.

## Source anchors and verification boundary

See the [53-repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
