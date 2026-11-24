"""Non-normative 2026-11-23 C0 documentation and code snapshot audit checks."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from scripts.validate_documentation_audit import validate
ROOT=Path(__file__).resolve().parents[1]

class DocumentationAuditTests(unittest.TestCase):
    def test_ledger_and_triage_are_consistent(self):
        self.assertEqual(validate(ROOT), [])

    def test_qualification_cannot_be_fabricated(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            for p in ('docs/inventory/repositories.json',
                      'docs/inventory/code-snapshots-55-2026-11-23.v1.json',
                      'docs/audit/2026-11-23-documentation-drift.v1.json'):
                (root/p).parent.mkdir(parents=True,exist_ok=True)
                shutil.copy2(ROOT/p,root/p)
            p=root/'docs/inventory/code-snapshots-55-2026-11-23.v1.json'
            obj=json.loads(p.read_text('utf8'))
            obj['repositories'][0]['tests_executed']='PASS'
            p.write_text(json.dumps(obj),'utf8')
            self.assertTrue(any('unsupported qualification' in x for x in validate(root)))

    def test_dik_remains_deferred(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            for p in ('docs/inventory/repositories.json',
                      'docs/inventory/code-snapshots-55-2026-11-23.v1.json',
                      'docs/audit/2026-11-23-documentation-drift.v1.json'):
                (root/p).parent.mkdir(parents=True,exist_ok=True)
                shutil.copy2(ROOT/p,root/p)
            p=root/'docs/audit/2026-11-23-documentation-drift.v1.json'
            obj=json.loads(p.read_text('utf8'))
            next(x for x in obj['findings'] if x['id']=='DOC-002')['coordination_status']='open_owner_documentation'
            p.write_text(json.dumps(obj),'utf8')
            self.assertTrue(any('diK must remain deferred' in x for x in validate(root)))
