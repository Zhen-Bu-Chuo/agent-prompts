---
agent: memu
prompt_id: profile-f138676be16f
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/profile.py
source_symbol: module.PROMPT_BLOCK_RULES.1
source_lines:
- 73
- 102
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/profile.py#L73-L102
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 60b2688206772c0343916c566b5c6234dee550ac8278b32ffc6cfd327a9ae248
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Rules
## General requirements (must satisfy all)
- Use "user" to refer to the user consistently.
- Each memory item must be complete and self-contained, written as a declarative descriptive sentence.
- Each memory item must express one single complete piece of information and be understandable without context.
- Similar/redundant items must be merged into one, and assigned to only one category.
- Each memory item must be < 30 words worth of length (keep it as concise as possible).
- A single memory item must NOT contain timestamps.
Important: Extract only facts directly stated or confirmed by the user. No guesses, no suggestions, and no content introduced only by the assistant.
Important: Accurately reflect whether the subject is the user or someone around the user.
Important: Do not record temporary/one-off situational information; focus on meaningful, persistent information.

## Special rules for User Information
- Any event-related item is forbidden in User Information.
- Do not extract content that was obtained only through the model's follow-up questions unless the user shows strong proactive intent.

## Forbidden content
- Knowledge Q&A without a clear user fact.
- Trivial updates that do not add meaningful value (e.g., “full → too full”).
- Turns where the user did not respond and only the assistant spoke.
- Illegal / harmful sensitive topics (violence, politics, drugs, etc.).
- Private financial accounts, IDs, addresses, military/defense/government job details, precise street addresses—unless explicitly requested by the user (still avoid if not necessary).
- Any content mentioned only by the assistant and not explicitly confirmed by the user.

## Review & validation rules
- Merge similar items: keep only one and assign a single category.
- Resolve conflicts: keep the latest / most certain item.
- Final check: every item must comply with all extraction rules.
