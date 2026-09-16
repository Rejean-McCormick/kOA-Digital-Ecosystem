# Tooling guidance

Expected tooling capabilities include:

- validate owner-system contracts and references;
- verify exact Kristal pin/canonicalization;
- validate Structured Epistemic State and Kristal manifests;
- inspect Working/Reference status and Reader Policy refs;
- emit/validate Build Record correlation evidence when used;
- validate/read kOA-Linux Release Set and release-channel compatibility;
- inspect `kristal_runtime` verification/active-state/activation/rollback receipts;
- invoke kOA Node Agent only through its narrow authorized lifecycle contract when required;
- inspect Koali Space/runtime-registration/readiness state separately from Runtime Pack state;
- redrive durable cross-system operations without changing logical idempotency identity.

Do not create new Digital Ecosystem Release Record or Runtime Activation State authorities when owner contracts already exist.
