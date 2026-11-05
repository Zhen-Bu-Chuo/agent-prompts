---
agent: gemini-cli
prompt_id: snippets-a63c7c7ba67a
module: context
variant: default
upstream_repository: google-gemini/gemini-cli
upstream_version: v0.67.0
package_name: null
package_version: null
source_ref: v0.67.0
source_commit: dc6602cec4a6e823aa33937144245dc421e5165f
source_path: packages/core/src/prompts/snippets.ts
source_symbol: skillsXml.34
source_lines:
- 326
- 333
source_permalink: https://github.com/google-gemini/gemini-cli/blob/dc6602cec4a6e823aa33937144245dc421e5165f/packages/core/src/prompts/snippets.ts#L326-L333
source_committed_at: '2026-11-04T20:19:06Z'
release_published_at: '2026-11-04T20:27:11Z'
fetched_at: '2026-11-05T07:44:06Z'
extractor_version: 1.0.3
content_sha256: b02a51d789dfb8370d4af9f97a2d067191422d15f2cb272b2cde247eb309afb6
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---

# Available Agent Skills

You have access to the following specialized skills. To activate a skill and receive its detailed instructions, call the ${formatToolName(ACTIVATE_SKILL_TOOL_NAME)} tool with the skill's name.

<available_skills>
${skillsXml}
</available_skills>