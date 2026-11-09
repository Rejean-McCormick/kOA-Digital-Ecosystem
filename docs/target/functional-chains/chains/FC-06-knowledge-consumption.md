# FC-06 — Derived knowledge, context preparation and exploration

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-04](FC-04-semantic-authoring.md), [FC-05](FC-05-knowledge-release.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** A reader, application or local tool requests a particular authorized semantic collection or derived view at a pinned revision.

**Expected final outcome:** Read-only, provenance-preserving navigation, context packs, encyclopedia articles or static views that never modify canonical Kristal state.

**Owner(s) of state and decisions:** Kristal Integration Pack for read transforms; Kompiler for context; Konstellation/Light for navigation; EncyKlopedia for public encyclopedia reading.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Resolve collection | Reader or context client | collection reference + access context → admissible pinned release | Visibility and exact release index validated |
| 2 | Project read schema | Integration Pack | Framework v11 semantic graph → approved derived read view | Retains semantic IDs, owner provenance, explicit lexical resolution state |
| 3 | Prepare context | Kompiler | approved derived view + scoped task → bounded Context Pack | No truth certification, semantic writeback or unbounded model context |
| 4 | Navigate | Konstellation / Light | authorized collection → graph search/read navigation | Private/public limits, namespace and static/offline compatibility enforced |
| 5 | Serve encyclopedia | EncyKlopedia | approved read products → multilingual article/search API | Separate acquisition engine remains Skope/EncyK |
| 6 | Refresh safely | Consumer | new authorized revision → validated rebuild/swap | Never silently replace a pinned view with incompatible source |

## Interfaces and authority gates

B-KNOW-10 through B-KNOW-13 are target. Consumer implementations may opt in separately; EncyKlopedia is not required to be a consumer of every canonical Kristal collection.

## Failure, privacy and forbidden shortcuts

No consumer may mint KQ/KP, validate canon, publish on behalf of an owner, expose private metadata, or call lexical fallback a verified human translation.

## Definition of done — acceptance and negative tests

Test same IDs across locales/clients, direct/fallback/missing label handling, private filtering, stale view visibility, invalid signature/digest/schema denial, offline static import and rebuild without changing source.

## Required code and contract alignment

Owner implementation: adopt one exact read-index/read-view compatibility matrix and run independent Pack→Kompiler, Pack→EncyKlopedia, public→Konstellation/Light fixtures.

## Product-specific notes

Public encyclopedic content may be editorially curated; such curation needs an explicit editorial owner and is not a rewrite of semantic canon.

## Source anchors and verification boundary

Integration Pack, Kompiler, Konstellation, Konstellation-Light and EncyKlopedia owner READMEs; B-KNOW-10/11/12/13.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
