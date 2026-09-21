# kOA Digital Ecosystem

kOA is a system of systems connecting civic decisions, governed work, epistemic artifacts, platform/runtime controls and presentation composition through explicit contracts.

## System map

```text
Konnaxion  <------ target cross-system protocol ------>  Orgo
    \                                                   /
     +---------------------> Da’at ---------------------+
                              |
                       Kristal-native contracts
                              |
                           Kristal
                              |
                       Runtime Pack artifacts
                              |
          kOA-Linux knowledge channel / Release Set
                              |
                        kristal_runtime
                              |
             kOA Node Agent (privileged transition,
                    only when required by profile)

Koali Spaces sits above admitted products as an optional presentation layer.
It does not acquire their business, workflow, epistemic or host authority.
```

The system map describes ecosystem membership and ownership relationships. A specific kOA-Linux profile may activate only a subset of these systems; profile composition is not the same thing as ecosystem membership.

**Control views:** [Authority map](../2-Technical-Reference/10-system/authority-map.md) · [Contract map](../2-Technical-Reference/40-integration/contract-map.md) · [Maturity map](../status/current.md)

## Owners

- **Konnaxion** — civic/public state and DecisionRecords.
- **Orgo** — workflow/work state and durable external operations.
- **Kristal** — epistemic artifacts and Runtime Pack semantics.
- **kOA-Linux** — platform profiles, trust/policy/resources, artifact admission and release-channel coordination.
- **kristal_runtime** — Runtime Pack verification, compatibility, active Runtime Pack selection/state, activation/rollback receipts and runtime health in kOA-Linux.
- **kOA Node Agent** — narrow authorized node-local lifecycle and privileged host operations.
- **Koali Spaces** — optional shell/presentation composition and Space lifecycle.
- **Interaction Kernel** — selected interoperability protocol/Profile layer where explicitly adopted; Konnaxion↔Orgo currently has qualified adoption for two Profile/version pairs.
- **Da’at** — ecosystem/IK-to-Kristal mapping/ACL boundary.

## Runtime Pack activation

The earlier statement “kOA-Linux owns Runtime Pack activation” is too broad. In the current kOA-Linux contracts:

```text
kristal_runtime
  owns verification state + active Runtime Pack record + activation/rollback receipts

kOA Node Agent
  can execute the narrow privileged host transition required by the active profile

Release Set
  binds compatible versions across release channels
```

Digital Ecosystem therefore references those owners rather than creating a separate global Runtime Activation State.

## Koali Spaces

Koali Spaces is presentation infrastructure. Its Space/application activation is a UI/composition lifecycle and **must not be interpreted as Kristal Runtime Pack activation**.

## Implementation status

See the current [maturity map](../status/current.md). Target architecture and product implementation evidence are distinct. Current Koali evidence includes a later successful Konnaxion pilot, while some product reference pages still describe that pilot as pending. Interaction Kernel adoption is selective: Konnaxion↔Orgo is qualified for two Profile/version pairs, while every other boundary still requires explicit owner adoption/conformance evidence.
