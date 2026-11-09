# FC-23 — Explicit transport, mapping and third-party interoperability

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-14](FC-14-identity-and-policy.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** Two independently owned products, or a third-party client and a product, agree to exchange a bounded event/command/artifact under explicit identity and profile constraints.

**Expected final outcome:** An admitted exchange that both parties interpret identically, with receiver-owned effects and exact acceptance/terminal receipts.

**Owner(s) of state and decisions:** Interaction Kernel for adopted typed envelopes/profiles; DaaT for external semantic mapping/PEP; producer and consumer owners for all real state.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Negotiate contract | Both owners | capability/identity map → explicit adopted profile and compatible versions | No assumption that IK adoption is universal |
| 2 | Authenticate | Sender host/trust + receiver PEP | workload identity and signed intent → admitted principal | TLS, actor verification and time/tenant binding as needed |
| 3 | Map optional foreign schema | DaaT where adopted | external fields → allowlisted owner-native fields | Mapping is transparent, versioned and reversible where required |
| 4 | Validate envelope | Receiver / IK profile implementation | typed payload → accepted/rejected request | Malformed or out-of-profile payloads fail closed |
| 5 | Execute owner operation | Receiver owner | accepted intent → product-owned state or pending work | No sender database write and no false success claim |
| 6 | Reconcile | Receiver/producer | terminal outcome → scoped receipt and retry disposition | Durable effects with idempotency and outbox where required |

## Interfaces and authority gates

The currently named adopted civic examples are `governance.decision.execute/1.0.0` and `accountability.impact.publish/1.0.0`. DaaT documents offline IK schema checks and host-injected ports, not a deployed global transport gateway.

## Failure, privacy and forbidden shortcuts

Never implement a cross-domain super-bus by assumption, invent new IK profile IDs without owners, skip security for a "native" mapping, or let a mapping engine certify external truth.

## Definition of done — acceptance and negative tests

Test golden payload acceptance, schema drift, tenant and actor spoofing, profile downgrade, unsupported extension, replay conflict, uncertain effect reconciliation, offline transport simulation and explicit mapping exclusions.

## Required code and contract alignment

Owner implementation: agree on a narrow profile per pair/use case, then add contract tests and receiver state-machine proof before updating the C0 accepted-boundary registry.

## Product-specific notes

Communication can be a validated file exchange or local library call. The requirement is **governed handoff**, not a mandatory always-on service mesh.

## Source anchors and verification boundary

Interaction-Kernel and DaaT owner READMEs, IK tandem Konnaxion/Orgo source contract docs; B-CIVIC-01/02 and B-SEC-01.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
