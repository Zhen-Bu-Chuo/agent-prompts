---
agent: hermes
prompt_id: system_prompt-6a2c6060d065
module: system
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: v2026.9.24
package_name: null
package_version: null
source_ref: v2026.9.24
source_commit: f97608f178d1ffeca59860195ab7da295f7c8e5f
source_path: agent/system_prompt.py
source_symbol: module.build_system_prompt_parts.1
source_lines:
- 786
- 786
source_permalink: https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/system_prompt.py#L786-L786
source_committed_at: '2026-09-24T10:08:47Z'
release_published_at: '2026-09-24T10:09:38Z'
fetched_at: '2026-10-30T05:29:46Z'
extractor_version: 1.0.3
content_sha256: 846c955590ffe13dd8825d1775ffaf42c1c33299c59d4c968e3b0631c9bd1b1a
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
{_pb.RUNTIME_ENVIRONMENT_HEADING}\n\n{environment_hints}\n\n{_pb.RUNTIME_ENVIRONMENT_END}