# Kami-inspired Operating Logic

本项目借鉴 Kami 的不是固定视觉风格，而是生成前后的运行纪律。`course-ppt-workflow` 仍然以“继承原有 PPT 模板并生成可编辑 PPTX”为核心。

## 8 个吸收点

1. **Contract first**
   - 先确定用途、受众、页数、模板、输出格式、是否需要校徽、是否需要图片。
   - 不在约束不清时直接排版。

2. **Intent extraction**
   - 提取 Purpose、Audience、Constraint、Success。
   - 对应到教学场景：课堂导入、论文精读、课程补充、组会汇报。

3. **Materials status**
   - 检查 PPT 模板、论文文本、图片/图表、校徽、输出目录和验证脚本是否可用。
   - 校徽优先从 `assets/logos/` 匹配，必要时从模板候选区域裁剪。

4. **Distill before compose**
   - 先从材料中提炼研究问题、核心概念、机制链条、证据和结论。
   - 不把论文摘要原文直接塞进 PPT。

5. **PPT pre-flight**
   - 生成前确认页数、页面类型、是否需要讨论题、是否使用课程模板或答辩模板。
   - 论文一般 2-4 页；组会精读可扩展到 5-8 页。

6. **Outline first**
   - 推荐先生成 PPT 大纲，明确每页标题、核心要点和逻辑关系，再进入模板化排版。

7. **Anti-pattern check**
   - 避免空泛总结、模板风格污染、文字超框、整页截图、课堂旁白和无机制链的摘要堆砌。

8. **Diagram choice**
   - 根据内容关系选择图示：机制链、对比表、路径图、时间线、风险传导链或四象限。

## 推荐运行链条

```text
材料输入 -> Contract -> Intent -> Materials -> Distill -> Outline -> Compose -> QA
```

## 三类默认输出

- **案例导入**：2-3 页，强调事实、冲突、概念连接和课堂讨论。
- **论文精读**：5-8 页，强调问题、结论、方法、机制、证据、风险和讨论。
- **课程补充/备课**：3-5 页，强调概念框架、流程机制、例题/案例和教学总结。

