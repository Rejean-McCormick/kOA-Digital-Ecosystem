"""Offline regressions for C0's 2026-11-24 lots 01–08 evidence ledger."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('c0_evidence_validator', ROOT/'scripts/validate_lots_01_08_evidence.py')
MODULE=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
LEDGER=json.loads((ROOT/'docs/audit/2026-11-24-lots-01-08-evidence.v1.json').read_text(encoding='utf-8'))

class TestLotsEvidence(unittest.TestCase):
    def test_valid_original(self):
        self.assertEqual([], MODULE.validate(LEDGER))
    def test_no_duplicate_target(self):
        broken=copy.deepcopy(LEDGER)
        broken['lots'][1]['target_files'][0]=copy.deepcopy(broken['lots'][0]['target_files'][0])
        self.assertTrue(any('duplicate target' in s for s in MODULE.validate(broken)))
    def test_no_dik_writes(self):
        broken=copy.deepcopy(LEDGER)
        broken['lots'][0]['target_files'][0]['repository']='diK'
        self.assertTrue(any('diK target forbidden' in s for s in MODULE.validate(broken)))
    def test_no_forged_qualification(self):
        broken=copy.deepcopy(LEDGER)
        broken['evidence_policy']['live_production_status']='PRODUCTION_PROVEN'
        self.assertTrue(any('production' in s for s in MODULE.validate(broken)))
    def test_reported_not_postinstall_readback(self):
        broken=copy.deepcopy(LEDGER)
        broken['totals']['post_install_sha256_readbacks']=74
        self.assertTrue(any('readback' in s for s in MODULE.validate(broken)))

if __name__ == '__main__': unittest.main()
