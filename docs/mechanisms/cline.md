# Cline prompt and mechanism sources

- Repository: [`cline/cline`](https://github.com/cline/cline)
- Selected release/branch: `v4.1.26`
- Commit: `a459f1d04dea030833b558be645011ab739c463b`
- SPDX metadata: `Apache-2.0`
- Collection status: `partial`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `tools` | `js-strings` | [`apps/cli/src/connectors/adapters/prompts.ts`](https://github.com/cline/cline/blob/a459f1d04dea030833b558be645011ab739c463b/apps/cli/src/connectors/adapters/prompts.ts) |

## Current coverage

- Coverage: `partial`.
- Pinned upstream version: `v4.1.26` at commit `a459f1d04dea030833b558be645011ab739c463b`.
- 当前稳定 monorepo 可静态提取 connector adapter system prompt；子代理文件只接收上游传入的 prompt，主对话运行时 system prompt 在 VS Code 扩展中动态组装。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 当前稳定 monorepo 中可以静态核实子代理和 CLI adapter 模板；主对话运行时消息包含 VScode 扩展动态组装部分，未把 TUI 提示输入当作模型 system prompt。
