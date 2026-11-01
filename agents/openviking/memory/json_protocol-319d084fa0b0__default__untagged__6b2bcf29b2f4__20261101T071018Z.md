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
source_commit: 6b2bcf29b2f4169b519dd96015b50adb3dca08f2
source_path: openviking/session/memory/extraction_output_protocol/json_protocol.py
source_symbol: module.JsonExtractionOutputProtocol.render_final_instruction.1
source_lines:
- 83
- 87
source_permalink: https://github.com/volcengine/OpenViking/blob/6b2bcf29b2f4169b519dd96015b50adb3dca08f2/openviking/session/memory/extraction_output_protocol/json_protocol.py#L83-L87
source_committed_at: '2026-11-01T04:54:11Z'
release_published_at: null
fetched_at: '2026-11-01T07:10:18Z'
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