# kOA Digital Ecosystem alignment status — 2026-09-21

This page records ecosystem alignment against the supplied Konnaxion, Orgo, Kristal, Interaction Kernel, current kOA-Linux docs/contracts snapshot and current Koali Spaces docs snapshot.

For the compact cross-system dashboard, see [`current.md`](./current.md). It keeps architecture, implementation, qualification, integration and production evidence as separate dimensions.

Latest cross-product qualification evidence: [`2026-09-21-konnaxion-orgo-ik-e2e-qualification.md`](./2026-09-21-konnaxion-orgo-ik-e2e-qualification.md).

## Overall result

The ecosystem documentation is aligned at the ownership/contract level, but adoption and implementation evidence remain system-specific.

| Area | Ecosystem documentation | Current evidence / remaining work |
|---|---|---|
| Kristal v5 epistemic model | Aligned | Structured Epistemic State, Working/Reference separation, Reader Policy and non-universal validation gate are preserved |
| kOA-Linux Runtime Pack ownership | Corrected | `kristal_runtime` owns verification/compatibility/active-state/activation+rollback receipts/runtime health; Node Agent is the narrow privileged host-transition path |
| kOA-Linux release model | Corrected | Release Set binds compatible `system`, `services`, `governance`, `knowledge` channel versions; Digital Ecosystem Release Record is deprecated as authority |
| Runtime Activation State | Corrected | Digital Ecosystem no longer creates a parallel authoritative state beside `kristal_runtime` |
| Koali Spaces ecosystem placement | Added | Optional presentation/composition subsystem; no product, epistemic or host authority |
| Koali Space activation vs Runtime Pack activation | Aligned | Explicitly separate lifecycles |
| Koali↔Konnaxion UI pilot | Later evidence present | 2026-09-08 notice records adapter 15/15, Konnaxion backend 148/148, Koali UI 29/29, readiness HTTP 200 and browser navigation verification |
| Koali current-reference docs | Drift remains in owner repo | `01-product/04-current-vs-target.md` and `15-reference/04-current-implementation-snapshot.md` still say first Konnaxion onboarding is pending |
| Interaction Kernel | Selective adoption qualified | Konnaxion↔Orgo is qualified for `governance.decision.execute/1.0.0` and `accountability.impact.publish/1.0.0`; no universal kOA-Linux or ecosystem-wide IK adoption is implied |
| Konnaxion↔Orgo IK handoff | **QUALIFIED 2026-09-21** | Direct finalized DecisionRecord→Orgo Signal→Workflow→Case→Task path passed the integrated E2E qualification; see `2026-09-21-konnaxion-orgo-ik-e2e-qualification.md` |
| Orgo→Konnaxion durable publication | **QUALIFIED 2026-09-21** | `IntegrationOperation`→`accountability.impact.publish/1.0.0`→Konnaxion impact ingress passed, including idempotent replay and divergent replay conflict |
| Da’at→Kristal v5 | Target mapping | Migration/conformance evidence remains owner-repository work |

## Precise kOA-Linux ownership model

```text
kOA-Linux platform
  owns profiles, trust/policy/resource boundaries,
  artifact admission and release-channel contracts

Release Set
  binds compatible versions across
  system / services / governance / knowledge channels

kristal_runtime
  owns Runtime Pack verification/compatibility,
  active Runtime Pack record,
  activation/rollback receipts,
  runtime health

kOA Node Agent
  executes narrow authorized privileged node-local
  activation/recovery transitions when required
```

This supersedes the coarser earlier wording that “kOA-Linux owns physical Runtime Pack activation” and supersedes the Digital Ecosystem-created Runtime Activation State as an authority.

## Koali Spaces placement

Koali Spaces is an optional global experience/presentation subsystem. It composes admitted application surfaces and owns Space lifecycle/presentation state only.

```text
Koali Space activation
≠ product business activation
≠ kOA-Linux release-channel activation
≠ Kristal Runtime Pack activation
```

A Koali view of Kristal/Runtime Pack material must preserve relevant status, certainty, authority and Reader Policy labels. Rendering does not compile, validate or recognize authority.

## Interaction Kernel status

Interaction Kernel is the selectively adopted cross-system protocol/Profile layer for explicit ecosystem boundaries. Current kOA-Linux documentation already defines its own canonical interaction types and contracts; therefore Digital Ecosystem treats IK adoption as explicit and system-specific rather than already universal.

For the Konnaxion↔Orgo boundary, `governance.decision.execute/1.0.0` and `accountability.impact.publish/1.0.0` now have integrated runtime evidence dated 2026-09-21. Other IK mappings remain system-specific targets until their owners publish equivalent adoption and conformance evidence.

## Deprecated Digital Ecosystem authorities

The following are retained only for compatibility/history:

- `Release Record v2` as an authoritative release object — use kOA-Linux Release Set and owner receipts instead;
- `Runtime Activation State` as a kOA-Linux authoritative record — use `kristal_runtime` owner records instead;
- `Konnaxion State` as universal Runtime Pack activation state;
- active Kristal v4 integration pages — retained as historical migration documentation only.

## Product-repository updates still required

1. **Koali Spaces:** update the two current-state reference pages that still say first real Konnaxion onboarding is pending; replace “Kristal: verrou de vérité” / “assertion canonique” terminology with v5 epistemic/authority language.
2. **kOA-Linux:** mount/link official subsystem documentation at reserved subsystem paths; continue contract/code convergence items already identified in `CODE_ALIGNMENT_NOTES.md` (including language-pack discriminator compatibility and generator/validator alignment).
3. **Konnaxion + Orgo:** keep the qualified IK Profile implementations and owner-repository tests aligned, and preserve the 2026-09-21 E2E scenario as a regression gate.
4. **Da’at:** publish verified Kristal v5 mapping/conformance against the pinned release.
5. **Digital Ecosystem:** future updates should reference owner contracts rather than introduce new authority records when a product/platform already owns the state.
