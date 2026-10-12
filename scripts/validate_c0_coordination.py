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

    # Separate, non-normative v10 workstream registry. It may not override the
    # frozen v6 knowledge-projection contract set or fabricate release evidence.
    v10path=root/'docs/2-Technical-Reference/40-integration/kristal-v10-alignment/workstreams.json'
    try:
        v10=json.loads(v10path.read_text(encoding='utf-8'))
    except (OSError,ValueError) as exc:
        issues.append(f'v10 workstreams: {exc}')
        v10={}
    if v10.get('format')!='koa.c0-kristal-v10-alignment/0.1-candidate':
        issues.append('v10 workstreams: unexpected format')
    if v10.get('authority')!='coordination_only_non_normative':
        issues.append('v10 workstreams: incorrect authority')
    if v10.get('no_implicit_publication_authorization') is not True:
        issues.append('v10 workstreams: implicit publication is forbidden')
    framework=v10.get('framework_baseline') or {}
    if framework.get('version')!='10.0.0-draft.3.1' or framework.get('status')!='draft':
        issues.append('v10 workstreams: invalid Framework draft baseline')
    if framework.get('exact_commit')!='unverified' and not re.fullmatch('[a-f0-9]{40}',str(framework.get('exact_commit'))):
        issues.append('v10 workstreams: invalid pinned Framework SHA')
    if framework.get('contract_set_sha256')!='unverified' and not re.fullmatch('[a-f0-9]{64}',str(framework.get('contract_set_sha256'))):
        issues.append('v10 workstreams: invalid contract-set SHA256')
    entries=v10.get('entries') or []
    ids=[]
    for row in entries:
        rid=row.get('id')
        ids.append(rid)
        if not isinstance(rid,str) or not re.fullmatch(r'[A-Z][A-Z0-9]*-\d\d',rid):
            issues.append(f'v10 workstreams: invalid id {rid!r}')
        if row.get('priority') not in ('P0','P1','P2','P3'):
            issues.append(f'v10 workstreams: invalid priority {rid}')
        if row.get('evidence_status') not in ('proposed','coordination_documented','observed_snapshot','blocked'):
            issues.append(f'v10 workstreams: unsupported evidence status {rid}')
        if row.get('implementation_status') not in ('not_verified','blocked','verified_local','qualified_integrated'):
            issues.append(f'v10 workstreams: invalid implementation status {rid}')
        if row.get('implementation_status')=='qualified_integrated' and row.get('remote_commit')=='unverified':
            issues.append(f'v10 workstreams: unsupported qualified claim {rid}')
        if row.get('remote_commit')!='unverified' and not re.fullmatch('[a-f0-9]{40}',str(row.get('remote_commit'))):
            issues.append(f'v10 workstreams: invalid remote SHA {rid}')
        for fld in ('owner_repository','summary','acceptance_gate'):
            if not isinstance(row.get(fld),str) or not row[fld].strip():
                issues.append(f'v10 workstreams: missing {fld} in {rid}')
        if not isinstance(row.get('depends_on'),list):
            issues.append(f'v10 workstreams: non-list dependencies for {rid}')
    if len(ids)!=len(set(ids)) or len(ids)<20:
        issues.append('v10 workstreams: duplicate IDs or incomplete coverage')
    allids=set(ids)
    for row in entries:
        rid=row.get('id')
        for dep in row.get('depends_on',[]):
            if dep not in allids or dep==rid:
                issues.append(f'v10 workstreams: invalid dependency {rid} -> {dep}')
    # Reject recursive dependency cycles rather than accepting a plan that
    # no owner could execute.
    edges={r.get('id'):r.get('depends_on',[]) for r in entries}
    marked=set(); active=set()
    def visit(n):
        if n in active:
            issues.append(f'v10 workstreams: dependency cycle at {n}');return
        if n in marked:return
        active.add(n)
        for dep in edges.get(n,[]):
            if dep in edges:visit(dep)
        active.remove(n);marked.add(n)
    for rid in ids:
        if rid in edges:visit(rid)
    for required in ('C0-01','F-01','M-01','M-02','C3-01','C3-02','KNAV-01','KNAV-02','KNAV-03'):
        if required not in allids: issues.append(f'v10 workstreams: required gate missing {required}')
    return issues

if __name__=='__main__':
    errors=validate()
    for issue in errors:print('ERROR:',issue)
    if errors:sys.exit(1)
    print('PASS: C0 coordination metadata and historical v6 baseline checks (not an E2E qualification)')
