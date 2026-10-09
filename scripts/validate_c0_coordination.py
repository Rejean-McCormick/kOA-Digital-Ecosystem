#!/usr/bin/env python3
"""Validate C0 coordination metadata only (never semantic or release qualification)."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'docs/2-Technical-Reference/40-integration/orchestration-c0'
STATUS = {
    'frozen_documented', 'producer_implemented_consumer_unverified',
    'profile_documented', 'local_tests_passed', 'owner_contract_and_example',
    'schema_exists_index_absent', 'demo_only_manual_workflow',
    'adapter_documented', 'four_local_tests_on_previous_target'
}

def validate(root=ROOT):
    base = root / 'docs/2-Technical-Reference/40-integration/orchestration-c0'
    issues=[]
    def load(filename,expect):
        p=base/filename
        try: obj=json.loads(p.read_text(encoding='utf-8'))
        except (OSError,ValueError) as exc:
            issues.append(f'{filename}: {exc}'); return {'entries':[]}
        if obj.get('format')!=expect: issues.append(f'{filename}: unexpected format')
        return obj
    registry=load('interfaces.json','koa.c0-interface-registry/0.1-candidate')
    versions=load('versions.json','koa.c0-version-matrix/0.1-candidate')
    ids=set()
    for x in registry.get('entries',[]):
        id=x.get('id');
        if not isinstance(id,str) or not re.fullmatch(r'I\d\d',id) or id in ids: issues.append(f'invalid or duplicate ID: {id!r}')
        ids.add(id)
        for field in ('lane','producer','consumer','contract','qualification','owner_chantier','open_gate','last_reviewed'):
            if not isinstance(x.get(field),str) or not x[field]:issues.append(f'{id}: missing {field}')
        if x.get('evidence_status') not in STATUS: issues.append(f'{id}: unexpected evidence status')
        if not isinstance(x.get('evidence'),list) or not x['evidence']:issues.append(f'{id}: missing evidence pointers')
        if x.get('tested_commit')!='not_pinned_in_snapshot' and not re.fullmatch(r'[a-f0-9]{40}',x['tested_commit']):issues.append(f'{id}: unpinned/malformed tested commit')
    if len(ids)!=10: issues.append('registry must contain the 10 tracked interfaces')
    if len(versions.get('entries',[]))<12: issues.append('version matrix missing expected owners')
    for x in versions.get('entries',[]):
        for f in ('component','observed_version','source_archive','evidence_path','gap','workstream'):
            if not x.get(f):issues.append('version row missing '+f)
    hist=root/'docs/2-Technical-Reference/40-integration/knowledge-projection-contract-set.json'
    try:
        pinned=json.loads(hist.read_text(encoding='utf-8'))
        if pinned['encyklopedia']['handoff']!='encyklopedia.corpus-harvest-handoff/1.0.0':
            issues.append('frozen v6 handoff has been silently changed')
        if pinned['kristal']['standard']!='6.0.0':issues.append('frozen v6 standard has been silently changed')
    except Exception as exc:issues.append('could not verify frozen contract-set: '+str(exc))
    for rel in ['README.md','docs/2-Technical-Reference/40-integration/contract-map.md','docs/status/current.md']:
        p=root/rel
        if not p.is_file() or 'orchestration-c0' not in p.read_text(encoding='utf-8'): issues.append('missing navigation link: '+rel)
    return issues

if __name__=='__main__':
    errors=validate()
    for issue in errors:print('ERROR:',issue)
    if errors:sys.exit(1)
    print('PASS: C0 coordination metadata and historical v6 baseline checks (not an E2E qualification)')
