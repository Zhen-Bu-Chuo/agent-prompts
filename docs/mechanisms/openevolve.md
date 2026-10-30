# OpenEvolve prompt and mechanism sources

- Repository: [`algorithmicsuperintelligence/openevolve`](https://github.com/algorithmicsuperintelligence/openevolve)
- Selected release/branch: `v0.4.0`
- Commit: `f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c`
- SPDX metadata: `Apache-2.0`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `evolution` | `raw` | [`openevolve/prompts/defaults/diff_user.txt`](https://github.com/algorithmicsuperintelligence/openevolve/blob/f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c/openevolve/prompts/defaults/diff_user.txt) |
| `evolution` | `raw` | [`openevolve/prompts/defaults/evaluation.txt`](https://github.com/algorithmicsuperintelligence/openevolve/blob/f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c/openevolve/prompts/defaults/evaluation.txt) |
| `evolution` | `raw` | [`openevolve/prompts/defaults/evaluator_system_message.txt`](https://github.com/algorithmicsuperintelligence/openevolve/blob/f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c/openevolve/prompts/defaults/evaluator_system_message.txt) |
| `evolution` | `raw` | [`openevolve/prompts/defaults/evolution_history.txt`](https://github.com/algorithmicsuperintelligence/openevolve/blob/f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c/openevolve/prompts/defaults/evolution_history.txt) |
| `evolution` | `raw` | [`openevolve/prompts/defaults/full_rewrite_user.txt`](https://github.com/algorithmicsuperintelligence/openevolve/blob/f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c/openevolve/prompts/defaults/full_rewrite_user.txt) |
| `evolution` | `raw` | [`openevolve/prompts/defaults/inspiration_program.txt`](https://github.com/algorithmicsuperintelligence/openevolve/blob/f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c/openevolve/prompts/defaults/inspiration_program.txt) |
| `evolution` | `raw` | [`openevolve/prompts/defaults/inspirations_section.txt`](https://github.com/algorithmicsuperintelligence/openevolve/blob/f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c/openevolve/prompts/defaults/inspirations_section.txt) |
| `evolution` | `raw` | [`openevolve/prompts/defaults/previous_attempt.txt`](https://github.com/algorithmicsuperintelligence/openevolve/blob/f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c/openevolve/prompts/defaults/previous_attempt.txt) |
| `evolution` | `raw` | [`openevolve/prompts/defaults/system_message.txt`](https://github.com/algorithmicsuperintelligence/openevolve/blob/f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c/openevolve/prompts/defaults/system_message.txt) |
| `evolution` | `raw` | [`openevolve/prompts/defaults/system_message_changes_description.txt`](https://github.com/algorithmicsuperintelligence/openevolve/blob/f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c/openevolve/prompts/defaults/system_message_changes_description.txt) |
| `evolution` | `raw` | [`openevolve/prompts/defaults/system_message_with_changes_description.txt`](https://github.com/algorithmicsuperintelligence/openevolve/blob/f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c/openevolve/prompts/defaults/system_message_with_changes_description.txt) |
| `evolution` | `raw` | [`openevolve/prompts/defaults/top_program.txt`](https://github.com/algorithmicsuperintelligence/openevolve/blob/f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c/openevolve/prompts/defaults/top_program.txt) |
| `evolution` | `raw` | [`openevolve/prompts/defaults/user_message_with_changes_description.txt`](https://github.com/algorithmicsuperintelligence/openevolve/blob/f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c/openevolve/prompts/defaults/user_message_with_changes_description.txt) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `v0.4.0` at commit `f7b633986c0b3dbd0a171f6eb0cb0f0ba4fdfb0c`.
- 静态归档候选程序生成、差异描述、历史、评价器和变异提示；实验程序、评估分数和选择状态由上游运行时动态维护。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 静态归档候选程序生成、差异描述、历史、评价器和变异提示；实验程序、评估分数和选择状态由上游运行时动态维护。
