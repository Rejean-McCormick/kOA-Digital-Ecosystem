# Integration — Kristal v5

kOA integrates against a pinned Kristal v5 release candidate. Kristal remains the sole normative authority for its schemas and epistemic semantics.

## Pin

- version: `5.0.0-rc.1`
- tag: `v5.0.0-rc.1`
- commit: `af703bf02ee04a69a5f2ad6694fa8b8e56ae2b19`
- canonicalization: `kristal.v5:jcs-rfc8785`
- canonicalization version: `1`
- schema-set digest used by Interaction Kernel: `sha256:7a94a1e8a91d5c5267b73b7f1e98977faa548324bc937bb491cd08d49fdc8c92`

## Core model

Kristal v5 separates:

```text
artifact existence
integrity
assertion status
certainty
validation
recognition
reader visibility
publication
activation
```

The normative structured input is **Structured Epistemic State**. Claim-IR remains available as an optional extractor proposal profile rather than a universal mandatory stage.

A Structured Epistemic State may compile to a **Working Exchange** before final validation/recognition. A **Reference Exchange** is a recognized reference artifact under declared authority/scope.

## Runtime Packs

A Runtime Pack declares at minimum its source Exchange reference and `source_artifact_status`. Packs derived from working and reference artifacts are not equivalent.

Reader Policy and Query Contract determine how eligible content is exposed; they do not rewrite the underlying epistemic status.

## kOA profile rule

kOA may apply stricter deployment policies. For example, a production/reference channel may require reference-derived packs before publication or activation. Such a restriction is a kOA/kOA-Linux policy, not a Kristal core rule.
