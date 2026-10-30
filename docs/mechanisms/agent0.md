# Agent0 prompt and mechanism sources

- Repository: [`aiming-lab/Agent0`](https://github.com/aiming-lab/Agent0)
- Selected release/branch: `main`
- Commit: `f775b5101e62fe92976831adf4a21a38fcc0a767`
- SPDX metadata: `Apache-2.0`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `execution` | `raw` | [`Agent0-VL/scripts/prompt.txt`](https://github.com/aiming-lab/Agent0/blob/f775b5101e62fe92976831adf4a21a38fcc0a767/Agent0-VL/scripts/prompt.txt) |
| `evaluation`, `execution`, `reflection` | `python` | [`Agent0-VL/verl/prompts/agent0_templates.py`](https://github.com/aiming-lab/Agent0/blob/f775b5101e62fe92976831adf4a21a38fcc0a767/Agent0-VL/verl/prompts/agent0_templates.py) |
| `curriculum` | `python` | [`Agent0/curriculum_train/verl/utils/dataset.py`](https://github.com/aiming-lab/Agent0/blob/f775b5101e62fe92976831adf4a21a38fcc0a767/Agent0/curriculum_train/verl/utils/dataset.py) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `main` at commit `f775b5101e62fe92976831adf4a21a38fcc0a767`.
- 主要分支用于 commit pinned 快照；课程数据、PersonaHub 人设、模型反馈由训练运行时加载，提示源码归档不会运行训练。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 主要分支用于 commit pinned 快照；课程数据、PersonaHub 人设、模型反馈由训练运行时加载，提示源码归档不会运行训练。
