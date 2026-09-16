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

## Owners

- **Konnaxion** — civic/public state and DecisionRecords.
- **Orgo** — workflow/work state and durable external operations.
- **Kristal** — epistemic artifacts and Runtime Pack semantics.
- **kOA-Linux** — platform profiles, trust/policy/resources, artifact admission and release-channel coordination.
- **kristal_runtime** — Runtime Pack verification, compatibility, active Runtime Pack selection/state, activation/rollback receipts and runtime health in kOA-Linux.
- **kOA Node Agent** — narrow authorized node-local lifecycle and privileged host operations.
- **Koali Spaces** — optional shell/presentation composition and Space lifecycle.
- **Interaction Kernel** — target interoperability protocol/Profile layer where adopted.
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

Target architecture and product implementation evidence are distinct. Current Koali evidence includes a later successful Konnaxion pilot, while some product reference pages still describe that pilot as pending. Interaction Kernel remains target cross-system architecture until explicit adoption/conformance is published by the owning systems/platform.
