# UV Setup Guide

This project uses **UV** - a fast, modern Python package manager and project manager.

## 🚀 Why UV?

- **10-100x faster** than pip
- **Unified tool** - replaces pip, pip-tools, pipx, poetry, pyenv, virtualenv
- **Deterministic builds** - lock files for reproducibility
- **Drop-in replacement** - uses standard `pyproject.toml`
- **No manual venv management** - UV handles it automatically

## 📦 Installation

### macOS/Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### macOS via Homebrew
```bash
brew install uv
```

### Windows
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 🏃 Quick Start

```bash
# Sync dependencies (creates venv + installs packages)
uv sync

# Run a script (UV handles venv automatically)
uv run scripts/sync_materials.py

# Run Python directly
uv run python
```

## 🔧 Common Commands

### Managing Dependencies

```bash
# Add a new dependency
uv add pdfplumber

# Add a dev dependency
uv add --dev pytest

# Remove a dependency
uv remove pdfplumber

# Update all dependencies
uv sync --upgrade

# Show installed packages
uv pip list
```

### Running Code

```bash
# Run a Python script
uv run scripts/tds_extractor.py -v tds_pdfs/

# Run Python interactively
uv run python

# Run a specific Python version
uv run --python 3.12 python script.py
```

### Lock File Management

```bash
# Update lock file
uv lock

# Sync from lock file (exact versions)
uv sync --frozen
```

## 📋 Project Dependencies

Current dependencies are defined in `pyproject.toml`:

```toml
[project]
dependencies = [
    "fuzzywuzzy>=0.18.0",    # Fuzzy string matching for TDS parsing
    "pandas>=2.3.3",          # Data manipulation (CSV processing)
    "pdfplumber>=0.11.8",     # PDF text extraction
]
```

### Optional Dependencies

If you need OCR for image-based PDFs:
```bash
uv add pytesseract pillow
```

If you need enhanced PDF processing:
```bash
uv add pypdf2 pdfminer.six
```

## 🌐 Virtual Environment

UV automatically creates and manages a virtual environment in `.venv/`.

### Manual Activation (rarely needed)
```bash
# Activate the venv (if you need to)
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# But usually just use: uv run <command>
```

### Why You Don't Need to Activate
UV's `uv run` automatically uses the project's virtual environment, so you never need to manually activate/deactivate.

## 🔄 Migration from pip/venv

If you previously used pip and venv:

### Before (pip)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python scripts/sync_materials.py
deactivate
```

### After (UV)
```bash
uv sync
uv run scripts/sync_materials.py
```

**That's it!** No activation/deactivation needed.

## 🐛 Troubleshooting

### "uv: command not found"
Your shell hasn't loaded the UV path yet:
```bash
source $HOME/.cargo/env  # Or restart your terminal
```

### "Python version not found"
UV can install Python versions for you:
```bash
uv python install 3.12
```

### "Package conflicts"
UV is very good at resolving conflicts, but if needed:
```bash
uv lock --upgrade-package problematic-package
uv sync
```

### Clear cache
```bash
uv cache clean
```

## 📚 Resources

- [UV Documentation](https://docs.astral.sh/uv/)
- [UV GitHub](https://github.com/astral-sh/uv)
- [Migration Guide](https://docs.astral.sh/uv/guides/migration/)

## 💡 Tips

### 1. Always use `uv run` for scripts
```bash
# Good ✅
uv run scripts/tds_extractor.py

# Also works, but more typing
source .venv/bin/activate
python scripts/tds_extractor.py
deactivate
```

### 2. Add dependencies correctly
```bash
# Production dependency
uv add pandas

# Development dependency (testing, etc.)
uv add --dev pytest black
```

### 3. Commit the lock file
```bash
git add uv.lock
git commit -m "Update dependencies"
```

The `uv.lock` file ensures everyone gets the exact same versions.

### 4. Check what's installed
```bash
uv pip list
# Or
uv tree  # Shows dependency tree
```

## 🎯 Next Steps

1. ✅ UV is installed and working
2. ✅ Dependencies are synced via `uv sync`
3. 🎯 Run your first script: `uv run scripts/sync_materials.py`
4. 🎯 Extract TDS data: `uv run scripts/tds_extractor.py -v tds_pdfs/`

---

**Questions?** Check the [UV docs](https://docs.astral.sh/uv/) or open an issue!
