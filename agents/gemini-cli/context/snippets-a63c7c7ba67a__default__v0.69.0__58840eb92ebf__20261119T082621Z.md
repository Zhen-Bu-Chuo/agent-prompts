---
agent: gemini-cli
prompt_id: snippets-a63c7c7ba67a
module: context
variant: default
upstream_repository: google-gemini/gemini-cli
upstream_version: v0.69.0
package_name: null
package_version: null
source_ref: v0.69.0
source_commit: 58840eb92ebf1474193a05817c34a74820bd444a
source_path: packages/core/src/prompts/snippets.ts
source_symbol: skillsXml.34
source_lines:
- 326
- 333
source_permalink: https://github.com/google-gemini/gemini-cli/blob/58840eb92ebf1474193a05817c34a74820bd444a/packages/core/src/prompts/snippets.ts#L326-L333
source_committed_at: '2026-11-19T01:38:02Z'
release_published_at: '2026-11-19T01:45:47Z'
fetched_at: '2026-11-19T08:26:21Z'
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