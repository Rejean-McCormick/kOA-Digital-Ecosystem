# FC-22 — Public discovery, documentation portals and explanatory scenarios

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-13](FC-13-editorial-publishing.md), [FC-18](FC-18-diagnostics-and-audit.md), [FC-17](FC-17-application-composition.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** A public visitor wants to learn about the initiative, find the correct system or inspect trustworthy, source-attributed explanation.

**Expected final outcome:** A navigable, accessible, dated public entry point exposing safe descriptions, owner links and accurately scoped evidence.

**Owner(s) of state and decisions:** HomePage-initkoa.org for site pages; initkoa-docs for compiled documentation navigation; Koali-Scenario-Mosaic for static scenario communication; C0 for approved architecture maps; GitHub Audit for dated public audit views.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Curate sources | C0 / owner docs | approved architecture pages and release views → public-safe navigation input | Do not substitute website prose for owner normative contract |
| 2 | Build site | HomePage / initkoa-docs / Mosaic | selected contents → tested site or static explanatory scenario | Each site retains its independent content ownership |
| 3 | Check disclosure | Site publisher | public candidate → approved target audience and licenses | No private code snapshot, credential, student or health data leaks |
| 4 | Publish | Site owner | approved build → URL/version receipt | Build/deploy status separate from ecosystem capability |
| 5 | Navigate | Visitor | homepage/docs/scenario → relevant owner or functional chain | Language/accessibility, canonical links and provenance available |
| 6 | Correct | Publisher | dated finding/correction → new published revision | Avoid rewriting evidence provenance or fabricating live status |

## Interfaces and authority gates

These are presentation and information channels, not a new architecture authority. GitHub Audit consumes pinned public-safe C0 outputs only under explicit publication workflow.

## Failure, privacy and forbidden shortcuts

Deny broken/silent redirects to unauthorized endpoints, unlabeled simulations, unreviewed maturity claims, generated source disclosure or automatic deployment from a documentation edit.

## Definition of done — acceptance and negative tests

Test site builds, internal/external link validity, source pin attribution, bilingual navigation, accessibility, update/supersession, public classification and visible labels for proposed vs qualified.

## Required code and contract alignment

Owner implementation: add the new functional-chain index to documentation site navigation only after release permission; validate links and schema; keep website deployment separate from C0 local docs.

## Product-specific notes

Scenario Mosaic examples are illustrative response patterns, not a literal test harness proving those interventions are operational.

## Source anchors and verification boundary

Homepage Next.js, initkoa-docs MkDocs, Scenario Mosaic Astro owner snapshots; C0 documentation and GitHub Audit publisher README.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
