---
agent: gemini-cli
prompt_id: snippets-7151b68cf5fa
module: context
variant: default
upstream_repository: google-gemini/gemini-cli
upstream_version: v0.71.1
package_name: null
package_version: null
source_ref: v0.71.1
source_commit: 7059de513d5987eba0f3a89932ff5cb8d66aa8f0
source_path: packages/core/src/prompts/snippets.ts
source_symbol: subAgentsXml.28
source_lines:
- 277
- 280
source_permalink: https://github.com/google-gemini/gemini-cli/blob/7059de513d5987eba0f3a89932ff5cb8d66aa8f0/packages/core/src/prompts/snippets.ts#L277-L280
source_committed_at: '2026-11-24T03:42:45Z'
release_published_at: '2026-11-24T03:50:24Z'
fetched_at: '2026-11-24T10:42:23Z'
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