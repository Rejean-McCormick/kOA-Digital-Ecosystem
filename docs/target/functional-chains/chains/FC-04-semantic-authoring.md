# FC-04 — Kristal semantic authoring and local conformance

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-03](FC-03-mapping-and-lexical-preparation.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** An approved author opens or creates a local Kristal workspace, optionally imports reviewed lexical/source mappings, and invokes a pinned build profile.

**Expected final outcome:** A reproducible local Kristal semantic state/build with explicit identity namespace, provenance, conformance results and no implicit publication.

**Owner(s) of state and decisions:** Kristal Framework as semantic standard; Kristal Authoring Kit as local workspace and build implementation; Arketype as optional nonnormative design material.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Choose profile | Author / Kit | approved project scope + Framework lock → workspace configuration | Exact Framework revision and conformance profile pinned |
| 2 | Declare semantic identities | Author / Framework rules | KQ/KP/KA/KS graph and typed relationships → canonical workspace draft | Identifiers are semantic, not translated terms or external Q/P IDs |
| 3 | Bind language | Author / diK tools as optional input | separate lexical catalogs → reviewed labels and language coverage | Missing/fallback labels are marked; translations do not rename graph nodes |
| 4 | Validate | Kit with Framework rules | workspace → structural/semantic diagnostics and errors | Fail on invalid namespace, referential integrity, incompatible profiles |
| 5 | Build locally | Kit | validated graph + exact tool/inputs → local artifact manifest and digest | Deterministic inputs and output; no public side effect |
| 6 | Offer qualification | Kit → KristalDiag, optional | candidate manifest → independent test request | Success remains a local candidate, not a release |

## Interfaces and authority gates

B-KNOW-06 needs mutually approved version compatibility. Framework v11/Kit v4/Integration Pack versions observed in snapshots are draft/alpha candidates, not globally qualified final API pins.

## Failure, privacy and forbidden shortcuts

External Wikidata Q/P cannot be substituted for KQ/KP; reading labels cannot define identity; Kit must never deploy to public Git from a mere successful local build.

## Definition of done — acceptance and negative tests

Test stable canonical identity across languages, crosswalk isolation, invalid KQ/KP/KA/KS, mixed-version rejection, reproducibility, preflight for private output, compatibility opt-in and safe restoration of failed workspace edits.

## Required code and contract alignment

Owner implementation: freeze a supported Framework/Kit/Pack matrix; add cross-repo approved and rejected fixtures; constrain authoring side effects to the selected local workspace.

## Product-specific notes

The authoring process may start from an empty project without FC-01/02/03. Those stages are optional enrichment, not compulsory upstream dependencies.

## Source anchors and verification boundary

Framework v11 draft.4, Authoring Kit v4 draft.4 and Arketype owner READMEs; B-KNOW-06 and downstream B-KNOW-07/08.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
