# DIK V5.18 — Local active semantic federation and public-sync proposal

Owner and integration status: Kristal Authoring Kit (local canon), Kristal
Manager (active derived index), diK (lexical tools and external crosswalk
proposals), kOA C0 (coordination). The implementation is a *local candidate*.

## One-shot sequence

1. Kit V5.17 retries already-evidenced accepted-precedence canonical updates,
   if any remain. All writes are versioned and journaled by the Kit.
2. Manager V5.16 regenerates verified active profiles and derived pointers.
3. Manager V5.18 builds the private total identity index keyed by namespace
   plus KQ/KP/KA/KS, separately recording reviewed source statuses, lexical
   labels and ambiguous external candidates.
4. A private synchronization *review plan* compares local canon to hosted
   `kristal-public`. It does not write to the public checkout or authorize a
   GitHub push.

Source-level exact hashes and active profile pins are checked when V5.18
reads local projections. The report distinguishes historical lexical hints
from canonical preferred terms and retains the missing-profile count.

## Explicit limits

- No automatic Wikidata exactMatch acceptance or inferred semantic identity.
- No auto-promotion of Kristals without complete active V11 authority.
- No public file writes, C1/C2 qualification, remote release, or RuntimeSet.
- Snapshot/fixture validation is not a claim of successful execution on the
  user's live Windows repositories.

Entry point: `scripts/apply_semantic_federation_v518.ps1 -Apply`.
