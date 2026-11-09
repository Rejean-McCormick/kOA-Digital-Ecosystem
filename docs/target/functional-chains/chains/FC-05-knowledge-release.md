# FC-05 — Knowledge diagnostics, instance management and authorized release

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-04](FC-04-semantic-authoring.md), [FC-18](FC-18-diagnostics-and-audit.md), [FC-19](FC-19-offline-portability.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** An author submits an exact local semantic build to independent validation, then separately requests release to a named audience and target.

**Expected final outcome:** An approved immutable release and/or eligible local instance reference, with separate qualification, authorization, publication and host lifecycle receipts.

**Owner(s) of state and decisions:** KristalDiag for independent checks; Kristal Manager for instance/sync eligibility; explicit content owner for approval; kristal-public / authorized publisher for hosted output.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Register local instance | Kristal Manager | workspace/Kit build reference → owner instance inventory | Instance registration carries no public release permission |
| 2 | Qualify candidate | KristalDiag / independent checks | exact build and dependency pins → scoped diagnostic evidence | Verifier version, failed checks and source digests retained |
| 3 | Request release | Content owner | qualified artifact + intended collection/visibility → authorization decision | Scope, audience, license, privacy and release channel explicit |
| 4 | Publish immutably | Authorized publisher / kristal-public | approved package → versioned collection index and derived outputs | Atomic publication with digest, manifest and recovery handle |
| 5 | Report receipt | Publisher and release owner | published revision → immutable reference, delivery evidence | Downstream readers can pin; no automatic host activation |
| 6 | Withdraw/supersede | Release owner | revocation/supersession request → corrected visibility and new index | Rollback preserves audit; privacy procedures handled explicitly |

## Interfaces and authority gates

`B-KNOW-07/08/09` are target links; the Manager→public edge is a proposal path and does not authorize automated pushing. Public Git commits can disclose bytes and require explicit per-Kristal consent. Konstellation-Publisher owner README describes rehearsal rather than proof of live deploy.

## Failure, privacy and forbidden shortcuts

Reject unpinned builds, missing independent checks, mismatched input hashes, unsupported license or private scope, stale approval and destinations outside authorized target; never auto-promote from Git sync.

## Definition of done — acceptance and negative tests

Test private-vs-public classification, subject digest mismatch, approval expiry, publication atomicity, duplicate release, unauthorized public destination, immutable index import, manual withdrawal and rollback/supersession.

## Required code and contract alignment

Owner implementation: prove a complete exact-input local qualification-to-publication lane with a mock public target before live permission; gate each distinct instance and scope.

## Product-specific notes

An approved hosted collection can remain read-only without any kOA-Linux deployment or Koali shell activation.

## Source anchors and verification boundary

KristalDiag, Manager, kristal-public, Konstellation-Publisher and Kontainer owner READMEs; B-KNOW-07/08/09.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
