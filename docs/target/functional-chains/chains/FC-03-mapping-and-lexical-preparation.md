# FC-03 — External alignment, lexical preparation and reviewed identity proposals

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-01](FC-01-research-and-acquisition.md), [FC-02](FC-02-source-custody.md), [FC-14](FC-14-identity-and-policy.md), [FC-23](FC-23-external-interop.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** A reviewer elects to map admitted source facts, external identifiers or dictionary candidates into an approved Kristal authoring context.

**Expected final outcome:** A versioned, reviewable proposal referencing external and internal identities without assigning new canonical authority.

**Owner(s) of state and decisions:** DaaT for external mapping boundary; diK for lexical dictionaries; Kristalizer for candidate reconciliation; SenTient for experimental extraction; reviewers for approval.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Select evidence | Reviewer + source owner | permitted source references or research candidates → scoped mapping job | External provenance and visibility retained |
| 2 | Map external schema | DaaT, when explicitly adopted | foreign fields plus pinned allowlist → owner-native candidate mapping | Verified caller/actor, policy decision and audit injection; no unreviewed scripts |
| 3 | Prepare language | diK | approved KQ/KP graph reference + lexical catalogs → locale coverage and candidates | Lexical layers do not rewrite KQ/KP, and fallback is explicit |
| 4 | Reconcile identity | Kristalizer / SenTient as candidate generators | external Q/P, strings, extracted entities → candidate crosswalk and collision report | No implicit merge by spelling, shared label or provider ID |
| 5 | Approve proposal | Authorized author/reviewer | candidate → rejected, held or approved staging package | Review decision, source digest and target workspace recorded |
| 6 | Stage into Kit | Kristalizer/diK/DaaT → Kit if adopted | approved candidate → scoped Kit import request | Kit decides compatibility and applies only authorized workspace changes |

## Interfaces and authority gates

`B-KNOW-03/04/05/14` are target or optional; Framework v11 draft.4 vs diK draft.3 target requires an owner-approved compatibility matrix before declaring a final contract. DaaT 0.3.0 is documented as an offline library, **not** a deployed IK network service.

## Failure, privacy and forbidden shortcuts

Missing actor binding, unknown mapping profile, cross-tenant data, lexical ambiguity, fake Q/P→KQ/KP substitution, namespace collision, unsupported draft pins or invalid catalog hash must stop staging.

## Definition of done — acceptance and negative tests

Include matching and nonmatching QIDs, homonyms, preferred-label conflicts, direct/fallback/missing locales, invalid ACL, denied Konfid decision, offline repeatability, rollback of proposed writes and negative `draft.3`/`draft.4` compatibility fixtures.

## Required code and contract alignment

Owner implementation: select final version pins; test DaaT security PEP and diK/Kristalizer exports against Kit import fixtures. Require explicit reviewer approval and no global automatic propagation.

## Product-specific notes

Arketype templates can inform candidate authoring structure but do not confer semantic authority. SenTient is experimental and must not be reported as a production reconciliation service.

## Source anchors and verification boundary

DaaT, diK, Kristalizer and SenTient owner READMEs; B-KNOW-02 through B-KNOW-05 and B-KNOW-14.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
