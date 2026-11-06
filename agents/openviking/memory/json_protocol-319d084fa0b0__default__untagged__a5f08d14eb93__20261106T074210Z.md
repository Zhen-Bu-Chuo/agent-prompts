---
agent: openviking
prompt_id: json_protocol-319d084fa0b0
module: memory
variant: default
upstream_repository: volcengine/OpenViking
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: a5f08d14eb9305803402e6ab71b88a66bf897187
source_path: openviking/session/memory/extraction_output_protocol/json_protocol.py
source_symbol: module.JsonExtractionOutputProtocol.render_final_instruction.1
source_lines:
- 83
- 87
source_permalink: https://github.com/volcengine/OpenViking/blob/a5f08d14eb9305803402e6ab71b88a66bf897187/openviking/session/memory/extraction_output_protocol/json_protocol.py#L83-L87
source_committed_at: '2026-11-06T07:33:38Z'
release_published_at: null
fetched_at: '2026-11-06T07:42:10Z'
extractor_version: 1.0.3
content_sha256: 3aec7f65523cd66ae785ab98f0e7f5882ece8ef2870a1f88917b101a2dc235ab
license: AGPL-3.0-only
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
You have reached the maximum number of tool call iterations. "
            "Do not call any more tools. Return your final result now as ONLY a valid JSON object "
            "matching the required schema. Do not include explanations or markdown. "
            "If there are no memory changes, return this exact empty-shape JSON with all fields present:\n"
            f"{skeleton}