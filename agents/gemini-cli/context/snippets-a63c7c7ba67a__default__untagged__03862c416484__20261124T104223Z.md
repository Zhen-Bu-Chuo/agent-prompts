---
agent: gemini-cli
prompt_id: snippets-a63c7c7ba67a
module: context
variant: default
upstream_repository: google-gemini/gemini-cli
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 03862c4164844c6cf8063b4cc48546ec1609cf2e
source_path: packages/core/src/prompts/snippets.ts
source_symbol: skillsXml.34
source_lines:
- 326
- 333
source_permalink: https://github.com/google-gemini/gemini-cli/blob/03862c4164844c6cf8063b4cc48546ec1609cf2e/packages/core/src/prompts/snippets.ts#L326-L333
source_committed_at: '2026-11-24T03:16:03Z'
release_published_at: null
fetched_at: '2026-11-24T10:42:23Z'
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