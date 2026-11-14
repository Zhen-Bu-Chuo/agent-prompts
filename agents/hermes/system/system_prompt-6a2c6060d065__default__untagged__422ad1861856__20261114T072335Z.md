---
agent: hermes
prompt_id: system_prompt-6a2c6060d065
module: system
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 422ad1861856dd9b80b947fbad9f39d1580f6b41
source_path: agent/system_prompt.py
source_symbol: module.build_system_prompt_parts.1
source_lines:
- 813
- 813
source_permalink: https://github.com/NousResearch/hermes-agent/blob/422ad1861856dd9b80b947fbad9f39d1580f6b41/agent/system_prompt.py#L813-L813
source_committed_at: '2026-11-14T03:48:17Z'
release_published_at: null
fetched_at: '2026-11-14T07:23:35Z'
extractor_version: 1.0.3
content_sha256: 846c955590ffe13dd8825d1775ffaf42c1c33299c59d4c968e3b0631c9bd1b1a
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
{_pb.RUNTIME_ENVIRONMENT_HEADING}\n\n{environment_hints}\n\n{_pb.RUNTIME_ENVIRONMENT_END}