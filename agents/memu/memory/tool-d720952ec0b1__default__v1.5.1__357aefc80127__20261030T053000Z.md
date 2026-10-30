---
agent: memu
prompt_id: tool-d720952ec0b1
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/tool.py
source_symbol: module.PROMPT_BLOCK_RULES.1
source_lines:
- 19
- 43
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/tool.py#L19-L43
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 1b8b8e8f916002d50e49f4e865a8fbd73b7b98fa8fcea9c416e202e8dafe1765
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Rules
## General requirements (must satisfy all)
- Each tool memory must capture: tool name, what it was used for, outcome, and when to use it again.
- Focus on patterns that help future tool selection decisions.
- Include success/failure context to help agents avoid repeated mistakes.
- Each memory should help answer: "When should I use this tool?"

## What TO Extract
- Successful tool usage patterns with context
- Failed tool attempts with lessons learned
- Tool combinations that work well together
- Performance insights (fast vs slow tools for different tasks)

## What NOT to Extract
- Trivial tool calls without learning value
- Duplicate patterns already captured
- Tool calls with no meaningful outcome

## Memory Item Content Requirements
- Include the tool name prominently
- Describe the use case or scenario
- Note the outcome (success/failure/partial)
- Provide a "when_to_use" hint for future retrieval
