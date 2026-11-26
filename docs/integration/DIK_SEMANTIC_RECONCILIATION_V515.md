# V5.15 — private semantic-reconciliation review coordination

**Evidence:** `OBSERVED_SNAPSHOT` and local unit tests; *not* live owner
review, Wikidata authenticity, remote qualification, deployment or publication.

| Responsibility | Owner | Gate |
| --- | --- | --- |
| Canonical v11 identities and revision registration | Local Kristal + Authoring Kit | Exact-state commitment and owner approval |
| Federated candidate semantic occurrences | Kristal-Manager V5.14 | Integrity only |
| Revision/lexical/Wikidata discrepancy cases | Kristal-Manager V5.15 | Private review, all `NOT_DECIDED` |
| Normative identity meaning/graph constraints | Framework + diK adopted contracts | Independent validation |
| Qualified public read surface | Kit / independent release owners | C1/C2 then explicit C3 authorization |

## Local-first workflow

1. Obtain exact **private** V5.14 SQLite from local Kristal sources, rather
   than selecting the latest filename automatically.
2. Run `scripts/check_semantic_reconciliation_v515.ps1 -SourceDb '<exact .sqlite>'`.
   The script writes a new review SQLite and JSON **outside Git repositories**
   under `%LOCALAPPDATA%\Kristal`. Source SHA-256 is pinned and rechecked.
3. Inspect paged cases with `python -m kristal_manager semantic-review-cases`.
   A case includes owner, namespace, semantic ID, language, candidate/accepted
   external status and source revision/path where applicable.
4. Review owners and evidence manually. V5.15 has **no decision-writing API**.
5. Future independent selection, native Kit revision, qualification, and
   publication require separately implemented approved workflows.

On the supplied 127-local-workspace snapshot, V5.15 found 991 review cases:
43 high-priority, 330 medium and 618 low. These are **review signals**:
367 source-scoped IDs had multiple active external `exactMatch` targets, 6
identity/language groups had competing preferred terms, 546 normalized terms
were shared across IDs, and 72 owners had multiple complete unselected
revisions. Rejected Wikidata targets were deliberately excluded from active
target conflict counts. No semantic identity has been merged.

The source V5.14 index includes 25,741 occurrences of source-recorded
`accepted`/`audited_rule` exact matches across revisions. None is independently
approved by V5.15 merely because the source says `accepted`.

This C0 document coordinates evidence only. Framework, local owner, diK, Kit,
qualifiers and publishing authorities retain their established boundaries.
