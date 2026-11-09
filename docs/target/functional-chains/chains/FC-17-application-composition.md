# FC-17 — Optional app shell, admitted surfaces and navigability

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-14](FC-14-identity-and-policy.md), [FC-16](FC-16-platform-lifecycle.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** A user enters an admitted application from its standalone route or an optional shared Koali Space under an appropriate workspace and identity context.

**Expected final outcome:** A usable, permission-correct UI surface with real product readiness/degradation and no transfer of application data ownership.

**Owner(s) of state and decisions:** Koali Spaces for optional shell, route and Surface Layer contracts; each product for its own UI/runtime; Koali Control Panel for local development navigation.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Discover | Koali Spaces optional | owner `koali.integration.json` manifest → candidate module contribution | Discovery alone grants no rights or executable URL allowance |
| 2 | Admit manifest | Space/platform owner | versioned manifest + allowed origins → active surface registration | CSP/runtime registry, capability and profile checks applied |
| 3 | Check readiness | Koali Spaces / owner probes | required frontend+API probes → ready/degraded/unavailable | All required probes conjunctive; healthy UI alone is not ready |
| 4 | Render | Koali Spaces | admitted product UI → module sidebar, route and shared page | Only UI composition and router state; owner app remains independent |
| 5 | Disable/recover | Space owner | failed/withdrawn surface → hidden/degraded surface | Product business state remains untouched |

## Interfaces and authority gates

`B-PLAT-02` target links kOA-Linux→Koali Spaces. Shell-level onboarding contracts are separate from IK and direct owner API contracts; product owners must explicitly opt in.

## Failure, privacy and forbidden shortcuts

Reject unapproved iframes/origins, forged module claims, missing required probes, stale workspace links, hidden cross-tenant routes and user-visible "ready" when a required backend is down.

## Definition of done — acceptance and negative tests

Test standalone product operation with shell disabled, manifest denial, CSP failure, required probe degradation, workspace link migration, route isolation, UI language and accessible navigation.

## Required code and contract alignment

Owner implementation: keep discovery explicit, pin accepted Surface Layer schema, test at least one product independently and through the optional shell, and preserve read-only status in UI registries.

## Product-specific notes

Presentation does not mint any new ability to read a private Kristal, edit an Orgo Task or bypass Konfid/owner access checks.

## Source anchors and verification boundary

Koali-Spaces owner README and surface registry/spec; Koali Control Panel docs; B-PLAT-02.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
