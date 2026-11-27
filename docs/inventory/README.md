# kOA repository inventory

For **all repository roles in the final-system design**, see the [target portfolio](../target/PORTFOLIO.md) and [target architecture](../target/architecture.md). This inventory remains an identity and declared-path registry, not evidence of integration.

This directory documents **the currently declared kOA repository perimeter**, keeping repository identities separate from archived surveys, third-party clones, and personal research projects.

- [`GRAPH_FOCUS.md`](GRAPH_FOCUS.md) — guide to focused graph views.
- [`graph-focus.v1.json`](graph-focus.v1.json) — typed focused paths, branches, contracts, documentary evidence, and maturity levels (separate from application qualification).
- [`repositories.json`](repositories.json) — **Canonical machine-readable inventory**, 55 registered repositories.
- [`additional-repositories.v1.json`](additional-repositories.v1.json) — registered additional owner repositories and associated wiki checkouts (Kin-City); shown separately in [`repositories.md`](repositories.md), outside the current 55-role architecture baseline.
- [**Key ecosystem repositories and tooling**](ECOSYSTEM_TOOLING.md) and [`companion-tools.v1.json`](companion-tools.v1.json) — verified GitHub links for **[kOA Doc Server](https://github.com/Rejean-McCormick/kOA-Doc-Server)** and **[kOADiag](https://github.com/Rejean-McCormick/kOADiag)**, declared local checkouts, and their hinge roles. These companion tools do not change the 55-entry canonical inventory.
- [`code-snapshots-53.v1.json`](code-snapshots-53.v1.json) — SHA-256 ledger for 53 offline code archives, with audit status `NOT_EVALUATED`.
- [`code-snapshots-55-2026-11-23.v1.json`](code-snapshots-55-2026-11-23.v1.json) — separately dated SHA-256 ledger for 55 supplied offline code snapshots from 23 November 2026; this does **not** supersede the historical 53-snapshot ledger or prove code/documentation conformity.
- [23 November documentation/code issue compilation](../audit/2026-11-23-documentation-drift.md) — triaged owner issues; diK deferred during its owner update.
- [`repositories.md`](repositories.md) — human-readable generated view of the same declared perimeter.
- [`owner-source-observations-2026-11-24.v1.json`](owner-source-observations-2026-11-24.v1.json) — dated **offline observation** of the EncyKlopedia and C0 source ZIPs (SHA-256, source boundaries and caveats). The 55 identities and all historical Git verification statuses remain unchanged.
- [diK/Kristalizer integration coordination](../2-Technical-Reference/40-integration/dik-kristalizer/README.md) — source-root evidence and the separate owner-boundary workstream.
- [`GITHUB_DESCRIPTIONS.md`](GITHUB_DESCRIPTIONS.md) — proposed GitHub descriptions for related applications.
- [`apps-skope-ekole.json`](apps-skope-ekole.json) — Skope / Ékole application metadata.

The [Ekole ownership map](../1-Overview/Components-Skope-and-Ekole.md#ekole) links Ekole Core to its two independent content repositories. The November 12 registration records a user-reported local Git marker for Ekole-Quebec. Its GitHub identity was checked separately.

[Atelier Images](https://github.com/Rejean-McCormick/Ekole-Atelier-Images) is registered under its GitHub name, `Ekole-Atelier-Images`. The documented Windows installation is `C:\mycode\Ekole\Atelier-Images`. GitHub identity was checked separately. The local `origin` and an exact source revision remain unverified.

## Inclusion rules

An entry belongs to the canonical register if it is within the declared kOA owner portfolio, has a declared GitHub identity and local path, and has not been explicitly excluded or retired. Out-of-scope research, third-party or wiki clones, missing paths, and historical captures do not automatically qualify. Documentation and diagnostic companion tools are listed separately.

Each row reflects **the quality of the latest recorded observation**; it does not certify that local disk contents, Git `origin`, or HEAD are unchanged today. An unverified local remote must be identified as unverified.

The optional `latest_snapshot_observation` field in `repositories.json` refers to **additional offline source evidence only**, not an upgrade of the `status` field. In particular, EncyKlopedia is already registered; the 24 November archive does not justify a duplicate entry or a change of GitHub identity. Its owner documentation separately identifies the V32.2 source, V8 documentation and an independently distributed V8 station, and warns of a historical GitHub naming collision.

## Additional repositories for CI triage

These repositories are tracked here for CI follow-up outside the C0 owner portfolio. The Windows paths are user-reported. Local Git origins and revisions remain unverified.

| Repository | Reported local checkout root | Reported local wiki page | Source available for triage |
|---|---|---|---|
| [King-Klown-Canon](https://github.com/Rejean-McCormick/King-Klown-Canon) | `C:\mycode\01-Text_Based_Git\King_Klown\king-clown-canon` (reported `.git` marker) | `C:\mycode\01-Text_Based_Git\King_Klown\king-klown-canon.wiki\Home.md` | User-reported checkout |
| [kOA-Digital-Ecosystem-GitHub-Audit](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit) | Unknown | `C:\mycode\kOA-Digital-Ecosystem-GitHub-Audit\kOA-Digital-Ecosystem-GitHub-Audit.wiki\Home.md` | Source snapshot supplied 2026-11-24 |
| [VotingMachine](https://github.com/Rejean-McCormick/VotingMachine) | Unknown | Unknown | Source snapshot supplied 2026-11-24 |

## Git synchronization safety

This inventory is **descriptive, not an instruction to publish**. A `scope=PUBLIC` entry is neither GitSink permission nor evidence that a repository is ready for pushing. Explicit selection, verification of the Git root and `origin`, and publication gates are required before any Git write.

For integration evidence, see [current status](../status/current.md) and the [authority map](../2-Technical-Reference/10-system/authority-map.md).

## Language work contexts (2026-11-26)

The [multilingual documentary view](../2-Technical-Reference/40-integration/multilingual/README.md) groups 12 components for work and export without changing the 55-entry canonical registry or target roles.

## Local documentary sources (2026-11-26)

See [`documentary-sources.v1.json`](documentary-sources.v1.json) for the six historical catalogue entries that were unresolved in the last Doc Server export. GF Audit is a local archive, Konnaxion's two diagnostic views are consolidated under the current owner, Kristal-Reference is archived (2026-10-03), LevelUpDiag-Kristal is consolidated into the local Navigation diagnostic, and UCKK is a functional domain whose three declared components replace the generic source. Doc Server reads this lifecycle policy at startup, falling back to its bundled copy. This register is descriptive, not a Git inventory or a permission to publish. The 55 canonical paths remain unchanged. Doc Server's actual installed root is recorded in [`companion-tools.v1.json`](companion-tools.v1.json).
