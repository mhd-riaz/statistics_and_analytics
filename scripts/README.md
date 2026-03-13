# Markdown Book PDF Script

This folder contains a Python CLI that combines Markdown files into a readable PDF book with:

- a cover page
- a table of contents
- chapter breaks between files
- page numbers and running header
- rendering for headings, paragraphs, lists, block quotes, code blocks, tables, and math blocks

For directory-based builds, the script starts the book with the workspace root [README.md](../README.md) when it exists, so the overall course index appears before unit or chapter files.

## Use The Requested Conda Python

```bash
source /Users/riaz/miniconda3/etc/profile.d/conda.sh
conda activate /Users/riaz/miniconda3
python scripts/markdown_book_pdf.py --output output/unit1-book.pdf unit_1/index.md unit_1/*.md
```

## Example Commands

Build one unit into a PDF:

```bash
source /Users/riaz/miniconda3/etc/profile.d/conda.sh
conda activate /Users/riaz/miniconda3
python scripts/markdown_book_pdf.py \
  --title "Unit 1 - Statistics and Probability" \
  --author "Riaz" \
  --output output/unit_1_book.pdf \
  unit_1/
```

That command now starts with [README.md](../README.md), then follows the linked order from [unit_1/index.md](../unit_1/index.md).

Build a custom set of chapters:

```bash
source /Users/riaz/miniconda3/etc/profile.d/conda.sh
conda activate /Users/riaz/miniconda3
python scripts/markdown_book_pdf.py \
  --title "AMES Revision Book" \
  --output output/revision-book.pdf \
  unit_1/index.md \
  unit_1/statistics-basics.md \
  unit_2/standardization.md
```

Exclude files:

```bash
source /Users/riaz/miniconda3/etc/profile.d/conda.sh
conda activate /Users/riaz/miniconda3
python scripts/markdown_book_pdf.py \
  --output output/classnotes-book.pdf \
  classNotes/session1 \
  --exclude "*/raw.md"
```

## Notes

- The script uses the environment's installed `reportlab` and `mistune` packages.
- Relative Markdown links are rendered as plain text in the PDF.
- LaTeX math is converted into readable Unicode math text for the PDF, including common Greek symbols and basic constructs such as fractions, square roots, sums, bars, hats, and boxed results.