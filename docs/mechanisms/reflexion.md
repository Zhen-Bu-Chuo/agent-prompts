# Reflexion prompt and mechanism sources

- Repository: [`noahshinn/reflexion`](https://github.com/noahshinn/reflexion)
- Selected release/branch: `main`
- Commit: `218cf0ef1df84b05ce379dd4a8e47f17766733a0`
- SPDX metadata: `MIT`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `reflection` | `python` | [`hotpotqa_runs/prompts.py`](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/prompts.py) |
| `system` | `raw` | [`webshop_runs/base_prompt.txt`](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/base_prompt.txt) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `main` at commit `218cf0ef1df84b05ce379dd4a8e47f17766733a0`.
- 研究代码库没有带版本发布，按 main commit 固定；此实现是论文/实验框架并含 benchmark few-shot 例子。记录专用反思模板与执行基准，不把实验日志当作 prompt。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 研究代码库没有带版本发布，按 main commit 固定；此实现是论文/实验框架并含 benchmark few-shot 例子。记录专用反思模板与执行基准，不把实验日志当作 prompt。
