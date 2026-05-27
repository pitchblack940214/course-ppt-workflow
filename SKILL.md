---
name: course-ppt-workflow
description: Create editable PowerPoint decks for lesson preparation, case briefings, and paper analysis from an existing PPT template; inherit the source deck style and prevent text overflow.
---

# Course PPT Workflow

Use this skill when creating editable PowerPoint teaching pages from an existing PPT template plus a case, article, paper, or teaching outline. It is designed for lecture preparation, case analysis, paper briefings, and graduate seminar presentations.

## Output Contract

- Create a standalone `.pptx`.
- For one paper, usually create 2-4 slides depending on content complexity; use 2 slides for short briefs and 3-4 slides for papers with richer theory, methods, findings, or implications.
- The deck must be editable: use text boxes, shapes, lines, arrows, and native PowerPoint elements.
- Do not use a full-slide screenshot or full-slide image as the slide.
- Preserve the source deck's visual grammar: slide size, dominant colors, title placement, footers, decorative bars, typography feel, and content density.
- All text and shapes must stay within slide bounds. No text may visibly overflow its frame or overlap another object.

## Workflow

1. Read the source course PPT.
   - Extract slide text to identify chapter topic, major concepts, key terms, and existing case wording.
   - Inspect sample slides or screenshots for aspect ratio, title style, palette, footer/decorative lines, card/list conventions, and density.
   - Identify reusable school or organization logos. Prefer the logo library when a known school is detected; otherwise inspect candidate regions such as top-left, top-right, bottom-left, bottom-right, header, and footer.

2. Build the teaching logic.
   - Slide 1: case introduction, key facts, mechanism or comparison.
   - Slide 2: course-concept explanation, process decomposition, risk boundary or policy implication.
   - For 3+ pages, use a progression such as definition -> practice -> risk/extension.

3. Text rules.
   - Present only points and logic.
   - Avoid classroom narration such as "students should understand", "classroom entry point", "we can see", or "this helps students".
   - Use compact labels and short phrases.
   - Prefer headings such as "case points", "mechanism", "transaction flow", "risk boundary", "policy implication".
   - If a sentence is too long for a small box, shorten the wording before reducing legibility.

4. Design rules.
   - Match the source template rather than inventing a new visual system.
   - Keep the layout lecture-like, not marketing-like.
   - Use the source deck's accent colors for titles, arrows, card headings, and bottom rules.
   - Use bold SimHei or another bold Heiti-style font for titles.
   - Use FangSong or SimSun for body text and logic-framework text unless the source deck clearly requires a different Chinese body font.
   - Reuse the source deck's school badge or organization logo when it is part of the template identity.
   - Leave safe margins around all content. For 16:9 slides, keep at least 0.25 in from edges and more near decorative footers.
   - If a card has more than two body lines, enlarge the card, reduce font size, or shorten the wording.

5. Validation gates.
   - Verify the output has the requested number of slides.
   - Verify picture object count matches the user's request.
   - Verify every object lies inside the slide canvas.
   - Manually reason about text fit: object bounds are not enough.
   - If overlap appears, repair the affected slide and rerun object-bound checks.
