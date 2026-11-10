#!/usr/bin/env python3
"""Safely promote four snapshot-only GitSink inventory entries after LOCAL Git checks.

Read-only by default. --apply updates only the canonical inventory and its
rendered Markdown, never Git remotes, commits, branches, or pushes.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / 'docs/inventory/repositories.json'
SNAPSHOT_ONLY = 'source_root_observed_in_smartdump_remote_unverified'
LOCAL_VERIFIED = 'local_git_marker_seen'
TARGETS = {
    'Rejean-McCormick/diK': r'C:\mycode\diK\diK',
    'Rejean-McCormick/Karacter': r'C:\mycode\Ekole\Karacter',
    'Rejean-McCormick/Kolor': r'C:\mycode\Ekole\Kolor',
    'Rejean-McCormick/Kristalizer': r'C:\mycode\Kristal\Kristalizer',
}


def github_identity(raw: str) -> str:
    """Extract an exact owner/repository, never a redirect or URL with credentials."""
    if not raw or raw != raw.strip() or any(c in raw for c in '\r\n\0'):
        return ''
    if raw.startswith('git@github.com:'):
        slug = raw[len('git@github.com:'):]
    elif raw.startswith('ssh://git@github.com/'):
        slug = raw[len('ssh://git@github.com/'):]
    elif raw.startswith('git://github.com/'):
        slug = raw[len('git://github.com/'):]
    elif raw.startswith(('https://', 'http://')):
        parsed = urlsplit(raw)
        try:
            valid_host = ((parsed.hostname or '').casefold() == 'github.com'
                          and not parsed.username and not parsed.password
                          and parsed.port is None and not parsed.query and not parsed.fragment)
        except ValueError:
            return ''
        if not valid_host:
            return ''
        slug = parsed.path.lstrip('/')
    else:
        return ''
    slug = slug.rstrip('/')
    if slug.lower().endswith('.git'):
        slug = slug[:-4]
    parts = slug.split('/')
    if len(parts) != 2 or not all(re.fullmatch(r'[A-Za-z0-9_.-]+', x) for x in parts):
        return ''
    return '/'.join(parts)


def git(repo: Path, *args: str) -> list[str] | None:
    env = dict(os.environ, GIT_OPTIONAL_LOCKS='0', GIT_TERMINAL_PROMPT='0')
    try:
        result = subprocess.run(
            ['git', *args], cwd=repo, env=env, text=True, errors='replace',
            capture_output=True, timeout=20, check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip().splitlines()


def same_path(left: Path | str, right: Path | str) -> bool:
    return os.path.normcase(os.path.realpath(os.fspath(left))) == os.path.normcase(os.path.realpath(os.fspath(right)))


def verify_checkout(repo: str, local_root: str) -> str:
    """Return a concise failure reason or empty string after direct local checks."""
    checkout = Path(local_root)
    if not checkout.is_absolute() or not checkout.is_dir():
        return 'local checkout missing or not absolute'
    if checkout.is_symlink() or (hasattr(checkout, 'is_junction') and checkout.is_junction()):
        return 'checkout is an alias/symlink/junction'
    if not ((checkout / '.git').is_dir() or (checkout / '.git').is_file()):
        return 'no .git marker at declared checkout'
    top = git(checkout, 'rev-parse', '--show-toplevel')
    if not top or len(top) != 1 or not same_path(top[0], checkout):
        return 'checkout is not the exact Git worktree root'
    raw = git(checkout, 'config', '--local', '--get-all', 'remote.origin.url')
    effective = git(checkout, 'remote', 'get-url', '--all', 'origin')
    raw_push = git(checkout, 'config', '--local', '--get-all', 'remote.origin.pushurl')
    effective_push = git(checkout, 'remote', 'get-url', '--push', '--all', 'origin')
    if not raw or len(raw) != 1 or not effective or len(effective) != 1:
        return 'origin missing or multiple origin URLs'
    if not effective_push or len(effective_push) != 1:
        return 'push URL missing or multiple push URLs'
    if raw_push and len(raw_push) != 1:
        return 'multiple explicit push URLs'
    urls = raw + effective + effective_push + (raw_push or [])
    if any(github_identity(url).casefold() != repo.casefold() for url in urls):
        return 'origin/push URL does not match exact declared GitHub repository'
    return ''


def promotion_plan(inventory: list[dict], *, targets: dict[str, str] | None = None) -> tuple[dict[str, str], list[dict]]:
    """All-or-nothing plan; preserve exactly 53 entries and unrelated metadata."""
    targets = TARGETS if targets is None else targets
    if len(inventory) != 53:
        raise ValueError('expected exactly 53 inventory entries')
    keys = [row.get('github_repo') for row in inventory]
    if len(set(keys)) != len(keys):
        raise ValueError('duplicate repository identities')
    by_repo = {row['github_repo']: row for row in inventory}
    results: dict[str, str] = {}
    revised = [dict(row) for row in inventory]
    out = {row['github_repo']: row for row in revised}
    for repo, expected_root in targets.items():
        row = by_repo.get(repo)
        if not row:
            results[repo] = 'BLOCKED: repository not in inventory'
            continue
        if row.get('scope') != 'PUBLIC' or row.get('local_root') != expected_root:
            results[repo] = 'BLOCKED: inventory scope/root differs from canonical declaration'
            continue
        if row.get('github_url') != 'https://github.com/' + repo:
            results[repo] = 'BLOCKED: inventory GitHub URL mismatch'
            continue
        if row.get('status') not in (SNAPSHOT_ONLY, LOCAL_VERIFIED):
            results[repo] = 'BLOCKED: unexpected inventory status'
            continue
        problem = verify_checkout(repo, expected_root)
        if problem:
            results[repo] = 'BLOCKED: ' + problem
        elif row['status'] == LOCAL_VERIFIED:
            results[repo] = 'VERIFIED: already promoted'
        else:
            out[repo]['status'] = LOCAL_VERIFIED
            results[repo] = 'VERIFIED: ready for local inventory promotion'
    return results, revised


def atomic_write(path: Path, value: str) -> None:
    handle, name = tempfile.mkstemp(prefix='.gitsink-inventory-', suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(handle, 'w', encoding='utf-8', newline='\n') as stream:
            stream.write(value)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='update local inventory after ALL four checkouts pass')
    args = parser.parse_args(argv)
    inventory = json.loads(INVENTORY.read_text(encoding='utf-8'))
    results, updated = promotion_plan(inventory)
    for repo, status in results.items():
        print(f'{repo}: {status}')
    if len(results) != len(TARGETS) or any(x.startswith('BLOCKED') for x in results.values()):
        print('No changes: all four local checkouts must pass. Never change remotes automatically.')
        return 1
    changed = updated != inventory
    if not args.apply:
        print('Audit only. Use --apply for local inventory promotion (no commit or push).')
        return 0
    if not changed:
        print('Inventory already promoted; nothing to write.')
        return 0
    atomic_write(INVENTORY, json.dumps(updated, ensure_ascii=False, indent=2) + '\n')
    from render_repository_inventory import render
    atomic_write(ROOT / 'docs/inventory/repositories.md', render(ROOT))
    print('Updated repositories.json and repositories.md. Review Git diff; GitSink requires a new simulation and manual selection.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
