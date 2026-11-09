# 04 — Full-system compositions and acceptance stories

**Status:** `TARGET_DESIGN` · **Purpose:** explain how autonomous functional chains combine into final user outcomes. A **composition is not a single synchronous call** and may have manual or offline handoffs.

Each scenario below inherits [ownership](01-authority-and-ownership.md), [receipts](02-contract-and-receipts.md) and [failure rules](03-state-trust-and-failure.md). The chain numbers identify *where to find the detailed specification*; a listed dependency does not assert a working integration today.

## S01 — A researcher turns a permitted source into a public, multilingual knowledge view

**Actor:** authorized research operator, semantic author and release owner. **Chains:** [FC-01](chains/FC-01-research-and-acquisition.md) → [FC-02](chains/FC-02-source-custody.md) → [FC-03](chains/FC-03-mapping-and-lexical-preparation.md) → [FC-04](chains/FC-04-semantic-authoring.md) → [FC-05](chains/FC-05-knowledge-release.md) → [FC-06](chains/FC-06-knowledge-consumption.md), with [FC-14](chains/FC-14-identity-and-policy.md) and [FC-18](chains/FC-18-diagnostics-and-audit.md).

1. Skope fixes a research perimeter, provider set, source policy, recipe and local evidence digest.
2. The selected Médiathèque instance **accepts custody**, issues a Source/Snapshot/Representation receipt and retains source permissions. A QID is still an external identifier, not a KQ.
3. DaaT/diK/Kristalizer produce reversible, reviewable candidates. An approved author selects identities and lexical entries under a pinned Framework profile; no automatic merge by label.
4. The Kit creates a local semantic build. KristalDiag independently evaluates the exact candidate. The owner grants specific release/publication permission separately.
5. An authorized publisher writes an immutable approved collection/read view; consumer clients import exact revisions and display direct/fallback/missing language information.

**Success proof:** each owner receipt links to the same approved lineage without transferring state authority; a public reader can show the KQ identity and source/provenance version. **Failure proof:** a rejected source, unknown KQ, private image, invalid lexical schema, failed independent test or absent publication grant prevents public output. **Not a requirement:** every author must use Skope, every Kristal must go public, or every read product must subscribe.

## S02 — An offline author creates a private Kristal without a research service

**Actor:** local author. **Chains:** [FC-04](chains/FC-04-semantic-authoring.md), optionally [FC-03](chains/FC-03-mapping-and-lexical-preparation.md), [FC-19](chains/FC-19-offline-portability.md) and [FC-06](chains/FC-06-knowledge-consumption.md).

The author pins a local Framework/Kit profile, builds a draft, uses a local dictionary when needed, validates it, and exports an integrity-checked private package for an admitted offline reader. No Skope, Médiathèque, GitHub, public release or Koali shell is intrinsically required. **Success:** semantic identity and private visibility survive round-trip; corrupted/incorrectly keyed packages fail. **Gate:** portability and possession are not authorization to redistribute.

## S03 — A civic decision becomes real work, then a reconciled accountability result

**Actor:** Konnaxion civic process and Orgo execution owners. **Chains:** [FC-09](chains/FC-09-world-contexts.md) + [FC-07](chains/FC-07-civic-deliberation.md) → [FC-23](chains/FC-23-external-interop.md) → [FC-08](chains/FC-08-governed-execution.md).

A World context is admitted; Konnaxion finalizes a DecisionRecord; an explicitly adopted IK `governance.decision.execute/1.0.0` request is received by Orgo. Orgo creates and runs **its own** Signal/Workflow/Case/Tasks; a durable outbox and terminal reconciliation determine whether effects happened. An adopted `accountability.impact.publish/1.0.0` handoff returns an impact record to Konnaxion. **Success:** a complete trace from finalized decision to terminal outcome without cross-owner database writes. **Failure:** duplicate intent produces one owner effect; an accepted command does not look like completed work; wrong World/tenant fails closed. The documented local IK qualification applies only to that exact environment/profile.

## S04 — A teaching team turns a situation into a supervised lesson and Moodle projection

**Actor:** educator and UCKK institutional authority. **Chains:** [FC-10](chains/FC-10-education-design.md) → [FC-11](chains/FC-11-learning-delivery.md), optionally [FC-08](chains/FC-08-governed-execution.md), [FC-02](chains/FC-02-source-custody.md) and [FC-21](chains/FC-21-creative-assets.md).

Kontexte supplies a reusable situation; Kompose develops a capsule and a **non-executable simulation**; Akor produces accessible mission roles. A teacher approves content and the neutral Ékole engine imports a content pack. If an actual operational mission is desired, Orgo separately admits the intent and owns real work. If a campus/Moodle projection is desired, UCKK authority separately approves and receives a write receipt. **Success:** class preview leaves Orgo and Moodle unchanged; approved live operations are idempotent and attributable; course projections can be rebuilt without altering Kristal canon. **Failure:** unapproved teacher/student privileges, mismatched campus identity, unsupported content language or corrupt media block their own boundary.

## S05 — Canonical concepts become faithful multilingual communication

**Actor:** language/editorial publisher. **Chains:** [FC-04](chains/FC-04-semantic-authoring.md) or another admitted typed content owner → [FC-12](chains/FC-12-language-runtime.md) → [FC-13](chains/FC-13-editorial-publishing.md) → [FC-22](chains/FC-22-public-presence.md).

A semantic input and its purpose are approved. SemantiK Architect selects a compatible qualified GF/grammar RuntimeSet and returns a traceable realization. Spek may build a document that a human editor approves before publication to a separately authorized site. **Success:** changing target language preserves source meaning and attaches runtime versions. **Failure:** absent lexical coverage, unqualified RuntimeSet, invented wording or editorial refusal yields explicit missing/blocked state. An editorial release is not a Framework publication.

## S06 — A new WorldRelease becomes available without changing civic history

**Actor:** Konnaxion/Orgo World owner and admitted host operator. **Chains:** [FC-09](chains/FC-09-world-contexts.md), [FC-16](chains/FC-16-platform-lifecycle.md), [FC-17](chains/FC-17-application-composition.md).

An owner prepares and qualifies a context release for the correct product; a platform operator independently admits the deployable artifact where needed; the application activates its World context; the optional Koali shell advertises the admitted surface only after required probes pass. **Success:** context identity and product version are visible, and prior business decisions remain owned by their original application. **Failure:** incompatible WorldRelease or failed backend means no falsely green surface; rollback of UI/config does not erase durable civic/operational records.

## S07 — An agent prepares an operation but never bypasses the real owner

**Actor:** authorized operator, Konductor workflow and Orgo. **Chains:** [FC-15](chains/FC-15-agentic-workflows.md) → [FC-14](chains/FC-14-identity-and-policy.md) → [FC-08](chains/FC-08-governed-execution.md).

Konductor receives a bounded job, proposes an action, records a checkpoint and requests explicit human/policy approval. Orgo then independently authenticates and admits a typed work intent if a profile is adopted. Konductor tracks the returned pending/terminal receipt. **Success:** the operator can explain which agent suggestion led to which approved Orgo effect. **Failure:** a prompt-injection request or model-invented resource identifier causes a denial; interrupted uncertain effects reconcile without duplication. **Current design gate:** no universal Konductor→Orgo contract identifier is approved in C0.

## S08 — A healthcare application uses knowledge without becoming a diagnostic authority

**Actor:** approved MediKristal operator. **Chains:** [FC-20](chains/FC-20-medical-domain.md), optionally [FC-06](chains/FC-06-knowledge-consumption.md), [FC-02](chains/FC-02-source-custody.md) and [FC-18](chains/FC-18-diagnostics-and-audit.md).

MediKristal retrieves permissioned references, presents attributable knowledge/pathway information and records a domain-owned event if allowed. Engineering diagnostics verify code against named tests. **Success:** tenant/patient privacy, provenance and uncertainty hold. **Failure:** stale/unsafe content, absent actor permission or unsupported clinical claims are blocked. **Critical boundary:** the provided evidence does not certify medical efficacy or authorize real patient-care decisions; those require separate clinical governance.

## S09 — Creative assets become part of a safe learning pack

**Actor:** artist/educator. **Chains:** [FC-21](chains/FC-21-creative-assets.md) → [FC-10](chains/FC-10-education-design.md) → [FC-11](chains/FC-11-learning-delivery.md).

Karacter supplies fictional character/story concepts; Kolor produces reviewed sheets and palettes; UCKK Assets or a content-pack owner records rights and a versioned reference; Kontexte/Ékole optionally consume it. **Success:** teacher can trace the artwork version and rights, and a later revision does not silently replace an ongoing class resource. **Failure:** unauthorized likeness, unsafe student media or unlicensed third-party content are rejected. **Current gate:** exact inter-tool export/import schema still needs owner adoption.

## S10 — A static collection reaches an offline reader safely

**Actor:** authorized collection owner and offline reader. **Chains:** [FC-05](chains/FC-05-knowledge-release.md) → [FC-19](chains/FC-19-offline-portability.md) → [FC-06](chains/FC-06-knowledge-consumption.md).

An authorized read surface is packaged in an integrity-checked portable artifact, transferred offline, and verified by Konstellation Light or an equivalent admitted reader. **Success:** content identity, language fallback and access class are preserved. **Failure:** tampered bytes, wrong encryption key or a private/public scope mismatch prevent import. Publisher dry-run is not live remote deployment.

## S11 — A controlled incident is recovered without rewriting other owners' state

**Actor:** incident operator and each affected system owner. **Chains:** [FC-24](chains/FC-24-operations-and-recovery.md), [FC-18](chains/FC-18-diagnostics-and-audit.md), [FC-16](chains/FC-16-platform-lifecycle.md).

A degraded backend is detected by required probes; the owning product pauses its relevant effect path, reconciles durable jobs, and the host rolls back an admitted release if necessary. Read-only derived views may rebuild from pinned inputs. **Success:** actual host state is measured and each owner declares its affected data status. **Failure:** if an outbox effect is uncertain, it remains pending; the Koali shell never labels it succeeded merely because routes respond.

## S12 — An external application exchanges typed data with an internal owner

**Actor:** trusted external workload and recipient owner. **Chains:** [FC-23](chains/FC-23-external-interop.md), [FC-14](chains/FC-14-identity-and-policy.md), optionally [FC-03](chains/FC-03-mapping-and-lexical-preparation.md).

The two parties adopt an exact capability/profile. DaaT may execute a pinned allowlisted mapping under an injected trusted identity and enforced policy. The receiver validates the payload and records its own receipt. **Success:** native and foreign schema mappings have transparent, different transformation burdens without ranking clients. **Failure:** missing IdP or audit provider, unauthorized mapping, unsupported profile or changed digest fails closed. DaaT's offline implementation is not claimed as a deployed global gateway.

## S13 — C0 publishes trustworthy navigational evidence

**Actor:** documentation maintainer and public audit publisher. **Chains:** [FC-18](chains/FC-18-diagnostics-and-audit.md) → [FC-22](chains/FC-22-public-presence.md).

A scoped exact-input owner diagnostic is received with its version, caveats and disclosure classification; C0 links it to the relevant chain/owner; an authorized public-safe projection is published by a portal or GitHub Audit. **Success:** a reader can distinguish proposed, locally qualified and deployed-observed facts. **Failure:** 53 matching snapshot digests are never presented as 53 passed product tests; unsigned/secret diagnostic files are not made public.

## S14 — The selected Konnaxion + Orgo VPS deployment profile

**Actor:** approved operator. **Chains:** [FC-07](chains/FC-07-civic-deliberation.md), [FC-08](chains/FC-08-governed-execution.md), [FC-16](chains/FC-16-platform-lifecycle.md), [FC-18](chains/FC-18-diagnostics-and-audit.md), [FC-24](chains/FC-24-operations-and-recovery.md).

The documented target is **Linux VPS + Docker + Konnaxion Capsule Agent** for a specific first tandem, not an ecosystem-wide architecture mandate. Before activation, exact ReleaseSet artifacts, independent KonnaxionDiag evidence, host PEP authorization, measured agent action and rollback readiness must be established. **Success proof is environmental**, not merely a local FakePlant IK test. C0 must keep target and verified state separate until the actual host receipts exist.

## Composition-wide acceptance

For any selected scenario, record: `scenario ID`, owners, starting identity/tenant, required source/contract version pins, ordered receipts, exact authorized effects, prohibited side effects, privacy scope, negative fixtures and a terminal evidence reference. A composition is qualified only when **all required owner boundaries in that named path** pass a shared pinned test; individual subsystem tests alone are insufficient.
