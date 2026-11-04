# Hindsight / Graphiti prompt and mechanism sources

- Repository: [`vectorize-io/hindsight`](https://github.com/vectorize-io/hindsight)
- Selected release/branch: `v1.2.0`
- Commit: `34a138684a899b6ec34175f7a2b633860466d289`
- SPDX metadata: `MIT`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `memory` | `python` | [`hindsight-api-slim/hindsight_api/engine/consolidation/prompts.py`](https://github.com/vectorize-io/hindsight/blob/34a138684a899b6ec34175f7a2b633860466d289/hindsight-api-slim/hindsight_api/engine/consolidation/prompts.py) |
| `reflection` | `python` | [`hindsight-api-slim/hindsight_api/engine/reflect/prompts.py`](https://github.com/vectorize-io/hindsight/blob/34a138684a899b6ec34175f7a2b633860466d289/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `v1.2.0` at commit `34a138684a899b6ec34175f7a2b633860466d289`.
- Graphiti/Hindsight 产品别名按用户附件记录；仓库实际为 Hindsight。采集 retain/recall/reflect pipeline 的自身提示词源码，不采集外部集成 Agent 内容。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- Graphiti/Hindsight 产品别名按用户附件记录；仓库实际为 Hindsight。采集 retain/recall/reflect pipeline 的自身提示词源码，不采集外部集成 Agent 内容。
