import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from collector.pipeline import collect_sources, validate_archive


class FakeGitHub:
    def repository(self, repo):
        if repo == 'example/broken':
            raise RuntimeError('source is temporarily unavailable')
        return {'full_name':repo, 'default_branch':'main', 'archived':False, 'license':{'spdx_id':'MIT'}}

    def releases(self, repo):
        return [{'tag_name':'v1.0.0','draft':False,'prerelease':False,'published_at':'2026-10-01T00:00:00Z'}]

    def commit(self, repo, ref):
        return {'sha':'a'*40,'commit':{'committer':{'date':'2026-10-01T00:00:00Z'}}}

    def tree(self, repo, sha):
        return ['LICENSE','prompts/system.md']

    def file(self, repo, sha, path):
        if path == 'LICENSE':
            return 'MIT License\nCopyright (c) example\nPermission is hereby granted, free of charge, to any person obtaining a copy.'
        return 'You are an assistant. Remember relevant facts and use available tools carefully.\n'


def adapter(slug='sample', repo='example/agent'):
    return dict(slug=slug,name=slug,repository=repo,coverage='supported',limitations=[],
                rules=[dict(glob='prompts/*.md',module='system',format='raw')])


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_source_failure_does_not_block_others(self):
        reports = collect_sources(self.root, [adapter('broken','example/broken'),adapter()], FakeGitHub(), initial_latest=True, workers=1)
        self.assertEqual({x['agent']:x['status'] for x in reports}, {'broken':'error','sample':'supported'})
        self.assertTrue((self.root/'indexes/sample.json').exists())

    def test_successful_source_is_unchanged_on_rerun(self):
        collect_sources(self.root,[adapter()],FakeGitHub(),initial_latest=True,workers=1)
        before = {str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file() and 'work' not in p.parts}
        collect_sources(self.root,[adapter()],FakeGitHub(),initial_latest=True,workers=1)
        after = {str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file() and 'work' not in p.parts}
        self.assertEqual(before, after)

    def test_initial_collection_contains_only_one_latest_snapshot(self):
        collect_sources(self.root,[adapter()],FakeGitHub(),initial_latest=True,workers=1)
        manifest = json.loads((self.root/'indexes/sample.json').read_text())
        self.assertEqual(len(manifest['snapshots']),1)
        self.assertEqual(manifest['snapshots'][0]['source_ref'],'v1.0.0')

    def test_unavailable_source_has_metadata_without_prompt_files(self):
        config = adapter()
        config.update(coverage='unavailable',rules=[],limitations=['No redistributable official prompt source.'])
        reports = collect_sources(self.root,[config],FakeGitHub(),initial_latest=True,workers=1)
        self.assertEqual(reports[0]['status'],'unavailable')
        self.assertEqual(len(list((self.root/'agents/sample').rglob('*.md'))),0)

    def test_failure_preserves_last_successful_snapshot(self):
        collect_sources(self.root,[adapter()],FakeGitHub(),initial_latest=True,workers=1)
        before=json.loads((self.root/'indexes/sample.json').read_text())['snapshots']
        collect_sources(self.root,[adapter(repo='example/broken')],FakeGitHub(),initial_latest=True,workers=1)
        after=json.loads((self.root/'indexes/sample.json').read_text())['snapshots']
        self.assertEqual(before,after)

    def test_archive_audit_detects_tampering(self):
        collect_sources(self.root,[adapter()],FakeGitHub(),initial_latest=True,workers=1)
        self.assertEqual(validate_archive(self.root),[])
        path=next((self.root/'agents/sample/system').glob('*.md'))
        path.write_bytes(path.read_bytes()+b'tampered')
        self.assertTrue(any('hash' in x.lower() for x in validate_archive(self.root)))


if __name__=='__main__':
    unittest.main()
