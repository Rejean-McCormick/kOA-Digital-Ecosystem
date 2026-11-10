# Branch 10 — Public architecture and documentation integration

**Status:** `LOCAL_IMPLEMENTATION_VALIDATED` / `TARGET_DESIGN`; offline, no GitHub push or site deployment. The four new owner archives, checksums and structural observations are in [the input manifest](branch10-inputs.v1.json).

## Goal and scope

The central C0 repository provides the **canonical architecture intent**; `initkoa-docs`, `HomePage-initkoa.org` and `Koali-Scenario-Mosaic` consume **public, read-only documentation metadata**. None becomes a new authority for Konnaxion decisions, Orgo Tasks, canonical Kristal semantic identities, student data, personal health data or source preservation.

### Source condition observed

The provided `kOA_Digital_Ecosystem_Code_snapshot(7).zip` contains documentation tooling, navigation and 53-repository tests but **omits its referenced `docs/target/` tree**. This branch reconstructed that target set from the 53 captured owner snapshots, documented roles, the existing scripts/tests and the functional design described in the conversation. This reconstructed documentation is **not claimed to be byte-identical to previously generated v3/v4 Markdown**. It must be owner-reviewed before a normative release.

### Inter-product contract for branch 10

The generated [`public-architecture.v1.json`](../target/public-architecture.v1.json) is a **minimal, nonnormative, public-design metadata export** containing 24 chain IDs/titles, 53 public repository identities/roles and 26 proposed boundary endpoints. It intentionally excludes source ZIP paths, local Windows paths, private data, measured production status, tests, credentials and publication permissions.

`initkoa-docs` mirrors source Markdown for reading. The Homepage and Mosaic may reuse the public JSON to generate **navigation and explanatory pages**. They must not claim public publishing, deployment or bilateral contract qualification because the data says `TARGET_DESIGN`.

### Owner-specific change list

- **C0:** restore the missing target documentation, generate/validate minimal public export, restore reproducible wiki renderer input, update CI and regression tests.
- **initkoa-docs:** add a checked offline renderer from pinned C0 source into a browsable MkDocs section, with source attribution and no forced live wiki dependency for that section.
- **Homepage:** add an accessible read-only ecosystem architecture section and a searchable/listable 24-chain view, with source/draft classification visible.
- **Scenario Mosaic:** add an EN/FR architecture index link preserving the 36 bilingual scenarios and offline preview; no scenario becomes operational evidence.

### Gates

A deployed site requires independent build, content/licensing review, explicit public target authorization and measured publication. Remote GitHub HEAD and the actual published docs portal were not accessed. Cross-owner contracts outside this branch remain `TBD` or unqualified.

## Local verification completed (not deployment proof)

- **C0:** 52 unit tests passed; validated C0 coordination, target architecture, Tandem VPS metadata, the rendered 53-role portfolio, 26-boundary registry, inventory, public export and deterministic 47-page wiki generator.
- **Documentation portal:** 3 unit tests passed; offline source mirror regenerated and verified, including 24 chain pages. The supplied snapshot was missing a configured `LogoK.svg` asset; the broken MkDocs theme reference was removed without synthesizing official branding.
- **Homepage:** Node built-in `validate-final-system.mjs` passed for 24 chains, 53 public owner roles and 26 non-deployed target edges. The new read-only ecosystem pages and navigation use a static copy of the exact public projection. Next.js build **not run**: node dependencies are unavailable in the supplied snapshot.
- **Scenario Mosaic:** canonical content validation passed (36 scenarios × EN/FR = 72 files); public manifest validator passed; offline preview regenerated (2 mosaic pages + 72 scenario pages + 2 architecture pages); image fallback validation passed. Full Astro build **not run**: node dependencies are unavailable. The uploaded snapshot lacked its optional family illustrations and brand mark; generic **nonofficial fallback** SVGs were created only for missing assets. Owner-approved original branding is required before any real publication.
- **Cross-owner:** SHA-256 of the public JSON projection is identical in all four repositories; exact source revision and endpoint integrations **not verified on GitHub or in production**.

## Publication and cross-branch handoff

The public projection is **static and nonnormative**. The two web sites and documentation portal must accept new content only after exact-source provenance, privacy/rights review and site-owner approval. This branch makes no owner changes in Skope, Framework, Orgo, Konnaxion, Moodle, Koali security or any other product. Future branches 01–09 must deliver exact producer/consumer adopted profiles, tests, and failure-case evidence to C0. C0 must not upgrade target edges or owner snapshots to deployed status solely because navigation renders.

**Release caution:** the `initkoa-docs` CI snapshot includes an existing automatic GitHub Pages deployment on changes to `main`. Public content owners must review this before merging; this branch did not trigger that deployment.
