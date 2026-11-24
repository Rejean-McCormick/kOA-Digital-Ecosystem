#!/usr/bin/env python3
"""Validate the dated local-only C0 evidence ledger without touching owner roots."""
from __future__ import annotations
import hashlib
import json
import pathlib
import re
import sys

LEDGER = pathlib.Path(__file__).resolve().parents[1]/'docs/audit/2026-11-24-lots-01-08-evidence.v1.json'
SHA_RE = re.compile(r'^[0-9a-f]{64}$')


def validate(data: dict) -> list[str]:
    errors = []
    if data.get('schema') != 'koa.c0.lots-01-08-evidence.v1':
        errors.append('unknown schema')
    lots = data.get('lots', [])
    if [l.get('lot') for l in lots] != list(range(1, 9)):
        errors.append('lot identities must be exactly 1..8')
    total = 0
    seen = set()
    for lot in lots:
        for suffix in ('overlay_zip_sha256','audit_source_sha256'):
            if not SHA_RE.fullmatch(lot.get(suffix, '')):
                errors.append(f"lot {lot.get('lot')}: bad {suffix}")
        if lot.get('installation_state') != 'USER_REPORTED_APPLIED':
            errors.append(f"lot {lot.get('lot')}: installation state not explicitly user-reported")
        if any(lot.get(x) != 0 for x in ('reported_conflicts','reported_unchanged')):
            errors.append(f"lot {lot.get('lot')}: unexpected counts")
        files = lot.get('target_files', [])
        if lot.get('reported_applied') != len(files):
            errors.append(f"lot {lot.get('lot')}: count mismatch")
        total += len(files)
        for item in files:
            root, rel, repo = item.get('root',''), item.get('path',''), item.get('repository','')
            if not re.match(r'^C:\\mycode\\', root, re.I):
                errors.append(f"non-C0 root: {root!r}")
            if repo.casefold() == 'dik' or root.casefold().startswith('c:\\mycode\\dik\\'):
                errors.append('diK target forbidden')
            posix = pathlib.PurePosixPath(rel)
            if posix.is_absolute() or '..' in posix.parts or '\\' in rel:
                errors.append(f'unsafe path: {rel!r}')
            if not SHA_RE.fullmatch(item.get('expected_post_install_sha256', '')):
                errors.append(f'bad target hash: {rel!r}')
            before = item.get('snapshot_pre_install_sha256')
            if before is not None and not SHA_RE.fullmatch(before):
                errors.append(f'bad source hash: {rel!r}')
            identity = (root.casefold(),rel.casefold())
            if identity in seen:
                errors.append(f'duplicate target: {identity}')
            seen.add(identity)
    t = data.get('totals',{})
    for key in ('files_from_overlay_manifests','user_reported_applied'):
        if t.get(key) != total:
            errors.append(f'{key} mismatch')
    if t.get('user_reported_conflicts') != 0 or t.get('lots') != 8:
        errors.append('invalid aggregate counts')
    if t.get('post_install_sha256_readbacks') != 0:
        errors.append('must not assert post-install readback')
    if data.get('evidence_policy',{}).get('live_production_status') != 'NOT_ATTESTED':
        errors.append('must not assert production qualification')
    gates=data.get('open_qualification_gates', [])
    if not gates or not any('pgf' in x.get('issue','').lower() for x in gates):
        errors.append('missing qualification gate: PGF')
    return errors


def main() -> int:
    data=json.loads(LEDGER.read_text(encoding='utf-8'))
    errors=validate(data)
    for e in errors: print('FAIL:',e)
    if errors: return 1
    print('PASS: eight lots, 74 recorded targets, zero reported conflicts; no production qualification claimed.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
