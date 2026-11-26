# V5.16: local-first semantic evolution, single operational overlay

The local authoring profile is the authoritative source of **which** v11
registry, graph, crosswalk and catalog are currently used inside a local
Kristal. The V5.14 federation observes all historical revisions and does
not itself select one. V5.16 adds the active, usable local semantic projection.

The one-step PowerShell 7 installer:

1. Verifies payload SHA-256, exact Git roots and target-file preconditions.
2. Applies its four-repository source/doc overlay with recoverable file backups.
3. Runs the focused local semantic evolution regression tests.
4. Builds a fresh source-pinned V5.14 integrity index and materializes the
   active semantic projection in each opted-in local Kristal.

No separate operator review cycles are required for this deterministic
read-layer evolution. Content-addressed local derived files preserve the
old versions, and pre-existing pointer bytes are backed up. The operation
never changes any canonical identities, claims an automatic Wikidata approval,
edits `kristal-public`, publishes, pushes Git or activates a RuntimeSet.

For a meaning-changing canonical correction, use Authoring Kit's recoverable
v11 artifact registration with supporting evidence; a derived convenience
index is not authorization to change the canon.
