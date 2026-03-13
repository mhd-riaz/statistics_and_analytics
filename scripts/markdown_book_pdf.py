#!/Users/riaz/miniconda3/bin/python

from __future__ import annotations

import argparse
import glob
import html
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import mistune
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4, LETTER
from reportlab.lib.styles import ParagraphStyle, StyleSheet1, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents


PAGE_SIZES = {
    "a4": A4,
    "letter": LETTER,
}

INLINE_CODE_RE = re.compile(r"`([^`]+)`")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
ITALIC_RE = re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)")

UNICODE_MONO_FONT_NAME = "Courier"
UNICODE_TEXT_FONT_NAME = "Helvetica"

GREEK_MAP = {
    "alpha": "α",
    "beta": "β",
    "gamma": "γ",
    "delta": "δ",
    "epsilon": "ε",
    "theta": "θ",
    "lambda": "λ",
    "mu": "μ",
    "nu": "ν",
    "pi": "π",
    "sigma": "σ",
    "phi": "φ",
    "psi": "ψ",
    "omega": "ω",
    "Gamma": "Γ",
    "Delta": "Δ",
    "Theta": "Θ",
    "Lambda": "Λ",
    "Pi": "Π",
    "Sigma": "Σ",
    "Phi": "Φ",
    "Psi": "Ψ",
    "Omega": "Ω",
}

COMMAND_MAP = {
    "cdot": "·",
    "times": "×",
    "pm": "±",
    "mp": "∓",
    "le": "≤",
    "leq": "≤",
    "ge": "≥",
    "geq": "≥",
    "neq": "≠",
    "approx": "≈",
    "to": "→",
    "infty": "∞",
    "nabla": "∇",
    "partial": "∂",
    "in": "∈",
    "cup": "∪",
    "cap": "∩",
    "emptyset": "∅",
    "sum": "Σ",
    "prod": "Π",
    "int": "∫",
    "min": "min",
    "max": "max",
}

SUPERSCRIPT_MAP = str.maketrans({
    "0": "⁰",
    "1": "¹",
    "2": "²",
    "3": "³",
    "4": "⁴",
    "5": "⁵",
    "6": "⁶",
    "7": "⁷",
    "8": "⁸",
    "9": "⁹",
    "+": "⁺",
    "-": "⁻",
    "=": "⁼",
    "(": "⁽",
    ")": "⁾",
    "n": "ⁿ",
    "i": "ⁱ",
    "x": "ˣ",
})

SUBSCRIPT_MAP = str.maketrans({
    "0": "₀",
    "1": "₁",
    "2": "₂",
    "3": "₃",
    "4": "₄",
    "5": "₅",
    "6": "₆",
    "7": "₇",
    "8": "₈",
    "9": "₉",
    "+": "₊",
    "-": "₋",
    "=": "₌",
    "(": "₍",
    ")": "₎",
    "a": "ₐ",
    "e": "ₑ",
    "h": "ₕ",
    "i": "ᵢ",
    "j": "ⱼ",
    "k": "ₖ",
    "l": "ₗ",
    "m": "ₘ",
    "n": "ₙ",
    "o": "ₒ",
    "p": "ₚ",
    "r": "ᵣ",
    "s": "ₛ",
    "t": "ₜ",
    "u": "ᵤ",
    "v": "ᵥ",
    "x": "ₓ",
})


@dataclass(frozen=True)
class Chapter:
    path: Path
    title: str
    text: str


class BookDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, book_title: str, **kwargs):
        super().__init__(filename, **kwargs)
        self.book_title = book_title
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="main")
        template = PageTemplate(id="book", frames=[frame], onPage=self._draw_header_footer)
        self.addPageTemplates([template])

    def afterFlowable(self, flowable):
        style_name = getattr(getattr(flowable, "style", None), "name", "")
        if style_name in {"Heading1", "Heading2", "Heading3", "ChapterTitle"}:
            level_map = {
                "ChapterTitle": 0,
                "Heading1": 0,
                "Heading2": 1,
                "Heading3": 2,
            }
            self.notify("TOCEntry", (level_map[style_name], flowable.getPlainText(), self.page))

    def _draw_header_footer(self, canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 9)
        canvas.setFillColor(colors.HexColor("#666666"))
        if doc.page > 1:
            canvas.drawString(doc.leftMargin, doc.pagesize[1] - 0.5 * inch, self.book_title)
        canvas.drawCentredString(doc.pagesize[0] / 2.0, 0.45 * inch, f"Page {doc.page}")
        canvas.restoreState()


def register_unicode_mono_font() -> str:
    candidates = [
        ("BookMono", "/System/Library/Fonts/SFNSMono.ttf"),
        ("BookMono", "/System/Library/Fonts/Supplemental/PTMono.ttc"),
        ("BookMono", "/System/Library/Fonts/Supplemental/Andale Mono.ttf"),
        ("BookMono", "/System/Library/Fonts/Supplemental/Courier New.ttf"),
    ]

    for font_name, font_path in candidates:
        try:
            pdfmetrics.registerFont(TTFont(font_name, font_path))
            return font_name
        except Exception:
            continue
    return "Courier"


def register_unicode_text_font() -> str:
    candidates = [
        ("BookSans", "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"),
        ("BookSans", "/Library/Fonts/Arial Unicode.ttf"),
    ]

    for font_name, font_path in candidates:
        try:
            pdfmetrics.registerFont(TTFont(font_name, font_path))
            return font_name
        except Exception:
            continue
    return "Helvetica"


UNICODE_MONO_FONT_NAME = register_unicode_mono_font()
UNICODE_TEXT_FONT_NAME = register_unicode_text_font()


def translate_script_letter(content: str) -> str:
    letters = {
        "F": "ℱ",
    }
    return letters.get(content, content)


def unicode_script(text: str, mapping: dict[int, str], fallback_prefix: str) -> str:
    if text and all(ord(char) in mapping for char in text):
        return text.translate(mapping)
    return f"{fallback_prefix}{{{text}}}"


def replace_latex_command(text: str, command: str, replacement: str) -> str:
    return re.sub(rf"\\{command}(?![A-Za-z])", replacement, text)


def extract_braced_content(text: str, start_index: int) -> tuple[str, int] | None:
    if start_index >= len(text) or text[start_index] != "{":
        return None

    depth = 0
    collected: list[str] = []
    for index in range(start_index, len(text)):
        char = text[index]
        if char == "{":
            depth += 1
            if depth > 1:
                collected.append(char)
            continue
        if char == "}":
            depth -= 1
            if depth == 0:
                return ("".join(collected), index + 1)
            collected.append(char)
            continue
        collected.append(char)
    return None


def replace_latex_function(text: str, command: str, arg_count: int, transform) -> str:
    marker = f"\\{command}"
    index = 0
    pieces: list[str] = []

    while index < len(text):
        next_index = text.find(marker, index)
        if next_index == -1:
            pieces.append(text[index:])
            break

        pieces.append(text[index:next_index])
        cursor = next_index + len(marker)
        args: list[str] = []
        ok = True
        for _ in range(arg_count):
            while cursor < len(text) and text[cursor].isspace():
                cursor += 1
            extracted = extract_braced_content(text, cursor)
            if extracted is None:
                ok = False
                break
            arg_text, cursor = extracted
            args.append(arg_text)

        if not ok:
            pieces.append(marker)
            index = next_index + len(marker)
            continue

        pieces.append(transform(*args))
        index = cursor

    return "".join(pieces)


def normalize_math_whitespace(text: str, block: bool) -> str:
    text = text.replace("\\left", "").replace("\\right", "")
    text = text.replace("\\,", " ").replace("\\;", " ").replace("\\!", "")
    text = text.replace("\\quad", "  ").replace("\\qquad", "    ")
    if block:
        text = text.replace("\\\\", "\n")
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n\s+", "\n", text)
    else:
        text = text.replace("\\\\", " ; ")
        text = re.sub(r"\s+", " ", text)
    return text.strip()


def latex_to_readable_math(text: str, *, block: bool = False) -> str:
    math_text = text.strip().strip("$")

    cases_pattern = re.compile(r"\\begin\{cases\}(.*?)\\end\{cases\}", re.DOTALL)
    while True:
        updated = cases_pattern.sub(
            lambda match: "cases: " + " ; ".join(
                latex_to_readable_math(part.replace("&", " ").strip(), block=False)
                for part in match.group(1).split("\\\\")
                if part.strip()
            ),
            math_text,
        )
        if updated == math_text:
            break
        math_text = updated

    math_text = replace_latex_function(math_text, "text", 1, lambda inner: inner)
    math_text = replace_latex_function(math_text, "operatorname", 1, lambda inner: inner)
    math_text = replace_latex_function(math_text, "mathrm", 1, lambda inner: inner)
    math_text = replace_latex_function(math_text, "mathbf", 1, lambda inner: inner)
    math_text = replace_latex_function(math_text, "mathbb", 1, lambda inner: inner)
    math_text = replace_latex_function(math_text, "mathcal", 1, translate_script_letter)
    math_text = replace_latex_function(math_text, "boxed", 1, lambda inner: f"[ {latex_to_readable_math(inner, block=False)} ]")
    math_text = replace_latex_function(math_text, "bar", 1, lambda inner: f"{latex_to_readable_math(inner, block=False)}̄")
    math_text = replace_latex_function(math_text, "hat", 1, lambda inner: f"{latex_to_readable_math(inner, block=False)}̂")
    math_text = replace_latex_function(
        math_text,
        "frac",
        2,
        lambda numerator, denominator: f"({latex_to_readable_math(numerator, block=False)})/({latex_to_readable_math(denominator, block=False)})",
    )
    math_text = replace_latex_function(
        math_text,
        "binom",
        2,
        lambda upper, lower: f"C({latex_to_readable_math(upper, block=False)}, {latex_to_readable_math(lower, block=False)})",
    )
    math_text = replace_latex_function(
        math_text,
        "sqrt",
        1,
        lambda inner: f"√({latex_to_readable_math(inner, block=False)})",
    )

    for command, glyph in {**GREEK_MAP, **COMMAND_MAP}.items():
        math_text = replace_latex_command(math_text, command, glyph)

    math_text = re.sub(
        r"_\{([^{}]+)\}",
        lambda match: unicode_script(latex_to_readable_math(match.group(1), block=False), SUBSCRIPT_MAP, "_"),
        math_text,
    )
    math_text = re.sub(
        r"\^\{([^{}]+)\}",
        lambda match: unicode_script(latex_to_readable_math(match.group(1), block=False), SUPERSCRIPT_MAP, "^"),
        math_text,
    )
    math_text = re.sub(
        r"_([A-Za-z0-9()+\-=])",
        lambda match: unicode_script(match.group(1), SUBSCRIPT_MAP, "_"),
        math_text,
    )
    math_text = re.sub(
        r"\^([A-Za-z0-9()+\-=])",
        lambda match: unicode_script(match.group(1), SUPERSCRIPT_MAP, "^"),
        math_text,
    )
    math_text = re.sub(r"\\([A-Za-z]+)", lambda match: match.group(1), math_text)
    return normalize_math_whitespace(math_text, block)


def build_styles() -> StyleSheet1:
    styles = getSampleStyleSheet()
    styles["Title"].fontName = "Helvetica-Bold"
    styles["Title"].fontSize = 24
    styles["Title"].leading = 30
    styles["Title"].alignment = TA_CENTER
    styles["Title"].spaceAfter = 18

    styles["Heading1"].fontName = "Helvetica-Bold"
    styles["Heading1"].fontSize = 18
    styles["Heading1"].leading = 22
    styles["Heading1"].spaceBefore = 16
    styles["Heading1"].spaceAfter = 8

    styles["Heading2"].fontName = "Helvetica-Bold"
    styles["Heading2"].fontSize = 14
    styles["Heading2"].leading = 18
    styles["Heading2"].spaceBefore = 12
    styles["Heading2"].spaceAfter = 6

    styles["Heading3"].fontName = "Helvetica-Bold"
    styles["Heading3"].fontSize = 12
    styles["Heading3"].leading = 15
    styles["Heading3"].spaceBefore = 10
    styles["Heading3"].spaceAfter = 4

    styles.add(
        ParagraphStyle(
            name="ChapterTitle",
            parent=styles["Heading1"],
            fontSize=22,
            leading=28,
            spaceBefore=0,
            spaceAfter=12,
            alignment=TA_CENTER,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SourcePath",
            parent=styles["Italic"],
            fontName="Helvetica-Oblique",
            fontSize=9,
            textColor=colors.HexColor("#666666"),
            alignment=TA_CENTER,
            spaceAfter=18,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyBook",
            parent=styles["BodyText"],
            fontName="Times-Roman",
            fontSize=11,
            leading=15,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ExampleTitle",
            parent=styles["BodyBook"],
            fontName="Helvetica-Bold",
            fontSize=11.5,
            leading=15,
            spaceBefore=10,
            spaceAfter=6,
            textColor=colors.HexColor("#1F3B57"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="GivenLabel",
            parent=styles["BodyBook"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=13,
            spaceBefore=4,
            spaceAfter=4,
            textColor=colors.HexColor("#444444"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="Quote",
            parent=styles["BodyBook"],
            leftIndent=18,
            rightIndent=12,
            textColor=colors.HexColor("#444444"),
            borderPadding=6,
            borderWidth=0.4,
            borderColor=colors.HexColor("#D4D4D4"),
            borderLeft=True,
            spaceBefore=2,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ListItem",
            parent=styles["BodyBook"],
            leftIndent=18,
            firstLineIndent=0,
            bulletIndent=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CodeBlock",
            parent=styles["Code"],
            fontName=UNICODE_MONO_FONT_NAME,
            fontSize=8.5,
            leading=11,
            leftIndent=0,
            rightIndent=0,
            spaceBefore=0,
            spaceAfter=0,
        )
    )
    styles.add(
        ParagraphStyle(
            name="MathBlock",
            parent=styles["CodeBlock"],
            fontName=UNICODE_TEXT_FONT_NAME,
            fontSize=10,
            leading=13,
        )
    )
    styles.add(
        ParagraphStyle(
            name="TOCHeading",
            parent=styles["Heading1"],
            alignment=TA_CENTER,
        )
    )
    return styles


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a readable PDF book from Markdown files and directories."
    )
    parser.add_argument("inputs", nargs="+", help="Markdown files, directories, or glob patterns.")
    parser.add_argument("-o", "--output", required=True, help="Output PDF path.")
    parser.add_argument("--title", help="Book title shown on the cover and header.")
    parser.add_argument("--author", default="Markdown Book Generator", help="Author metadata.")
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Glob pattern to exclude. Repeatable.",
    )
    parser.add_argument(
        "--page-size",
        choices=sorted(PAGE_SIZES),
        default="a4",
        help="PDF page size.",
    )
    parser.add_argument(
        "--margin",
        type=float,
        default=0.75,
        help="Page margin in inches.",
    )
    return parser.parse_args(argv)


def expand_inputs(raw_inputs: Iterable[str], excludes: Iterable[str]) -> list[Path]:
    collected: list[Path] = []
    seen: set[Path] = set()
    exclude_patterns = list(excludes)
    saw_directory_input = False

    for raw in raw_inputs:
        matches = [Path(match) for match in sorted(glob.glob(raw, recursive=True))] if any(ch in raw for ch in "*?[]") else []
        candidates = matches or [Path(raw)]
        for candidate in candidates:
            if candidate.is_dir():
                saw_directory_input = True
                paths = ordered_markdown_files_for_directory(candidate)
            elif candidate.is_file() and candidate.suffix.lower() == ".md":
                paths = [candidate]
            else:
                continue
            for path in paths:
                normalized = workspace_relative(path)
                resolved = normalized.resolve()
                if resolved in seen or is_excluded(normalized, exclude_patterns):
                    continue
                seen.add(resolved)
                collected.append(normalized)

    if saw_directory_input:
        collected = prepend_root_readme(collected, seen, exclude_patterns)
    return collected


def prepend_root_readme(paths: list[Path], seen: set[Path], exclude_patterns: list[str]) -> list[Path]:
    root_readme = Path.cwd() / "README.md"
    if not root_readme.is_file():
        return paths

    normalized = workspace_relative(root_readme)
    resolved = normalized.resolve()
    if resolved in seen or is_excluded(normalized, exclude_patterns):
        return paths

    seen.add(resolved)
    return [normalized, *paths]


def ordered_markdown_files_for_directory(directory: Path) -> list[Path]:
    all_paths = sorted((path for path in directory.rglob("*.md") if path.is_file()), key=sort_key)
    ordering: list[Path] = []

    for anchor_name in ("index.md", "README.md", "readme.md"):
        anchor = directory / anchor_name
        if not anchor.is_file():
            continue
        ordering.append(anchor)
        ordering.extend(linked_markdown_paths(anchor))
        break

    seen: set[Path] = set()
    ordered_unique: list[Path] = []
    for path in ordering + all_paths:
        resolved = path.resolve()
        if resolved in seen or not path.is_file() or path.suffix.lower() != ".md":
            continue
        if directory.resolve() not in resolved.parents and resolved != directory.resolve():
            continue
        seen.add(resolved)
        ordered_unique.append(path)
    return ordered_unique


def linked_markdown_paths(markdown_file: Path) -> list[Path]:
    text = markdown_file.read_text(encoding="utf-8")
    linked_paths: list[Path] = []
    for target in re.findall(r"\[[^\]]+\]\(([^)#]+\.md)\)", text, flags=re.IGNORECASE):
        resolved = (markdown_file.parent / target).resolve()
        if resolved.is_file():
            linked_paths.append(workspace_relative(resolved))
    return linked_paths


def workspace_relative(path: Path) -> Path:
    resolved = path.resolve()
    try:
        return resolved.relative_to(Path.cwd().resolve())
    except ValueError:
        return resolved


def is_excluded(path: Path, patterns: list[str]) -> bool:
    path_text = path.as_posix()
    return any(path.match(pattern) or path_text.endswith(pattern) for pattern in patterns)


def sort_key(path: Path) -> tuple[str, int, str]:
    lower_name = path.name.lower()
    priority = 1
    if lower_name in {"readme.md", "index.md"}:
        priority = 0
    return (path.parent.as_posix(), priority, lower_name)


def normalize_title(text: str) -> str:
    cleaned = re.sub(r"\s+", " ", text).strip()
    return cleaned or "Untitled"


def chapter_title_from_markdown(path: Path, text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return normalize_title(stripped.lstrip("# "))
    return normalize_title(path.stem.replace("-", " ").replace("_", " ").title())


def build_chapters(paths: list[Path]) -> list[Chapter]:
    chapters: list[Chapter] = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        chapters.append(Chapter(path=path, title=chapter_title_from_markdown(path, text), text=text))
    return chapters


def build_book(output_path: Path, title: str, author: str, chapters: list[Chapter], page_size: str, margin: float):
    styles = build_styles()
    parser = mistune.create_markdown(renderer="ast", plugins=["table", "math"])
    output_path.parent.mkdir(parents=True, exist_ok=True)

    doc = BookDocTemplate(
        str(output_path),
        book_title=title,
        pagesize=PAGE_SIZES[page_size],
        leftMargin=margin * inch,
        rightMargin=margin * inch,
        topMargin=margin * inch,
        bottomMargin=margin * inch,
        title=title,
        author=author,
    )

    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(name="TOCLevel1", fontName="Helvetica", fontSize=11, leading=14, leftIndent=12, firstLineIndent=-12, spaceBefore=4),
        ParagraphStyle(name="TOCLevel2", fontName="Helvetica", fontSize=10, leading=12, leftIndent=28, firstLineIndent=-10, textColor=colors.HexColor("#555555")),
        ParagraphStyle(name="TOCLevel3", fontName="Helvetica", fontSize=9, leading=11, leftIndent=42, firstLineIndent=-10, textColor=colors.HexColor("#777777")),
    ]

    story = build_front_matter(styles, title, author, chapters, toc)
    for index, chapter in enumerate(chapters):
        if index > 0:
            story.append(PageBreak())
        story.extend(chapter_to_flowables(chapter, parser, styles))

    doc.build(story)


def build_front_matter(styles: StyleSheet1, title: str, author: str, chapters: list[Chapter], toc: TableOfContents):
    story = [Spacer(1, 1.2 * inch)]
    story.append(Paragraph(title, styles["Title"]))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph(author, styles["SourcePath"]))
    story.append(Paragraph(f"{len(chapters)} chapter(s)", styles["SourcePath"]))
    story.append(PageBreak())
    story.append(Paragraph("Table of Contents", styles["TOCHeading"]))
    story.append(Spacer(1, 0.2 * inch))
    story.append(toc)
    story.append(PageBreak())
    return story


def chapter_to_flowables(chapter: Chapter, parser, styles: StyleSheet1):
    tokens = parser(chapter.text)
    story = [Paragraph(chapter.title, styles["ChapterTitle"])]
    story.append(Paragraph(chapter.path.as_posix(), styles["SourcePath"]))

    skipped_title = False
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if token["type"] == "blank_line":
            index += 1
            continue
        if not skipped_title and token["type"] == "heading" and token.get("attrs", {}).get("level") == 1:
            skipped_title = True
            index += 1
            continue
        if is_example_start(token):
            example_flowables, index = collect_example_flowables(tokens, index, styles)
            story.append(KeepTogether(example_flowables))
            continue
        story.extend(token_to_flowables(token, styles))
        index += 1
    return story


def token_to_flowables(token: dict, styles: StyleSheet1, list_depth: int = 0):
    token_type = token["type"]
    if token_type == "heading":
        level = token.get("attrs", {}).get("level", 1)
        style_name = {1: "Heading1", 2: "Heading2", 3: "Heading3"}.get(level, "Heading3")
        return [Paragraph(render_inline(token.get("children", [])), styles[style_name])]
    if token_type == "paragraph":
        markdown_table = paragraph_markdown_table(token, styles)
        if markdown_table is not None:
            return [markdown_table]
        style_name = paragraph_style_name(token)
        return [Paragraph(render_inline(token.get("children", [])), styles[style_name])]
    if token_type == "block_quote":
        return block_quote_flowables(token, styles)
    if token_type == "list":
        return list_flowables(token, styles, list_depth)
    if token_type == "block_code":
        return [code_box(token.get("raw", ""), styles, label=token.get("attrs", {}).get("info", ""))]
    if token_type == "block_math":
        return [code_box(latex_to_readable_math(token.get("raw", ""), block=True), styles, label="math", is_math=True)]
    if token_type == "table":
        return [table_flowable(token, styles)]
    if token_type in {"thematic_break"}:
        return [Spacer(1, 4), HRFlowable(width="100%", color=colors.HexColor("#CCCCCC")), Spacer(1, 6)]
    if token_type in {"block_html", "inline_html"}:
        return []
    return []


def block_quote_flowables(token: dict, styles: StyleSheet1):
    flowables = []
    for child in token.get("children", []):
        if child["type"] == "paragraph":
            markdown_table = paragraph_markdown_table(child, styles)
            if markdown_table is not None:
                flowables.append(markdown_table)
            else:
                flowables.append(Paragraph(render_inline(child.get("children", [])), styles["Quote"]))
        else:
            flowables.extend(token_to_flowables(child, styles))
    return flowables


def collect_example_flowables(tokens: list[dict], start_index: int, styles: StyleSheet1):
    flowables = []
    index = start_index

    while index < len(tokens):
        token = tokens[index]
        if token["type"] == "blank_line":
            index += 1
            continue
        if index != start_index and (token["type"] in {"heading", "thematic_break"} or is_example_start(token)):
            break
        flowables.extend(token_to_flowables(token, styles))
        index += 1

    flowables.append(Spacer(1, 6))
    return flowables, index


def is_example_start(token: dict) -> bool:
    if token.get("type") != "paragraph":
        return False
    text = paragraph_plain_text(token).strip()
    return text.startswith("Example ")


def is_given_label(token: dict) -> bool:
    if token.get("type") != "paragraph":
        return False
    return paragraph_plain_text(token).strip() == "Given:"


def paragraph_style_name(token: dict) -> str:
    if is_example_start(token):
        return "ExampleTitle"
    if is_given_label(token):
        return "GivenLabel"
    return "BodyBook"


def paragraph_plain_text(token: dict) -> str:
    return "".join(paragraph_text_fragment(child) for child in token.get("children", []))


def list_flowables(token: dict, styles: StyleSheet1, depth: int):
    ordered = token.get("attrs", {}).get("ordered", False)
    story = []
    for index, item in enumerate(token.get("children", []), start=1):
        bullet = f"{index}." if ordered else "-"
        item_text = render_list_item_text(item)
        list_style = ParagraphStyle(
            name=f"ListItemDepth{depth}",
            parent=styles["ListItem"],
            leftIndent=18 + depth * 16,
            bulletIndent=6 + depth * 16,
        )
        if item_text:
            story.append(Paragraph(item_text, list_style, bulletText=bullet))
        for child in item.get("children", []):
            if child["type"] == "list":
                story.extend(list_flowables(child, styles, depth + 1))
            elif child["type"] not in {"paragraph", "block_text"}:
                story.extend(token_to_flowables(child, styles, depth + 1))
    return story


def render_list_item_text(item: dict) -> str:
    pieces: list[str] = []
    for child in item.get("children", []):
        if child["type"] == "paragraph":
            pieces.append(render_inline(child.get("children", [])))
        elif child["type"] == "block_text":
            pieces.append(render_inline(child.get("children", [])))
    return "<br/>".join(piece for piece in pieces if piece)


def paragraph_markdown_table(token: dict, styles: StyleSheet1) -> Table | None:
    lines = paragraph_lines(token.get("children", []))
    if len(lines) < 2:
        return None

    if not all(line.strip().startswith("|") for line in lines[:2]):
        return None

    separator = lines[1].strip()
    if not re.match(r"^\|\s*:?-{3,}:?(\s*\|\s*:?-{3,}:?)+\s*\|?$", separator):
        return None

    parsed_rows = [split_markdown_table_row(line) for line in lines if line.strip().startswith("|")]
    if len(parsed_rows) < 2:
        return None

    header = parsed_rows[0]
    body_rows = parsed_rows[2:]
    if not header:
        return None

    table_rows: list[list[Paragraph]] = [
        [Paragraph(html.escape(cell), styles["BodyBook"]) for cell in header]
    ]
    for row in body_rows:
        padded = row + [""] * (len(header) - len(row))
        table_rows.append([
            Paragraph(html.escape(cell), styles["BodyBook"]) for cell in padded[: len(header)]
        ])

    table = Table(table_rows, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EAEAEA")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#BFBFBF")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def paragraph_lines(children: list[dict]) -> list[str]:
    raw_text = "".join(paragraph_text_fragment(child) for child in children)
    return [line.rstrip() for line in raw_text.splitlines() if line.strip()]


def paragraph_text_fragment(node: dict) -> str:
    node_type = node["type"]
    if node_type == "text":
        return node.get("raw", "")
    if node_type in {"softbreak", "linebreak"}:
        return "\n"
    if node_type == "inline_math":
        return latex_to_readable_math(node.get("raw", ""), block=False)
    if node_type in {"strong", "emphasis", "link"}:
        return "".join(paragraph_text_fragment(child) for child in node.get("children", []))
    if node_type == "codespan":
        return node.get("raw", "")
    if "children" in node:
        return "".join(paragraph_text_fragment(child) for child in node["children"])
    return node.get("raw", "")


def split_markdown_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def table_flowable(token: dict, styles: StyleSheet1) -> Table:
    rows: list[list[Paragraph]] = []
    children = token.get("children", [])
    if not children:
        return Table([[]])

    header = next((child for child in children if child["type"] == "table_head"), None)
    body = next((child for child in children if child["type"] == "table_body"), None)

    if header:
        rows.append([
            Paragraph(render_inline(cell.get("children", [])), styles["BodyBook"])
            for cell in header.get("children", [])
        ])
    if body:
        for row in body.get("children", []):
            rows.append([
                Paragraph(render_inline(cell.get("children", [])), styles["BodyBook"])
                for cell in row.get("children", [])
            ])

    table = Table(rows, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EAEAEA")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#BFBFBF")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def code_box(raw_text: str, styles: StyleSheet1, label: str = "", is_math: bool = False):
    content = raw_text.rstrip("\n") or " "
    parts = []
    if label:
        parts.append(Paragraph(html.escape(label), styles["SourcePath"]))
    text_style = styles["MathBlock"] if is_math else styles["CodeBlock"]
    box = Table(
        [[Preformatted(content, text_style)]],
        colWidths=[None],
        hAlign="LEFT",
    )
    box.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F7F7F7")),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D5D5D5")),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    parts.append(box)
    parts.append(Spacer(1, 8))
    return KeepTogether(parts)


def render_inline(children: list[dict]) -> str:
    return "".join(render_inline_node(child) for child in children).strip()


def render_inline_node(node: dict) -> str:
    node_type = node["type"]
    if node_type == "text":
        return apply_basic_inline_markup(html.escape(node.get("raw", "")))
    if node_type == "softbreak":
        return "<br/>"
    if node_type == "linebreak":
        return "<br/>"
    if node_type == "strong":
        return f"<b>{render_inline(node.get('children', []))}</b>"
    if node_type == "emphasis":
        return f"<i>{render_inline(node.get('children', []))}</i>"
    if node_type == "codespan":
        return f"<font face='{UNICODE_MONO_FONT_NAME}'>{html.escape(node.get('raw', ''))}</font>"
    if node_type == "link":
        text = render_inline(node.get("children", [])) or html.escape(node.get("attrs", {}).get("url", ""))
        url = node.get("attrs", {}).get("url", "")
        if url.startswith("http://") or url.startswith("https://"):
            return f"<a href='{html.escape(url, quote=True)}'>{text}</a>"
        return text
    if node_type == "inline_math":
        return f"<font face='{UNICODE_TEXT_FONT_NAME}'>{html.escape(latex_to_readable_math(node.get('raw', ''), block=False))}</font>"
    if node_type == "image":
        alt_text = html.escape(node.get("attrs", {}).get("alt", "image"))
        return f"[Image: {alt_text}]"
    if "children" in node:
        return render_inline(node["children"])
    return html.escape(node.get("raw", ""))


def apply_basic_inline_markup(text: str) -> str:
    text = INLINE_CODE_RE.sub(
        lambda match: f"<font face='{UNICODE_MONO_FONT_NAME}'>{html.escape(match.group(1))}</font>",
        text,
    )
    text = BOLD_RE.sub(lambda match: f"<b>{match.group(1)}</b>", text)
    text = ITALIC_RE.sub(lambda match: f"<i>{match.group(1)}</i>", text)
    return text


def infer_book_title(args_title: str | None, chapters: list[Chapter]) -> str:
    if args_title:
        return args_title
    if len(chapters) == 1:
        return chapters[0].title
    parent_names = {chapter.path.parent.name for chapter in chapters}
    if len(parent_names) == 1:
        return normalize_title(next(iter(parent_names)).replace("_", " ").title())
    return "Markdown Book"


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    paths = expand_inputs(args.inputs, args.exclude)
    if not paths:
        print("No Markdown files found for the given inputs.", file=sys.stderr)
        return 1

    chapters = build_chapters(paths)
    title = infer_book_title(args.title, chapters)
    build_book(Path(args.output), title, args.author, chapters, args.page_size, args.margin)

    print(f"Created {args.output} from {len(chapters)} Markdown file(s).")
    for chapter in chapters:
        print(f" - {chapter.path.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))