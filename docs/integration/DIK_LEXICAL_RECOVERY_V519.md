# V5.19 one-shot local recovery

Run INSTALLER_PS7.ps1 -Apply from the verified overlay. Installer checks base
V5.16/V5.18 implementation fingerprints, adds seven files, saves a receipt in
_overlay_backups, runs focused regressions, refreshes derived V5.16/V5.18
and builds SEMANTIC_V519_*.sqlite and SEMANTIC_V519_*.json under LocalAppData/Kristal.
The fresh V5.18 public-plan JSON is a draft; no public writes are authorized.

Do not run concurrent authoring or manager operations. On failure, read the
terminal output. Source additions remain installed, existing files are not
replaced. Reruns accept already installed identical files. No canonical
rollback is needed for this recovery because it makes no canonical writes.
The inherited V5.16 projection refresh creates its own private backups.

Scope: no native graph conversion, no new V11 profile, no new Wikidata approval,
no publication. The new data is explicitly unreviewed. A verified local dump or
other authenticated evidence is a prerequisite for canonical lexical promotion.
