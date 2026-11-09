# FC-16 — Platform build, admission, deployment and rollback

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-14](FC-14-identity-and-policy.md), [FC-18](FC-18-diagnostics-and-audit.md), [FC-24](FC-24-operations-and-recovery.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** An operator selects a deployable product, exact build/release, host profile and target environment, then requests an authorized lifecycle transition.

**Expected final outcome:** A measured host/runtime state with admission, activation and recovery receipts, without changing product-owned canonical or business data.

**Owner(s) of state and decisions:** kOA-Linux for platform policy/profiles; Koali Control Panel for developer/operator preparation; Capsule Manager and privileged agent in their adopted deployment scope.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Prepare build | Product + Control Panel | source/lock/profile → reproducible candidate build | No security trust inferred from GUI readiness |
| 2 | Qualify release | Independent diag + platform policy | artifact, SBOM, profile → scoped evidence | Clean image/offline/recovery criteria according to profile |
| 3 | Authorize admission | kOA-Linux or selected host authority | exact signed ReleaseSet → admission decision | Exact identity, provenance, compatibility and policy checked |
| 4 | Deploy | Authorized agent/host | admitted ReleaseSet → installed services | Privileged action restricted to named resources and target |
| 5 | Activate/verify | Host runtime owner | installed revision → active state and health receipts | Actual host observation, not just CI pass |
| 6 | Recover | Host/runtime owner | failure → rollback, last-known-good or manual recovery | Rollback outcome measured; stateful product data separately owned |

## Interfaces and authority gates

`B-PLAT-01` Control Panel→kOA-Linux is proposed. The selected Linux VPS + Docker + Konnaxion Capsule Agent tandem is a **specific target profile**, not a universal requirement; kOA-Linux may be an independent optional platform path.

## Failure, privacy and forbidden shortcuts

Block unsigned or unqualified artifacts, stale policy, forged diagnostic evidence, dirty worktree if profile requires clean build, unauthorized host shell, invalid image/offline readiness and silent rollback of owner business state.

## Definition of done — acceptance and negative tests

Test exact ReleaseSet pinning, schema mismatch, denied activation, host PEP invocation, unhealthy service, offline/rollback profile, lost agent, last-known-good recovery and post-activation measured receipts.

## Required code and contract alignment

Owner implementation: close actual ReleaseSet→agent PEP→host observation proof; keep product publication and Space activation as later independent states.

## Product-specific notes

Platform admission is not required for a purely offline local notebook, desktop tool or static collection read without host deployment.

## Source anchors and verification boundary

kOA-Linux v0.8 beta, Koali Control Panel, Konnaxion Capsule Manager, LevelUpDiag-kOA-Linux and C0 tandem VPS profile docs; B-PLAT-01.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
