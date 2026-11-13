"""Snapshot C0 registration; local GitSink enrollment is not qualification."""
from pathlib import Path
import json
import shutil
import tempfile
import unittest
import importlib.util

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('c0_validate',ROOT/'scripts/validate_c0_coordination.py')
c0=importlib.util.module_from_spec(spec);spec.loader.exec_module(c0)

class DikKristalizerRegistrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry=json.loads((ROOT/'docs/inventory/repositories.json').read_text(encoding='utf8'))
        cls.graph=json.loads((ROOT/'docs/inventory/graph-registry.v1.json').read_text(encoding='utf8'))
        cls.lanes=json.loads((ROOT/'docs/2-Technical-Reference/40-integration/dik-kristalizer/coordination.json').read_text(encoding='utf8'))

    def test_repository_roots_from_smartdump(self):
        byrepo={r['github_repo']:r for r in self.registry}
        self.assertEqual(len(self.registry),55)
        for name,path in [('diK',r'C:\mycode\diK\diK'),('Kristalizer',r'C:\mycode\Kristal\Kristalizer')]:
            row=byrepo['Rejean-McCormick/'+name]
            self.assertEqual(row['local_root'],path)
            self.assertIn(row['status'], ('source_root_observed_in_smartdump_remote_unverified',
                                         'local_git_marker_seen'))
            self.assertEqual(row['scope'],'PUBLIC')

    def test_source_versions_and_unresolved_cross_version_gate(self):
        comp={x['id']:x for x in self.lanes['components']}
        self.assertEqual(comp['dik']['observed_version'],'1.0.0-alpha.7')
        self.assertEqual(comp['kristalizer']['observed_version'],'1.2.2')
        self.assertIn('draft.3',comp['dik']['framework_target'])
        self.assertIn('draft.4',comp['kristalizer']['framework_target'])
        self.assertTrue(self.lanes['no_implicit_publication_authorization'])
        self.assertTrue(self.lanes['no_canonical_authority_transfer'])
        self.assertEqual(self.lanes['authority'],'coordination_only_non_normative')

    def test_graph_registry_cross_consistency(self):
        self.assertEqual(self.graph['reference_count'],len(self.registry))
        systems={s['id'] for s in self.graph['systems']}
        self.assertTrue({'dik','kristalizer','kristal','architect'}.issubset(systems))
        edges=[e for e in self.graph['relations'] if e['from'] in ('dik','kristalizer') or e['to'] in ('dik','kristalizer')]
        self.assertGreaterEqual(len(edges),4)
        for e in edges:
            self.assertEqual(e['verification'],'not_certified')
            self.assertTrue(e['source'].endswith('dik-kristalizer/README.md'))

    def test_legacy_baseline_unmodified(self):
        old=json.loads((ROOT/'docs/2-Technical-Reference/40-integration/knowledge-projection-contract-set.json').read_text())
        self.assertEqual(old['kristal']['standard'],'6.0.0')
        self.assertEqual(old['encyklopedia']['handoff'],'encyklopedia.corpus-harvest-handoff/1.0.0')
        self.assertEqual(c0.validate(ROOT),[])

    def test_unsafe_flags_and_git_qualification_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            copy=Path(td)
            # Only paths required by the global coordination validator.
            shutil.copytree(ROOT/'docs',copy/'docs')
            shutil.copy(ROOT/'README.md',copy/'README.md')
            cfg=copy/'docs/2-Technical-Reference/40-integration/dik-kristalizer/coordination.json'
            d=json.loads(cfg.read_text(encoding='utf8'));d['no_implicit_publication_authorization']=False
            cfg.write_text(json.dumps(d),encoding='utf8')
            self.assertTrue(any('unsafe flag' in e for e in c0.validate(copy)))
            d['no_implicit_publication_authorization']=True
            cfg.write_text(json.dumps(d),encoding='utf8')
            inv=copy/'docs/inventory/repositories.json';rows=json.loads(inv.read_text(encoding='utf8'))
            next(x for x in rows if x['github_repo']=='Rejean-McCormick/diK')['status']='github_and_local_remote_verified'
            inv.write_text(json.dumps(rows),encoding='utf8')
            self.assertTrue(any('invalid inventory status' in e for e in c0.validate(copy)))
            next(x for x in rows if x['github_repo']=='Rejean-McCormick/diK')['status']='local_git_marker_seen'
            inv.write_text(json.dumps(rows),encoding='utf8')
            self.assertFalse(any('invalid inventory status' in e for e in c0.validate(copy)))

if __name__=='__main__':unittest.main()
