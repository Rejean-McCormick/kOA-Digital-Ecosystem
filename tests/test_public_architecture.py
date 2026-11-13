"""Validate the safe public C0 design projection (not a deployed artifact)."""
import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from export_public_architecture import build

class PublicArchitectureTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads((ROOT/'docs/target/public-architecture.v1.json').read_text(encoding='utf8'))

    def test_export_is_deterministic(self):
        self.assertEqual(self.data,build(ROOT))

    def test_only_public_non_deployment_metadata(self):
        self.assertEqual(self.data['status'],'TARGET_DESIGN_NOT_DEPLOYMENT_EVIDENCE')
        self.assertEqual(self.data['classification'],'PUBLIC_DESIGN_METADATA_ONLY')
        self.assertEqual(len(self.data['chains']),24)
        self.assertEqual(len(self.data['repositories']),55)
        self.assertEqual(len(self.data['boundaries']),26)
        data=json.dumps(self.data)
        for secret in ('local_root','source_member','snapshot_member','password','git_revision','C:\\mycode\\'):
            self.assertNotIn(secret,data)

    def test_no_qualified_edge_claim(self):
        self.assertTrue(all(x['state']=='target_design_not_qualified' for x in self.data['boundaries']))
        self.assertTrue(all(x['state']=='target_design_not_qualified' for x in self.data['chains']))

if __name__=='__main__':unittest.main()
