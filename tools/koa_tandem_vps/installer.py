"""Safe C0 VPS decision documentation overlay; no remote or database side effects."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from zipfile import ZipFile

REPO = Path(__file__).resolve().parents[2]
MANIFEST = Path(__file__).with_name('manifest.json')
PAYLOAD = Path(__file__).with_name('payload.zip')
BACKUPS = REPO.parent / 'Tandem_Local' / 'koa_vps_profile' / 'backups'
IGNORE = shutil.ignore_patterns('.git', '.venv', '__pycache__', '.pytest_cache', 'node_modules', '*.pyc')


def checksum(path):
    if not path.is_file() or path.is_symlink():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_path(relative):
    x = Path(relative)
    if (x.is_absolute() or '\\' in relative or x.as_posix() != relative
            or '..' in x.parts or not x.parts or any(s.startswith('.') and s not in ('.github', '.gitignore') for s in x.parts)):
        raise RuntimeError(f'Unsafe payload path: {relative}')
    parent=REPO
    for piece in x.parts[:-1]:
        parent=parent/piece
        if parent.is_symlink():
            raise RuntimeError(f'Symlink parent path forbidden: {relative}')
    return REPO/x


def load():
    obj = json.loads(MANIFEST.read_text(encoding='utf-8'))
    if obj.get('schema')!='koa-tandem-vps-c0-overlay/v1':
        raise RuntimeError('Unexpected manifest')
    files=obj['files']
    with ZipFile(PAYLOAD) as archive:
        if sorted(archive.namelist())!=sorted(files):
            raise RuntimeError('Payload/manifest files differ')
        for relative, hashes in files.items():
            check_path(relative)
            if hashlib.sha256(archive.read(relative)).hexdigest()!=hashes['after']:
                raise RuntimeError(f'Corrupted payload: {relative}')
    return files


def classify(files):
    statuses={}
    for relative,hashes in files.items():
        path=check_path(relative)
        if path.is_symlink() or (path.exists() and not path.is_file()):
            s='DRIFT_TYPE'
        else:
            actual=checksum(path)
            s='ALREADY_UPDATED' if actual==hashes['after'] else 'READY' if actual==hashes['before'] else 'DRIFT'
        statuses[relative]=s
    return statuses


def require(files, after_only=False):
    statuses=classify(files)
    for relative,status in statuses.items(): print(f'[{status}] {relative}')
    allowed={'ALREADY_UPDATED'} if after_only else {'READY','ALREADY_UPDATED'}
    if any(status not in allowed for status in statuses.values()):
        raise RuntimeError('Local file drift: refused to overwrite repository changes')
    return statuses


def test_repo(repo):
    for args in ([sys.executable,'scripts/validate_c0_coordination.py'],
                 [sys.executable,'scripts/validate_tandem_vps_profile.py'],
                 [sys.executable,'-m','unittest','discover','-s','tests','-v']):
        print('[TEST]', ' '.join(args[1:]),flush=True)
        result=subprocess.run(args, cwd=repo, timeout=90, check=False)
        if result.returncode:
            raise RuntimeError(f'Validation failed (exit {result.returncode}); no installation approved')


def install(files):
    states=require(files)
    todo=[x for x,s in states.items() if s=='READY']
    if not todo:
        test_repo(REPO)
        print('[OK] Already updated; nothing written')
        return
    # Stage a repo copy and test the exact proposed overlay, without touching live checkout.
    with tempfile.TemporaryDirectory(prefix='koa-c0-vps-staging-') as work:
        stage=Path(work)/'repo'
        shutil.copytree(REPO,stage,ignore=IGNORE)
        with ZipFile(PAYLOAD) as archive:
            for relative in files:
                target=stage/relative
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes(archive.read(relative))
        test_repo(stage)
    if require(files)!=states:
        raise RuntimeError('Target content changed while testing; abort')
    date=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    backup=BACKUPS/date
    backup.mkdir(parents=True,exist_ok=False)
    recorded={}
    for relative in todo:
        target=check_path(relative)
        was_file=target.is_file()
        recorded[relative]=was_file
        if was_file:
            old=backup/'original'/relative
            old.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(target,old)
    metadata={'schema':'koa-tandem-vps-rollback/v1','files':recorded,'date':date,'rolled_back':False}
    (backup/'state.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
    written=[]
    try:
        with ZipFile(PAYLOAD) as archive:
            for relative in todo:
                target=check_path(relative)
                target.parent.mkdir(parents=True,exist_ok=True)
                temp=target.with_name(target.name+'.koa-vps-tmp')
                temp.write_bytes(archive.read(relative))
                os.replace(temp,target)
                written.append(relative)
        require(files,after_only=True)
    except Exception:
        for relative in reversed(written):
            target=check_path(relative)
            if recorded[relative]:shutil.copy2(backup/'original'/relative,target)
            else:target.unlink(missing_ok=True)
        raise
    print('[OK] C0 VPS profile updated; backup =',backup)
    print('[INFO] Documentation/CI only; Agent, remote VPS, databases and secrets unchanged')


def rollback(files):
    if not BACKUPS.is_dir():raise RuntimeError('No backup found')
    available=sorted((x for x in BACKUPS.iterdir() if (x/'state.json').is_file()),reverse=True)
    item=next((x for x in available if not json.loads((x/'state.json').read_text(encoding='utf-8'))['rolled_back']),None)
    if item is None:raise RuntimeError('No active backup found')
    meta=json.loads((item/'state.json').read_text(encoding='utf-8'))
    # Check *all* files first. Never undo a file changed after the installer.
    for relative, existed in meta['files'].items():
        if checksum(check_path(relative))!=files[relative]['after']:
            raise RuntimeError(f'Updated code diverged: {relative}; rollback refused')
        if existed and checksum(item/'original'/relative)!=files[relative]['before']:
            raise RuntimeError(f'Backup checksum mismatch: {relative}')
    for relative,existed in meta['files'].items():
        target=check_path(relative)
        if existed:shutil.copy2(item/'original'/relative,target)
        else:target.unlink(missing_ok=True)
    meta['rolled_back']=True
    (item/'state.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
    print('[OK] Changes reverted from backup',item)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=('preview','install','verify','rollback'))
    args=parser.parse_args()
    print('=== kOA DIGITAL ECOSYSTEM / TANDEM VPS C0 PROFILE /',args.mode.upper(),'===',flush=True)
    print('[REPO]',REPO)
    if not (REPO/'AGENTS.md').is_file() or not (REPO/'docs/status/current.md').is_file():
        raise RuntimeError('Wrong repository root: kOA Digital Ecosystem expected')
    files=load()
    if args.mode=='preview':
        require(files)
        print('[OK] Preview read-only; no publication/deployment or DB calls')
    elif args.mode=='install':install(files)
    elif args.mode=='verify':
        require(files,after_only=True)
        test_repo(REPO)
        print('[OK] All owner/C0 coordination checks passed; production still blocked')
    else:rollback(files)


if __name__=='__main__':
    try:main()
    except (RuntimeError,OSError,ValueError,KeyError,AssertionError) as exc:
        print(f'[BLOQUE] {type(exc).__name__}: {exc}',file=sys.stderr)
        sys.exit(2)
