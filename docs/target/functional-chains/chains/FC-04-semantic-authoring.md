# FC-04 — Canonical Kristal authoring and conformance

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** Kristal-Framework / Kristal-Authoring-Kit / Arketype.

**Initiator:** An authorized author selects an exact compatible semantic profile and workspace.

**Expected result:** Validated local Kristal state and reproducible candidate build, not a public release.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Pin profile | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | declare KQ/KP/KA/KS | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | separate language dictionaries | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | validate | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | build locally. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** B-KNOW-03 to B-KNOW-08. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

Wrong profile, invalid semantic namespace or unreviewed mapping is rejected; labels never rename semantic identity.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Deterministic local build and negative schema fixtures; no publish side effect.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Freeze exact Framework v11/Kit v4 draft compatibility before broad migrations; templates remain nonnormative.

## Source anchors and verification boundary

See the [53-repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
