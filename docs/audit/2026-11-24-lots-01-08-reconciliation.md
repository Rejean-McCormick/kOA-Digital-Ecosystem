# C0 reconciliation: corrective lots 01–08 — 2026-11-24

**Scope and classification.** Offline consolidation of previously user-reported overlay installations and audited source snapshots. C0 has **not independently read the user's current repositories**. Status `USER_REPORTED_APPLIED` is not a revision-qualified owner acceptance or a production signal. C0 must retain exact owner authority and fail-closed admission.

## Provenance

The package digests and all 74 expected post-overlay file hashes are in [`2026-11-24-lots-01-08-evidence.v1.json`](2026-11-24-lots-01-08-evidence.v1.json); the open acceptance gates are in [`2026-11-24-lots-01-08-qualification-backlog.csv`](2026-11-24-lots-01-08-qualification-backlog.csv). The original dated audit reports and the ZIP manifests remain the source documents, rather than this commentary.

| Lot | Original source report | Overlay archive | Applied reported | Source tests or boundaries |
|---:|---|---|---:|---|
| 1 | `audit_ekole_pastorale_2026-11-23.md` | `koa_overlay_ekole_pastorale_2026-11-23.zip` | 10 | Pastorale: 35 v9 states; 14 targeted tests on Windows per user report; no global cross-repo qualification. |
| 2 | `koa_lot2_audit_2026-11-23.md` | `koa_overlay_correctif_lot2_2026-11-23.zip` | 10 | Focused source suites, Kristal Framework pin checks, Skope–Mediatheque synthetic handoff; live owner pair tests pending. |
| 3 | `koa_lot3_audit_2026-11-23.md` | `koa_overlay_correctif_lot3_2026-11-23.zip` | 6 | Targeted unit/contract checks; owner pin and public release qualification remain separate. |
| 4 | `koa_lot4_audit_2026-11-23.md` | `koa_overlay_correctif_lot4_2026-11-23.zip` | 14 | Atelier-Images 64/64 after corrections; courses 202/202 hashes; sibling-based full integration and pedagogy decisions pending. |
| 5 | `koa_lot5_audit_2026-11-23.md` | `koa_overlay_correctif_lot5_2026-11-23.zip` | 10 | Capsule Manager targeted 102; LevelUpDiag-Orgo 95; KonnaxionDiag 81; Orgo Worlds Node 34; full services and deployment not qualified. |
| 6 | `koa_lot6_audit_2026-11-23.md` | `koa_overlay_correctif_lot6_compatible_dik_v59_2026-11-24.zip` | 6 | Ency V32 30/30 on copy; 3 V5.9 preflight; C4 publish gate remains BLOCKED. |
| 7 | `koa_lot7_audit_2026-11-24.md` | `koa_overlay_correctif_lot7_2026-11-24.zip` | 11 | 267 Python tests passed, 2 skipped on copy; 21 doc validations; QEMU/PostgreSQL live excluded; Koali pnpm lock SHA checked on Windows. |
| 8 | `koa_lot8_audit_2026-11-24.md` | `koa_overlay_correctif_lot8_2026-11-24.zip` | 7 | LevelUpDiag 30/30 on copy; SemantiK Architect 144; RuntimeSet PGF release remains FAIL/BLOCKED. |

## Installation vs. qualification

- **Reported installations:** 74 file applications, 0 conflicts, from 8 overlay manifests and the user conversation; no direct readback of those 74 Windows files has been performed by this consolidation.
- **Earlier C0 documentary check:** a 2026-11-23 post-overlay snapshot matched 10/10 C0 files and 22/22 earlier owner-documentation files. That is an earlier binary comparison, **not** the same as a post-lot-8 checkout verification; do not merge those counts into the 74.
- **Pastorales lot 1:** owner confirmation covers a 10-file Pastorale patch and scoped local rebuild; the original C0 documentary update is a separate earlier artifact. Later complementary Kristal Manager/C0 overlay installation is **not attested** in the available record.
- **Lot 6 diK V5.9:** six EncyKlopedia guard hashes were verified at install time, without writes to the diK repository. The current state of diK is under its owner.
- **Lot 7 Koali Spaces:** `pnpm-lock.yaml` matched the expected SHA-256 during the owner's read-only check. No lockfile changes were applied.
- **Lot 8 SemantiK:** changes repair a diagnostic exception and stale configuration, **not** the underlying missing PGF; the standard campaign remains `FAIL/BLOCKED` where applicable.
- **Snapshot artifacts:** archive membership and test outcomes are not live Git HEAD evidence. A file missing from SmartDump may be excluded by capture policy and is not automatically missing on disk.

## Outstanding independent acceptance gates

| Gate | Status | Owner / boundary | Required evidence |
|---|---|---|---|
| QUAL-01 | `BLOCKED_OWNER_DECISION` | Konstellation-Light | Independent owner approval, exact pin and public release evidence. |
| QUAL-02 | `AWAITING_OWNER_CHECK` | Konstellation | Lock integrity, correct Node version, release workflow in controlled environment. |
| QUAL-03 | `BLOCKED_SOURCE_EVIDENCE` | SemantiK Architect | Authorized PGF artifacts and strict qualified RuntimeSet conformance; do not synthesize grammars. |
| QUAL-04 | `NOT_EXECUTED` | kOA-Linux | Linux/QEMU host, real images, recovery and sandbox validation. |
| QUAL-05 | `NOT_EXECUTED` | Konfid | Owner Postgres test service, concurrency / migration / audit replay. |
| QUAL-06 | `NOT_EXECUTED` | Konnaxion / Orgo | Owner-to-owner contract replay against running services. |
| QUAL-07 | `OPEN_OWNER_DECISION` | Ekole / Akor / Kontexte | Pedagogical sign-off before any mission/course link replacement. |
| QUAL-08 | `NOT_EXECUTED` | Ekole / sibling repos | Run complete integration tests with authorized sibling repositories. |
| QUAL-09 | `AWAITING_OWNER_CHECK` | Atelier-Images | Confirm actual Windows file and SmartDump inclusion policy; do not invent visual asset. |
| QUAL-10 | `AWAITING_OWNER_CHECK` | Spek | Check real Windows artifacts and source-controlled build; retain strict verification. |
| QUAL-11 | `OPEN_OWNER_RECONCILIATION` | Konstellation-Publisher | Separate active vs historical inventory and qualify fresh manifest if owner approves. |
| QUAL-12 | `AWAITING_OWNER_CHECK` | Konstellation-Light | Resolve approved logo source and compatible auditor without relaxing C4. |
| QUAL-13 | `NOT_EXECUTED` | SenTient | Authorized models, dependencies and complete controlled test environment. |
| QUAL-14 | `NOT_EXECUTED` | UCKK Ops Console | Windows PS7 runbooks and owner-approved local / remote test hosts. |
| QUAL-15 | `NOT_EXECUTED` | Koali-Control-Panel / LevelUpDiag-Koali | Run owner pair qualification before promoting diagnostic role. |
| QUAL-16 | `OPEN_SOURCE_GAP` | Ecole Pastorale | Owner source recovery or approved new guides, then recheck links. |
| QUAL-17 | `OPEN_OWNER_DECISION` | docs-initkoa-org | Owner validates cadence and public scope; no auto-publication. |
| QUAL-18 | `AWAITING_POST_INSTALL_READBACK` | C0 | Fresh owner C0 snapshot, exact revisions, no rewriting historical audit. |
| QUAL-19 | `DEFERRED_OWNER` | diK | Any diK changes handled exclusively by user; verify cross-repo compatibility without modifying diK. |
| QUAL-20 | `AWAITING_POST_INSTALL_READBACK` | All lots / C0 | Run read-only target fingerprint verification; no automatic repairs. |

## Coordination decisions and restrictions

1. This consolidation adds evidence only; owner source code and original C0 status, inventory, historical audit registers and `docs/target/` are untouched.
2. Respect C0 vocabulary: `OBSERVED_SNAPSHOT`, `DOCUMENTED`, `USER_DECIDED`, `PROPOSED`, `BLOCKED`, `UNKNOWN`; **installation is not qualification**.
3. Do not close historical findings based solely on a documentation overlay; require actual target-file SHA readback and owner acceptance.
4. No diK source modification, Git action, network publication, artifact promotion, service activation, QEMU bypass, C4 gate relaxation or synthetic PGF/model/PDF/lockfile is authorized.
5. Run the read-only Windows verifier for latest target-file bytes, then resolve individual `MISSING`/`DRIFT` records with each owner. A successful hash match is a source synchronization check only.

## Historical distinctions

The 23 November 55-snapshot inventory is distinct from the earlier 53-snapshot provenance ledger; neither is regenerated here. The original 17-item C0 documentation drift audit must remain historical. Previous reports describing the absence of `docs/target/` in SmartDump do not imply that owner repository files are absent from a newer checkout. The additional C0 + Kristal Manager follow-up ZIP is recorded as prepared; its installation is not attested by the evidence available to this consolidation.
