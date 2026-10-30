# Voyager prompt and mechanism sources

- Repository: [`MineDojo/Voyager`](https://github.com/MineDojo/Voyager)
- Selected release/branch: `main`
- Commit: `55e45a880755d0c8c66ca7fb5fe7962ac8974f89`
- SPDX metadata: `MIT`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `execution` | `raw` | [`voyager/prompts/action_response_format.txt`](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/action_response_format.txt) |
| `execution` | `raw` | [`voyager/prompts/action_template.txt`](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/action_template.txt) |
| `execution`, `reflection` | `raw` | [`voyager/prompts/critic.txt`](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/critic.txt) |
| `curriculum`, `execution` | `raw` | [`voyager/prompts/curriculum.txt`](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/curriculum.txt) |
| `curriculum`, `execution` | `raw` | [`voyager/prompts/curriculum_qa_step1_ask_questions.txt`](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/curriculum_qa_step1_ask_questions.txt) |
| `curriculum`, `execution` | `raw` | [`voyager/prompts/curriculum_qa_step2_answer_questions.txt`](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/curriculum_qa_step2_answer_questions.txt) |
| `curriculum`, `execution` | `raw` | [`voyager/prompts/curriculum_task_decomposition.txt`](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/curriculum_task_decomposition.txt) |
| `execution`, `skills` | `raw` | [`voyager/prompts/skill.txt`](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/skill.txt) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `main` at commit `55e45a880755d0c8c66ca7fb5fe7962ac8974f89`.
- 上游没有 stable release；使用 main commit 固定。本仓库作为 Agent 技能从经验生成和复用机制的研究样本；示例技能程序不采集为提示词。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 上游没有 stable release；使用 main commit 固定。本仓库作为 Agent 技能从经验生成和复用机制的研究样本；示例技能程序不采集为提示词。
