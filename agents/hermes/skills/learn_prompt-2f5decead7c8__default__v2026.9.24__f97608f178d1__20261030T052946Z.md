---
agent: hermes
prompt_id: learn_prompt-2f5decead7c8
module: skills
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: v2026.9.24
package_name: null
package_version: null
source_ref: v2026.9.24
source_commit: f97608f178d1ffeca59860195ab7da295f7c8e5f
source_path: agent/learn_prompt.py
source_symbol: module.build_learn_prompt.1
source_lines:
- 145
- 196
source_permalink: https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/learn_prompt.py#L145-L196
source_committed_at: '2026-09-24T10:08:47Z'
release_published_at: '2026-09-24T10:09:38Z'
fetched_at: '2026-10-30T05:29:46Z'
extractor_version: 1.0.3
content_sha256: 612a4562879e644a26edcb406be3b264f5df4c0a348e020b3a7cd146ed6e4886
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
[/learn] The user wants you to learn a reusable skill from the "
        "request below, and save it.\n\n"
        f"THE REQUEST:\n{req}\n\n"
        "The request is open-ended and may mix two kinds of content, in any "
        "order: SOURCES to gather (directories, file paths, URLs, \"what we "
        "just did\", pasted notes) AND REQUIREMENTS that shape the skill "
        "(what to focus on, what to leave out, scope, naming, the angle to "
        "take). Treat EVERY part of the request as load-bearing. In "
        "particular, prose that comes after a path or link is NOT incidental "
        "— it is the user telling you what they want from that source. A "
        "request like `<url> focus on the auth flow, skip the deprecated "
        "endpoints` means: gather the URL AND honor \"focus on auth, skip "
        "deprecated\" as authoring requirements. Never fetch the first source "
        "and ignore the rest.\n\n"
        "Do this:\n"
        "1. Inventory every source the user named, using the tools you already "
        "have — `read_file`/`search_files` for local files or directories, "
        "`web_extract` for URLs, the current conversation history if they "
        "referred to something you just did, and the text they pasted as-is. "
        "Gather a small source now. For a large source, inspect enough to map "
        "its chapters or major topics, but do not load the whole corpus into "
        "conversation context; process it incrementally in step 2b. "
        "If the request is ambiguous about scope, make a reasonable choice "
        "and note it; do not stall.\n"
        "1b. Apply every requirement, focus, and constraint in the request to "
        "the skill you author — these govern what the SKILL.md covers and "
        "emphasizes, not just which sources you read.\n"
        "2. Save the skill with `skill_manage`. First check the available "
        "skills for one covering this source or topic. If one exists, load it "
        "with `skill_view`, then extend its SKILL.md with `skill_manage` patch "
        "(or edit for a necessary full rewrite) and add or update supporting "
        "files with `skill_manage` write_file. Only when no matching skill "
        "exists, create one with `skill_manage` action=\"create\" and pick a "
        "sensible category. If the procedure needs a non-trivial script, add "
        "it under the skill's `scripts/` with `skill_manage` write_file and "
        "reference it by relative path.\n"
        "2b. Pick the shape by the source, not by habit: a workflow or small "
        "source gets ONE tight SKILL.md; a book, paper stack, spec, or large "
        "docs corpus gets the knowledge-base layout below — a lean SKILL.md "
        "index plus per-chapter `references/` files added with `skill_manage` "
        "write_file. If a single SKILL.md would force you to summarize away "
        "most of the material, that is the signal to go expansive. For this "
        "layout, create or load the skill after inventorying the source, then "
        "read, distill, and persist one chapter/topic at a time before reading "
        "the next; finish by reconciling the SKILL.md index with every "
        "reference file you wrote.\n\n"
        f"{_SOURCE_HYGIENE}\n\n"
        f"{_AUTHORING_STANDARDS}\n\n"
        f"{_KNOWLEDGE_SKILL_STANDARDS}\n\n"
        "When done, tell the user the skill name, its category, a one-line "
        "summary of what it captured, and — for a knowledge-base skill — the "
        "list of reference files it can load on demand.