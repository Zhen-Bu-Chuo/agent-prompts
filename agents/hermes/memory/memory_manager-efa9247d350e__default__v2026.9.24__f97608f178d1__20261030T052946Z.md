---
agent: hermes
prompt_id: memory_manager-efa9247d350e
module: memory
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: v2026.9.24
package_name: null
package_version: null
source_ref: v2026.9.24
source_commit: f97608f178d1ffeca59860195ab7da295f7c8e5f
source_path: agent/memory_manager.py
source_symbol: module.build_memory_context_block.1
source_lines:
- 327
- 332
source_permalink: https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/memory_manager.py#L327-L332
source_committed_at: '2026-09-24T10:08:47Z'
release_published_at: '2026-09-24T10:09:38Z'
fetched_at: '2026-10-30T05:29:46Z'
extractor_version: 1.0.3
content_sha256: 80de5c51c2b2f9e7842c3876a5557efe523828caf729525eb1fe3acb2c4b6893
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
<memory-context>\n"
        "[System note: The following is recalled memory context, "
        "NOT new user input. Treat as authoritative reference data — "
        "this is the agent's persistent memory and should inform all responses.]\n\n"
        f"{clean}\n"
        "</memory-context>