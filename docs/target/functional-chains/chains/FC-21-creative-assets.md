# FC-21 — Creative characters, palette and educational asset preparation

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-10](FC-10-education-design.md), [FC-11](FC-11-learning-delivery.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** An author creates fictional characters, visuals, scenes or palettes for a story, learning scenario or educational media pack.

**Expected final outcome:** A licensed and versioned creative artifact with attributable provenance, style/accessibility metadata and optional approved content-pack reference.

**Owner(s) of state and decisions:** Karacter for fictional characters/stories; Kolor for pose, palette and character-sheet production; UCKK-Assets for institution-owned content; education products for reuse approval.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Create fiction | Karacter | author brief → fictional character, narrative and simulation draft | Author controls content and avoids misrepresenting fiction as a real subject |
| 2 | Produce artwork | Kolor | approved design brief → sheets, palettes, pose/media exports | Review asset dimensions, color accessibility, licensing |
| 3 | Review assets | Creative/content owner | draft character/media → approved/rejected version | Rights, safety, audience and cultural context documented |
| 4 | Package for education | UCKK Assets or content pack owner | approved media → immutable asset reference in content pack | Separate institution and curriculum permissions |
| 5 | Consume | Kontexte/Ékole or another adopter | asset reference → lesson/layout visual | Product adapts usage but never takes creative source authority |
| 6 | Revise | Original owner | corrected asset → new version plus supersession note | Old lessons remain pinned until their owners update |

## Interfaces and authority gates

No final standard machine contract for Karacter→Kolor→Ékole is specified in the 26-edge registry. Treat file exports as optional until format and acceptance are agreed.

## Failure, privacy and forbidden shortcuts

No uncontrolled use of personal likeness, licensed third-party media, student photos or real medical/civic identities. Character simulation cannot become authoritative psychology or fact.

## Definition of done — acceptance and negative tests

Test license metadata, attribution, corrupt image rejection, palette accessibility, versioned replacement, bilingual layout, sensitive-content filters and unchanged canonical Kristal IDs.

## Required code and contract alignment

Owner implementation: agree on simple visual asset manifest and content-pack import, including review/rights records; avoid merging creative tooling into Framework semantic source code.

## Product-specific notes

An asset can be reused without requiring the knowledge pipeline; educational reuse is a separate consent/policy choice.

## Source anchors and verification boundary

Karacter and Kolor owner READMEs, UCKK-Assets docs, Kontexte/Ékole role descriptions; newly registered creative tools are separate from Kristal canon.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
