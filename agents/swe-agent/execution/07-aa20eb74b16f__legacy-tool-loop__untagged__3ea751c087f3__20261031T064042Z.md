---
agent: swe-agent
prompt_id: 07-aa20eb74b16f
module: execution
variant: legacy-tool-loop
upstream_repository: SWE-agent/SWE-agent
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 3ea751c087f32b16e039a2233dd6eefecef325d5
source_path: config/sweagent_0_7/07.yaml
source_symbol: agent.templates.next_step_template
source_lines:
- 1
- 102
source_permalink: https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/config/sweagent_0_7/07.yaml#L1-L102
source_committed_at: '2026-07-16T15:21:18Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:42Z'
extractor_version: 1.0.3
content_sha256: 925ac99fc65c929c64b949eba9d2b89280842fe5e12ebde9e2afc2a871642de8
license: MIT
source_kind: structured_template
extraction_notes: Value selected from a structured configuration; line range cites the complete file.
---
{{observation}}
(Open file: {{open_file}})
(Current directory: {{working_dir}})
bash-$