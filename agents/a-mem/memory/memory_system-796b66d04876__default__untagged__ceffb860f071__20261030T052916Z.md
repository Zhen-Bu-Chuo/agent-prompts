---
agent: a-mem
prompt_id: memory_system-796b66d04876
module: memory
variant: default
upstream_repository: agiresearch/A-mem
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: ceffb860f0712bbae97b184d440df62bc910ca8d
source_path: agentic_memory/memory_system.py
source_symbol: module.AgenticMemorySystem.find_related_memories_raw.2
source_lines:
- 341
- 341
source_permalink: https://github.com/agiresearch/A-mem/blob/ceffb860f0712bbae97b184d440df62bc910ca8d/agentic_memory/memory_system.py#L341-L341
source_committed_at: '2025-12-12T21:15:29Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: f663b1b18fa36cb9386f64694280666ef1e28a140a66efda6d8a141d8db14445
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
talk start time:{neighbor.timestamp}\tmemory content: {neighbor.content}\tmemory context: {neighbor.context}\tmemory keywords: {str(neighbor.keywords)}\tmemory tags: {str(neighbor.tags)}\n