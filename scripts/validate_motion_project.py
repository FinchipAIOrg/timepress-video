#!/usr/bin/env python3
"""Validate a Timepress motion project folder.

This lightweight check catches common packaging and previewability mistakes
without requiring Node, browser automation, or video encoders.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


BANNED = [
    (r"Math\.random\s*\(", "Use deterministic values, not Math.random()."),
    (r"Date\.now\s*\(", "Use deterministic values, not Date.now()."),
    (r"repeat\s*:\s*-1", "Use finite GSAP repeats; repeat:-1 breaks capture."),
    (r"data-layer\s*=", "Use data-track-index, not data-layer."),
    (r"data-end\s*=", "Use data-duration, not data-end."),
    (r"<br\s*/?>", "Avoid forced line breaks; use layout and max-width."),
    (r"requestAnimationFrame\s*\(", "Do not construct capture-critical motion with requestAnimationFrame()."),
]

REQUIRED_HTML_SNIPPETS = [
    ("data-composition-id", "Missing composition id."),
    ("data-width=\"1920\"", "Expected 1920 width for the default 16:9 composition."),
    ("data-height=\"1080\"", "Expected 1080 height for the default 16:9 composition."),
    ("window.__timelines", "Missing timeline registration."),
    ("gsap.timeline({ paused: true", "GSAP timeline must be paused for capture."),
    ("<svg", "Expected inline SVG for the motion frame."),
]

REQUIRED_DESIGN_SNIPPETS = [
    ("Visual Preset", "DESIGN.md should name the selected visual preset."),
    ("3-second read", "DESIGN.md should define the intended quick read."),
    ("What NOT to Do", "DESIGN.md should include anti-patterns."),
]


def check_file(path: Path, label: str) -> str:
    if not path.exists():
        return f"missing {label}: {path}"
    if path.stat().st_size == 0:
        return f"empty {label}: {path}"
    return ""


def scan_patterns(text: str, patterns: list[tuple[str, str]]) -> list[str]:
    errors: list[str] = []
    for pattern, message in patterns:
        if re.search(pattern, text, flags=re.IGNORECASE):
            errors.append(message)
    return errors


def validate(project_dir: Path) -> list[str]:
    errors: list[str] = []
    index = project_dir / "index.html"
    design = project_dir / "DESIGN.md"

    for path, label in [(project_dir, "project directory"), (index, "index.html"), (design, "DESIGN.md")]:
        err = check_file(path, label)
        if err:
            errors.append(err)

    if not index.exists() or not design.exists():
        return errors

    html = index.read_text(encoding="utf-8")
    design_text = design.read_text(encoding="utf-8")

    for snippet, message in REQUIRED_HTML_SNIPPETS:
        if snippet not in html:
            errors.append(message)

    for snippet, message in REQUIRED_DESIGN_SNIPPETS:
        if snippet not in design_text:
            errors.append(message)

    errors.extend(scan_patterns(html, BANNED))

    label_count = len(re.findall(r"<text\b", html, flags=re.IGNORECASE))
    if label_count > 18:
        errors.append(f"Too many SVG text labels ({label_count}); keep Timepress motion frames sparse.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Timepress motion project.")
    parser.add_argument("project_dir", type=Path)
    args = parser.parse_args()

    errors = validate(args.project_dir.resolve())
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    print(f"Validated {args.project_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
