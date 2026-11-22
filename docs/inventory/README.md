# kOA repository inventory

For **all repository roles in the final-system design**, see the [target portfolio](../target/PORTFOLIO.md) and [target architecture](../target/architecture.md). This inventory remains an identity and declared-path registry, not evidence of integration.

This directory documents **the currently declared kOA repository perimeter**, keeping repository identities separate from archived surveys, third-party clones, and personal research projects.

- [`GRAPH_FOCUS.md`](GRAPH_FOCUS.md) — guide to focused graph views.
- [`graph-focus.v1.json`](graph-focus.v1.json) — typed focused paths, branches, contracts, documentary evidence, and maturity levels (separate from application qualification).
- [`repositories.json`](repositories.json) — **Canonical machine-readable inventory**, 55 registered repositories.
- [**Key ecosystem repositories and tooling**](ECOSYSTEM_TOOLING.md) and [`companion-tools.v1.json`](companion-tools.v1.json) — verified GitHub links for **[kOA Doc Server](https://github.com/Rejean-McCormick/kOA-Doc-Server)** and **[kOADiag](https://github.com/Rejean-McCormick/kOADiag)**, declared local checkouts, and their hinge roles. These companion tools do not change the 55-entry canonical inventory.
- [`code-snapshots-53.v1.json`](code-snapshots-53.v1.json) — SHA-256 ledger for 53 offline code archives, with audit status `NOT_EVALUATED`.
- [`repositories.md`](repositories.md) — human-readable generated view of the same declared perimeter.
- [diK/Kristalizer integration coordination](../2-Technical-Reference/40-integration/dik-kristalizer/README.md) — source-root evidence and the separate owner-boundary workstream.
- [`GITHUB_DESCRIPTIONS.md`](GITHUB_DESCRIPTIONS.md) — proposed GitHub descriptions for related applications.
- [`apps-skope-ekole.json`](apps-skope-ekole.json) — Skope / Ékole application metadata.

The [Ekole ownership map](../1-Overview/Components-Skope-and-Ekole.md#ekole) links Ekole Core to its two independent content repositories. The November 12 registration records a user-reported local Git marker for Ekole-Quebec. Its GitHub identity was checked separately.

[Atelier Images](https://github.com/Rejean-McCormick/Ekole-Atelier-Images) is registered under its GitHub name, `Ekole-Atelier-Images`. The documented Windows installation is `C:\mycode\Ekole\Atelier-Images`. GitHub identity was checked separately. The local `origin` and an exact source revision remain unverified.

## Inclusion rules

An entry belongs to the canonical register if it is within the declared kOA owner portfolio, has a declared GitHub identity and local path, and has not been explicitly excluded or retired. Out-of-scope research, third-party or wiki clones, missing paths, and historical captures do not automatically qualify. Documentation and diagnostic companion tools are listed separately.

Each row reflects **the quality of the latest recorded observation**; it does not certify that local disk contents, Git `origin`, or HEAD are unchanged today. An unverified local remote must be identified as unverified.

## Git synchronization safety

This inventory is **descriptive, not an instruction to publish**. A `scope=PUBLIC` entry is neither GitSink permission nor evidence that a repository is ready for pushing. Explicit selection, verification of the Git root and `origin`, and publication gates are required before any Git write.

For integration evidence, see [current status](../status/current.md) and the [authority map](../2-Technical-Reference/10-system/authority-map.md).
