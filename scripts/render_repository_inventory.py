#!/usr/bin/env python3
"""Regenerate the canonical repository identity view (never live-Git evidence)."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/inventory/repositories.json'
OUTPUT = ROOT / 'docs/inventory/repositories.md'


def render(root: Path = ROOT) -> str:
    inventory = json.loads((root/'docs/inventory/repositories.json').read_text(encoding='utf-8'))
    lines = [
        '# kOA repository identity inventory', '',
        '> **Generated file:** edit `repositories.json` and run `python scripts/render_repository_inventory.py`.',
        '> Snapshot-derived local roots do not verify Git remote, HEAD, public visibility, integration or deployment.', '',
        f'**Repositories in the declared C0 perimeter:** {len(inventory)}.',
        'Source-of-truth for this list: [`repositories.json`](repositories.json).',
        'Offline code snapshot digests: [`code-snapshots-53.v1.json`](code-snapshots-53.v1.json).', '',
        '| Repository | Declared verification status | Reported local checkout root |',
        '|---|---|---|',
    ]
    for row in sorted(inventory, key=lambda x: x['github_repo'].lower()):
        repo = row['github_repo']
        slug = repo.split('/')[-1].replace('|', r'\|')
        rootpath = row['local_root'].replace('|', r'\|')
        lines.append(f'| [{slug}]({row["github_url"]}) | `{row["status"]}` | `{rootpath}` |')
    lines += [
        '', '## Interpretation and authority', '',
        '- `source_root_observed_in_smartdump_remote_unverified`: local path recorded by a snapshot, not proof of current GitHub origin or permissions.',
        '- `local_git_marker_seen`: a Git marker was previously reported, not proof of current remote or revision.',
        '- `github_and_local_remote_verified`: historical investigation label; re-verify before any Git operation.',
        '- Repository inclusion defines C0 architectural scope only. Product implementations, contracts and releases belong to their owners.',
        '- No push, publication, privilege, runtime activation or public-content release follows from this inventory.', '',
        'For roles and functional boundaries, start with the [target portfolio](../target/PORTFOLIO.md) and [architecture](../target/architecture.md).', '',
    ]
    return '\n'.join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    content = render()
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding='utf-8') != content:
            print('ERROR: repository inventory markdown is stale')
            return 1
        print('PASS: repository inventory rendering is synchronized')
        return 0
    OUTPUT.write_text(content, encoding='utf-8')
    print(f'WROTE {OUTPUT.relative_to(ROOT)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
