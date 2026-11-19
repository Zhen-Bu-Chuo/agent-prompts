# Gemini CLI prompt and mechanism sources

- Repository: [`google-gemini/gemini-cli`](https://github.com/google-gemini/gemini-cli)
- Selected release/branch: `v0.69.0`
- Commit: `58840eb92ebf1474193a05817c34a74820bd444a`
- SPDX metadata: `Apache-2.0`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `context` | `js-strings` | [`packages/core/src/prompts/snippets.ts`](https://github.com/google-gemini/gemini-cli/blob/58840eb92ebf1474193a05817c34a74820bd444a/packages/core/src/prompts/snippets.ts) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `v0.69.0` at commit `58840eb92ebf1474193a05817c34a74820bd444a`.
- 按核心提示词模块筛选；项目/会话配置、用户规则、动态 MCP 工具清单和实际子代理消息取决于运行时。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 按核心提示词模块筛选；项目/会话配置、用户规则、动态 MCP 工具清单和实际子代理消息取决于运行时。
