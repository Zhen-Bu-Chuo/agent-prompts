# EvoMap Evolver prompt and mechanism sources

- Repository: [`EvoMap/evolver`](https://github.com/EvoMap/evolver)
- Selected release/branch: `v2.0.49`
- Commit: `2986e59400b8b33084e4bf1d5a94fffc2c2d97f0`
- SPDX metadata: `GPL-3.0-or-later`
- Collection status: `partial`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `evolution` | `js-strings` | [`packages/evolver-core/dist/exec/prompt.js`](https://github.com/EvoMap/evolver/blob/2986e59400b8b33084e4bf1d5a94fffc2c2d97f0/packages/evolver-core/dist/exec/prompt.js) |

## Current coverage

- Coverage: `partial`.
- Pinned upstream version: `v2.0.49` at commit `2986e59400b8b33084e4bf1d5a94fffc2c2d97f0`.
- v2.0.46 只提供 transpiled dist 源码；README 标注 GPL-3.0-or-later，没有独立根 LICENSE 文件。保留 README license 声明与源码链接。
- personality/prompt.js 已混淆并排除；exec/prompt.js 中仅保存静态可读字符串片段，标记为片段而非重建完整运行时 prompt。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- v2.0.46 只提供 transpiled dist 源码；README 标注 GPL-3.0-or-later，没有独立根 LICENSE 文件。保留 README license 声明与源码链接。
- personality/prompt.js 已混淆并排除；exec/prompt.js 中仅保存静态可读字符串片段，标记为片段而非重建完整运行时 prompt。
