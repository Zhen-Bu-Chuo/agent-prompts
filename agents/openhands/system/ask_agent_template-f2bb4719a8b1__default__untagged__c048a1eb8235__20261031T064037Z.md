---
agent: openhands
prompt_id: ask_agent_template-f2bb4719a8b1
module: system
variant: default
upstream_repository: OpenHands/software-agent-sdk
upstream_version: null
package_name: openhands-sdk
package_version: null
source_ref: main
source_commit: c048a1eb82353b0586f3ce600708394a68ebb246
source_path: openhands-sdk/openhands/sdk/context/prompts/templates/ask_agent_template.j2
source_symbol: document
source_lines:
- 1
- 11
source_permalink: https://github.com/OpenHands/software-agent-sdk/blob/c048a1eb82353b0586f3ce600708394a68ebb246/openhands-sdk/openhands/sdk/context/prompts/templates/ask_agent_template.j2#L1-L11
source_committed_at: '2026-10-30T14:47:57Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:37Z'
extractor_version: 1.0.3
content_sha256: 551296745d954c9fd3cb06b2fd67b1a7cfca94d80090c13de1e65e95b6ec1192
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
<QUESTION>
Based on the activity so far answer the following question

## Question
{{ question }}


<IMPORTANT>
This is a question, do not make any tool call and just answer my question.
</IMPORTANT>
</QUESTION>
