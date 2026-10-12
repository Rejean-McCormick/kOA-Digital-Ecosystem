# Historical inventory-update proposal — October 9, 2026

**Historical proposal status, not a live deployment assertion.** The paths in this ZIP are *relative to* the actual checkout:

`C:\mycode\kOA_Digital_Ecosystem\kOA_Digital_Ecosystem`

## Proposed tracked changes

1. Replace `docs/inventory/repositories.json` with the 115-row reconciliation.
2. Replace `docs/inventory/repositories.md` with its matching human-readable projection.
3. Replace `docs/inventory/README.md` to document observation statuses, null roots and scope.
4. Replace the repository's `GitSink.bat` with a fail-fast version compatible with the GitSink Runner's call `cmd /d /c GitSink.bat Automated-update`.

The `reports/` folder is supporting evidence for review and **does not have to be copied into the repository**.

## Evidence summary

- 66 currently public repositories in Rejean-McCormick account, checked independently with GitHub-connected account tools.
- Of the 66: 57 mapped to a path explicitly marked `[GIT]`; 3 unknown local roots; 3 historical paths not found; `UCKK` ambiguous; `Omni-Wiki` and `OurAI` excluded from local follow-up.
- 100 distinct `[GIT]` markers in user-supplied `mycode_arborescence_git.txt`.
- 6 additional nested wiki checkouts known from older GitSink output, not freshly discovered by the depth-stopped tree.
- 49 local/external/wiki entries supplement the 66 canonical public records. GitHub `full_name` canonicalized in the public list only.

## GitSink.bat change

The original batch ran add, commit and push unconditionally, and ended with `pause`. The proposed batch:
- works from the directory containing itself and demands a `.git` folder or file;
- checks `git` availability and *stops* on an `add`, diff, commit or push failure;
- handles an empty working tree without mistaking it for an error;
- tries `git -c core.longpaths=true add --all` on Windows;
- leaves a nonzero exit code so the Runner can report a failure;
- does not prompt for commit message or pause when launched unattended;
- retains `git add --all`, commit and push behavior when it is **explicitly executed** (it is not a read-only tool).

WARNING: `GitSink.bat` still stages *all* files. Review `.gitignore`, the changed files and secrets **before** running it. Also, replacing only this file in the kOA checkout does not update the copies in all the other local repositories. The GitSink Runner operates on each local repository's own batch.

## Recommended local application

1. Back up the four current files in the kOA checkout.
2. Compare the proposal against the checkout, especially JSON null roots/statuses and any inventory consumers.
3. Copy the four tracked files under the checkout root.
4. Validate JSON (Python `python -m json.tool docs/inventory/repositories.json > NUL`) and inspect `git diff`.
5. Commit/push the changes manually *after inspection*, not through an unreviewed mass GitSink run.
6. Test `GitSink.bat` in a disposable test repository on Windows before deploying it across other repositories.

GitHub integration previously returned HTTP 403 for writes; no claim is made that changes can be pushed directly through that integration.

No `cmd.exe` was available in the build environment; only static checks can be done on the batch here.
