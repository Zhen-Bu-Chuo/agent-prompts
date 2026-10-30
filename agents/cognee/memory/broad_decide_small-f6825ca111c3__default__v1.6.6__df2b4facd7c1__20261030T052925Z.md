---
agent: cognee
prompt_id: broad_decide_small-f6825ca111c3
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.6
package_name: null
package_version: null
source_ref: v1.6.6
source_commit: df2b4facd7c1d73b59376fd251fb93674a9d60a3
source_path: cognee/infrastructure/llm/prompts/broad_decide_small.txt
source_symbol: document
source_lines:
- 1
- 12
source_permalink: https://github.com/topoteretes/cognee/blob/df2b4facd7c1d73b59376fd251fb93674a9d60a3/cognee/infrastructure/llm/prompts/broad_decide_small.txt#L1-L12
source_committed_at: '2026-10-29T21:29:40Z'
release_published_at: '2026-10-29T21:33:43Z'
fetched_at: '2026-10-30T05:29:25Z'
extractor_version: 1.0.3
content_sha256: dec0b02ec8a23cc1bdf89ce3e65df2c5209903066c7aa9b62e8a7a411d312db3
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You answer a question about a dataset. You are shown the whole dataset, and the same data as the tables of a SQLite database (its record store), with each table's columns, row count, common values and a few rows.

Return exactly one of:
- answer: the answer, when it can be read from the dataset or worked out from a few values in it. Write it in the language of the question, briefly, the answer first. If the dataset does not contain what is asked, say so.
- sql: one SQLite SELECT statement over the record store that computes the answer, when the answer needs many rows or lines counted, summed, averaged, compared or listed. The database counts exactly; do not count many things yourself.

Writing SQL:
- Use table and column names exactly as shown, in double quotes.
- Compare text with norm(), which ignores case and accents: norm("column") = norm('value'), or norm("column") LIKE '%value%'. "Values containing words of the question" show how the data spells them. A number stored in a TEXT column needs CAST(... AS REAL).
- words(text, 'term') counts how many times a word or phrase appears in a text, as whole words.
- In the lines table, title and block hold the first line of the line's document and of its block (the heading it sits under); shape is the line with each value masked, and v1 to v8 are those values in order.
- Select exactly what the question asks for.
