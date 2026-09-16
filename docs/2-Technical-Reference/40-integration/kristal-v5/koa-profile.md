# kOA profile for Kristal v5

This document defines kOA-specific integration constraints without changing Kristal semantics.

## Compilation and epistemic state

Keep compilation, validation, recognition, publication and activation separate. A Working Exchange may exist before final validation/recognition where policy permits.

## Runtime Pack on kOA-Linux

When a Kristal Runtime Pack is adopted by kOA-Linux:

- the platform artifact uses the `knowledge` release channel;
- Release Set compatibility can be required by the platform profile;
- `kristal_runtime` owns local Runtime Pack verification/compatibility and active-state records;
- `kristal_runtime` emits activation/rollback receipts and owns runtime health;
- kOA Node Agent executes the narrow privileged host transition when required;
- Koali Space activation remains unrelated presentation state.

## Reader Policy

Reader Policy is part of the consumption contract. Consumers preserve labels needed to distinguish source status, certainty, validation, recognition and dispute/rejection state.

## Da’at

Ecosystem/IK-facing Kristal requests route through Da’at or another explicitly adopted anti-corruption/mapping boundary. Da’at verifies the pinned dependency, applies versioned mappings and preserves Kristal-owned semantics.
