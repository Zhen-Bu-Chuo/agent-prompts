---
agent: gemini-cli
prompt_id: snippets-7151b68cf5fa
module: context
variant: default
upstream_repository: google-gemini/gemini-cli
upstream_version: v0.66.0
package_name: null
package_version: null
source_ref: v0.66.0
source_commit: 970413207732f5d4d8c50540c7fc359c44fdaaf2
source_path: packages/core/src/prompts/snippets.ts
source_symbol: subAgentsXml.28
source_lines:
- 277
- 280
source_permalink: https://github.com/google-gemini/gemini-cli/blob/970413207732f5d4d8c50540c7fc359c44fdaaf2/packages/core/src/prompts/snippets.ts#L277-L280
source_committed_at: '2026-10-27T20:19:20Z'
release_published_at: '2026-10-27T20:26:28Z'
fetched_at: '2026-10-30T05:29:35Z'
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