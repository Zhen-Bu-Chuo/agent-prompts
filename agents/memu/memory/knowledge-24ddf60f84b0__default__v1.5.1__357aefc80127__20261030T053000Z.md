---
agent: memu
prompt_id: knowledge-24ddf60f84b0
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/knowledge.py
source_symbol: module.PROMPT_BLOCK_RULES.1
source_lines:
- 64
- 92
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/knowledge.py#L64-L92
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: c34414fd3c7998f1743eec4197a0ec474061fc2fa87153669602c834b7575109
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Rules
## General requirements (must satisfy all)
- Each memory item must be complete and self-contained, written as a declarative descriptive sentence.
- Each memory item must express one single complete piece of information and be understandable without context.
- Similar/redundant items must be merged into one, and assigned to only one category.
- Each memory item must be < 50 words worth of length (keep it concise but include relevant details).
- Focus on factual knowledge, concepts, definitions, and explanations.
- Focus on objective information that can be learned or referenced.
Important: Extract only knowledge directly stated or discussed in the conversation. No guesses or unsupported extensions.

## Special rules for Knowledge Information
- Personal opinions, subjective preferences, or personal experiences are forbidden in Knowledge Information.
- Focus on objective facts, concepts, and explanations.
- User-specific traits, events, or behaviors are not knowledge items.

## Forbidden content
- Opinions or subjective statements without factual basis.
- Personal experiences or events (these belong to event type).
- User preferences or behavioral patterns (these belong to profile/behavior type).
- Trivial or commonly known facts that add no value.
- Illegal / harmful sensitive topics (violence, politics, drugs, etc.).
- Any content that is speculative or not clearly established in the conversation.

## Review & validation rules
- Merge similar items: keep only one and assign a single category.
- Resolve conflicts: keep the latest / most certain item.
- Final check: every item must comply with all extraction rules.
