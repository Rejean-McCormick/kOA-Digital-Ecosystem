#!/usr/bin/env python3
"""Build a minimal, source-derived public architecture summary (never product state).

No local paths, credentials, snapshot filenames or tests/execution claims are exported.
Consumers may mirror this JSON after their own publication approval; generation alone
is not authorization to deploy a public site.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/target/public-architecture.v1.json'

def build(root: Path = ROOT) -> dict:
    source = root / 'docs/target/functional-chains'
    chain_files = sorted((source/'chains').glob('FC-*.md'))
    assert len(chain_files) == 24, 'Expected 24 chain documents'
    all_chains=[]
    for file in chain_files:
        raw=file.read_text(encoding='utf-8')
        head=re.search(r'^# (FC-\d\d) — (.+)$',raw,re.M)
        owner=re.search(r'^\*\*Owner\(s\):\*\* (.+)$',raw,re.M)
        outcome=re.search(r'^\*\*Expected result:\*\* (.+)$',raw,re.M)
        assert head and owner and outcome, f'Invalid chain: {file}'
        all_chains.append({'id':head.group(1),'title':head.group(2),
                           'owners':owner.group(1).rstrip('.'),
                           'outcome':outcome.group(1).rstrip('.'),
                           'source_path':file.relative_to(root).as_posix(),
                           'state':'target_design_not_qualified'})
    portfolio=json.loads((root/'docs/target/portfolio.v1.json').read_text(encoding='utf8'))
    owners=portfolio['repositories']
    edges=json.loads((root/'docs/target/boundaries.v1.json').read_text(encoding='utf8'))['links']
    assert len(edges)==26
    items=[{'repository':r['repository'],'family':r['family'],'role':r['target_role']} for r in owners]
    boundary_items=[{'id':b['id'],'journey':b['journey'],'producer':b['producer'],
                     'consumer':b['consumer'],'state':b['state']} for b in edges]
    digest=hashlib.sha256((''.join(f.read_text(encoding='utf8') for f in chain_files)).encode('utf8')).hexdigest()
    return {'format':'koa.public-architecture.v1','as_of':portfolio['as_of'],
            'classification':'PUBLIC_DESIGN_METADATA_ONLY',
            'status':'TARGET_DESIGN_NOT_DEPLOYMENT_EVIDENCE',
            'source':'kOA-Digital-Ecosystem/docs/target',
            'source_sha256':digest,
            'scope':{'chain_count':24,'repository_count':len(owners),'boundary_count':26},
            'chains':all_chains,'repositories':items,'boundaries':boundary_items}

def main() -> int:
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true')
    args=parser.parse_args(); expected=json.dumps(build(),ensure_ascii=False,indent=2)+'\n'
    if args.check:
        if not OUT.is_file() or OUT.read_text(encoding='utf8')!=expected:
            print('ERROR: public architecture export out of date');return 1
        print('PASS: public architecture export up to date');return 0
    OUT.write_text(expected,encoding='utf8');print('WROTE',OUT.relative_to(ROOT));return 0

if __name__=='__main__':raise SystemExit(main())
