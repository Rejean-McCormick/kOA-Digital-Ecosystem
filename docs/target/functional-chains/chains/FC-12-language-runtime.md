# FC-12 — Faithful linguistic realization and RuntimeSet qualification

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-04](FC-04-semantic-authoring.md), [FC-03](FC-03-mapping-and-lexical-preparation.md), [FC-14](FC-14-identity-and-policy.md), [FC-18](FC-18-diagnostics-and-audit.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** An admitted semantic or typed mathematical input requires an auditable human-language output in a supported locale and grammar profile.

**Expected final outcome:** A faithful realization with explicit language and grammar version, direct/fallback/missing state, or a principled failure.

**Owner(s) of state and decisions:** SemantiK Architect for semantic-to-language planning/realization; GF/grammar owners for grammar truth; SemantiK Runtime Orchestrator for RuntimeSet promotion.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Verify source intent | SemantiK Architect | approved typed input + audience/locale → validated realization request | Planner cannot silently invent missing semantic facts |
| 2 | Resolve lexical bindings | Lexical authority/diK where adopted | semantic identities + separate catalog → language-specific bindings | Versioned and auditable; missing label visible |
| 3 | Select realizer | SemantiK Architect + GF runtime | profile + grammar version → exact RuntimeSet selection | No implicit fallback to unqualified runtime |
| 4 | Qualify runtime | Independent diagnostics | runtime candidates + gold/negative fixtures → scoped conformance evidence | Report is evidence, not promotion permission |
| 5 | Promote or rollback | Runtime Orchestrator | approved RuntimeSet + policy → active runtime version | Orchestrator sequences; does not rewrite semantics or GF grammar |
| 6 | Realize and return | SemantiK Architect | typed plan + admitted RuntimeSet → text with trace | Faithfulness, locale and provenance retained |

## Interfaces and authority gates

`B-LANG-01` is proposed; GF Wordbench and grammar libraries are adjacent projects, not centrally owned replacement grammars. Framework and GF compatibility must be pinned independently.

## Failure, privacy and forbidden shortcuts

No fabricated translation, no silent unsupported fallback, no mixing of test-only RuntimeSets with production, no editor-controlled mutation of semantic intent.

## Definition of done — acceptance and negative tests

Test supported/missing language, semantic round-trip expectations, grammar mismatch, wrong runtime revision, intentionally ambiguous input, negative realization fixtures, rollback to known-good and denied unqualified promotion.

## Required code and contract alignment

Owner implementation: adopt one immutable RuntimeSet manifest/profile for SA↔GF↔Orchestrator, with independent language diagnostics and per-locale failure semantics.

## Product-specific notes

Typed mathematical content needs a separately verified policy; do not infer correctness of math exposition from general grammar smoke tests.

## Source anchors and verification boundary

SemantiK Architect, SemantiK Runtime Orchestrator and LevelUpDiag SemantiK owner docs; GF Wordbench and grammar projects in adjacent survey; B-LANG-01.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
