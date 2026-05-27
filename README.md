# AI Course PPT Workflow

一个面向高校课程备课的 AI 辅助 PPT 生成流程。它用于把课程 PPT、论文、案例或教学大纲转化为可编辑的教学补充页，并尽量继承原课程课件的色彩、字体、页脚和版式风格。

## 适用场景

- 论文导读与课堂案例梳理
- 章节知识点补充页
- 开放性课程论文选题说明
- 金融、国际贸易、数字经济等课程的课堂讲授材料
- 需要把大纲快速整理为可编辑 PPTX 的备课任务

## 核心原则

- 输出可编辑 PPTX，而不是整页截图。
- 标题使用黑体或黑体风格字体，并加粗。
- 正文、逻辑框架和说明文字使用仿宋或宋体。
- 继承课程 PPT 的主色调、标题位置、页脚线和讲义式密度。
- 所有文字、图形、图片必须在页面范围内。
- 真实课程 PPT、教材截图和论文 PDF 不应直接开源；示例应尽量脱敏或改写。

## 仓库结构

```text
.
├─ SKILL.md                         # 可复用的备课流程规则
├─ prompts/                         # 可直接复制给 AI 的提示词模板
├─ scripts/                         # PPT 生成、风格读取和版式检查脚本
├─ examples/                        # 示例大纲、案例解读 PPT、论文解读 PPT 与授权示例论文
├─ templates/                       # 可放置自定义课程模板
└─ docs/                            # 工作流、版权与隐私说明
```

## 快速开始

安装依赖：

```powershell
pip install -r requirements.txt
```

生成脱敏示例 PPT：

```powershell
python scripts/generate_ppt.py --outline examples/input_outline.md --output examples/output_sample.pptx
```

检查 PPT 是否有元素越界：

```powershell
python scripts/validate_ppt_bounds.py examples/output_sample.pptx
```

## 开源边界

本仓库建议开源：

- 备课流程、提示词、脚本和脱敏示例
- 论文题名、研究主题和课堂梳理框架
- 自行生成或无版权风险的示意图

不建议开源：

- 学校课程原始 PPT
- 论文 PDF 原文
- 教材截图、CNKI 下载文件、付费数据库材料
- 含学生信息、教师内部安排或学校内部标识的文件

若确认具有分享权限，也可以在 `examples/paper_briefs/` 中放置少量论文原文示例，并在目录说明中标注来源与用途。

## 许可证

本项目采用 MIT License。
