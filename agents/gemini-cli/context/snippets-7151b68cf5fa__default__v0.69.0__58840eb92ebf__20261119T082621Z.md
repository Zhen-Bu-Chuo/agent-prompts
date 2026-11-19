---
agent: gemini-cli
prompt_id: snippets-7151b68cf5fa
module: context
variant: default
upstream_repository: google-gemini/gemini-cli
upstream_version: v0.69.0
package_name: null
package_version: null
source_ref: v0.69.0
source_commit: 58840eb92ebf1474193a05817c34a74820bd444a
source_path: packages/core/src/prompts/snippets.ts
source_symbol: subAgentsXml.28
source_lines:
- 277
- 280
source_permalink: https://github.com/google-gemini/gemini-cli/blob/58840eb92ebf1474193a05817c34a74820bd444a/packages/core/src/prompts/snippets.ts#L277-L280
source_committed_at: '2026-11-19T01:38:02Z'
release_published_at: '2026-11-19T01:45:47Z'
fetched_at: '2026-11-19T08:26:21Z'
extractor_version: 1.0.3
content_sha256: cbb2af38fc01d8c0abed2178cda67306faac0836aea828cc84f2c251d22b67de
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---
  <subagent>
    <name>${agent.name}</name>
    <description>${agent.description}</description>
  </subagent>