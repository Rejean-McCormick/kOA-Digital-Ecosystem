# FC-13 — Editorial documents and reviewed multilingual publication

**Classification:** `TARGET_DESIGN` — final-system requirement, **not proof of integration or deployment**.

**Inherits:** [System model](../00-system-model.md), [authority](../01-authority-and-ownership.md), [contracts and receipts](../02-contract-and-receipts.md), [failure rules](../03-state-trust-and-failure.md).

## Functional promise

**Owner(s):** Spek / SemantiK-Architect / site publishers.

**Initiator:** An authorized editor selects releasable content and an intended public audience.

**Expected result:** Reviewed accessible editorial artifact with version, provenance and publication approval.

## Nominal end-to-end behavior

| Step | Stage | Required outcome |
|---|---|---|
| 1 | Select licensed source | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 2 | draft wording | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 3 | compose Spek document | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 4 | human review | Scoped owner state and evidence receipt; no hidden mutation of other systems |
| 5 | release. | Scoped owner state and evidence receipt; no hidden mutation of other systems |

## Interfaces and authority gates

**Target boundary references:** B-LANG-02. These identify candidate or scoped adopted contracts; they do not certify complete multi-owner deployment. Producer disclosure and receiving-owner admission are separate decisions.

Where no exact interface is adopted, keep `TBD` rather than inventing a protocol ID. All privileged effects must be checked at the actual enforcing owner.

## Failure, privacy and forbidden shortcuts

Machine-generated text and a semantic source do not automatically authorize public publishing.

Owner-specific tenant/actor identity, source classification, integrity checks, replay and correction must be preserved. No debug dashboard or public documentation site may disclose private content.

## Definition of done — acceptance and negative tests

Human refusal, access class, locale and correction/withdrawal tests.

To qualify the full chain, pin both producer and consumer revisions and execute negative fixtures, recovery and idempotency scenarios. An owner code snapshot alone does not demonstrate running behavior.

## Required code and contract alignment

Adopt editor-owned manifest and a separately authorized public publishing destination.

## Source anchors and verification boundary

See the [repository portfolio](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md) for source member names, hashes, declared local roots and evidence limitations. Contract boundaries are catalogued in [the C0 target ledger](../../BOUNDARIES.md). This is intended final behavior, not evidence of a currently operational multi-repository integration.
