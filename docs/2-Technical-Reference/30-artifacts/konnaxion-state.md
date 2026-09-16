# Konnaxion State — historical compatibility note

The former Konnaxion State artifact assumed Konnaxion universally owned Runtime Pack verification/activation/rollback.

That assumption is not valid in the current architecture.

For kOA-Linux deployments:

- Konnaxion may own civic/product desired selection or application intent;
- `kristal_runtime` owns Runtime Pack verification and active-state records;
- kOA Node Agent performs narrow privileged node-local transitions where required;
- Release Set/channel compatibility belongs to kOA-Linux platform contracts.

Do not emit new Konnaxion State records as authoritative Runtime Pack activation state.
