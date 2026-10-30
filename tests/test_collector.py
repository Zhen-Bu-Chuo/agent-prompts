import json
import tempfile
import unittest
from pathlib import Path

from collector.extract import extract
from collector.archive import archive_snapshot, safe_relative
from collector.sources import choose_release


def snapshot(commit='a' * 40, version='v1.0.0', ref_kind='release'):
    return dict(repository='example/agent', source_commit=commit,
                source_ref=version, upstream_version=version, ref_kind=ref_kind,
                source_committed_at='2026-10-01T00:00:00Z', release_published_at=None,
                license='MIT', package_version=None)


def record(path='prompts/system.md', body='You are a helpful coding agent.', variant='default'):
    return dict(source_path=path, module='system', variant=variant,
                fragment=extract(body, 'raw')[0])


class ExtractionTests(unittest.TestCase):
    def test_raw_prompt_preserves_whitespace(self):
        self.assertEqual(extract('  hello\n\n', 'raw')[0].content, '  hello\n\n')

    def test_python_extracts_static_and_dynamic_without_docstrings(self):
        source = '\"\"\"Module documentation should not be archived\"\"\"\nSYSTEM = "You are an assistant."\nMEMORY = f"Recall {name} before answering."\n'
        items = extract(source, 'python', min_chars=10)
        self.assertEqual(len(items), 2)
        self.assertIn('You are an assistant.', [x.content for x in items])
        self.assertTrue(any('{name}' in x.content and x.kind == 'dynamic_template' for x in items))

    def test_python_symbol_filter(self):
        items = extract('PROMPT="Remember the user"\nEXAMPLE="Do not collect this"', 'python', min_chars=5, key_pattern='PROMPT')
        self.assertEqual([x.content for x in items], ['Remember the user'])

    def test_javascript_nested_interpolation_stays_one_fragment(self):
        source = 'const system = `You are ${enabled ? `a ${role}` : "a helper"}. Use tools.`;'
        items = extract(source, 'js-templates', min_chars=10)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].content, 'You are ${enabled ? `a ${role}` : "a helper"}. Use tools.')

    def test_javascript_ignores_comments(self):
        source = '// `do not collect this comment`\nconst x = `A real system prompt.`;'
        self.assertEqual([x.content for x in extract(source, 'js-templates', min_chars=10)], ['A real system prompt.'])

    def test_javascript_ordinary_role_strings(self):
        source = 'const mode = { roleDefinition: "You are a careful planner.", id: "plan" };'
        items = extract(source, 'js-strings', min_chars=10, key_pattern='roleDefinition')
        self.assertEqual([x.content for x in items], ['You are a careful planner.'])

    def test_javascript_line_fragments_preserve_source_escapes(self):
        source = "const prompt = ['Remember the user\\n', 'Reflect before the next attempt'];"
        items = extract(source, 'js-strings', min_chars=10)
        self.assertEqual(items[0].content, 'Remember the user\\n')

    def test_javascript_regex_does_not_desynchronize_lexer(self):
        source = "const quote = /\"([^\\\"]+)\"|'([^']+)'/g; const system = `You are a careful helper.`;"
        items = extract(source, 'js-strings', min_chars=10)
        self.assertEqual([x.content for x in items], ['You are a careful helper.'])

    def test_rust_prompt_string_extracts_raw_and_ignores_comments(self):
        source = '''// let ignored = r#"A fake prompt in a comment."#;
const SYSTEM_PROMPT: &str = r#"You are an agent. Preserve this prompt exactly."#;
const COMMAND = "echo never run this";
'''
        items = extract(source, 'rust-strings', min_chars=20, key_pattern='SYSTEM_PROMPT')
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].content, 'You are an agent. Preserve this prompt exactly.')

    def test_yaml_only_selects_prompt_fields(self):
        items = extract('agent:\n  system_template: "You are a programmer"\n  command: "echo do not execute me"\n', 'yaml', min_chars=5)
        self.assertEqual([x.content for x in items], ['You are a programmer'])

    def test_json_prompt_fields(self):
        items = extract('{"system_prompt":"You are an assistant", "version":"1.0.0"}', 'json', min_chars=5)
        self.assertEqual([x.content for x in items], ['You are an assistant'])


class VersionTests(unittest.TestCase):
    def test_filters_monorepo_packages_and_prereleases(self):
        releases = [dict(tag_name='sdk-v9', draft=False, prerelease=False),
                    dict(tag_name='v3.0.0-beta', draft=False, prerelease=True),
                    dict(tag_name='v2.0.0', draft=False, prerelease=False),
                    dict(tag_name='v1.0.0', draft=False, prerelease=False)]
        self.assertEqual(choose_release(releases, r'^v\d+\.\d+\.\d+$')['tag_name'], 'v2.0.0')

    def test_no_usable_release_returns_none(self):
        self.assertIsNone(choose_release([dict(tag_name='v1',draft=True,prerelease=False)]))

    def test_misflagged_rc_release_is_not_stable(self):
        self.assertIsNone(choose_release([dict(tag_name='v1.6.6rc1',draft=False,prerelease=False)]))


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.adapter = dict(slug='sample', name='Sample', repository='example/agent', coverage='supported', limitations=[])

    def tearDown(self):
        self.tmp.cleanup()

    def archive(self, snap=None, records=None):
        return archive_snapshot(self.root, self.adapter, snap or snapshot(), [record()] if records is None else records,
                                collected_at='2026-10-30T01:00:00Z')

    def test_unchanged_run_is_byte_identical(self):
        self.archive()
        before = {str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.archive()
        after = {str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_same_content_new_release_reuses_file(self):
        self.archive()
        self.archive(snapshot('b'*40, 'v2.0.0'))
        self.assertEqual(len(list((self.root/'agents/sample/system').glob('*.md'))), 1)
        manifest = json.loads((self.root/'indexes/sample.json').read_text())
        self.assertEqual(len(manifest['snapshots']), 2)

    def test_changed_prompt_keeps_history(self):
        self.archive()
        self.archive(snapshot('b'*40,'v2.0.0'), [record(body='You are a careful coding agent.')])
        self.assertEqual(len(list((self.root/'agents/sample/system').glob('*.md'))), 2)

    def test_variants_keep_distinct_identity(self):
        self.archive(records=[record(variant='plan'), record(variant='build')])
        self.assertEqual(len(list((self.root/'agents/sample/system').glob('*.md'))), 2)

    def test_moved_prompt_reuses_content_and_records_new_source(self):
        self.archive()
        self.archive(snapshot('b'*40,'v2.0.0'),[record(path='new/system.md')])
        manifest = json.loads((self.root/'indexes/sample.json').read_text())
        current = manifest['snapshots'][-1]
        self.assertEqual(current['entries'][0]['source_path'], 'new/system.md')
        self.assertEqual(len(current['changes']['moved']), 1)
        self.assertEqual(len(list((self.root/'agents/sample/system').glob('*.md'))), 1)

    def test_removal_keeps_existing_archive(self):
        self.archive()
        self.archive(snapshot('b'*40,'v2.0.0'),[])
        manifest = json.loads((self.root/'indexes/sample.json').read_text())
        self.assertEqual(len(manifest['snapshots'][-1]['changes']['removed']), 1)
        self.assertEqual(len(list((self.root/'agents/sample/system').glob('*.md'))), 1)

    def test_path_traversal_and_windows_paths_rejected(self):
        for value in ['../evil','/absolute','C:/absolute','a/../../evil','a\\..\\evil']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                safe_relative(value)

    def test_archive_contains_provenance_and_exact_body(self):
        self.archive()
        text = next((self.root/'agents/sample/system').glob('*.md')).read_text()
        self.assertIn('source_commit: '+ 'a'*40, text)
        self.assertIn('source_permalink:', text)
        self.assertTrue(text.endswith('You are a helpful coding agent.'))


if __name__ == '__main__':
    unittest.main()
