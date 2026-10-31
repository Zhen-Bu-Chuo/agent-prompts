---
agent: openviking
prompt_id: python_protocol-7430eba90411
module: memory
variant: default
upstream_repository: volcengine/OpenViking
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 3dedecc0d4827624eba7e583a81c36e9c326872b
source_path: openviking/session/memory/extraction_output_protocol/python_protocol.py
source_symbol: module.PythonExtractionOutputProtocol.render_final_instruction.1
source_lines:
- 284
- 286
source_permalink: https://github.com/volcengine/OpenViking/blob/3dedecc0d4827624eba7e583a81c36e9c326872b/openviking/session/memory/extraction_output_protocol/python_protocol.py#L284-L286
source_committed_at: '2026-10-31T05:46:41Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:38Z'
extractor_version: 1.0.3
content_sha256: b051d8f0f0b35a52c008a8d59f5b03e5440638bd6c0a58d46e3a7d96ee06de93
license: AGPL-3.0-only
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You have reached the maximum number of tool call iterations. Do not call any more tools. Return the complete restricted Python memory SDK program now. Output only Python code. If there are no changes, return only sdk.commit().