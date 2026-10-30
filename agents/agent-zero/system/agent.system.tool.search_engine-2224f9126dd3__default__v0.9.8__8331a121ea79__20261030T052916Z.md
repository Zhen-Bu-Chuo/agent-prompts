---
agent: agent-zero
prompt_id: agent.system.tool.search_engine-2224f9126dd3
module: system
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.tool.search_engine.md
source_symbol: document
source_lines:
- 1
- 16
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.tool.search_engine.md#L1-L16
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: 623c1d15e54992baf54ca5322354a76a2d13f7bf58629d5f3fbac9a586fea0a9
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
### search_engine:
provide query arg get search results
returns list urls titles descriptions
**Example usage**:
~~~json
{
    "thoughts": [
        "...",
    ],
    "headline": "Searching web for video content",
    "tool_name": "search_engine",
    "tool_args": {
        "query": "Video of...",
    }
}
~~~
