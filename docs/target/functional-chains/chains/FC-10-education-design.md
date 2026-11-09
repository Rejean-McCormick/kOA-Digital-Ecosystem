# FC-10 — Situation design, learning capsules and supervised missions

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-21](FC-21-creative-assets.md), [FC-14](FC-14-identity-and-policy.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** An educator selects an age/context-appropriate situation, prepares a capsule and decides whether to keep it simulated or request supervised real work.

**Expected final outcome:** A reviewed situation/lesson/mission blueprint with safe roles, assessment intent, non-executable preview and optional authorized Orgo intent.

**Owner(s) of state and decisions:** Kontexte for reusable situations; Kompose for pedagogy, plan/simulation; Akor for collaborative role missions; educators for approval.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Design situation | Kontexte | source scenario, cultural scope, inclusion rules → situation model | Versioned owner context; student-sensitive data minimized |
| 2 | Compose lesson | Kompose | Kontexte situation + curriculum goals → capsule/plan and simulation | Simulation explicitly marked; no real Task in preview |
| 3 | Assign mission roles | Akor | approved capsule → role-specific, accessible mission previews | Participant visibility and collaboration rules enforced |
| 4 | Teacher review | Educator / institution | previews → approved/rejected learning intent | Only explicitly authorized actor can switch to real execution |
| 5 | Optionally request work | Kompose/Akor → Orgo | approved intent → request for real Case/Task | Orgo independently authorizes and creates owner-owned work |
| 6 | Reflect/assess | Educational owner | supervised outcomes → learning review | Assessment is educational data, not semantic canon or Orgo execution truth |

## Interfaces and authority gates

`B-EDU-01/02/03` are proposed. Contracts must distinguish preview, dry-run, intent and real action; do not import the civic DecisionRecord profile as a shortcut.

## Failure, privacy and forbidden shortcuts

No direct Orgo database write, no automatic autonomous mission activation, no exposed minor/student data, and no confused roles between learning participation and administrative execution.

## Definition of done — acceptance and negative tests

Test diverse group participation, declined teacher approval, false-positive simulated activity, idempotent intent replay, partial mission completion, child-safe content classification and blocked unauthorized Orgo invocation.

## Required code and contract alignment

Owner implementation: formalize Kontexte→Kompose capsule schema, Kompose/Akor→Orgo intent schemas and institution-specific permissions; make dry-run mandatory in previews.

## Product-specific notes

Education modules can be independent components within an Ékole experience; this diagram does not require a microservice per classroom component.

## Source anchors and verification boundary

Kontexte, Kompose and Akor READMEs plus Ekole teacher-preview owner specs; B-EDU-01/02/03.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
