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
source_commit: 21ae0e1238fdf466fa52a85a6ebf75d6899e49da
source_path: agent/system_prompt.py
source_symbol: module.build_system_prompt_parts.1
source_lines:
- 806
- 806
source_permalink: https://github.com/NousResearch/hermes-agent/blob/21ae0e1238fdf466fa52a85a6ebf75d6899e49da/agent/system_prompt.py#L806-L806
source_committed_at: '2026-11-08T03:38:20Z'
release_published_at: null
fetched_at: '2026-11-08T06:56:29Z'
extractor_version: 1.0.3
content_sha256: 846c955590ffe13dd8825d1775ffaf42c1c33299c59d4c968e3b0631c9bd1b1a
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
{_pb.RUNTIME_ENVIRONMENT_HEADING}\n\n{environment_hints}\n\n{_pb.RUNTIME_ENVIRONMENT_END}