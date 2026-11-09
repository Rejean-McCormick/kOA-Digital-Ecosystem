# FC-15 — Bounded, inspectable AI workflows and owner-mediated actions

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-14](FC-14-identity-and-policy.md), [FC-08](FC-08-governed-execution.md), [FC-18](FC-18-diagnostics-and-audit.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** An authorized operator submits a bounded agent job with tools, data classifications, budget, allowed effects and explicit review points.

**Expected final outcome:** An inspectable job trace and approved action requests; any real operational changes occur only after the receiving product admits them.

**Owner(s) of state and decisions:** Konductor for proposed agent plans, jobs, checkpoints and review; each external product for authoritative effects; Konfid/owner PEP for permission.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Declare job | Konductor | goal, scope, budget, tools, caller → immutable job intent | Allowed tools and data limits enumerated; no arbitrary host execution |
| 2 | Plan | Agent under Konductor | job intent → proposed steps and evidence requests | Model output treated as untrusted candidate |
| 3 | Checkpoint | Konductor / reviewer | proposals → approved, revised or stopped plan | Human gates required where risk or owner policy demands |
| 4 | Request effect | Konductor → owner adapter | approved command → typed owner request | Owner reauthenticates and enforces; no direct database write |
| 5 | Observe effect | Target owner → Konductor | accepted/pending/terminal receipt → job checkpoint | Success asserted only on terminal owner evidence |
| 6 | Recover | Konductor | interruption → bounded resume/cancel | Replays use owner idempotency; uncertain effects reconcile |

## Interfaces and authority gates

No adopted generic Konductor→Orgo interface ID is registered in BOUNDARIES. If a real work operation is needed, define a separate accepted Orgo intent profile rather than bypassing Orgo through agent tools.

## Failure, privacy and forbidden shortcuts

No broad credentials in prompts, no autonomous irreversible execution without approval, no confusion of a model confidence score with qualification, no claim that a design repository is a deployed service.

## Definition of done — acceptance and negative tests

Test tool allowlists, prompt injection resistance, sensitive-data redaction, approval expiration, model hallucinated identifiers, duplicate action replay, crash/restart checkpoint durability and owner denial.

## Required code and contract alignment

Owner implementation: prioritize a minimal verifiable job-state executor plus one synthetic owner adapter; add real capabilities only after code tests and policy approval.

## Product-specific notes

An agent may prepare documentation or propose a change without becoming a separate Orgo Case manager or Kristal canonical author.

## Source anchors and verification boundary

Konductor README and Initial Technical Design in owner snapshot; code snapshot contains primarily design/reference content rather than a demonstrated deployed control plane.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
