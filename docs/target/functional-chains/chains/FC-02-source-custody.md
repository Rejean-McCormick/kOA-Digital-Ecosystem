# FC-02 — Source custody, snapshots and media preservation

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-01](FC-01-research-and-acquisition.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** An admitted source provider deposits source evidence or an instance administrator imports a local collection.

**Expected final outcome:** Durable custody objects with verified source identity, snapshot and representation records, hashes, permissions and a receiver-owned acceptance receipt.

**Owner(s) of state and decisions:** Médiathèque shared engine; independently controlled Médiathèque library instances, including `Mediatheque-blank`; depositing owner.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Admit | Library instance owner | source package, owner/tenant identity → admission decision | Policy and library/instance boundary checked before writing |
| 2 | Validate | Médiathèque engine | candidate source/snapshot/files → digest and structure check | Fail closed on invalid bytes, unsupported format or ownership scope |
| 3 | Preserve | Médiathèque instance | validated source → Source/Snapshot/Representation/FileVersion references | One stable source identity; versioned immutable evidence and checksums |
| 4 | Acknowledge | Médiathèque instance | accepted write → durable custody receipt | Duplicate with same intent returns prior receipt; conflicting replay denied |
| 5 | Serve references | Médiathèque instance → authorized consumers | custody identifiers → permission-filtered references | No silent source download or raw media disclosure |

## Interfaces and authority gates

`B-KNOW-01` for Skope intake and `B-KNOW-02` for reference presentation are target edges; other consumers such as UCKK/Ékole require separately adopted library adapter contracts.

## Failure, privacy and forbidden shortcuts

A storage receipt is neither a quality judgment nor semantic canon; application/tenant library isolation must survive operator tools and template instances.

## Definition of done — acceptance and negative tests

Prove accepted/duplicate/conflicting import, checksum corruption, blocked inter-instance access, unauthorized private source fetch, backup/recovery, and referential integrity of Snapshot/Representation versions.

## Required code and contract alignment

Owner implementation: define one version-pinned package and durable receipt between Skope and the Médiathèque receiver; test `Mediatheque-blank` isolation and instance-local storage.

## Product-specific notes

The shared engine is code; each library instance owns its data. A source can remain private forever even after it becomes available for controlled semantic authoring.

## Source anchors and verification boundary

Médiathèque engine and blank-instance owner READMEs; B-KNOW-01 and B-KNOW-02; supplied code has import/export tooling.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
