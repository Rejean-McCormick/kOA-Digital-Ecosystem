# FC-19 — Portable Kristal artifacts, offline readers and transaction rehearsal

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-04](FC-04-semantic-authoring.md), [FC-05](FC-05-knowledge-release.md), [FC-06](FC-06-knowledge-consumption.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** An authorized owner wants to move an approved local artifact to an isolated device or make an authorized static read copy, without assuming network service.

**Expected final outcome:** A verifiable portable package or static read surface with explicit release scope, integrity, optional encryption, import receipt and safe restoration.

**Owner(s) of state and decisions:** Kontainer for integrity/encryption of portable packages; Authoring Kit/Manager for authored state; Konstellation Light for local/static reading; Konstellation Publisher for fail-closed rehearsal.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Freeze input | Content/instance owner | local state or approved read surface → pinned immutable export manifest | Private vs public classification and dependencies pinned |
| 2 | Package | Kontainer or owner tool | approved source + metadata → portable integrity-checked container | Encryption where required; keys never stored in public manifests |
| 3 | Transfer | Operator / trusted medium | package → offline device/collection | No automatic release permission inferred from possession |
| 4 | Verify/import | Target owner / Konstellation Light | manifest + digests/keys → admitted local read instance | Exact schema and trust requirements enforced |
| 5 | Rehearse publication | Publisher tool | approved release plan → dry-run transaction evidence | No live remote write unless separately authorized and implemented |
| 6 | Recover | Target owner | failed import or package corruption → safe refusal or previous state | No destructive partial import |

## Interfaces and authority gates

Konstellation Publisher owner snapshot explicitly describes transaction rehearsal, **not live deployment**. Portable integrity and read feasibility do not prove public collection authorization.

## Failure, privacy and forbidden shortcuts

Reject wrong password/key, corrupted package, unapproved public export, private field leakage, incompatible reader version and duplicated conflicting import.

## Definition of done — acceptance and negative tests

Test offline import, tamper rejection, encrypted/no-key denial, reproducible manifest, locale fallback in static viewer, partial transfer recovery and explicit no-network default.

## Required code and contract alignment

Owner implementation: standardize optional container manifest and static read contract; demonstrate read-only offline validation before extending to live publication.

## Product-specific notes

This chain enables local-first use without mandating kOA-Linux, an online account, Koali Spaces or a public repository.

## Source anchors and verification boundary

Kontainer, Konstellation-Light, Konstellation-Publisher and Kit owner READMEs; B-KNOW-08/09/13 when relevant.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
