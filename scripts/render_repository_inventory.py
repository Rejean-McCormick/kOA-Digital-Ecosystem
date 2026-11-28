#!/usr/bin/env python3
"""Regenerate the canonical repository identity view (never live-Git evidence)."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/inventory/repositories.json'
OUTPUT = ROOT / 'docs/inventory/repositories.md'


def _offline_observation(row: dict) -> str:
    """Offline source observation is documentary metadata, not remote verification."""
    observed = row.get('latest_snapshot_observation')
    if not isinstance(observed, dict):
        return '—'
    if observed.get('status') != 'OBSERVED_SNAPSHOT':
        raise ValueError('Unexpected offline observation status')
    date = observed.get('date', '')
    ledger = observed.get('ledger', '')
    if (not isinstance(date, str) or not isinstance(ledger, str) or
            not ledger.startswith('docs/inventory/') or
            not ledger.endswith('.json') or
            '/' in ledger[len('docs/inventory/'):]):
        raise ValueError('Invalid offline observation reference')
    return f'{date} · [offline record]({ledger[len("docs/inventory/"):]})'


def render(root: Path = ROOT) -> str:
    inventory = json.loads((root/'docs/inventory/repositories.json').read_text(encoding='utf-8'))
    lines = [
        '# kOA repository identity inventory', '',
        '> **Generated file:** edit `repositories.json` and run `python scripts/render_repository_inventory.py`.',
        '> Snapshot-derived local roots and offline records do not verify Git remote, HEAD, public visibility, integration or deployment.', '',
        f'**Repositories in the declared C0 perimeter:** {len(inventory)}.',
        'Source-of-truth for this list: [`repositories.json`](repositories.json).',
        'Offline code snapshot digests: [`code-snapshots-53.v1.json`](code-snapshots-53.v1.json).',
        'Separate companion engineering repositories: [Doc Server, kOADiag and GitHub Audit](ECOSYSTEM_TOOLING.md). [Public audit dashboard](https://rejean-mccormick.github.io/kOA-Digital-Ecosystem-GitHub-Audit/).', '',
        '| Repository | Declared verification status | Reported local checkout root | Latest offline source evidence |',
        '|---|---|---|---|',
    ]
    for row in sorted(inventory, key=lambda x: x['github_repo'].lower()):
        repo = row['github_repo']
        slug = repo.split('/')[-1].replace('|', r'\|')
        rootpath = row['local_root'].replace('|', r'\|')
        lines.append(f'| [{slug}]({row["github_url"]}) | `{row["status"]}` | `{rootpath}` | {_offline_observation(row)} |')
    additional_path = root / 'docs/inventory/additional-repositories.v1.json'
    if additional_path.is_file():
        additional = json.loads(additional_path.read_text(encoding='utf-8'))['repositories']
        seen = {row['github_repo'].casefold() for row in inventory}
        lines += [
            '', '## Additional registered repositories and wiki checkouts', '',
            'These identities are recorded separately from the current 55-role target baseline; no GitSink enrollment or architectural admission follows.', '',
            'Source: [`additional-repositories.v1.json`](additional-repositories.v1.json).', '',
            '| Repository | Reported local checkout root | Wiki / reported local home | Verification |',
            '|---|---|---|---|',
        ]
        for row in sorted(additional, key=lambda x: x['github_repo'].lower()):
            key = row['github_repo'].casefold()
            if key in seen:
                raise ValueError('Duplicate repository identity across inventories: ' + row['github_repo'])
            seen.add(key)
            wiki = row.get('wiki')
            wiki_cell = f'[{row["github_repo"].split("/")[-1]}.wiki]({wiki["github_url"]}) · `{wiki["local_home"]}`' if wiki else '—'
            status = f'`{row["status"]}`' + (f'; wiki: `{wiki["status"]}`' if wiki else '')
            lines.append(f'| [{row["github_repo"].split("/")[-1]}]({row["github_url"]}) | `{row["local_root"]}` | {wiki_cell} | {status} |')
    lines += [
        '', '## Interpretation and authority', '',
        '- `source_root_observed_in_smartdump_remote_unverified`: local path recorded by a snapshot, not proof of current GitHub origin or permissions.',
        '- `local_git_marker_seen`: a Git marker was previously reported, not proof of current remote or revision.',
        '- `github_verified_local_origin_unverified`: GitHub identity checked separately from the reported checkout path.',
        '- `github_and_local_remote_verified`: historical investigation label; re-verify before any Git operation.',
        '- `OBSERVED_SNAPSHOT` is **separate from** the declared verification status; it records only supplied offline ZIP evidence.',
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
