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
source_commit: 0ac57c029b848d109eef940afe0db4b5a0c3dad0
source_path: packages/core/src/prompts/snippets.ts
source_symbol: skillsXml.34
source_lines:
- 326
- 333
source_permalink: https://github.com/google-gemini/gemini-cli/blob/0ac57c029b848d109eef940afe0db4b5a0c3dad0/packages/core/src/prompts/snippets.ts#L326-L333
source_committed_at: '2026-11-02T19:18:51Z'
release_published_at: null
fetched_at: '2026-11-03T07:37:34Z'
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