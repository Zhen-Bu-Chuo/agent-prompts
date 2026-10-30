---
agent: memu
prompt_id: event-199f444a5619
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/event.py
source_symbol: module.PROMPT_BLOCK_RULES.1
source_lines:
- 74
- 105
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/event.py#L74-L105
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 0b140d5b4f60c7d5152fb6e4eccb1d3d3ab5b49c9d75b1f9641fb155956333c6
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
- Each memory item must be < 50 words worth of length (keep it concise but include relevant details).
- Focus on specific events that happened at a particular time or period.
- Include relevant details such as time, location, and participants where available.
Important: Extract only events directly stated or confirmed by the user. No guesses, no suggestions, and no content introduced only by the assistant.
Important: Accurately reflect whether the subject is the user or someone around the user.

## Special rules for Event Information
- Behavioral patterns, habits, preferences, or factual knowledge are forbidden in Event Information.
- Focus on concrete happenings, activities, and experiences.
- Do not extract content that was obtained only through the model's follow-up questions unless the user shows strong proactive intent.

## Forbidden content
- Knowledge Q&A without a clear user event.
- Trivial daily activities unless significant (e.g., routine meals, commuting).
- Temporary, ephemeral situations that lack meaningful significance.
- Turns where the user did not respond and only the assistant spoke.
- Illegal / harmful sensitive topics (violence, politics, drugs, etc.).
- Private financial accounts, IDs, addresses, military/defense/government job details, precise street addresses—unless explicitly requested by the user (still avoid if not necessary).
- Any content mentioned only by the assistant and not explicitly confirmed by the user.

## Review & validation rules
- Merge similar items: keep only one and assign a single category.
- Resolve conflicts: keep the latest / most certain item.
- Final check: every item must comply with all extraction rules.
