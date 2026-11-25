# diK V5.13 — local canonical source to public read surface

Status: **candidate observation and review procedure**. It confers no revision-selection authority, C1/C2 qualification, or deployment grant.

## Responsibilities

1. **Local Kristal** (`C:\mycode\Kristal\locals\Kristal-*`): owner of `canon/`, domain decisions and additive revisions. Historic labels, evidence, and assertions remain intact.
2. **diK**: namespace-qualified KQ/KP/KA/KS registries, multilingual dictionaries and reviewed Wikidata links. Lexical similarities or a local SHA do not establish `exactMatch`.
3. **Framework and Authoring Kit**: structural contracts, isolated candidate construction and native validations.
4. **Manager**: read-only drift observation, explicit private staging and separate exact local commit preparation.
5. **Bootstrap, Integration Pack and KristalDiag**: node/contract/C3 diagnostics without silent canonical or workflow repairs.
6. **Independent C1/C2 authorities**: exact-input qualification and commit-specific approval. Public release and RuntimeSet activation remain separate.

## Windows diagnostic

From the Git root of `kOA_Digital_Ecosystem`:

```powershell
& .\scripts\check_kristal_local_first_v513.ps1
```

The command reads 127 local workspaces and the public collection, comparing only **declared canonical artifacts** within its defined scope. With `-Output`, it writes a new private report outside both trees; without it, it writes JSON to stdout. An absent public artifact that is also absent from the corresponding `.kristal/sync-manifest.json` is classified `EXCLUDED_FROM_PUBLIC_READ_SURFACE` and is never copied automatically.

A graph-pinned v11 revision selection is **separate** from file integrity. Wikidata QIDs are references, not Kristal identities. Neither `OBSERVATION_ONLY` nor schema parity is an approval to prepare a public commit, push, or reconcile `.kristal/bootstrap-state.json`. These operations retain their own owner and independent gates. Any `BLOCKED_INTEGRITY` result stops preparation for owner review.

## Snapshot baseline (November 24, 2026)

126 hosted members out of 127 local workspaces; 126 canonical indices and 985 shared canonical artifacts byte-identical; 7 local files outside public sync manifests; `pitheory-prime-bridge` local only. Among declared crosswalks, 154 `exactMatch` occurrences have `status=accepted`, all carrying `review.method=audited_rule` and requiring separate evidence review. These are **supplied snapshot observations**, not claims about a future Windows checkout or Wikidata semantic qualification.
