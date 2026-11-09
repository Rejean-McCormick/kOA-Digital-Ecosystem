# FC-14 — Identity, authorization, security policy and real enforcement

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-23](FC-23-external-interop.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** A caller requests to read, write, publish, deploy or execute against a resource in a precisely defined tenant, audience and purpose.

**Expected final outcome:** A deny-by-default decision bound to principal, resource, action and intent digest, followed by a separate observed enforcement receipt for permitted effects.

**Owner(s) of state and decisions:** Actual IdP/trust provider for authentication; Konfid for scoped policy decisions; DaaT and every product for enforcing PEPs; platform/agent for host effects.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Authenticate | Trusted identity source | workload/actor credentials → validated claims | No credentials from user-supplied text or untrusted app metadata |
| 2 | Build request | Caller / owner PEP | principal, tenant, resource, action, digest → policy request | Identity and digest are exact and bounded |
| 3 | Decide | Konfid or selected owner policy engine | policy request → allow/deny and obligations | Scoped, time-bounded, no universal administrator bypass |
| 4 | Enforce | DaaT or other actual PEP | decision + exact effect → permit or deny | Recheck freshness, actor, tenant, resource and obligations |
| 5 | Audit/reconcile | Enforcing owner | effect attempt → durable audit/receipt | Successful policy decision is not proof of successful effect |

## Interfaces and authority gates

`B-SEC-01` is proposed; DaaT currently documents host-injected identity/policy/audit dependencies and is **not** a self-contained deployed security service. Every other product must maintain local enforcement even if central decisions are consulted.

## Failure, privacy and forbidden shortcuts

On absent audit sink, expired policy, unknown actor, replay/digest mismatch, cross-tenant request, stale delegation or unenforced obligations, fail closed.

## Definition of done — acceptance and negative tests

Test allow/deny, expired decision, invalid workload binding, substituted resource digest, revoked actor, PEP bypass prevention, tenant isolation, lost Konfid availability and minimal nonsecret audit trail.

## Required code and contract alignment

Owner implementation: connect real trusted policy transport and each PEP; prove actual effect suppression on denial, not just a "deny" response returned to UI.

## Product-specific notes

No policy engine gets automatic global authority over civic, semantic, clinical, student or host data; each actual owner remains responsible for effect scope.

## Source anchors and verification boundary

Konfid owner README and DaaT 0.3.0 offline security-gate docs; Konfid→DaaT proposed B-SEC-01.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
