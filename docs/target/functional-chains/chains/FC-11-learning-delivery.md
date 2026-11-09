# FC-11 — Neutral learning engine, content packs and UCKK projections

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-10](FC-10-education-design.md), [FC-02](FC-02-source-custody.md), [FC-06](FC-06-knowledge-consumption.md), [FC-14](FC-14-identity-and-policy.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** A teacher or institution admits a versioned course/content pack, selects learning contexts and may publish a bounded projection into campus/Moodle workflows.

**Expected final outcome:** A usable learner experience and, where approved, a rebuildable institution-owned learning/Moodle projection with source and permission receipts.

**Owner(s) of state and decisions:** Ékole Core and its student/teacher interfaces; independent Ékole-Pastorale and UCKK-Assets content owners; UCKK/Ops Console and Moodle institution owner.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Prepare pack | Content owner | curriculum/media/Kristal references → signed or pinned content-pack candidate | Content pack remains independent of neutral Ékole engine |
| 2 | Import locally | Ékole | admitted pack → instructional graph and teacher/student views | Schema validation, locale and source provenance recorded |
| 3 | Preview instructional use | Teacher | module and participants → classroom plan / read-only preview | No Moodle or Orgo state mutated by preview |
| 4 | Approve institutional projection | UCKK authority | approved pack/course mapping → scoped Moodle operation plan | Institution retains enrollment and Moodle authorization |
| 5 | Materialize where approved | UCKK Ops Console / Moodle adapter | authorized plan → institution-owned learning objects | Idempotent writes, external receipt and per-resource reconciliation |
| 6 | Rebuild or withdraw | UCKK owner | pinned source plus operation receipts → corrected derived projection | No rewriting of canonical Kristal semantics |

## Interfaces and authority gates

`B-EDU-04` is proposed for Ékole→UCKK Ops Console. A Moodle write is **not** proven by a candidate plan, UI preview or engine test. Media custody via Médiathèque and semantic read models are optional and separately permissioned.

## Failure, privacy and forbidden shortcuts

Deny content packs with invalid owner/locale/licensing, unauthorized student access, unapproved direct Moodle writes, mismatched courses, cross-school tenant use and silent overwrite of institutional data.

## Definition of done — acceptance and negative tests

Test clean pack import, content withdrawal, locale fallback, isolated institution, lesson preview without writes, dry-run vs live approval, duplicate Moodle import, rollback/reconciliation and rebuildable educational projection.

## Required code and contract alignment

Owner implementation: select final content-pack schema and UCKK import/Moodle receipt protocol; keep Ékole engine neutral and independent pastoral content independently governed.

## Product-specific notes

`uckk-moodle` is in the adjacent-source survey rather than the 53-register; it may supply implementation evidence but must not be silently added as a registered first-class owner.

## Source anchors and verification boundary

Ékole, Ékole-Pastorale, UCKK-Assets, UCKK-Ops-Console and `uckk-moodle` adjacent owner docs; B-EDU-04.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
