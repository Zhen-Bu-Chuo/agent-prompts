# Mem0 prompt and mechanism sources

- Repository: [`mem0ai/mem0`](https://github.com/mem0ai/mem0)
- Selected release/branch: `v2.2.1`
- Commit: `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`
- SPDX metadata: `Apache-2.0`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `memory` | `python` | [`mem0/configs/prompts.py`](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/mem0/configs/prompts.py) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `v2.2.1` at commit `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`.
- 覆盖记忆事实抽取、合并和召回提示词常量；provider/model/system message 仍由运行时拼接。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 覆盖记忆事实抽取、合并和召回提示词常量；provider/model/system message 仍由运行时拼接。
