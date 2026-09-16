# Runtime Activation State — deprecated compatibility artifact

**Status:** Deprecated for kOA-Linux Runtime Pack activation.

The current kOA-Linux contracts already assign authoritative Runtime Pack state to `kristal_runtime`, including:

- `runtime_pack_verification_record`;
- `active_runtime_pack_record`;
- activation receipts;
- rollback receipts;
- runtime health state.

Digital Ecosystem MUST NOT create another authoritative Runtime Activation State beside those records.

kOA Node Agent may execute the narrow privileged node-local transition when required, but its receipt does not replace `kristal_runtime`'s active-state record.

For standalone deployments outside kOA-Linux, the deployment may define another owner, but that owner remains deployment-specific rather than a universal Digital Ecosystem artifact.

The former `schemas/runtime-activation-state.schema.json` is retained only for migration readers.
