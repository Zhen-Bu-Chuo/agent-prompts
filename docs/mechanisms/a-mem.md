# A-MEM prompt and mechanism sources

- Repository: [`agiresearch/A-mem`](https://github.com/agiresearch/A-mem)
- Selected release/branch: `main`
- Commit: `ceffb860f0712bbae97b184d440df62bc910ca8d`
- SPDX metadata: `MIT`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `memory` | `python` | [`agentic_memory/memory_system.py`](https://github.com/agiresearch/A-mem/blob/ceffb860f0712bbae97b184d440df62bc910ca8d/agentic_memory/memory_system.py) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `main` at commit `ceffb860f0712bbae97b184d440df62bc910ca8d`.
- 仓库无稳定 release，使用 main 固定提交；只提取记忆演化与元数据分析模板，不重建运行时向量、关系网络或模型输出。llm_controller 只转发调用方传入的提示词，不含静态提示词模板。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 仓库无稳定 release，使用 main 固定提交；只提取记忆构造的静态模板，不重建运行时向量、关系网络或模型输出。
