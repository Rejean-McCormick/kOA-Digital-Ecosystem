#!/usr/bin/env python3
"""Render and check the *reported* semantic-stack Windows root map."""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PureWindowsPath

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/inventory/semantic-stack-local-roots.v1.json'
OUTPUT = ROOT / 'docs/inventory/SEMANTIC_STACK_LOCAL_ROOTS.md'
EVIDENCE = {
    'USER_REPORTED_DIRECTORY_SCAN': 'User-provided directory scan',
    'SUPPLIED_SNAPSHOT_INDEX': 'Supplied code snapshot index (`source_root`)',
    'USER_REPORTED_GIT_MARKER': 'User-reported `.git` directory',
}


def validate(root: Path = ROOT) -> list[dict]:
    data = json.loads((root / 'docs/inventory/semantic-stack-local-roots.v1.json').read_text(encoding='utf-8'))
    if data['schema'] != 'koa.semantic_stack.local_roots.v1':
        raise ValueError('Unexpected local root map schema')
    if data['authority'] != 'coordination_only_non_normative':
        raise ValueError('A local path map cannot grant canonical authority')
    entries = data['entries']
    if len(entries) != 14 or len({r['name'] for r in entries}) != 14:
        raise ValueError('Exactly 14 distinct workstream components are required')
    canonical = {
        r['github_repo']: r
        for r in json.loads((root / 'docs/inventory/repositories.json').read_text(encoding='utf-8'))
    }
    for row in entries:
        path = row['local_root']
        if not (isinstance(path, str) and path.startswith('C:\\mycode\\')
                and '..' not in PureWindowsPath(path).parts
                and PureWindowsPath(path).name != '.git'):
            raise ValueError(f'Unsafe or invalid checkout root: {row["name"]}')
        if row['evidence'] not in EVIDENCE:
            raise ValueError(f'Unknown evidence class: {row["name"]}')
        if row['name'] == 'GF_Wordbench':
            if (row['github_repo'] is not None or
                    path != r'C:\mycode\Grammatical-Framework\GF_Wordbench' or
                    row['evidence'] != 'USER_REPORTED_GIT_MARKER'):
                raise ValueError('GF_Wordbench is a separately reported local checkout')
        else:
            repo = row['github_repo']
            if repo not in canonical or canonical[repo]['local_root'] != path:
                raise ValueError(f'Path conflicts with canonical C0 inventory: {row["name"]}')
            if row['name'] == 'diK' and (
                    path != r'C:\mycode\diK\diK' or
                    row['evidence'] != 'SUPPLIED_SNAPSHOT_INDEX'):
                raise ValueError('diK source_root was documented in the supplied index')
            if row['name'] == 'SemantiK-Architect' and (
                    path != r'C:\mycode\SemantiK_Architect\SemantiK_Architect' or
                    row['evidence'] != 'SUPPLIED_SNAPSHOT_INDEX'):
                raise ValueError('SemantiK-Architect source_root was documented in the supplied index')
    return entries


def render(root: Path = ROOT) -> str:
    entries = validate(root)
    lines = [
        '# Semantic-stack local checkout roots (24 November 2026)',
        '',
        '> **Generated file:** edit `semantic-stack-local-roots.v1.json` and run '
        '`python scripts/render_semantic_stack_local_roots.py`.',
        '> Reported Windows paths are offline coordination evidence, not live Git, HEAD, '
        'origin, qualification, or publication authorization.',
        '',
        'This operational list identifies the 14 repositories or local worktrees selected '
        'for the diK/EncyK/Kristal semantic-alignment overlay. Thirteen entries mirror '
        '[the existing 55-repository C0 identity inventory](repositories.md); '
        '`GF_Wordbench` is tracked **only in this workstream list**, without an '
        'unverified GitHub identity or a change in the C0 perimeter.',
        '',
        '| Component | Reported Windows checkout root | Evidence |',
        '|---|---|---|',
    ]
    for row in entries:
        lines.append(
            f'| `{row["name"]}` | `{row["local_root"]}` | {EVIDENCE[row["evidence"]]} |'
        )
    lines.extend([
        '',
        '## Interpretation',
        '',
        '- `diK` and `SemantiK-Architect` roots were confirmed in the supplied '
        '24 November code snapshot indexes. The project name `SemantiK-Architect` '
        'uses a hyphen in the GitHub identity, while the local folder uses underscores.',
        '- The operator reported moving `GF_Wordbench` up one directory: the Git '
        'metadata is now at `C:\\mycode\\Grammatical-Framework\\GF_Wordbench\\.git`. '
        'The checkout root excludes `.git`.',
        '- The other roots were reported in the operator\'s recursive directory scan. '
        'Duplicate names inside `DocServer`, backups, vendor copies, `src/` and '
        'archives are **not** selected checkout roots.',
        '- The historical snapshot indexes and prior audit records remain unchanged; '
        'moving a checkout does not retroactively change archival evidence.',
        '- This list does not approve an overlay, canonical Kristal writes, Wikidata '
        'crosswalk promotion, GitSink enrollment, or public deployment.',
        '',
        '## Read-only Windows verification',
        '',
        'Run from the C0 checkout root:',
        '',
        '```powershell',
        'pwsh -NoProfile -File .\\scripts\\check_semantic_stack_local_roots.ps1 | Format-Table -AutoSize',
        '```',
        '',
        'Use `-RequireAll` to fail if any checkout is missing or the discovered Git root '
        'does not exactly match the reported path. This check never modifies repositories.',
        '',
    ])
    return '\n'.join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    expected = render()
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding='utf-8') != expected:
            print('ERROR: semantic-stack local roots markdown is stale')
            return 1
        print('PASS: semantic-stack local roots are synchronized with the canonical identity inventory')
        return 0
    OUTPUT.write_text(expected, encoding='utf-8')
    print(f'WROTE {OUTPUT.relative_to(ROOT)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
