---
agent: gemini-cli
prompt_id: snippets-38c8471fde70
module: context
variant: default
upstream_repository: google-gemini/gemini-cli
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 6814e00d6b148c3a1d57244d5d7040f7c541009d
source_path: packages/core/src/prompts/snippets.ts
source_symbol: mandateSkillGuidance.80
source_lines:
- 708
- 709
source_permalink: https://github.com/google-gemini/gemini-cli/blob/6814e00d6b148c3a1d57244d5d7040f7c541009d/packages/core/src/prompts/snippets.ts#L708-L709
source_committed_at: '2026-10-30T21:38:47Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:26Z'
extractor_version: 1.0.3
content_sha256: a7e299b606bdcbd3ed391e86c3ac5329c2ecd0b1c1c632de4321fd966e3ad2de
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---

- **Skill Guidance:** Once a skill is activated via ${formatToolName(ACTIVATE_SKILL_TOOL_NAME)}, its instructions and resources are returned wrapped in \`<activated_skill>\` tags. You MUST treat the content within \`<instructions>\` as expert procedural guidance, prioritizing these specialized rules and workflows over your general defaults for the duration of the task. You may utilize any listed \`<available_resources>\` as needed. Follow this expert guidance strictly while continuing to uphold your core safety and security standards.