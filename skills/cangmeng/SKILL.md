---
name: cangmeng
description: cangmeng 公开基础版：统一选择极简纸张海报、pulp 印刷海报和授权 PNG 的来源元数据清理；其他照片艺术、文化视觉及照片书流程通过用户本机合法安装的扩展接入。用户提到 cangmeng、苍梦或这些视觉任务时使用。不要把尚未安装的扩展宣称为内置能力。
---

# cangmeng · 公开基础版

根据用户当前用途选择一个流程，仅执行该阶段。这个包包含两份 MIT 海报指南与一个新增的有限范围 PNG 工具；完整的 11 模块私人整合包不随仓库分发。

## 内置流程

- 旧纸、大留白、微型主体、极简 Zine：完整读取 `modules/minimal-zine/guide.md` 后执行。原技能名为 `gc-minimal-zine-poster-v0-1`。
- 高饱和背景、硬边、金黄色粗标题、pulp 印刷海报：完整读取 `modules/pulp-print/guide.md` 后执行。原技能名为 `neil-quentin`。
- 用户自有或获授权 PNG 的 AI 来源元数据：先用 `scripts/png_provenance.py identify <input.png>` 识别，再用 `clean <input.png> --output <new.png> --report <new.json>` 输出新文件。脚本相对本技能目录定位，解释器使用实际可用 Python。它只处理 C2PA caBX 与明确标记的 AI 来源文本块，保留像素与色彩块；拒绝覆盖。不得声称清除了所有隐形水印或证明图片不是 AI 生成。其他格式与可见水印需要对应扩展或工具，不改扩展名冒充完成。

## 可选本地扩展

用户提到下列任务时，运行 `<python> scripts/list_extensions.py --json`，或在用户指定的技能根目录使用 `--root <directory>`。它仅检查已知目录，不联网、不下载、不复制其他技能。

| 需求 | 查找的原技能目录 |
|---|---|
| 情绪抽象、不留原照的 Zine | scene-distillation-zine-v1-3 |
| 水彩、丝网、墨洗、版画、表现性绘画 | scene-to-art-lab |
| CRT、复古窗口、像素界面 | tait-crt-interface-skill |
| 文化器物、纹样、视觉基因、品牌视觉 | culture-fragment-poster-engine |
| 可交互照片书 | create-photo-flipbook-ui |
| 瓷器碎片拼合 | xxd-panel-224 |
| 稚拙民艺叙事 | xxd-panel-100 |
| 等距纸上微缩 | xxd-panel-028 |
| PNG 以外或可见 AI 标记清理 | remove-ai-watermarks |

已找到时，完整读取返回的原技能 `SKILL.md`，并遵守它的许可、前置条件和引用资料。其相对路径从原技能目录解析；不要复制到本仓库或重新授权。安装在本机不等于允许商用、专业用途或再分发。尤其 scene-to-art-lab 的个人非商用限制仍适用。

未找到时，说明该功能是尚未安装的可选扩展，给出已核实的上游链接或请用户提供来源。不要虚构已安装、自动下载授权不明内容，或用另一种风格冒充所请求模块。

## 图像工具与素材

生图或改图前，从用户请求及会话中确认 Image2 API 或内置 image_gen 的选择。没有选择时先问一次；同一批沿用选择，不暗中切换。只做元数据处理、检查扩展或浏览说明时无需生图选择。

对现有照片先查看原图。用所选图像工具完成栅格创作，项目资产另存到用户指定目录或当前项目。输出数量、比例、文字、原照是否保留及重试次数按当前指南和用户要求；不把一个模块的规则强加给另一个模块。不要拿示例或旧输出代替本次用户素材。

只处理用户拥有或获授权的素材，清理功能不移除摄影师署名、版权水印或商标。需要整图重生成的操作不属于普通元数据清理，需单独说明并取得同意。

## 署名与能力边界

原有两份指南署名和 MIT 许可分别保留在模块目录。cangmeng 的整合工作是统一入口、本地扩展发现、使用说明与 PNG 工具；不声称所有上游流程由整合者原创。读取本技能内置的 `references/third-party-notices.md` 了解来源和许可；原许可随模块保存。仓库中的 `PUBLICATION_PLAN.md` 另有公开版与私人版的差异说明，它不构成运行时依赖。
