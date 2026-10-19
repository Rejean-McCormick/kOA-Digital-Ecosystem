#!/usr/bin/env python3
"""Validate a non-normative C0 tandem deployment decision, never runtime admission."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PROFILE = Path('docs/2-Technical-Reference/40-integration/tandem-vps-capsule-agent')
GATES = {f'G{i}' for i in range(9)}
STATES = {'IN_PROGRESS','BLOCKED','NOT_QUALIFIED','LOCAL_E2E_ONLY'}
WORK_STATES = {'DOCUMENTED_PROFILE','NOT_INTEGRATED','NOT_QUALIFIED','LOCAL_E2E_ONLY','NOT_IMPLEMENTED_OR_NOT_DEMONSTRATED','BLOCKED'}
OBS_STATES = {'USER_REPORTED_LOCAL_E2E_VERIFIED','USER_REPORTED_LOCAL_TESTED'}


def validate(root=ROOT):
    issues=[]
    path=root/PROFILE/'deployment-profile.json'
    try: obj=json.loads(path.read_text(encoding='utf-8'))
    except (ValueError, OSError) as exc: return [f'profile is not readable JSON: {exc}']
    if obj.get('format') != 'koa.c0-tandem-deployment-profile/0.1-candidate': issues.append('invalid format')
    if obj.get('authority') != 'coordination_only_non_normative': issues.append('C0 is not deployment authority')
    decision=obj.get('decision') or {}
    if decision.get('id')!='TANDEM-D01' or decision.get('status')!='USER_DECIDED' or decision.get('value')!='vps-linux-docker-capsule-agent' or decision.get('scope')!='first_priority_target_only' or decision.get('not_a_production_approval') is not True:
        issues.append('unapproved or broadened deployment-profile decision')
    target=obj.get('target') or {}
    for field,expected in [('platform','linux-vps'),('container_runtime','docker'),('deployment_executor','Konnaxion_Capsule_Manager/kx_agent'),('identity_mode','standalone_first_optional_common_oidc'),('world_scoping','strict_world_and_release')]:
        if target.get(field)!=expected: issues.append(f'wrong target {field}')
    if target.get('application_components')!=['Konnaxion','Orgo']: issues.append('unexpected components')
    if 'kOA-Linux' not in target.get('optional_platform',[]): issues.append('platform alternative lost')
    for field in ('public_exposure','vps_vendor','hostname','oidc_provider'):
        if target.get(field)!='NOT_DECIDED':issues.append(f'{field}: unapproved configuration claim')
    safety=obj.get('safety') or {}
    for field in ('allow_runtime_activation','allow_publication','allow_automatic_schema_migration','allow_cross_tenant_writes','allow_security_gate_bypass'):
        if safety.get(field) is not False: issues.append(f'forbidden authorization: {field}')
    for field in ('no_private_keys_in_repository','product_sessions_and_authorizations_remain_local','composite_rollback_is_not_cross_database_atomic'):
        if safety.get(field) is not True: issues.append(f'weakened invariant: {field}')
    observations=obj.get('observations') or []
    if set(x.get('id') for x in observations)!= {'IK-FAKEPLANT-20261018','LOT1A-20261018','LOT1B-20261018'}:
        issues.append('missing/duplicate or invented baseline observations')
    for row in observations:
        if row.get('status') not in OBS_STATES or row.get('not_production') is not True:
            issues.append(f'overstated local observation: {row.get("id")}')
        for fld in ('owner','scope','evidence'):
            if not isinstance(row.get(fld),str) or not row[fld].strip(): issues.append(f'missing observation field {fld}')
    owners=obj.get('owner_workstreams') or []
    ids=[x.get('id') for x in owners]
    expected={'TANDEM-W0','TANDEM-W1C','TANDEM-W2','TANDEM-W3','TANDEM-W4','TANDEM-W5','TANDEM-W6'}
    if set(ids)!=expected or len(ids)!=len(expected):issues.append('missing or duplicate workstreams')
    edges={}
    for row in owners:
        rid=row.get('id')
        if row.get('status') not in WORK_STATES:issues.append(f'unapproved workstream success: {rid}')
        for fld in ('owner_repository','summary','acceptance'):
            if not isinstance(row.get(fld),str) or not row[fld].strip():issues.append(f'missing workstream {fld}: {rid}')
        deps=row.get('depends_on')
        if not isinstance(deps,list):issues.append(f'dependency list missing: {rid}'); deps=[]
        edges[rid]=deps
        for dep in deps:
            if dep not in expected or dep==rid: issues.append(f'invalid dependency {rid} -> {dep}')
    seen=set();active=set()
    def visit(n):
        if n in active:issues.append(f'cyclic workstreams: {n}');return
        if n in seen:return
        active.add(n)
        for dep in edges.get(n,[]):
            if dep in edges:visit(dep)
        active.remove(n); seen.add(n)
    for rid in edges:visit(rid)
    gates=obj.get('release_gates') or []
    gateids=[x.get('id') for x in gates]
    if set(gateids)!=GATES or len(gateids)!=len(GATES):issues.append('release gate G0-G8 coverage invalid')
    for row in gates:
        if row.get('state') not in STATES:issues.append(f'unsupported/overstated gate {row.get("id")}')
        if not isinstance(row.get('source'),str) or len(row['source'])<12:issues.append(f'gate evidence note missing: {row.get("id")}')
    if next((x.get('state') for x in gates if x.get('id')=='G8'),None)!='BLOCKED':
        issues.append('G8 must remain blocked without operational approval')
    pins=obj.get('pins') or {}
    required=('konnaxion_commit','orgo_commit','capsule_manager_commit','konnaxiondiag_commit','interaction_kernel_contract_set_digest','release_set_digest','image_digests','migration_heads')
    for fld in required:
        val=pins.get(fld)
        if val != 'UNVERIFIED' and not (isinstance(val,str) and re.fullmatch(r'[0-9a-f]{40}|sha256:[0-9a-f]{64}',val)):
            issues.append(f'invalid pin: {fld}')
    for path in ['README.md','docs/index.md','docs/status/current.md','docs/2-Technical-Reference/10-system/authority-map.md','docs/2-Technical-Reference/50-operations/releases.md']:
        f=root/path
        if not f.is_file() or 'tandem-vps-capsule-agent' not in f.read_text(encoding='utf-8'):
            issues.append(f'missing C0 profile navigation in {path}')
    for name in ['README.md','acceptance.md','evidence-ledger.md','decision-log.md']:
        if not (root/PROFILE/name).is_file():issues.append(f'missing profile document: {name}')
    return issues


if __name__=='__main__':
    issues=validate()
    for issue in issues:print('ERROR:',issue)
    if issues:sys.exit(1)
    print('PASS: user-selected VPS profile metadata; no signed release or VPS admission implied')
