# 02 — Cross-owner contract, evidence and receipt model

**Status:** `TARGET_DESIGN` · **Purpose:** common design requirements, **not** an invented platform wire protocol. Product owners retain their exact schema authority.

## Boundary contract checklist

Before a producer and a consumer claim integration, they must bilaterally establish:

1. **Identity:** owning producer/consumer, audience, tenant/World/workspace, actor or workload subject, scope and authn source.
2. **Version:** stable interface/profile ID, accepted semantic or payload schema version, compatibility constraints and rejected versions.
3. **Provenance:** source identifier, immutable input revision and digest, producer implementation revision, creation time, classification/visibility.
4. **Payload:** mandatory fields, optional fields, bounded sizes, encoding, known extensions, secret handling, privacy rules and external/reference semantics.
5. **Permissions:** disclosure approval from producer, consumer admission, and any downstream privileged-effect authorization at its PEP.
6. **Delivery:** request/response or durable async contract, idempotency key and replay window, durable journal where real effects require it, dead-letter/quarantine policy.
7. **Outcomes:** explicit acceptance/rejection/duplicate/conflict receipt, and terminal effect result where effects are asynchronous.
8. **Recovery:** retry limits, backwards-compatible reprocessing, rollback/rebuild ownership, correlation for tracing and operator escalation.
9. **Qualification:** exact producers and consumers pinned to revisions, tests for good/bad fixtures, and named proof that both sides agree on the same payload.

A file transfer, local CLI call, shared package or direct HTTP request can implement a boundary if these properties are satisfied. **Do not require IK for every integration.** For an IK-adopted boundary, its normative envelope/profile fills the applicable parts of the checklist, while owner authorization and durable state remain separate.

## Conceptual receipt, not normative JSON

```text
receipt_ref             receiver-owned immutable reference
boundary_ref            adopted interface/profile and version (or pending TBD)
producer_ref            owner + exact input revision/digest
consumer_ref            receiver owner + implementation revision
request_scope           tenant, principal, resource and intended effect
idempotency_ref         stable caller key bound to immutable request digest
admission               accepted | rejected | already_accepted | conflict
execution               not_requested | pending | succeeded | failed | reconciled
output_ref              receiver-owned artifact/Case/Task/release/read-model reference
observed_at             trusted observation time, not a source of authority
verification_ref        signature/verifier/run, when appropriate to risk
```

No chain may treat `accepted` as equivalent to `succeeded`; the receiver often accepts a job before any real effect occurs. A duplicate request with identical intent is an idempotent replay; the **same key with different bytes is a conflict**, never a silent update.

## The five kinds of proof

| Proof | What it establishes | What it does not establish |
|---|---|---|
| Owner snapshot with file hash | These exact bytes were supplied | Current remote Git HEAD, correctness, deployment |
| Local owner test receipt | One checkout passed named checks | A separate consumer accepts the contract |
| Independent diagnostic report | Named checks over exact subject/version | Release approval, data/publication permission |
| Bilateral integration evidence | Exact pair of pinned producer/consumer revisions handled named fixtures | Unrelated products, production traffic or wider security scope |
| Environment/host observation | Named deployment emitted measured health and effect receipts | Other environments, future stability or universal release approval |

For contract and source anchors already modeled, consult [target boundaries](../BOUNDARIES.md) and [snapshot reconciliation](../SNAPSHOT_RECONCILIATION.md). Missing exact interface IDs are design questions, not documentation errors to fill with a guess.

## Compatibility and change control

- **Additive changes** still require consumer proof where validation is strict.
- **Breaking schema/namespace changes** require explicit opt-in upgrade/migration and rejection fixtures; never rewrite canonical KQ/KP/KA/KS identifiers behind the reader.
- **Pinned derived read views** may be rebuilt against newly authorized releases only after compatibility checks; freshness and provenance must remain visible.
- **Confidential artifacts** cannot become public through logs, manifests, dashboards or automated Git pushes. A public destination is an explicit authorization target.
- **Safety-critical effects** (student, financial, clinical, privileged infrastructure or civic authority) need owner-specific controls above this minimum.
