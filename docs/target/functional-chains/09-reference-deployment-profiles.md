# 09 — Reference operating and deployment profiles

**Status:** `TARGET_DESIGN`. These are **compositions** of functional chains, not a declaration that a matching deployment is available. Products can be used separately; the final architecture must avoid forcing optional services into all profiles.

## Profile map

| Target profile | Required functional capabilities | Optional extensions | Explicit non-requirements |
|---|---|---|---|
| **P-A: Offline authoring workstation** | FC-04 semantic authoring; FC-14 local authorization appropriate to owner scope; FC-24 local recovery | FC-03 lexical preparation, FC-19 packaging, FC-06 static reading, FC-18 diagnostics | Network research, public Git, kOA-Linux, Orgo, Koali shell |
| **P-B: Authorized public knowledge reader** | FC-05 released/pinned collection; FC-06 compatible consumer; FC-14 public/private disclosure; FC-24 reader health | FC-12 language realization, FC-13 editorial content, FC-22 public portal, FC-19 offline export | Source acquisition, workspace editing, platform appliance |
| **P-C: Civic execution tandem** | FC-07 finalized Konnaxion decision; FC-08 Orgo execution; FC-14 enforced identity; FC-23 adopted boundary; FC-24 reconciliation | FC-09 World context, FC-16 host deployment, FC-17 shell, FC-18 independent diagnostic | Canonical Kristal authoring, Moodle, public wiki publication |
| **P-D: Campus learning site** | FC-10 approved lesson design; FC-11 Ékole/institution learning projection; FC-14 institution permissions; FC-24 data recovery | FC-02 media, FC-06 knowledge, FC-08 actual supervised work, FC-21 assets | Compulsory live Orgo Cases for every lesson, mandatory Skope acquisition |
| **P-E: Integrated kOA host** | FC-14 host and product authorization; FC-16 admission/activation; FC-18 release qualification; FC-24 measured recovery | FC-17 Koali Spaces, any independently admitted product chains | One global database or a claim that shell admission grants domain authorization |
| **P-F: Language/editorial workstation** | FC-12 pinned grammar/realization where used; FC-13 editorial review; FC-14 disclosure | FC-04 semantic input, FC-22 web publication, FC-18 language diagnostics | Automatic truth certification or forced public publication |
| **P-G: Controlled medical-domain workspace** | FC-20 MediKristal; FC-14 privacy/role controls; FC-24 incident response; independent clinical/institutional safety governance | FC-02 source custody, FC-06 approved read views, FC-18 engineering tests | A clinical certification claim from code-unit tests or this C0 design |
| **P-H: Creative/learning design studio** | FC-21 attributable creative assets; FC-14 content rights/access policy; FC-24 local recovery | FC-10 Kontexte/Kompose scenarios; FC-11 Ékole/UCKK assets; FC-19 portable export | Semantic canon mutation, production deployment of all tools |

Profile-specific requirements such as operating system, host, Docker, URL, resource envelopes, release channel or authentication provider are **owner decisions**; C0 will record an adopted specific profile rather than invent a universal deployment matrix. The **previously selected first civic tandem** is Linux VPS + Docker + Konnaxion Capsule Agent; that is an explicit selection for P-C, not a blanket requirement for P-A through P-H.

## Profile acceptance protocol

1. Name the profile/environment and included product **versions**, with exact deployment and contract pins.
2. Identify which chains are **required** for this instance, and which are deliberately out of scope.
3. Obtain owner approval and independent evidence for every privileged effect, media disclosure or public release.
4. Execute the relevant [cross-chain scenario](04-cross-chain-compositions.md) and [qualification campaign](06-qualification-and-acceptance.md) against the actual selected producer/consumer revisions.
5. Prove the **negative path**: what happens if one required owner, schema, identity provider, source, host or read view is missing?
6. Exercise restoration/reconciliation for that profile; publishing a design-only diagram or CI pass is insufficient.
7. Update the maturity map with **only the proven named scope**, not a global "ecosystem operational" badge.

## Minimum publication/operation separation

A hosted read-only collection can be published without a running Koali Space. A desktop authoring environment may exchange files without a platform deploy. An Orgo Case can be created through an admitted backend request while the UI is down. A deployed product may be visible through its own web UI even when a shared Koali shell is disabled. A Moodle course materialization needs institutional approval whether or not a semantic source was qualified. These are architecture properties, not exceptions.
