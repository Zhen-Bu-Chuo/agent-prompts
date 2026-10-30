---
agent: goose
prompt_id: session_name-f17d499deb0f
module: system
variant: default
upstream_repository: aaif-goose/goose
upstream_version: v1.57.0
package_name: null
package_version: null
source_ref: v1.57.0
source_commit: 30bba95105e59bc3e7df624cf6b4d433690cfe12
source_path: crates/goose/src/prompts/session_name.md
source_symbol: document
source_lines:
- 1
- 19
source_permalink: https://github.com/aaif-goose/goose/blob/30bba95105e59bc3e7df624cf6b4d433690cfe12/crates/goose/src/prompts/session_name.md#L1-L19
source_committed_at: '2026-10-27T17:47:18Z'
release_published_at: '2026-10-28T19:26:10Z'
fetched_at: '2026-10-30T05:29:38Z'
extractor_version: 1.0.3
content_sha256: 9a104ad7750b0a71884334a43349a17b1a542623536bba4dc287986b9ea6f43f
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Generate a short title (four words or less) for this conversation.

Title what the work is ABOUT, not the mechanical activity. Many conversations share the same workflow steps (creating a PR, setting up a worktree, drafting an email, summarizing a document); a good title carries the distinguishing subject instead — a ticket or issue ID, feature name, customer or company, person, document, event, or project.

Rules:
- If a ticket or issue identifier (like ABC-123) appears in the messages, include it in the title. Use identifiers found only in hints when the messages make their relevance clear.
- Prefer names of companies, projects, or documents over generic activity words.
- Prefer a company or project name over a person's name when both are present.
- If there is genuinely no distinguishing subject, a plain activity title is fine — never invent specifics that are not present.

Reply with only the title, nothing else. Do not show your reasoning.

Examples:
- "how do I reverse a list in python?" → Python list reversal
- "set up a git worktree for BOT-1565 session auto titles" → BOT-1565 session auto-titles
- "open the payments repo and create a PR for the refund timeout fix" → Refund timeout fix
- "help me draft a follow-up email about the renewal" (hints mention Acme) → Acme renewal follow-up
- "summarize this spreadsheet" (attached "Q3 pipeline.xlsx") → Q3 pipeline summary
- "what's the weather in Tokyo?" → Tokyo weather
