# Integrator guide

## Identify the owner

Determine which product/component owns the state. Do not infer authority from hosting, rendering, process topology or transport.

## Cross-system protocol

Use an explicitly adopted Interaction Kernel Profile where available. Until product/platform adoption is published, do not relabel existing kOA-Linux internal/component contracts as IK.

## Kristal

Route ecosystem-facing Kristal work through the appropriate mapping boundary, preserve the exact Kristal Standard `6.0.0` content-digest pin, and preserve v6 `kristal_state` semantics (`valuations[]`, `coordinates`, `applicability`, `record_role`, `actionability`, validation/recognition and `artifact_status`). Treat Working/Reference only as declared v6 artifact-status concepts or explicitly defined derived artifacts.

## kOA-Linux release/activation

Reference Release Set/channel compatibility. For Runtime Packs, use `kristal_runtime` owner records. Use kOA Node Agent only for the narrow privileged node transition required by its contract.

## Koali

Treat Space/application activation as presentation composition. Never map it to Runtime Pack activation or product business authority.
