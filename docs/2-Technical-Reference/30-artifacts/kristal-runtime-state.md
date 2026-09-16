# Kristal Runtime local state on kOA-Linux

This page references the current kOA-Linux `kristal_runtime` component contract.

## Authoritative local records

`kristal_runtime` owns local Runtime Pack state including:

- verification/compatibility record;
- active Runtime Pack record;
- activation receipt;
- rollback receipt;
- runtime health state.

## Boundary

`kristal_runtime` does not own:

- Kristal's global epistemic semantics;
- Orgo/Konnaxion domain state;
- governance policy;
- resource scheduling;
- host privilege;
- release-channel identity.

## Privileged transition

When activation requires node-local privileged mutation, kOA Node Agent executes the narrow authorized transition. The owner of active Runtime Pack state remains `kristal_runtime`.
