# FC-18 — Independent diagnostics and time-scoped evidence

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** KristalDiag / KonnaxionDiag / LevelUpDiag tools / kOA C0.

**Initiator:** An owner requests a qualification campaign against an exact source, dependency and verifier revision.

**Expected result:** Scoped diagnostic verdict and safe evidence metadata, not a release or deploy permission.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Pin subject | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | run checks/negative fixtures | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | publish verdict | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | owner review | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | safe C0 projection. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** B-KNOW-07. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

A code snapshot, workflow or empty branch report cannot be labeled tested/deployed.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Verifier independence, negative fixtures and altered evidence rejection; no secret audit publication.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Standardize owner-specific receipts and let C0 publish only evidence classified for its audience.

## Source anchors and verification boundary

See the [repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
