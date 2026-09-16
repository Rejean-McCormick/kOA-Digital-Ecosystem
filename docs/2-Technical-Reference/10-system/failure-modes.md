# Failure modes

Failure handling follows the owner and transition that failed.

## Integration delivery
Timeouts, duplicate delivery, idempotency conflicts and reconciliation drift are protocol/delivery failures, not automatically domain failures.

## Kristal compilation / validation / recognition
Compile, validation/review and authority recognition remain distinct. Failed or unfinished validation can block later policy transitions without erasing a Working Exchange that was validly compiled.

## kOA-Linux release compatibility
Release Set/channel incompatibility blocks the affected release/activation transition and preserves the previous valid state.

## Runtime Pack verification/activation
`kristal_runtime` can reject a candidate for schema, identity, digest, provenance, trust, compatibility, release-channel or downgrade/substitution reasons. Activation/rollback failure preserves/restores the last valid runtime state according to its contract.

If a privileged node-local transition fails, kOA Node Agent reports that operation separately; it does not create a competing Runtime Pack active state.

## Koali Spaces
Space admission/readiness/rendering failures degrade presentation/application composition only. They must not be reported as Runtime Pack activation failures unless the underlying owner runtime actually failed.
