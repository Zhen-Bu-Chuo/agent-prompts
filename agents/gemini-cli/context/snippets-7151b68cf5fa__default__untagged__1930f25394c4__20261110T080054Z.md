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
source_commit: 1930f25394c4b6338b64ffdb43083fca41614798
source_path: packages/core/src/prompts/snippets.ts
source_symbol: subAgentsXml.28
source_lines:
- 277
- 280
source_permalink: https://github.com/google-gemini/gemini-cli/blob/1930f25394c4b6338b64ffdb43083fca41614798/packages/core/src/prompts/snippets.ts#L277-L280
source_committed_at: '2026-11-09T22:27:15Z'
release_published_at: null
fetched_at: '2026-11-10T08:00:54Z'
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