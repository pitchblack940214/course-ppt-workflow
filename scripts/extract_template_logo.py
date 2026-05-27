"""Extract a reusable logo badge from a PPT template.

Some PPT templates do not store the school or brand logo as a standalone image.
The logo may be composed of shapes, text boxes, and vector elements. This script
keeps a practical fallback: export one representative slide to PNG and crop the
logo area from a configurable candidate region.

Windows + PowerPoint is required for the slide export step.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image


PRESET_CROPS = {
    "top-right": (1010, 35, 1215, 115),
    "top-left": (35, 35, 270, 125),
    "bottom-right": (980, 600, 1235, 700),
    "bottom-left": (35, 600, 310, 700),
    "header": (0, 0, 1280, 150),
    "footer": (0, 570, 1280, 720),
}


def export_slide_with_powerpoint(pptx: Path, slide_index: int, output_png: Path) -> None:
    try:
        import win32com.client  # type: ignore
    except Exception as exc:  # pragma: no cover - depends on local Windows env
        raise RuntimeError("PowerPoint COM export requires pywin32 on Windows.") from exc

    app = win32com.client.Dispatch("PowerPoint.Application")
    presentation = app.Presentations.Open(str(pptx), True, False, False)
    try:
        presentation.Slides.Item(slide_index).Export(str(output_png), "PNG", 1280, 720)
    finally:
        presentation.Close()
        app.Quit()


def crop_logo(source_png: Path, output_png: Path, crop_box: tuple[int, int, int, int]) -> None:
    image = Image.open(source_png).convert("RGBA")
    image.crop(crop_box).save(output_png)


def resolve_crop_box(crop: str) -> tuple[int, int, int, int]:
    if crop in PRESET_CROPS:
        return PRESET_CROPS[crop]
    crop_box = tuple(int(part.strip()) for part in crop.split(","))
    if len(crop_box) != 4:
        raise ValueError("--crop must be a preset name or four comma-separated integers.")
    return crop_box


def copy_from_logo_library(query: str, output_png: Path) -> bool:
    repo_root = Path(__file__).resolve().parents[1]
    logo_dir = repo_root / "assets" / "logos"
    manifest = logo_dir / "manifest.json"
    if not query or not manifest.exists():
        return False

    records = json.loads(manifest.read_text(encoding="utf-8"))
    normalized = query.lower()
    for record in records:
        haystack = " ".join(
            str(record.get(key, ""))
            for key in ["id", "name", "school", "school_en", "notes"]
        ).lower()
        if normalized in haystack or any(part and part in haystack for part in normalized.split()):
            source = logo_dir / record["file"]
            output_png.parent.mkdir(parents=True, exist_ok=True)
            output_png.write_bytes(source.read_bytes())
            return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("template_pptx", type=Path)
    parser.add_argument("--school", help="School or organization name for logo-library lookup.")
    parser.add_argument("--slide", type=int, default=8, help="Representative slide number to export.")
    parser.add_argument("--output", type=Path, required=True, help="Output logo PNG path.")
    parser.add_argument(
        "--crop",
        default="top-right",
        help=(
            "Logo crop preset or exported 1280x720 coordinates. "
            "Presets: top-right, top-left, bottom-right, bottom-left, header, footer."
        ),
    )
    parser.add_argument("--keep-preview", type=Path, help="Optional exported slide preview path.")
    args = parser.parse_args()

    crop_box = resolve_crop_box(args.crop)

    if args.school and copy_from_logo_library(args.school, args.output):
        print(args.output)
        return

    preview = args.keep_preview or args.output.with_name(args.output.stem + "_slide_preview.png")
    export_slide_with_powerpoint(args.template_pptx.resolve(), args.slide, preview.resolve())
    crop_logo(preview, args.output, crop_box)  # type: ignore[arg-type]
    if args.keep_preview is None:
        preview.unlink(missing_ok=True)
    print(args.output)


if __name__ == "__main__":
    main()
