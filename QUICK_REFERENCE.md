# Quick Reference - UV Commands for This Project

## 🎯 Most Common Commands

### First Time Setup
```bash
uv sync
```

### Sync CSV Materials to HTML
```bash
uv run scripts/sync_materials.py
```

### Extract TDS Data from PDFs
```bash
# Single file
uv run scripts/tds_extractor.py -v path/to/tds.pdf

# Whole folder
uv run scripts/tds_extractor.py -v tds_pdfs/
```

---

## 📦 Managing Dependencies

### Add a New Package
```bash
uv add package-name
```

### Update Dependencies
```bash
uv sync --upgrade
```

### List Installed Packages
```bash
uv pip list
```

---

## 🐍 Running Python

### Run a Script
```bash
uv run python script.py
```

### Python REPL
```bash
uv run python
```

---

## 🔧 Maintenance

### Update UV Itself
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or via Homebrew
brew upgrade uv
```

### Clean Cache (if issues)
```bash
uv cache clean
```

---

## 📊 Project-Specific Workflows

### Update Material Database
```bash
# 1. Edit data/material_db.csv
# 2. Sync to JavaScript format
uv run scripts/sync_materials.py

# 3. Copy data/materials_sync.js into orcaslicer_assistant.html
```

### Add New Material from TDS
```bash
# 1. Extract data from TDS
uv run scripts/tds_extractor.py -v new_material.pdf

# 2. Review output/extraction_report.txt

# 3. Add to CSV: data/material_db.csv

# 4. Sync to HTML
uv run scripts/sync_materials.py
```

### Batch Process Multiple TDS Files
```bash
# Put all PDFs in tds_pdfs/ folder
mkdir -p tds_pdfs
# ... copy PDFs there ...

# Extract all
uv run scripts/tds_extractor.py -v tds_pdfs/

# Check results
cat output/extraction_report.txt
```

---

## 🆘 Troubleshooting

### Script Won't Run
```bash
# Make sure you're in project root
pwd  # Should show: .../m3dp_orcaslicer_settings_recommender

# Resync dependencies
uv sync
```

### Import Errors
```bash
# Check what's installed
uv pip list

# Reinstall from lock file
uv sync --frozen
```

### Python Version Issues
```bash
# Check current Python
uv run python --version

# Install specific version
uv python install 3.12
```

---

## 💡 Tips

- **No need to activate venv** - `uv run` handles it
- **Commit `uv.lock`** - ensures reproducible builds
- **Use `uv add`** not `pip install` - keeps `pyproject.toml` updated

---

**Need more help?** See `UV_SETUP.md` for detailed guide.
