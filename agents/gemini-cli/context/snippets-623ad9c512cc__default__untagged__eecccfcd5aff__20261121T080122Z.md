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
source_commit: eecccfcd5aff25de5e78135ca20f7abe3f566955
source_path: packages/core/src/prompts/snippets.ts
source_symbol: skillsXml.32
source_lines:
- 318
- 322
source_permalink: https://github.com/google-gemini/gemini-cli/blob/eecccfcd5aff25de5e78135ca20f7abe3f566955/packages/core/src/prompts/snippets.ts#L318-L322
source_committed_at: '2026-11-20T19:19:05Z'
release_published_at: null
fetched_at: '2026-11-21T08:01:22Z'
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