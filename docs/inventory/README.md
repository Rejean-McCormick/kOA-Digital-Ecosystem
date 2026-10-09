# Repository inventory — how to interpret it

This folder inventories *observed paths*, not software maturity, admission, authority, security or release readiness.

The Oct 9 2026 proposal combines 66 public GitHub repositories, the user-supplied `C:\mycode` tree with 100 `.git` markers, and previous GitSink origin observations. It also records 49 additional local, third-party or wiki checkouts (115 rows total). **Do not equate `.git` presence with verification of repository identity or integrity.**

- `repositories.json`: machine-readable rows, includes historical fields `local_root`, `github_repo`, `github_url`, `status`, `description`, `source_docs_paths`, `note`, and new `scope` / `evidence` metadata.
- `repositories.md`: a matching readable projection.
- `local_root` **may be `null`** where no root was verified, and consumers must not assume every row is a checkout that should be cloned or synchronized.
- `status` is an observation field: `local_git_marker_seen`, `previous_gitsink_observation_only`, `legacy_path_not_found`, `local_root_unknown`, `ambiguous_repository_identity`, `excluded_from_followup`.

**Exceptions:** `Omni-Wiki` and `OurAI` remain explicitly excluded from anomaly follow-up, per user request. UCKK is ambiguous and is not automatically mapped to the UCKK-Moodle checkout. Six other public repositories lack an identified Git marker in the supplied tree.

**Compatibility:** This is an inventory schema evolution from the 40 historical rows and their former statuses. Review callers that assume `local_root` is always a string or depend on legacy status names before replacing the production inventory. Historic 2026-09-28 corpus snapshots should remain historical and not be silently overwritten.

```text
inventoried != integrated != admitted != qualified != released != deployed
```
