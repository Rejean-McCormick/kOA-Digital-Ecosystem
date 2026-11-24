#!/usr/bin/env python3
"""Validate dated C0 offline evidence/triage metadata, without product qualification."""
from __future__ import annotations
import json
from pathlib import Path
import re
import sys
ROOT = Path(__file__).resolve().parents[1]
LEDGER = 'docs/inventory/code-snapshots-55-2026-11-23.v1.json'
AUDIT = 'docs/audit/2026-11-23-documentation-drift.v1.json'

def validate(root: Path = ROOT) -> list[str]:
    problems=[]
    try:
        inventory=json.loads((root/'docs/inventory/repositories.json').read_text('utf8'))
        ledger=json.loads((root/LEDGER).read_text('utf8'))
        audit=json.loads((root/AUDIT).read_text('utf8'))
    except (OSError,ValueError) as exc:
        return [f'Cannot read audit source: {exc}']
    canon={r['github_repo']:r['local_root'] for r in inventory}
    rows=ledger.get('repositories',[])
    names=[r.get('repository') for r in rows if isinstance(r,dict)]
    if (ledger.get('format')!='koa.code-snapshot-ledger/1.1' or
        ledger.get('as_of')!='2026-11-23' or ledger.get('source_archive')!='SmartDump_20261123_101022.zip' or
        ledger.get('snapshot_count')!=55 or len(rows)!=55 or len(names)!=len(set(names)) or
        set(names)!=set(canon)):
        problems.append('55-snapshot ledger scope/identity mismatch')
    for r in rows:
        if not isinstance(r,dict): problems.append('non-object ledger row');continue
        repo=r.get('repository')
        if repo not in canon: problems.append(f'{repo}: unknown inventory owner');continue
        if r.get('declared_source_root')!=canon[repo]: problems.append(f'{repo}: source_root mismatch')
        if not re.fullmatch(r'[a-f0-9]{64}',str(r.get('snapshot_sha256'))): problems.append(f'{repo}: bad snapshot hash')
        if not re.fullmatch(r'[a-f0-9]{64}',str(r.get('index_sha256'))): problems.append(f'{repo}: bad index hash')
        if r.get('evidence_level')!='OBSERVED_SNAPSHOT' or r.get('tests_executed')!='NOT_RUN' or r.get('doc_code_conformity')!='NOT_EVALUATED' or r.get('git_revision') is not None:
            problems.append(f'{repo}: unsupported qualification or commit claim')
        if not isinstance(r.get('reported_file_count'),int) or r['reported_file_count']<1:
            problems.append(f'{repo}: invalid file count')
        if not isinstance(r.get('captured_at_local'),str) or not r['captured_at_local'].startswith('2026-11-23T'):
            problems.append(f'{repo}: wrong capture date')
    if audit.get('format')!='koa.c0-documentation-drift-audit/1.0' or audit.get('as_of')!='2026-11-23':
        problems.append('audit format/date inconsistent')
    findings=audit.get('findings',[])
    ids=[r.get('id') for r in findings if isinstance(r,dict)]
    if len(findings)!=17 or len(set(ids))!=17 or sum(x.startswith('DOC-') for x in ids if isinstance(x,str))!=14:
        problems.append('audit issue totals wrong')
    if sum(x.startswith('VER-') for x in ids if isinstance(x,str))!=2 or 'REL-001' not in ids:
        problems.append('audit compatibility/release totals wrong')
    for row in findings:
        if not isinstance(row,dict): problems.append('non-object finding'); continue
        id=row.get('id')
        if row.get('owner_code_changed_by_c0') is not False or row.get('qualification_claim') is not False:
            problems.append(f'{id}: unauthorized modification or qualification claim')
        if id in ('DOC-002','DOC-009','VER-002') and (row.get('coordination_status')!='deferred_owner_updating' or row.get('proposed_owner_action') is not None):
            problems.append(f'{id}: diK must remain deferred')
        if id=='DOC-001' and row.get('coordination_status')!='snapshot_gap_remote_tree_present':
            problems.append('DOC-001: remote target coverage must not be mislabeled as current absence')
    return problems

if __name__=='__main__':
    errors=validate()
    if errors:
        for e in errors: print('FAIL:',e)
        sys.exit(1)
    print('PASS: 55-digest ledger and 17 dated findings remain descriptive and aligned')
