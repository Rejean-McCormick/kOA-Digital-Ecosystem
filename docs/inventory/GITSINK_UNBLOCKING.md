# GitSink: safely enroll four snapshot-only repositories

The C0 repository inventory currently contains four `PUBLIC` entries with status
`source_root_observed_in_smartdump_remote_unverified`: **diK, Karacter, Kolor,
and Kristalizer**. Their source paths were recorded from SmartDump, not from a
verified local Git checkout. The Runner correctly reports `HORS_AUTORISATION`;
existence of a same-named GitHub repository alone does not verify a Windows
`origin` or authorize publishing files.

## Procedure on the Windows machine that owns `C:\mycode`

From the **kOA-Digital-Ecosystem** checkout, with Python 3.9 or newer and Git
installed:

```powershell
cd C:\mycode\kOA_Digital_Ecosystem\kOA_Digital_Ecosystem
python scripts\verify_gitsink_inventory.py
```

This is a **read-only audit**. It checks each unchanged `local_root` against the
actual worktree root, `.git` marker, `remote.origin.url` (raw and effective),
and origin push URL (raw and effective). All identities must point **directly**
to their declared `Rejean-McCormick/<repo>`; rewrites, alternate destinations,
multiple URLs, and missing checkouts fail closed. It never performs `fetch`,
`git add`, `commit`, `push`, or changes to Git configuration.

If **all four** report `VERIFIED`, update only the two local inventory views:

```powershell
python scripts\verify_gitsink_inventory.py --apply
python scripts\render_repository_inventory.py --check
python scripts\validate_c0_coordination.py
git diff -- docs/inventory/repositories.json docs/inventory/repositories.md
```

`--apply` changes the four inventory statuses to `local_git_marker_seen`, **not**
`github_and_local_remote_verified`; it does not claim a current remote HEAD,
qualified integration, release, or permission to push. It updates no unrelated
repo entries. If even one verification fails, **nothing is written**: diagnose
that specific checkout and do not manually override the inventory or repoint
its remote without independent confirmation.

Review the diff, then use the normal approved Git process to commit the two
inventory files to kOA. Because GitSink reads the **local** kOA inventory, a
new GitSink Runner **simulation/rescan** is needed after applying the change;
its independent direct-origin, safe-batch, and other checks still apply. A repo
becoming `PRET` does **not** authorize a push. Execution still requires explicit
manual selection after simulation. Recheck the intended files before any
public push, especially for Kristal-related data.

If the Runner instead reports `BATCH_ABSENT`, `BATCH_NON_SECURISÉ`, or
`ORIGIN_DIFFERENT`, those are separate local issues that this inventory
procedure intentionally does not bypass.
