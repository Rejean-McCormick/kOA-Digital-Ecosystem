# V5.17: one-shot local canonical precedence + derived view refresh

This release applies exactly one deterministic editorial rule to the active
local v11 crosswalk: an already accepted, registered-KS-backed Wikidata Q/P
has priority over competing different-Q/P candidate exactMatches of the
same scoped KQ/KP. New canonical crosswalk versions are registered through
the Authoring Kit's recoverable transaction journal and selected with
historical profile backup. V5.16 projections are then regenerated locally.

The same PS7 `-Apply` command verifies exact Git roots, payload hashes,
target preconditions, runs focused regression tests, preflights local sources,
applies eligible canonical changes and rebuilds derived active dictionaries.

Baseline snapshot (2026-11-25): 13 owners, 43 scoped identities and 202
competing candidates were eligible. The live script recomputes that number
from the user's installed workspaces; it refuses unexpected drift and
provides an interruption progress report.

No candidate is promoted to accepted, no lexical homonym is merged and no
canonical history is rewritten. The operation does not touch `kristal-public`,
Git remotes, published states or RuntimeSets. Interrupted multi-owner batches
can leave completed append-only registrations; follow the Kit recovery docs.
