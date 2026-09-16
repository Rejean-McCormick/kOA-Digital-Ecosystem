# Components and systems

| System / boundary | Owns | Does not own |
|---|---|---|
| **Konnaxion** | civic/public state, DecisionRecord, readings, product state | Orgo work state, Kristal epistemic state, Runtime Pack active state |
| **Orgo** | Signal, Workflow, Case, Task, IntegrationOperation, outbox/reconciliation | Konnaxion civic outcomes, Kristal recognition, host privilege |
| **Kristal** | Structured Epistemic State, Working/Reference Exchange, validation, recognition, Reader Policy, Runtime Pack semantics | platform Release Set, host privilege, Orgo/Konnaxion state |
| **kOA-Linux** | platform profiles, trust/policy/resources, artifact admission, release channels, lifecycle contracts | subsystem business semantics |
| **kristal_runtime** | Runtime Pack verification/compatibility state, active Runtime Pack record, activation/rollback receipts, runtime health | governance policy, resource scheduling, host privilege, workflow state |
| **kOA Node Agent** | narrow node-local privileged lifecycle/activation/recovery operations | release authority, epistemic authority, business authority |
| **Koali Spaces** | optional presentation composition, routing, shell, Space activation and admitted surfaces | product business authority, Kristal authority, host privilege |
| **Da’at** | mapping/ACL at the Kristal integration boundary | Kristal core semantics or participant state |
| **Interaction Kernel** | target envelope/Profile/reliability semantics where adopted | participant state; current kOA-Linux internal contract authority |
| **SemantiK Architect** | language planning/realization | civic/workflow/epistemic authority |
| **SenTient** | candidate extraction/resolution/reconciliation | reference recognition or activation authority |

## No global control plane

No system automatically controls every ecosystem transition. Release-channel coordination, workflow state, epistemic state, Runtime Pack active state, privileged host operations and presentation state remain separate owners.

## kOA-Linux component/subsystem distinction

Konnaxion, Orgo, SemantiK Architect and Koali Spaces are subsystem/product boundaries relative to kOA-Linux. Native kOA-Linux components such as `kristal_runtime` and kOA Node Agent have distinct local contracts. Hosting a subsystem does not transfer its domain authority to kOA-Linux.
