# 02 — Contract and receipts

**Status:** `TARGET_DESIGN`.

A cross-owner interface must specify sender/recipient identities, principal and tenant, versioned schema, source digest, classification, data bounds, producer disclosure rule, receiver admission, idempotency key and replay window, terminal success/failure semantics and recovery.

**Receipt fields (conceptual):** boundary ID, producer revision, receiver revision, request hash, tenant, actor, admission outcome, terminal effect state, immutable output reference, verifier and observation time. An accepted message is never proof of a succeeded external effect. Same-intent replay must be idempotent; same key with altered intent is a conflict.

[Functional chain index](README.md) · [Repository coverage](05-repository-coverage.md) · [Acceptance](06-qualification-and-acceptance.md)
