# kOA Digital Ecosystem Documentation

kOA is an ecosystem for producing, distributing, and operating deterministic knowledge-backed runtime behavior across environments. It defines the **system architecture**, **node responsibilities**, **kOA-owned artifacts**, and **operational workflows**. Kristal defines the **normative boundary artifacts** (Exchange, Runtime Pack, Render Bundle, etc.).

## Non-redundancy rule

* **Kristal v4 is the sole normative source** for Kristal artifact contracts and schemas.
* kOA documentation **must not duplicate** Kristal schemas, field lists, or canonicalization rules.
* kOA documentation may define **kOA-specific constraints and profiles** for how kOA uses Kristal v4.

See: `40-integration/kristal-v4/`

## Start here

* System summary: `00-overview/system-at-a-glance.md`
* Architecture & invariants: `10-system/architecture.md`, `10-system/trust-boundaries.md`, `10-system/determinism.md`
* Nodes (interfaces + responsibilities): `20-nodes/index.md`
* kOA-owned artifacts + schemas: `30-artifacts/index.md`
* Kristal integration (pinned + profile + conformance): `40-integration/kristal-v4/index.md`
* Common identity / optional OIDC federation: `40-integration/identity-oidc/index.md`
* Konnaxion/eThikos ↔ Orgo integration profile: `40-integration/orgo-konnaxion/index.md`
* Operations (pipeline, release, rollback): `50-operations/pipeline.md`
* Guides (implementers/integrators/testing/tooling): `60-guides/`

## Documentation map

* `00-overview/` — scope, glossary, FAQ, quick orientation
* `10-system/` — architecture, lifecycle, components, trust boundaries, determinism, failure modes
* `20-nodes/` — node specs (inputs/outputs at the artifact-type level; behavior; error modes)
* `30-artifacts/` — kOA-native artifacts and their schemas (does not contain Kristal artifacts)
* `40-integration/` — integration profiles, including Kristal v4 and common identity/OIDC
* `50-operations/` — runbooks and operational procedures
* `60-guides/` — practical implementation and integration guidance
* `90-reference/` — ADRs and reference terminology

## Authoring conventions

* Each page should clearly indicate whether it is:

  * **Normative for kOA** (YES/NO)
  * **External normative reference** (Kristal v4 pinned reference or none)
* If a page needs Kristal specifics, **link to the pinned Kristal v4 source** in `40-integration/kristal-v4/pinned-dependency.md` rather than copying content.

## Key pointers

* Kristal v4 integration entry: `40-integration/kristal-v4/index.md`
* Common identity integration entry: `40-integration/identity-oidc/index.md`
* Konnaxion/eThikos ↔ Orgo integration entry: `40-integration/orgo-konnaxion/index.md`
* Pinned Kristal v4 dependency: `40-integration/kristal-v4/pinned-dependency.md`
* kOA profile and conformance: `40-integration/kristal-v4/koa-profile.md`, `40-integration/kristal-v4/conformance.md`
