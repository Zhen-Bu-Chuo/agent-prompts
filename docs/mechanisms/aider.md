# Aider prompt and mechanism sources

- Repository: [`Aider-AI/aider`](https://github.com/Aider-AI/aider)
- Selected release/branch: `v0.86.0`
- Commit: `a4be6ccd87ebaa59b361f3f028d116ce1761b626`
- SPDX metadata: `Apache-2.0`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `planning` | `python` | [`aider/coders/architect_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/architect_prompts.py) |
| `modes` | `python` | [`aider/coders/ask_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/ask_prompts.py) |
| `context` | `python` | [`aider/coders/base_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/base_prompts.py) |
| `context` | `python` | [`aider/coders/context_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/context_prompts.py) |
| `editing` | `python` | [`aider/coders/editblock_fenced_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/editblock_fenced_prompts.py) |
| `editing` | `python` | [`aider/coders/editblock_func_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/editblock_func_prompts.py) |
| `editing` | `python` | [`aider/coders/editblock_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/editblock_prompts.py) |
| `editing` | `python` | [`aider/coders/editor_editblock_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/editor_editblock_prompts.py) |
| `editing` | `python` | [`aider/coders/editor_whole_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/editor_whole_prompts.py) |
| `modes` | `python` | [`aider/coders/help_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/help_prompts.py) |
| `editing` | `python` | [`aider/coders/patch_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/patch_prompts.py) |
| `editing` | `python` | [`aider/coders/single_wholefile_func_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/single_wholefile_func_prompts.py) |
| `editing` | `python` | [`aider/coders/udiff_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/udiff_prompts.py) |
| `editing` | `python` | [`aider/coders/udiff_simple_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/udiff_simple_prompts.py) |
| `editing` | `python` | [`aider/coders/wholefile_func_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/wholefile_func_prompts.py) |
| `editing` | `python` | [`aider/coders/wholefile_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/wholefile_prompts.py) |
| `execution`, `memory` | `python` | [`aider/prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/prompts.py) |
| `modes` | `python` | [`aider/watch_prompts.py`](https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/watch_prompts.py) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `v0.86.0` at commit `a4be6ccd87ebaa59b361f3f028d116ce1761b626`.
- 按最新稳定发布 v0.86.0 的 coder 模式采集；不把主分支新改动视为稳定版。
- 静态保留 Python format/f-string 占位；模型参数、仓库地图、聊天记录、被编辑文件和运行时测试结果由程序另行注入。
- editor_diff_fenced_prompts.py 仅继承其他提示类且无独立长文本；继承来源已覆盖。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 按最新稳定发布 v0.86.0 的 coder 模式采集；不把主分支新改动视为稳定版。
- 静态保留 Python format/f-string 占位；模型参数、仓库地图、聊天记录、被编辑文件和运行时测试结果由程序另行注入。
- editor_diff_fenced_prompts.py 仅继承其他提示类且无独立长文本；继承来源已覆盖。
