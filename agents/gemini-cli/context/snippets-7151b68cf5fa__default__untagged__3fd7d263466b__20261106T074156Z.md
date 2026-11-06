---
agent: gemini-cli
prompt_id: snippets-7151b68cf5fa
module: context
variant: default
upstream_repository: google-gemini/gemini-cli
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 3fd7d263466b9e5d30b2da1ebf85dae956a0fb86
source_path: packages/core/src/prompts/snippets.ts
source_symbol: subAgentsXml.28
source_lines:
- 277
- 280
source_permalink: https://github.com/google-gemini/gemini-cli/blob/3fd7d263466b9e5d30b2da1ebf85dae956a0fb86/packages/core/src/prompts/snippets.ts#L277-L280
source_committed_at: '2026-11-05T21:17:03Z'
release_published_at: null
fetched_at: '2026-11-06T07:41:56Z'
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