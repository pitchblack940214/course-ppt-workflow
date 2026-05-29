"""Lightweight quality checks for generated PPTX teaching decks."""

from __future__ import annotations

import argparse
from pathlib import Path

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE


ANTI_PATTERNS = [
    "学生应理解",
    "学生应该理解",
    "课堂导入点",
    "我们可以看到",
    "这里可以输入",
    "写点小标题",
]


def validate(path: Path) -> int:
    prs = Presentation(str(path))
    width, height = prs.slide_width, prs.slide_height
    failures = 0
    print(f"file: {path}")
    print(f"slides: {len(prs.slides)}")

    for index, slide in enumerate(prs.slides, 1):
        pictures = 0
        out_of_bounds = []
        text = []
        for shape in slide.shapes:
            if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
                pictures += 1
            if getattr(shape, "has_text_frame", False) and shape.text.strip():
                text.append(shape.text.strip())
            if (
                shape.left < 0
                or shape.top < 0
                or shape.left + shape.width > width
                or shape.top + shape.height > height
            ):
                out_of_bounds.append(shape.name)

        joined = "\n".join(text)
        hits = [item for item in ANTI_PATTERNS if item in joined]
        failures += len(out_of_bounds) + len(hits)
        print(
            f"slide {index}: texts={len(text)}, pictures={pictures}, "
            f"out_of_bounds={len(out_of_bounds)}, anti_patterns={hits}"
        )
    return failures


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    args = parser.parse_args()
    raise SystemExit(1 if validate(args.pptx) else 0)


if __name__ == "__main__":
    main()

