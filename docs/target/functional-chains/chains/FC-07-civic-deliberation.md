# FC-07 — Civic participation, deliberation and legitimate decisions

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-09](FC-09-world-contexts.md), [FC-14](FC-14-identity-and-policy.md), [FC-23](FC-23-external-interop.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** An admitted participant takes part in a civic process under a defined Universe/World/tenant and governance policy.

**Expected final outcome:** A finalized, authentic DecisionRecord plus audit-visible civic state and optionally a governed execution intent.

**Owner(s) of state and decisions:** Konnaxion for civic/public participation, deliberation and finalized DecisionRecord; Konnaxion-Worlds for selected World context.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Admit and scope | Konnaxion | subject + permissions + World context → scoped participation | No cross-tenant or cross-World authority leakage |
| 2 | Deliberate | Konnaxion | allowed proposals/feedback → reviewable deliberation state | Privacy, roles and decision rules remain owner-defined |
| 3 | Finalize | Konnaxion | outcome + legitimacy rules → immutable/traceable DecisionRecord | Finalization is explicit and not equivalent to creating tasks |
| 4 | Request execution | Konnaxion → Orgo if authorized | DecisionRecord reference → bounded governed-work intent | Adopted IK profile and receiver admission checked |
| 5 | Receive impact | Orgo → Konnaxion when ready | terminal operations receipt → Konnaxion accountability projection | Impact cannot revise the original decision invisibly |

## Interfaces and authority gates

The documented IK profiles `governance.decision.execute/1.0.0` and `accountability.impact.publish/1.0.0` have scoped local qualification evidence; that does not qualify arbitrary World deployments or all civic use cases.

## Failure, privacy and forbidden shortcuts

Deny forged finalization, mismatched World identity, retroactive decision mutation, replay with different intent and unauthorized operational actions. Different participation roles cannot be collapsed.

## Definition of done — acceptance and negative tests

Test finalization authority, private role filtering, exact DecisionRecord identifier, duplicate execution request, audit trace from decision to impact and independent reader denial for nonpublic decisions.

## Required code and contract alignment

Owner implementation: preserve Konnaxion as sole owner of civic decisions; pin WorldRelease and IK deployment profile; connect only qualified intents to Orgo.

## Product-specific notes

No additional exceptions. Refer to the global contract and lifecycle rules.

## Source anchors and verification boundary

Konnaxion owner README; Konnaxion-Worlds README; qualified local Konnaxion↔Orgo IK profile described in the C0 coordination docs.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
