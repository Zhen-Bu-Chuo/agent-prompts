# Graphiti prompt and mechanism sources

- Repository: [`getzep/graphiti`](https://github.com/getzep/graphiti)
- Selected release/branch: `v0.31.2`
- Commit: `d72407dcedac911e1be9fc15b55e8c05a3efcc36`
- SPDX metadata: `Apache-2.0`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `memory` | `python` | [`graphiti_core/prompts/eval.py`](https://github.com/getzep/graphiti/blob/d72407dcedac911e1be9fc15b55e8c05a3efcc36/graphiti_core/prompts/eval.py) |
| `memory` | `python` | [`graphiti_core/prompts/extract_nodes.py`](https://github.com/getzep/graphiti/blob/d72407dcedac911e1be9fc15b55e8c05a3efcc36/graphiti_core/prompts/extract_nodes.py) |
| `memory` | `python` | [`graphiti_core/prompts/extract_nodes_and_edges.py`](https://github.com/getzep/graphiti/blob/d72407dcedac911e1be9fc15b55e8c05a3efcc36/graphiti_core/prompts/extract_nodes_and_edges.py) |
| `memory` | `python` | [`graphiti_core/prompts/lib.py`](https://github.com/getzep/graphiti/blob/d72407dcedac911e1be9fc15b55e8c05a3efcc36/graphiti_core/prompts/lib.py) |
| `memory` | `python` | [`graphiti_core/prompts/snippets.py`](https://github.com/getzep/graphiti/blob/d72407dcedac911e1be9fc15b55e8c05a3efcc36/graphiti_core/prompts/snippets.py) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `v0.31.2` at commit `d72407dcedac911e1be9fc15b55e8c05a3efcc36`.
- 只归档源码中被 prompt module 引用的实体抽取、关系判定、去重和摘要模板；运行态 Episode 与实体索引作为数据上下文，不写入提示词归档。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 只归档源码中被 prompt module 引用的实体抽取、关系判定、去重和摘要模板；运行态 Episode 与实体索引作为数据上下文，不写入提示词归档。
