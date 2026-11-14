"""Standalone integration-observer tests: pins and owner authority remain separate."""
import importlib.util
import hashlib
import json
from pathlib import Path
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parents[1] / 'scripts/daat_owner_readiness.py'
SPEC = importlib.util.spec_from_file_location('daat_owner_readiness', SOURCE)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class DaATOwnerReadinessTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.snap = self.base/'snapshots'
        self.snap.mkdir()
        self.inventory = self.base/'repositories.json'
        records = []
        for role, (repo, dirname) in MODULE.REPO_NAMES.items():
            records.append({'github_repo': 'Rejean-McCormick/'+repo,
                            'local_root': 'C:\\mycode\\Test\\'+dirname})
            (self.snap/dirname).mkdir(exist_ok=True)
            if role in MODULE.REQUIRED:
                root = self.snap/dirname
                for marker in MODULE.REQUIRED[role]:
                    dest = root/marker
                    dest.parent.mkdir(parents=True,exist_ok=True)
                    dest.write_text('fixture marker\n',encoding='utf-8')
                report = {
                    'schema':'koa.daat-owner-observation/0.1.0-local',
                    'role':role, 'evidence_status':'OBSERVED_SNAPSHOT',
                    'read_only':True, 'markers':list(MODULE.REQUIRED[role]),
                    'prototype_consumer_adopted':False,
                    'ik_ingress_approved':False,
                    'canonical_write_authorized':False,
                    'publication_authorized':False,
                }
                desc = root/'integrations/daat/owner-observation.json'
                desc.parent.mkdir(parents=True,exist_ok=True)
                desc.write_text(json.dumps(report),encoding='utf-8')
        self.inventory.write_text(json.dumps(records),encoding='utf-8')
        fw=self.snap/'Kristal-Framework'
        (fw/'VERSION').write_text('11.0.0-draft.4\n',encoding='utf-8')
        kit=self.snap/'Kristal-Authoring-Kit'
        (kit/'VERSION').write_text('4.0.0-draft.4\n',encoding='utf-8')
        pin={}
        for i in range(11):
            name=f'schemas/v11/{"kristal-semantic-graph" if i == 0 else f"schema{i}"}.schema.json'
            dest=fw/name;dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_text(f'{{"schema":{i}}}',encoding='utf-8')
            pin[name]=hashlib.sha256(dest.read_bytes()).hexdigest()
        tool=fw/'tools/v11/interop_preflight.py'
        tool.parent.mkdir(parents=True,exist_ok=True)
        tool.write_text('print(42)\n',encoding='utf-8')
        pin['tools/v11/interop_preflight.py']=hashlib.sha256(tool.read_bytes()).hexdigest()
        pin['VERSION']=hashlib.sha256((fw/'VERSION').read_bytes()).hexdigest()
        profile={'profile':'kristal-integration-framework-pin/v11.0-draft.4',
                 'version':'11.0.0-draft.4', 'files':pin}
        for repo in ('Kristal-Authoring-Kit','Kristal-Integration-Pack'):
            dest=self.snap/repo/'contracts/v11-framework-pin.json'
            dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_text(json.dumps(profile),encoding='utf-8')
        dik=self.snap/'diK'
        py=dik/'pyproject.toml';py.write_text('version = "1.0.0a7"\n',encoding='utf-8')
        for i in range(11):
            name=f'schemas/v11/{"kristal-semantic-graph" if i == 0 else f"schema{i}"}.schema.json'
            dest=dik/'src/dik/_framework'/name
            dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_bytes((fw/name).read_bytes())

    def run_observer(self):
        return MODULE.run(self.inventory,snapshot_root=self.snap)

    def test_local_parity_never_qualifies_owner(self):
        r=self.run_observer()
        self.assertEqual(r['status'],'LOCAL_CHECKS_COMPLETED_OWNER_ADMISSIONS_BLOCKED')
        self.assertEqual(r['owner_admissions_qualified'],0)
        self.assertEqual(len(r['owners']),9)
        self.assertTrue(all(x['status']=='OBSERVED_SNAPSHOT' for x in r['owners']))
        self.assertTrue(all(x['canonical_write_authorized'] is False for x in r['owners']))
        self.assertEqual(r['cross_owner_checks']['framework_kit_integration_pack']['files_checked'],13)
        self.assertEqual(r['cross_owner_checks']['framework_dik']['schemas_checked'],11)
        self.assertNotIn(str(self.base),json.dumps(r))

    def test_modified_framework_file_detected(self):
        p=self.snap/'Kristal-Framework/schemas/v11/schema1.schema.json'
        p.write_text('{"tampered":true}',encoding='utf-8')
        r=self.run_observer()
        self.assertEqual(r['cross_owner_checks']['framework_kit_integration_pack']['status'],'INCOMPLETE')
        self.assertIn('framework_pin_drift',str(r['cross_owner_checks']))
        self.assertEqual(r['owner_admissions_qualified'],0)

    def test_modified_dik_schema_detected(self):
        p=self.snap/'diK/src/dik/_framework/schemas/v11/schema3.schema.json'
        p.write_text('{"tampered":true}',encoding='utf-8')
        r=self.run_observer()
        self.assertEqual(r['cross_owner_checks']['framework_dik']['status'],'INCOMPLETE')
        self.assertIn('dik_schema_byte_drift',str(r['cross_owner_checks']))

    def test_forged_owner_approval_refused(self):
        p=self.snap/'Kristal-Authoring-Kit/integrations/daat/owner-observation.json'
        data=json.loads(p.read_text(encoding='utf-8'))
        data['canonical_write_authorized']=True
        p.write_text(json.dumps(data),encoding='utf-8')
        r=self.run_observer()
        self.assertEqual(r['owners'][0]['status'],'INCOMPLETE')
        self.assertIn('unqualified_authority_claim',str(r['owners'][0]['issues']))

    def test_missing_owner_or_marker_does_not_look_verified(self):
        (self.snap/'Skope/VERSION').unlink()
        r=self.run_observer()
        row=next(x for x in r['owners'] if x['role']=='skope')
        self.assertEqual(row['status'],'INCOMPLETE')
        self.assertTrue(row['issues'])

    def test_duplicate_json_keys_rejected(self):
        self.inventory.write_text('[{"x":1,"x":2}]',encoding='utf-8')
        with self.assertRaisesRegex(MODULE.ObservationError,'duplicate_json_key'):
            self.run_observer()

    def test_path_escape_and_symlink_refused(self):
        with self.assertRaisesRegex(MODULE.ObservationError,'unsafe_relative_path'):
            MODULE.safe_file(self.snap,'../private.json')
        repo=self.snap/'Skope'
        (repo/'unsafe').symlink_to(self.base, target_is_directory=True)
        with self.assertRaisesRegex(MODULE.ObservationError,'symlink_in_observed_path'):
            MODULE.safe_file(repo,'unsafe/repositories.json')


if __name__=='__main__':
    unittest.main()
