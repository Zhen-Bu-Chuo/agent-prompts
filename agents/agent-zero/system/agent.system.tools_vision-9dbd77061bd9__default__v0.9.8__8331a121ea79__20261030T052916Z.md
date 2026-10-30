---
agent: agent-zero
prompt_id: agent.system.tools_vision-9dbd77061bd9
module: system
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.tools_vision.md
source_symbol: document
source_lines:
- 1
- 21
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.tools_vision.md#L1-L21
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: b356931e6995df25454e2dfce7eabb80a6356255c74f180304ce83981256d27e
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
## "Multimodal (Vision) Agent Tools" available:

### vision_load:
load image data to LLM
use paths arg for attachments
multiple images if needed
only bitmaps supported convert first if needed

**Example usage**:
```json
{
    "thoughts": [
        "I need to see the image...",
    ],
    "headline": "Loading image for visual analysis",
    "tool_name": "vision_load",
    "tool_args": {
        "paths": ["/path/to/image.png"],
    }
}
```
