# diK V5.14 — private semantic observatory coordination

**Status:** `PROPOSED` implementation with `OBSERVED_SNAPSHOT` evidence only.
**Coordinator:** C0. **Index owner:** Kristal-Manager. **Canonical owner:**
local Kristal / Authoring Kit. **Semantics:** Framework v11 and diK's adopted
contracts. **Wikidata:** external reference service, not identity authority.

## Observed snapshot, not production deployment

The private candidate scanner recognizes v11 revisions in locally declared
`canon/state.index.json` files, including path variants under
`canon/domain/v11`, direct revisions, and `/updates`, and typed shorter role
names. It preserves lexical labels, language and source JSON, namespace-scoped
semantic IDs, revision, and Wikidata mappings as **nonselected occurrences**.

The local/public V5.13.2 comparison previously reported `OBSERVATION_ONLY`,
127 local / 126 hosted, with 126 matching state indexes and zero blockers;
it did *not* certify semantics. V5.14 is an additional **private candidate
index**, never a revision selector, canonical registry, outbound API or
public-hosting instruction.

## Operational interface

Run `scripts/check_semantic_observatory_v514.ps1` from this repository. It
invokes Manager with the exact known local roots and writes uniquely named
private `.sqlite` and `.json` under `%LOCALAPPDATA%\Kristal`. The Python CLI
can also read an owner-provided offline ZIP snapshot without extracting it.
Queries accept a bare KQ/KP, exact lexical term or Wikidata Q/P and an optional
**`--namespace-id`** to disambiguate; each result retains original revision,
source, status and record JSON. A candidate snapshot is neither live inventory
nor external Wikidata evidence.

## Acceptance gates

1. `OBSERVED_SNAPSHOT`: importer, integrity checks, adversarial unit tests.
2. `OWNER_REVIEW`: resolve incomplete layers and any true cross-owner
   `(namespace_id,id)` collision; separately review lexical and revision drift.
3. `REVIEWED_SELECTION`: explicit source digest and revision selection by the
   canonical owner, with preserved historical candidates.
4. `INDEPENDENT_QUALIFICATION`: exact-source Framework v11/TCK checks,
   human Wikidata `exactMatch` reviews with KS evidence, C1/C2 trust.
5. `AUTHORIZED_PUBLICATION`: derived Kit read surface, independent release
   controls C3, then a separately approved Git publication; activation is yet
   another decision.

No part of V5.14 performs steps 2–5 automatically. `kristal-public` remains
strictly read-only throughout this phase.
