# Kristal v5 integration

**External normative authority:** Kristal v5 owner repository

The current knowledge acquisition/projection boundary uses the Kristal `5.0.0-rc.3` **release-candidate contract set** and Referent Registry `1.0.0`. The supplied rc.3 release metadata has no resolved commit SHA yet, so this is a frozen contract baseline rather than a completed immutable release pin.

Other downstream integrations may still hold older immutable Kristal locks until their owners explicitly update them. Digital Ecosystem never rewrites those locks implicitly.

## Core semantics

- Structured Epistemic State is the primary structured epistemic input.
- Referent Registry `1.0.0` supplies domain-neutral referent identity semantics.
- Claim-IR and Resolved Claim-IR are optional extraction/resolution profiles, not a universal pipeline.
- Compilation may produce a Working Exchange before final validation/recognition.
- Validation, certainty and authority recognition are independent axes.
- Reference Exchange means recognized reference under declared authority/scope, not universal truth.
- Runtime Packs preserve source-artifact status and reader policy metadata.
- Product-owned mutable state enters Kristal only through explicit immutable source artifacts/exports with provenance.
- Runtime/query/consumer materializations remain derived and non-authoritative.

See:

- [`pinned-dependency.md`](./pinned-dependency.md)
- [`contract-pointers.md`](./contract-pointers.md)
- [`koa-profile.md`](./koa-profile.md)
- [`conformance.md`](./conformance.md)
- [`../knowledge-projection.md`](../knowledge-projection.md)
