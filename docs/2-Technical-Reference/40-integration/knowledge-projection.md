# Knowledge acquisition → Kristal canon → consumer projection

**Status:** current frozen cross-repository contract baseline

## Authority direction

```text
source acquisition
    → EncyKlopedia immutable evidence / referent candidates
    → Da’at mapping / ACL
    → Kristal referent identity + epistemic canon
    → rebuildable UCKK / Univers-Cité projection
```

## Current contract set

| Surface | Current identifier |
|---|---|
| Kristal release-candidate contract baseline | `5.0.0-rc.3` |
| Kristal Referent Registry | `kristal.referent-registry/1.0.0` |
| Kristal knowledge-model bundle | `sha256:07fe0527ab29a4b40870efdd0c9e0c67c91de919e5428047245b2a2c04f8ea98` |
| EncyKlopedia handoff | `encyklopedia.corpus-harvest-handoff/1.0.0` |
| IK build request | `kristal.build.request/1.1.0` |
| IK artifact ready | `kristal.artifact.ready/1.1.0` |
| UCKK / Univers-Cité projection | `uckk.univers-cite-projection/1.0.0` |

Machine-readable set: [`knowledge-projection-contract-set.json`](./knowledge-projection-contract-set.json).

## Ownership

### EncyKlopedia

Owns source discovery/acquisition, provider resolution, lossless evidence/provenance, referent candidates and the immutable handoff. A referent candidate is not automatically a validated claim or recognized referent.

### Da’at

Owns mapping/ACL behavior at the Kristal boundary. It adapts payloads without acquiring source authority or redefining Kristal semantics.

### Kristal

Owns domain-neutral referent identity semantics, assertions, evidence/provenance, validation/recognition and canonical epistemic artifacts. External identifiers remain evidence/identifiers, not authority.

### UCKK / Univers-Cité

Owns consumer projection choices: scope membership, primary view, derived glossary, Moodle materialization and media-library presentation. A projection is rebuildable from pinned Kristal artifacts and never becomes the Kristal source of truth.

### Interaction Kernel

Carries only explicitly adopted versioned profiles. It owns no participant operational or epistemic state.

## Release-state caveat

The supplied Kristal `kristal-release.json` declares:

```text
version  5.0.0-rc.3
status   release-candidate
tag      v5.0.0-rc.3
commit   unresolved / null
```

Therefore:

- the **contract baseline is frozen** for this knowledge boundary;
- rc.3 must **not** be described as a completed immutable published release until the tag resolves to a commit;
- existing downstream integrations locked to an older immutable Kristal release remain separately locked until their owners explicitly update them.

## Non-confusions

```text
acquisition evidence      ≠ validation
referent candidate        ≠ recognized referent
external identifier       ≠ authority
Kristal artifact          ≠ Moodle record
consumer projection       ≠ source of truth
IK transport              ≠ participant state
contract baseline frozen  ≠ release commit resolved
```
