#!/usr/bin/env python3
"""Generate or verify a human-readable final-system portfolio from structured C0 data."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/target/portfolio.v1.json'
OUTPUT = ROOT / 'docs/target/PORTFOLIO.md'


def render(root: Path = ROOT) -> str:
    target = json.loads((root / 'docs/target/portfolio.v1.json').read_text(encoding='utf-8'))
    rows = target['repositories']
    lines = [
        f'# Final-system portfolio — {len(rows)} registered repositories',
        '',
        '> **Generated file** — edit `portfolio.v1.json` and run `python scripts/render_target_portfolio.py`.',
        '> This is **TARGET_DESIGN**, not proof of production, contract adoption, GitHub HEAD or authorization.',
        '> Roles are C0 descriptions inferred from each available owner snapshot; primary authority stays in that owner repository.',
        '',
        f'**Registered repositories:** {len(rows)}. Owner-source files in supplied snapshots: {sum(r["evidence"] == "owner_snapshot" for r in rows)}. Sources unavailable: {sum(r["evidence"] == "source_absent" for r in rows)}.',
        '',
        '| Repository | Target function / responsibility | Family | Documentation basis |',
        '|---|---|---|---|',
    ]
    for row in sorted(rows, key=lambda item: item['repository'].lower()):
        name = row['repository']
        slug = name.split('/')[-1]
        role = row['target_role'].replace('|', r'\|').replace('\n', ' ')
        basis = 'Owner archive snapshot' if row['evidence'] == 'owner_snapshot' else '**No owner source in supplied archive**'
        lines.append(f'| [{slug}](https://github.com/{name}) | {role} | `{row["family"]}` | {basis} |')
    lines += [
        '',
        '## Source traceability',
        '',
        'The machine-readable [portfolio registry](portfolio.v1.json) records the exact archive member and SHA-256 digest for every owner-source-backed row. For missing source archives, no role was presented as owner-confirmed. This C0 portfolio is not an admission of discovered neighboring projects; see [the canonical inventory](../inventory/README.md).',
        '',
        '## Next reading',
        '',
        '[Final-system architecture](architecture.md) · [Cross-system journeys](journeys.md) · [Code alignment instructions](CODE_ALIGNMENT_INSTRUCTIONS.md)',
        '',
    ]
    return '\n'.join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='fail if generated Markdown is out of date')
    args = parser.parse_args()
    expected = render()
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding='utf-8') != expected:
            print('ERROR: docs/target/PORTFOLIO.md out of sync; run scripts/render_target_portfolio.py')
            return 1
        print('PASS: rendered final-system portfolio matches structured source')
    else:
        OUTPUT.write_text(expected, encoding='utf-8')
        print(f'WROTE {OUTPUT.relative_to(ROOT)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
