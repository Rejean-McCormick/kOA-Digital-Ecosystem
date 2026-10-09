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

if __name__=='__main__':unittest.main()
