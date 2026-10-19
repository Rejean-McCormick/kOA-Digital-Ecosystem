"""C0 VPS profile decision: no unauthorized deployment claims or status promotion."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
PATH=Path('docs/2-Technical-Reference/40-integration/tandem-vps-capsule-agent/deployment-profile.json')
spec=importlib.util.spec_from_file_location('tandem_validate',ROOT/'scripts/validate_tandem_vps_profile.py')
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class TandemVpsDecisionTests(unittest.TestCase):
    def test_selected_profile_valid(self):
        self.assertEqual(mod.validate(ROOT),[])

    def with_mutation(self, mutation):
        with tempfile.TemporaryDirectory() as td:
            target=Path(td)
            for p in ['README.md','docs/index.md','docs/status/current.md','docs/2-Technical-Reference/10-system/authority-map.md','docs/2-Technical-Reference/50-operations/releases.md']:
                dst=target/p;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/p,dst)
            sourcedir=ROOT/PATH.parent
            shutil.copytree(sourcedir,target/PATH.parent)
            p=target/PATH
            obj=json.loads(p.read_text(encoding='utf-8'))
            mutation(obj)
            p.write_text(json.dumps(obj,indent=2),encoding='utf-8')
            return mod.validate(target)

    def test_runtime_activation_claim_rejected(self):
        self.assertTrue(any('forbidden authorization' in s for s in self.with_mutation(lambda x:x['safety'].update(allow_runtime_activation=True))))

    def test_premature_production_gate_rejected(self):
        self.assertTrue(any('G8 must remain blocked' in s for s in self.with_mutation(lambda x:x['release_gates'][8].update(state='PASS'))))

    def test_agent_workstream_false_success_rejected(self):
        self.assertTrue(any('unapproved workstream success' in s for s in self.with_mutation(lambda x:x['owner_workstreams'][1].update(status='QUALIFIED_INTEGRATED'))))

    def test_wrong_platform_rejected(self):
        self.assertTrue(any('wrong target' in s for s in self.with_mutation(lambda x:x['target'].update(platform='kubernetes'))))

    def test_unauthorized_production_approval_rejected(self):
        self.assertTrue(any('unapproved or broadened' in s for s in self.with_mutation(lambda x:x['decision'].update(not_a_production_approval=False))))

    def test_cycle_rejected(self):
        self.assertTrue(any('cyclic workstreams' in s for s in self.with_mutation(lambda x:x['owner_workstreams'][0].update(depends_on=['TANDEM-W6']))))

    def test_duplicate_gate_rejected(self):
        self.assertTrue(any('G0-G8' in s for s in self.with_mutation(lambda x:x['release_gates'][1].update(id='G0'))))

    def test_missing_lot1_local_citation_rejected(self):
        self.assertTrue(any('baseline observations' in s for s in self.with_mutation(lambda x:x['observations'].pop())))

    def test_unpinned_commit_format_rejected(self):
        self.assertTrue(any('invalid pin' in s for s in self.with_mutation(lambda x:x['pins'].update(konnaxion_commit='master'))))


if __name__=='__main__':unittest.main()
