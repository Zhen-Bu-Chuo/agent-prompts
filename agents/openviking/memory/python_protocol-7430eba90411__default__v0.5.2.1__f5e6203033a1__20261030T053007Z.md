---
agent: openviking
prompt_id: python_protocol-7430eba90411
module: memory
variant: default
upstream_repository: volcengine/OpenViking
upstream_version: v0.5.2.1
package_name: null
package_version: null
source_ref: v0.5.2.1
source_commit: f5e6203033a13469c3d9a937f2ca39492ea69c51
source_path: openviking/session/memory/extraction_output_protocol/python_protocol.py
source_symbol: module.PythonExtractionOutputProtocol.render_final_instruction.1
source_lines:
- 284
- 286
source_permalink: https://github.com/volcengine/OpenViking/blob/f5e6203033a13469c3d9a937f2ca39492ea69c51/openviking/session/memory/extraction_output_protocol/python_protocol.py#L284-L286
source_committed_at: '2026-10-27T13:40:45Z'
release_published_at: '2026-10-27T13:44:25Z'
fetched_at: '2026-10-30T05:30:07Z'
extractor_version: 1.0.3
content_sha256: b051d8f0f0b35a52c008a8d59f5b03e5440638bd6c0a58d46e3a7d96ee06de93
license: AGPL-3.0-only
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You have reached the maximum number of tool call iterations. Do not call any more tools. Return the complete restricted Python memory SDK program now. Output only Python code. If there are no changes, return only sdk.commit().