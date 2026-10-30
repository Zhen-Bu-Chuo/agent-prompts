# memU prompt and mechanism sources

- Repository: [`NevaMind-AI/memU`](https://github.com/NevaMind-AI/memU)
- Selected release/branch: `v1.5.1`
- Commit: `357aefc8012705bfde723f141d52f675fe712bed`
- SPDX metadata: `Apache-2.0`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `memory` | `python` | [`src/memu/prompts/category_patch/category.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/category_patch/category.py) |
| `memory` | `python` | [`src/memu/prompts/category_summary/category.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/category_summary/category.py) |
| `memory` | `python` | [`src/memu/prompts/category_summary/category_with_refs.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/category_summary/category_with_refs.py) |
| `memory` | `python` | [`src/memu/prompts/memory_type/behavior.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/behavior.py) |
| `memory` | `python` | [`src/memu/prompts/memory_type/event.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/event.py) |
| `memory` | `python` | [`src/memu/prompts/memory_type/knowledge.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/knowledge.py) |
| `memory` | `python` | [`src/memu/prompts/memory_type/profile.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/profile.py) |
| `memory` | `python` | [`src/memu/prompts/memory_type/skill.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/skill.py) |
| `memory` | `python` | [`src/memu/prompts/memory_type/tool.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/tool.py) |
| `memory` | `python` | [`src/memu/prompts/preprocess/audio.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/preprocess/audio.py) |
| `memory` | `python` | [`src/memu/prompts/preprocess/conversation.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/preprocess/conversation.py) |
| `memory` | `python` | [`src/memu/prompts/preprocess/document.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/preprocess/document.py) |
| `memory` | `python` | [`src/memu/prompts/preprocess/image.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/preprocess/image.py) |
| `memory` | `python` | [`src/memu/prompts/preprocess/video.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/preprocess/video.py) |
| `memory` | `python` | [`src/memu/prompts/retrieve/judger.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/retrieve/judger.py) |
| `memory` | `python` | [`src/memu/prompts/retrieve/llm_category_ranker.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/retrieve/llm_category_ranker.py) |
| `memory` | `python` | [`src/memu/prompts/retrieve/llm_item_ranker.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/retrieve/llm_item_ranker.py) |
| `memory` | `python` | [`src/memu/prompts/retrieve/llm_resource_ranker.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/retrieve/llm_resource_ranker.py) |
| `memory` | `python` | [`src/memu/prompts/retrieve/pre_retrieval_decision.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/retrieve/pre_retrieval_decision.py) |
| `memory` | `python` | [`src/memu/prompts/retrieve/query_rewriter.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/retrieve/query_rewriter.py) |
| `memory` | `python` | [`src/memu/prompts/retrieve/query_rewriter_judger.py`](https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/retrieve/query_rewriter_judger.py) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `v1.5.1` at commit `357aefc8012705bfde723f141d52f675fe712bed`.
- 按 v1.5.1 Apache-2.0 许可的源提示模块采集；跨 agent 的实际 memory 注入由 provider adaptor 在运行时决定。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 按 v1.5.1 Apache-2.0 许可的源提示模块采集；跨 agent 的实际 memory 注入由 provider adaptor 在运行时决定。
