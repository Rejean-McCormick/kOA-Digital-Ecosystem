"""Scope-limited tests for the C0 document registry and historical baseline safety."""
import importlib.util
from pathlib import Path
import json
import tempfile
import shutil
import unittest

ROOT=Path(__file__).resolve().parents[1]
MODULE=ROOT/'scripts/validate_c0_coordination.py'
spec=importlib.util.spec_from_file_location('c0_validate',MODULE)
c0=importlib.util.module_from_spec(spec)
spec.loader.exec_module(c0)

class C0CoordinatorTests(unittest.TestCase):
    def test_registry_passes(self):
        self.assertEqual(c0.validate(ROOT), [])

    def test_baseline_is_frozen(self):
        p=ROOT/'docs/2-Technical-Reference/40-integration/knowledge-projection-contract-set.json'
        data=json.loads(p.read_text(encoding='utf-8'))
        self.assertEqual(data['encyklopedia']['handoff'],'encyklopedia.corpus-harvest-handoff/1.0.0')
        self.assertEqual(data['kristal']['standard'],'6.0.0')

    def test_registry_evidence_not_mislabelled_qualified(self):
        p=ROOT/'docs/2-Technical-Reference/40-integration/orchestration-c0/interfaces.json'
        rows=json.loads(p.read_text(encoding='utf-8'))['entries']
        self.assertEqual(len(rows),10)
        self.assertFalse(any(x['qualification']=='qualified_integrated' for x in rows))
        self.assertEqual(next(x for x in rows if x['id']=='I02')['qualification'],'pending_real_consumer')


    def test_v10_registry_is_separate_from_legacy(self):
        path=ROOT/'docs/2-Technical-Reference/40-integration/kristal-v10-alignment/workstreams.json'
        obj=json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(obj['authority'],'coordination_only_non_normative')
        self.assertTrue(obj['no_implicit_publication_authorization'])
        self.assertEqual(obj['framework_baseline']['status'],'draft')
        self.assertGreaterEqual(len(obj['entries']),20)
        self.assertEqual(c0.validate(ROOT), [])

    def test_v10_rejects_unsubstantiated_qualification(self):
        with tempfile.TemporaryDirectory() as td:
            copy=Path(td)
            shutil.copytree(ROOT/'docs/2-Technical-Reference',copy/'docs/2-Technical-Reference')
            shutil.copytree(ROOT/'docs/status',copy/'docs/status')
            shutil.copy(ROOT/'README.md',copy/'README.md')
            p=copy/'docs/2-Technical-Reference/40-integration/kristal-v10-alignment/workstreams.json'
            data=json.loads(p.read_text(encoding='utf-8'))
            data['entries'][0]['implementation_status']='qualified_integrated'
            data['entries'][0]['remote_commit']='unverified'
            p.write_text(json.dumps(data),encoding='utf-8')
            self.assertTrue(any('unsupported qualified claim' in issue for issue in c0.validate(copy)))

    def test_v10_rejects_dependency_cycle(self):
        with tempfile.TemporaryDirectory() as td:
            copy=Path(td)
            shutil.copytree(ROOT/'docs/2-Technical-Reference',copy/'docs/2-Technical-Reference')
            shutil.copytree(ROOT/'docs/status',copy/'docs/status')
            shutil.copy(ROOT/'README.md',copy/'README.md')
            p=copy/'docs/2-Technical-Reference/40-integration/kristal-v10-alignment/workstreams.json'
            data=json.loads(p.read_text(encoding='utf-8'))
            byid={x['id']:x for x in data['entries']}
            byid['C0-01']['depends_on']=['KNAV-03']
            p.write_text(json.dumps(data),encoding='utf-8')
            self.assertTrue(any('dependency cycle' in issue for issue in c0.validate(copy)))

if __name__=='__main__':unittest.main()
