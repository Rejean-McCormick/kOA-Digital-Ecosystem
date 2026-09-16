# Integrator guide

## Identify the owner

Determine which product/component owns the state. Do not infer authority from hosting, rendering, process topology or transport.

## Cross-system protocol

Use an explicitly adopted Interaction Kernel Profile where available. Until product/platform adoption is published, do not relabel existing kOA-Linux internal/component contracts as IK.

## Kristal

Route ecosystem-facing Kristal work through the appropriate mapping boundary, preserve exact v5 pin and epistemic labels, and distinguish Working from Reference state.

## kOA-Linux release/activation

Reference Release Set/channel compatibility. For Runtime Packs, use `kristal_runtime` owner records. Use kOA Node Agent only for the narrow privileged node transition required by its contract.

## Koali

Treat Space/application activation as presentation composition. Never map it to Runtime Pack activation or product business authority.
