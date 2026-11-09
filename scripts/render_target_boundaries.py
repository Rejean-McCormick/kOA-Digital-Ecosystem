#!/usr/bin/env python3
"""Render target-only boundaries without changing the published legacy graph registry."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'docs/target/BOUNDARIES.md'


def render(root: Path = ROOT) -> str:
    obj = json.loads((root / 'docs/target/boundaries.v1.json').read_text(encoding='utf-8'))
    links = obj['links']
    result = [
        '# Target owner-to-owner boundaries', '',
        '> Generated from [boundaries.v1.json](boundaries.v1.json). Edit the JSON and rerun `python scripts/render_target_boundaries.py`.',
        '> **These are intended design edges, not a qualified integration graph.** No edge grants code, release or publication authority.',
        '',
        f'**Target links:** {len(links)}. Only explicitly adopted exact interface names are recorded; `TBD` requires bilateral owner agreement.',
        '',
        '| Journey | Producer → consumer | Purpose | Interface | Implementation acceptance gate |',
        '|---|---|---|---|---|',
    ]
    for link in links:
        a = link['producer'].split('/')[-1]
        b = link['consumer'].split('/')[-1]
        def esc(v: str) -> str:
            return v.replace('|', r'\|').replace('\n',' ')
        result.append(f'| `{link["journey"]}` | **{a} → {b}** (`{link["id"]}`) | {esc(link["purpose"])} | `{link["interface"] or "TBD"}` | {esc(link["evidence_required"])} |')
    result += ['', '## Interpretation', '',
               'Every row is scoped to a possible journey and remains `target_design_not_qualified`. For civic links, the profile name is an observed adopted identifier; the row does not assert real deployment. The currently consumed [graph registry](../inventory/graph-registry.v1.json) stays separate until the downstream publisher and owners agree on a migration.', '',
               '[Architecture](architecture.md) · [Journeys](journeys.md) · [Code alignment plan](CODE_ALIGNMENT_INSTRUCTIONS.md)', '']
    return '\n'.join(result)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    expected = render()
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding='utf-8') != expected:
            print('ERROR: target boundaries Markdown is not synchronized')
            return 1
        print('PASS: target boundaries Markdown synchronized')
    else:
        OUTPUT.write_text(expected, encoding='utf-8')
        print('WROTE docs/target/BOUNDARIES.md')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
