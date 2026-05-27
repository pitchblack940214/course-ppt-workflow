# Logo Library

本目录存放可复用的学校或机构标识素材，用于在生成 PPT 时更稳定地识别和复用模板中的校徽。

## 已收录

- `sichuan_university_badge_red.png`：四川大学红底校徽组合。

## 使用逻辑

1. 优先根据模板文字、学校名称或用户指定学校，在 `manifest.json` 中查找已有校徽。
2. 如果校徽库没有匹配项，再从模板典型页眉区域识别或裁剪。
3. 如果模板中的校徽不是独立图片，而是由形状和文字组成，可以导出代表性幻灯片后裁剪候选区域。
4. 候选区域不固定为页眉右上角，也可能在左上角、右下角、左下角、页眉横条或页脚横条。

脚本支持的候选区域包括：

- `top-right`
- `top-left`
- `bottom-right`
- `bottom-left`
- `header`
- `footer`

也可以手动传入 `left,top,right,bottom` 坐标。
