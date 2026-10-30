---
agent: cognee
prompt_id: broad_decide_large-7666730e716d
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.6
package_name: null
package_version: null
source_ref: v1.6.6
source_commit: df2b4facd7c1d73b59376fd251fb93674a9d60a3
source_path: cognee/infrastructure/llm/prompts/broad_decide_large.txt
source_symbol: document
source_lines:
- 1
- 14
source_permalink: https://github.com/topoteretes/cognee/blob/df2b4facd7c1d73b59376fd251fb93674a9d60a3/cognee/infrastructure/llm/prompts/broad_decide_large.txt#L1-L14
source_committed_at: '2026-10-29T21:29:40Z'
release_published_at: '2026-10-29T21:33:43Z'
fetched_at: '2026-10-30T05:29:25Z'
extractor_version: 1.0.3
content_sha256: f7a9c015e82857c941a096c8b4a91701e1012f9875871349716070fd5c55a02c
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You answer a question about a dataset that is too large to show. You are shown its record store: the tables of a SQLite database holding all of its data, with each table's columns, row count, common values and a few rows.

Return exactly one of sql or needs_reading, plus search_queries:
- sql: one SQLite SELECT statement over the record store that computes the answer, when the answer is a count, total, list or lookup that matching words or values can express. The database reads every row and counts exactly.
- needs_reading: true when the answer depends on what the text means: what happened, who did what, why, how something is described. A query matches words; it cannot tell what a passage says. Then write no sql.
- search_queries: always. Two or three short phrasings of the passage that would answer the question, worded as the text itself might word it (names, events, objects; no question words). They choose the parts of the text that are read.

Writing SQL:
- Use table and column names exactly as shown, in double quotes.
- Compare text with norm(), which ignores case and accents: norm("column") = norm('value'), or norm("column") LIKE '%value%'. "Values containing words of the question" show how the data spells them. A number stored in a TEXT column needs CAST(... AS REAL).
- words(text, 'term') counts how many times a word or phrase appears in a text, as whole words.
- In the lines table, title and block hold the first line of the line's document and of its block (the heading it sits under); shape is the line with each value masked, and v1 to v8 are those values in order. A line's wording can be matched with LIKE on norm(text) or on shape.
- "Start of document", "Heading-like lines" and "Short lines that appear more than once" show how the text is laid out. Match headings by their exact wording. A heading listed twice is usually a table of contents plus the heading itself: count distinct headings, or the ones after the table of contents.
- Select exactly what the question asks for.
