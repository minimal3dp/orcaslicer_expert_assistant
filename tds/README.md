This folder contains manufacturer Technical Data Sheets (TDS) used as sources for extracting material properties.

Guidance:
- Prefer vendor PDFs with tabulated properties and units.
- Keep filenames informative: `<Brand>_<Material>_TDS_<version>.pdf` where possible.
- Avoid spaces; use `_` or `-` and include key tokens (e.g., `ABS`, `PETG`, `PA12`, `CF`, `GF`).
- If a PDF is a slide deck or image-heavy, extraction may need `pdftotext` or manual review.

Extraction:
- Run `scripts/extract_tds.py` (see `docs/workflows/tds-extraction-workflow.md`).
- Output goes to `data/processed/tds_extracted.csv`.

Notes:
- The extractor uses heuristics and regex patterns; review `Extraction_Warnings` in the output CSV.
- If a file consistently fails, add a brand/material pattern or open an issue with a snippet of the problematic text.

## Markdown & OCR workflow

For better reliability, convert PDFs to Markdown before extraction:

1. Run conversion script:
	```bash
	uv run python scripts/convert_pdfs_to_markdown.py --in data/sources --out data/sources/markdown
	```
2. Re-run extractor pointing at the markdown directory:
	```bash
	uv run python scripts/extract_tds.py --sources-dir data/sources/markdown --out data/processed/tds_extracted.csv
	```

If `pdftotext` is unavailable or a PDF is scanned, the converter will attempt OCR via `tesseract` (install with `brew install tesseract`). Empty markdown files receive a placeholder for manual annotation.

Directory suggestion:
```
data/sources/
  pdf/        # (optional) move original PDFs here
  markdown/   # generated .md files for extraction
```

## OCR fallback in extraction

`extract_tds.py` now attempts OCR automatically if direct PDF text extraction fails and `tesseract` is installed.

## Provenance

TDS-derived values are stored in parallel `_TDS` columns plus `TDS_Source_File` in the merged CSV `data/processed/material_db_with_tds.csv` for review before promoting to authoritative columns.
