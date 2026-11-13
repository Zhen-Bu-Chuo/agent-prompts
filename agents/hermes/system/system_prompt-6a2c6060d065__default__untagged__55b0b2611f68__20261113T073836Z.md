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
source_commit: 55b0b2611f683a12450163b9fe423abbd61a9923
source_path: agent/system_prompt.py
source_symbol: module.build_system_prompt_parts.1
source_lines:
- 813
- 813
source_permalink: https://github.com/NousResearch/hermes-agent/blob/55b0b2611f683a12450163b9fe423abbd61a9923/agent/system_prompt.py#L813-L813
source_committed_at: '2026-11-13T07:28:14Z'
release_published_at: null
fetched_at: '2026-11-13T07:38:36Z'
extractor_version: 1.0.3
content_sha256: 846c955590ffe13dd8825d1775ffaf42c1c33299c59d4c968e3b0631c9bd1b1a
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
{_pb.RUNTIME_ENVIRONMENT_HEADING}\n\n{environment_hints}\n\n{_pb.RUNTIME_ENVIRONMENT_END}