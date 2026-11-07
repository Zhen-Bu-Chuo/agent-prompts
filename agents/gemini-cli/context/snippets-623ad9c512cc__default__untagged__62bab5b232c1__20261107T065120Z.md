---
agent: gemini-cli
prompt_id: snippets-623ad9c512cc
module: context
variant: default
upstream_repository: google-gemini/gemini-cli
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 62bab5b232c15b925d31e655ce844ab939c882b7
source_path: packages/core/src/prompts/snippets.ts
source_symbol: skillsXml.32
source_lines:
- 318
- 322
source_permalink: https://github.com/google-gemini/gemini-cli/blob/62bab5b232c15b925d31e655ce844ab939c882b7/packages/core/src/prompts/snippets.ts#L318-L322
source_committed_at: '2026-11-06T21:43:53Z'
release_published_at: null
fetched_at: '2026-11-07T06:51:20Z'
extractor_version: 1.0.3
content_sha256: 9823da193b7fe912db21b35375ef4d99cb18c7fd462e33d0be2420ffcbfb665f
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---
  <skill>
    <name>${skill.name}</name>
    <description>${skill.description}</description>
    <location>${skill.location}</location>
  </skill>