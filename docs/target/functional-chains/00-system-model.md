# 00 — Final-system functional model

**Status:** `TARGET_DESIGN` · **Applies to:** FC-01 through FC-24 · **Read before:** any chain.

## Purpose

The final kOA ecosystem is a **federation of independently owned products** with explicit, reproducible handoffs. It is not a single application, one universal event bus, one canonical database, or a requirement to deploy all repositories together. A repository may contain source code, a diagnostic engine, a content pack, a runtime adapter, a document portal, an offline tool, an instance template, or a product UI. The portfolio has **53 registered repository identities**; the number of running services is intentionally unspecified.

Every functional chain describes a *useful outcome* independently of its current implementation. It identifies an owner, the initiating actor, inputs, controlled state changes, output, visible experience, forbidden shortcuts, failure responses and the proof required for acceptance.

## Three distinct kinds of authority

1. **Epistemic authority:** what counts as approved canonical Kristal semantic identity/state. Owned by the appropriate Framework/authoring/release authority; neither research nor an LLM assigns this automatically.
2. **Business and institutional authority:** civic decisions (Konnaxion), operational Cases and Tasks (Orgo), institutional/Moodle decisions (UCKK), application data (individual owners), and domain policies.
3. **Execution and release authority:** whether an artifact may be published, installed, made public, activated on a host, or shown in an admitted Space. This is not inherited from semantic or business authority.

Authorization, qualification, publication, activation and presentation are separate questions even when the same human coordinates them.

## Functional zones

```text
Research and source evidence             Independent owners of state
  Skope / integrated EncyK                 Konnaxion | Orgo | UCKK | domain apps
          |                                           ^
  Médiathèque custody                                 | explicit admitted intent
          |                                           |
Mapping / lexical preparation             Education design and agentic requests
  DaaT, diK, Kristalizer                    Kontexte / Kompose / Akor / Konductor
          |
  Framework + Authoring Kit  --> qualified/published knowledge --> read clients
          |                       |                         (Kompiler, Konstellation,
  diagnostics & owner approval    |                          EncyKlopedia, Ékole)
          |                       v
  instance/release management   optional platform admit/activate --> Koali Spaces
                              (separate presentation lifecycle)

Cross-cutting: identity / policy / owner enforcement, IK when adopted,
               diagnostics, observability, portability and recovery.
```

**This is a dependency diagram, not a required synchronous transaction.** A local author can work without research; a read client can use an authorized offline release; civic work does not depend on semantic authoring; Koali Spaces is optional. No arrows imply an already signed bilateral contract.

## Common shape of a functional chain

| Property | Required question |
|---|---|
| Outcome | What user-visible or machine-verifiable result is produced? |
| Actor and admission | Who can request it, in which tenant/context and with what permissions? |
| Ownership | Which repository owns authoritative state and final decisions? |
| Inputs | Which exact versioned artifacts, references or source bytes are accepted? |
| Processing | Which bounded stages are performed, without silent policy changes? |
| Outputs | What immutable or durable receipt supports the outcome? |
| Failure | What is rejected, quarantined, retried or rolled back? |
| Verification | Which owner-level and cross-owner tests prove the named capability? |

## Data classifications

- **Raw/untrusted evidence:** unreviewed provider data, documents, suggested terms, model output and external identifiers. Never canonical by transport.
- **Preserved source:** immutable or versioned custody objects with a provenance chain and access policy. Storage acceptance does not validate truth.
- **Candidate/review material:** proposed mappings, translations, plans, learning intents or agent suggestions. Explicitly non-authoritative.
- **Canonical semantic state:** approved, versioned Kristal identities and typed relations constrained by the selected Framework profile.
- **Owner business state:** durable product operations/decisions, not writable by another product's UI or bridge.
- **Derived projections:** read models, contexts, search indexes, educational exports and presentation state; must be identifiable and rebuildable from permitted inputs.
- **Publication/activation state:** authorization-specific release records and runtime receipts, distinct from content/data state.

## Required invariants

- One authoritative owner per mutable state and per owner decision; no cross-owner database writes.
- Explicit, versioned and tested contracts at actual product boundaries. IK is optional and only used where adopted; a central C0 schema is not a substitute for bilateral agreement.
- No implicit acquisition → semantic approval, diagnosis → permission, build → publication, release → host activation, or host activation → Space activation.
- Derived objects must carry their origin version and classification; consumers must not claim more authority than their producer supplied.
- Deny by default on missing permissions, incompatible versions, invalid digests, or undecidable ownership.
- Human review and auditability for high-impact changes; agents, GUIs, and diagnostics are not hidden superusers.
- Offline operation, degraded mode and recovery are designed per owner and per chain, not promised universally.

## How the 24 chains compose

**Knowledge lane:** FC-01 → FC-02 → FC-03 → FC-04 → FC-05 → FC-06; each arrow is optional unless the selected use case requires it.

**Civic lane:** FC-07 → FC-08, with FC-09 for World context and FC-23 for admitted contracts.

**Education lane:** FC-10 → FC-11; actual work may hand off to FC-08, but pedagogical simulation never silently becomes a real Case.

**Communication lane:** FC-04 or approved business input → FC-12 → FC-13 → FC-22, as applicable; publishing text never grants semantic truth.

**Operational wrapper:** FC-14 + FC-18 + FC-24 govern any high-impact handoff; FC-16/FC-17 are optional host and UI lifecycles; FC-15 and FC-19 are bounded automation/portable paths; FC-20 and FC-21 are separate domain capabilities.

Use [the contract model](02-contract-and-receipts.md), [lifecycle rules](03-state-trust-and-failure.md) and [scenarios](04-cross-chain-compositions.md) to interpret these compositions.
