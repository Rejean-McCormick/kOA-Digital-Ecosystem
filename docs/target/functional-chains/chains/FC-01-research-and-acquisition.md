# FC-01 — Bounded research and noncanonical acquisition

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** None required; this chain can start independently.  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** A researcher or authorized local operator selects a named scope, provider set and review purpose.

**Expected final outcome:** A reproducible research batch with provenance, stable candidate references and explicitly noncanonical export.

**Owner(s) of state and decisions:** Skope; integrated EncyK source-acquisition modules; external data providers as non-authoritative inputs.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Select scope | Skope | named research profile, approved provider selectors → bounded recipe | Scope and provider restrictions are recorded; no arbitrary unbounded crawl |
| 2 | Collect | Skope / integrated EncyK | permitted provider sources → raw/source references and candidate QIDs | External IDs are labeled as external and retrieval failures are visible |
| 3 | Inspect | Research reviewer | candidate batch → accepted/rejected research subset | Review distinguishes preserved source bytes from inferred or extracted claims |
| 4 | Freeze package | Skope | reviewed batch → immutable handoff digest, provenance and intended classification | Export is deterministic for a pinned recipe and source snapshot |
| 5 | Request custody | Skope → Médiathèque, optional | evidence package → custody request | No automatic semantic approval or public Git write |

## Interfaces and authority gates

`B-KNOW-01` is proposed; confirm the exact producer payload, provenance requirements, engine-vs-instance receiver, access policy and receiver receipt. FC-02 is not a synchronous dependency for local research.

## Failure, privacy and forbidden shortcuts

Unsafe provider payload, denied sources, missing origin, over-limit scope, corrupted export and retry with altered digest must fail or quarantine; do not present acquisition as fact checking.

## Definition of done — acceptance and negative tests

Given a pinned synthetic recipe, repeated export yields the same content identity; a missing source produces a bounded error; a reviewer can reject candidates; replay at the receiver is idempotent; malformed or unauthorized evidence cannot enter custody.

## Required code and contract alignment

Owner implementation: align Skope export with a Médiathèque intake fixture and durable receipt; retain the split between Skope integrated EncyK acquisition and the separate EncyKlopedia reader.

## Product-specific notes

Not every local research run has to enter Kristal. Research can terminate with a private report; upstream content licensing and retention must be checked before later public reuse.

## Source anchors and verification boundary

Skope README and config/extraction-profiles in the owner snapshot; target edge B-KNOW-01.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
