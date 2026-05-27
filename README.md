# Course PPT Workflow

> A reusable workflow for turning course slides, paper briefs, teaching cases,
> and lecture outlines into editable PowerPoint teaching materials.

Course PPT Workflow is a small open-source teaching toolkit for instructors who
prepare Chinese university lectures with AI assistance. It keeps the workflow
close to real classroom use: inherit the visual style of an existing course
deck, compress papers or cases into teachable logic, generate editable `.pptx`
slides, and validate that slide objects stay inside the page.

本项目用于沉淀一套可复用的高校备课 PPT 流程：根据课程原有 PPT 的色彩、字体、标题位置和页脚风格，将论文、案例或教学大纲整理为可编辑的课堂讲授页，并通过脚本检查版式边界。

## Installation

Clone the repository:

```powershell
git clone https://github.com/pitchblack940214/course-ppt-workflow.git
cd course-ppt-workflow
```

Install the Python dependencies:

```powershell
pip install -r requirements.txt
```

Generate the sample deck:

```powershell
python scripts/generate_ppt.py --outline examples/input_outline.md --output examples/output_sample.pptx
```

Validate slide bounds:

```powershell
python scripts/validate_ppt_bounds.py examples/output_sample.pptx
```

## Workflow Index

### `course-ppt-case-brief`

**What it does**

Creates editable PowerPoint teaching supplements from a course deck plus a case,
article, paper, or lecture outline.

**Typical use cases**

- Convert a research paper into two teaching slides.
- Explain a case through concepts from the course PPT.
- Turn a lecture outline into a compact 2-4 page supplement.
- Prepare assignment instructions or course-paper topics in the same visual style as the course deck.

**Key rules**

- Output editable `.pptx`, not full-slide screenshots.
- Inherit the source course deck's color palette, title placement, footer line, and teaching density.
- Use bold SimHei or Heiti-style fonts for titles.
- Use FangSong or SimSun for body text and logic-framework text.
- Keep every text box, shape, line, arrow, and image inside the slide canvas.
- Avoid classroom narration such as "students should understand"; show points and logic directly.

**Reference files**

- [`SKILL.md`](SKILL.md)
- [`prompts/course_ppt_case_brief.md`](prompts/course_ppt_case_brief.md)
- [`prompts/outline_to_teaching_slides.md`](prompts/outline_to_teaching_slides.md)

### `ppt-layout-validation`

**What it does**

Checks whether a generated `.pptx` has objects outside the slide canvas and
summarizes text and picture counts per slide.

**Key rules**

- Run after every generated deck.
- Treat object-bound checks as a first pass; manual visual review is still needed for text overflow.
- Use picture counts to confirm whether a page is image-assisted or fully text/shape based.

**Reference files**

- [`scripts/validate_ppt_bounds.py`](scripts/validate_ppt_bounds.py)

### `style-extraction`

**What it does**

Prints a lightweight style summary from a course PPT, including slide size,
common fonts, font sizes, and font colors.

**Key rules**

- Use it before generating a deck from a new course template.
- Do not upload private course PPTs unless you have permission.
- Use the extracted style as a guide, not as a replacement for manual visual judgment.

**Reference files**

- [`scripts/extract_style_from_ppt.py`](scripts/extract_style_from_ppt.py)

## Examples

This repository includes small examples for showing the workflow.

| Folder | Content |
| --- | --- |
| [`examples/case_briefs`](examples/case_briefs) | Case-brief PPT examples |
| [`examples/paper_briefs`](examples/paper_briefs) | Paper-brief PPT examples and selected source material |
| [`examples/input_outline.md`](examples/input_outline.md) | A public outline used by the sample generator |
| [`examples/output_sample.pptx`](examples/output_sample.pptx) | A generated editable sample deck |

## Repository Layout

```text
.
├─ SKILL.md
├─ prompts/
├─ scripts/
├─ examples/
│  ├─ case_briefs/
│  └─ paper_briefs/
├─ templates/
├─ docs/
├─ requirements.txt
└─ README.md
```

## Privacy and Copyright

The repository is designed to open-source the workflow, not private teaching
materials.

Recommended to share:

- Workflow rules and prompt templates.
- Scripts for generating and validating slides.
- Desensitized teaching outlines and example PPTs.
- Paper titles, research themes, and classroom explanation frameworks.
- Source PDFs only when sharing is permitted.

Avoid sharing:

- Private course PPTs from a university or department.
- Textbook screenshots or scanned chapters.
- Paid database downloads without permission.
- Files containing student information, internal teaching arrangements, or non-public school identifiers.

See [`docs/privacy_and_copyright.md`](docs/privacy_and_copyright.md) for the full note.

## License

MIT License.
