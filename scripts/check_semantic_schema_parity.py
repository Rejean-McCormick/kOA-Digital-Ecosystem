#!/usr/bin/env python3
"""Read-only cross-check of the 11 Framework v11 schemas vendored by diK.

This does not select a Kristal revision, assess Wikidata truth, or approve a
release. A mismatch is a review gate, not a reason to rewrite either owner.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def roots_from_manifest(root: Path = ROOT) -> dict[str, Path]:
    manifest = json.loads((root / 'docs/inventory/semantic-stack-local-roots.v1.json').read_text(encoding='utf-8'))
    if manifest.get('schema') != 'koa.semantic_stack.local_roots.v1':
        raise ValueError('Unrecognized semantic-stack root manifest')
    return {item['name']: Path(item['local_root']) for item in manifest['entries']}


def verify(roots: dict[str, Path]) -> dict:
    framework = roots['Kristal-Framework'] / 'schemas/v11'
    vendored = roots['diK'] / 'src/dik/_framework/schemas/v11'
    results = []
    if not framework.is_dir() or not vendored.is_dir():
        return {'profile': 'koa.semantic-schema-parity/0.1', 'status': 'BLOCKED_MISSING_SCHEMA_DIRECTORY',
                'schemas_checked': 0, 'results': []}
    left = {p.name for p in framework.glob('*.schema.json') if p.is_file()}
    right = {p.name for p in vendored.glob('*.schema.json') if p.is_file()}
    for filename in sorted(left | right):
        a, b = framework / filename, vendored / filename
        if a.is_symlink() or b.is_symlink() or not a.is_file() or not b.is_file():
            results.append({'schema': filename, 'status': 'BLOCKED_MISSING_OR_SYMLINKED'})
            continue
        sha_a = hashlib.sha256(a.read_bytes()).hexdigest()
        sha_b = hashlib.sha256(b.read_bytes()).hexdigest()
        results.append({'schema': filename, 'status': 'MATCH' if sha_a == sha_b else 'DRIFT',
                        'framework_sha256': sha_a, 'dik_sha256': sha_b})
    return {'profile': 'koa.semantic-schema-parity/0.1',
            'status': 'MATCH' if len(results) == 11 and all(r['status'] == 'MATCH' for r in results)
                      else 'BLOCKED_SCHEMA_DRIFT',
            'schemas_checked': len(results), 'results': results,
            'interpretation': 'integrity only; not cross-repository qualification or canonical authority'}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--framework-root', type=Path, help='Explicit local Framework checkout')
    parser.add_argument('--dik-root', type=Path, help='Explicit local diK checkout')
    args = parser.parse_args()
    roots = roots_from_manifest()
    if args.framework_root:
        roots['Kristal-Framework'] = args.framework_root
    if args.dik_root:
        roots['diK'] = args.dik_root
    outcome = verify(roots)
    print(json.dumps(outcome, indent=2, sort_keys=True))
    return 0 if outcome['status'] == 'MATCH' else 2


if __name__ == '__main__':
    raise SystemExit(main())
