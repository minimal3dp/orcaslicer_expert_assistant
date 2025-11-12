# Scripts Directory

This directory contains Python scripts for managing material data and extracting information from Technical Data Sheets (TDS).

## 📋 Available Scripts

### 1. `tds_extractor.py` - TDS PDF Data Extraction

Extracts printing parameters and material properties from PDF Technical Data Sheets, regardless of manufacturer template format.

**Features:**
- Handles different PDF layouts automatically
- Extracts temperatures, speeds, mechanical properties
- Detects special requirements (enclosure, hardened nozzle, etc.)
- Confidence scoring for extraction quality
- Batch processing of multiple PDFs

**Installation:**

```bash
# Dependencies are managed via UV (see Quick Start Guide above)
# Just run: uv sync
```

**Usage:**

```bash
# Extract from a single TDS file
uv run scripts/tds_extractor.py path/to/polymaker_pla_tds.pdf

# Extract from a folder of TDS files
uv run scripts/tds_extractor.py path/to/tds_folder/

# Verbose mode (see extraction details)
uv run scripts/tds_extractor.py -v path/to/tds_folder/

# Custom output location
uv run scripts/tds_extractor.py -o custom_output/ path/to/tds_folder/
```

**Note:** UV automatically handles the virtual environment, so use `uv run` to execute scripts.

**Output:**
- `output/extracted_materials.json` - Structured data
- `output/extraction_report.txt` - Human-readable report with confidence scores

**Supported Data Points:**
- ✅ Nozzle temperature (min/max/recommended)
- ✅ Bed temperature (min/max)
- ✅ Print speeds
- ✅ Tensile strength, modulus, elongation
- ✅ Heat deflection temperature (HDT)
- ✅ Glass transition temperature (Tg)
- ✅ Density, shore hardness
- ✅ Drying requirements
- ✅ Special requirements detection

---

### 2. `sync_materials.py` - CSV to JavaScript Converter

Converts the `material_db.csv` into JavaScript format for use in `orcaslicer_assistant.html`.

**Installation:**

```bash
# Dependencies are managed via UV (see Quick Start Guide above)
# Just run: uv sync
```

**Usage:**

```bash
# Basic sync (outputs to data/materials_sync.js)
uv run scripts/sync_materials.py

# Custom paths
uv run scripts/sync_materials.py --csv data/material_db.csv --output data/materials.js

# Output as JSON instead of JavaScript
uv run scripts/sync_materials.py --json --output data/materials.json

# Compact format (no whitespace, for production)
uv run scripts/sync_materials.py --compact
```

**Note:** UV automatically handles the virtual environment, so use `uv run` to execute scripts.

**Output:**
- JavaScript file with `const materialsData = {...}` object
- Ready to copy-paste into HTML file

**What it does:**
1. Reads all materials from CSV
2. Converts to JavaScript-compatible format
3. Estimates missing values (fan speeds, etc.)
4. Generates descriptive notes
5. Formats for easy integration

---

## 🚀 Quick Start Guide

### Step 1: Install Python Dependencies

This project uses **UV** for fast, modern Python package management.

```bash
# Install UV (if not already installed)
# macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or using Homebrew:
brew install uv

# Windows:
# powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Sync dependencies (UV will create venv and install everything)
uv sync

# Or if you need to add/update dependencies:
# uv add pdfplumber pandas fuzzywuzzy
```

**Note:** UV automatically creates and manages the virtual environment for you. No need to manually activate it - UV handles this when you run scripts!

### Step 2: Sync Your CSV to HTML

```bash
# This will create data/materials_sync.js
uv run scripts/sync_materials.py

# Check the output
cat data/materials_sync.js
```

Then manually copy the `materialsData` object into your HTML file around line 163.

### Step 3: (Optional) Extract TDS Data

When you have TDS PDFs:

```bash
# Create a folder for your TDS files
mkdir tds_pdfs

# Copy your PDFs there, then run:
uv run scripts/tds_extractor.py -v tds_pdfs/

# Check the results
cat output/extraction_report.txt
cat output/extracted_materials.json
```

---

## 📁 File Organization

Recommended structure for TDS files:

```
tds_pdfs/
├── polymaker/
│   ├── polymaker_pla_tds.pdf
│   ├── polymaker_petg_tds.pdf
│   └── polymaker_pa12cf_tds.pdf
├── prusament/
│   ├── prusament_pla_tds.pdf
│   └── prusament_petg_tds.pdf
└── bambu/
    ├── bambu_pla_basic_tds.pdf
    └── bambu_tpu_95a_tds.pdf
```

The extractor will automatically detect brands from folder names!

---

## 🔧 Troubleshooting

### "pdfplumber not installed"

```bash
uv add pdfplumber
# Then run: uv sync
```

### "No text extracted from PDF"

Some PDFs are image-based. Try:
1. Use PDF OCR tool first (Adobe Acrobat, online tools)
2. Or manually enter key data into CSV

### "Low confidence extraction"

Common reasons:
- Non-standard TDS format
- Image-based PDF (needs OCR)
- Missing data in original TDS

**Solution:** Check `extraction_report.txt` for details, then manually fill gaps in CSV.

### Script says "file not found"

Make sure you're running from the project root:

```bash
# Check your location
pwd
# Should show: .../m3dp_orcaslicer_settings_recommender

# Run scripts with proper path
uv run scripts/tds_extractor.py tds_pdfs/
```

---

## 🎯 Workflow for Adding New Materials

### Option A: You have a TDS PDF

1. **Extract data from PDF:**
   ```bash
   uv run scripts/tds_extractor.py path/to/new_material_tds.pdf -v
   ```

2. **Review extracted data:**
   ```bash
   cat output/extraction_report.txt
   ```

3. **Manually add to CSV:**
   - Open `data/material_db.csv`
   - Add new row with extracted data
   - Fill any missing fields manually

4. **Sync to HTML:**
   ```bash
   uv run scripts/sync_materials.py
   ```

5. **Update HTML:**
   - Copy `data/materials_sync.js` content
   - Replace `materialsData` object in HTML

### Option B: No TDS, manual entry

1. **Add to CSV directly:**
   - Open `data/material_db.csv`
   - Add new row with all known properties
   - Use similar materials as reference for unknowns

2. **Sync to HTML:**
   ```bash
   uv run scripts/sync_materials.py
   ```

3. **Update HTML:**
   - Copy and paste into HTML file

---

## 📊 Data Validation

After syncing, you should:

1. **Check material count:**
   ```bash
   # Count materials in CSV
   wc -l data/material_db.csv
   
   # Count materials in generated JS
   grep -c '"common"' data/materials_sync.js
   ```

2. **Verify no duplicates:**
   ```bash
   # Check for duplicate material names
   cut -d',' -f1 data/material_db.csv | sort | uniq -d
   ```

3. **Test in browser:**
   - Open `orcaslicer_assistant.html`
   - Check material dropdown has all materials
   - Test a few materials to ensure data displays correctly

---

## 🧪 Advanced Usage

### Custom TDS Pattern Matching

Edit `tds_extractor.py` and add patterns to `PATTERNS` dict:

```python
PATTERNS = {
    'nozzle_temp': [
        r'(?:nozzle|extrusion|print(?:ing)?)\s*temp(?:erature)?[:\s]*(\d{3})[°\s]*C',
        # Add your custom pattern here:
        r'your_pattern_here',
    ],
}
```

### Merge Extracted TDS with CSV

After extraction, you can merge new data with existing CSV:

```python
import pandas as pd
import json

# Load extracted data
with open('output/extracted_materials.json') as f:
    tds_data = json.load(f)

# Load existing CSV
csv_data = pd.read_csv('data/material_db.csv')

# Merge logic here...
```

---

## 💡 Tips

1. **Brand-specific profiles:** When adding TDS data, include brand name in material name
   - Example: "Polymaker PolyLite PLA" vs "Generic PLA"

2. **Keep raw TDS files:** Store original PDFs even after extraction
   - Create `tds_pdfs/archive/` for originals

3. **Version control:** Commit `material_db.csv` after each update
   ```bash
   git add data/material_db.csv
   git commit -m "Added Bambu Lab PLA Basic"
   ```

4. **Documentation:** Add notes about data sources
   - Comment in CSV or maintain separate `DATA_SOURCES.md`

---

## 🐛 Known Issues

1. **Image-based PDFs:** Cannot extract text automatically
   - **Workaround:** Use OCR tool first

2. **Multi-column layouts:** May extract in wrong order
   - **Workaround:** Check confidence score, manually verify

3. **Ambiguous units:** Sometimes MPa vs GPa unclear
   - **Workaround:** Script tries to detect, but verify manually

---

## 🤝 Contributing

When adding new extraction patterns:

1. Test on at least 3 different manufacturer TDS files
2. Add test case in comments
3. Document the pattern in code comments

Example:
```python
# Pattern for Bambu Lab TDS format (tested on PLA Basic, PETG-HF, PA-CF)
r'Nozzle\s*Temp\.?[:\s]*(\d{3})[°\s]*C',
```

---

## 📚 Further Reading

- [pdfplumber documentation](https://github.com/jsvine/pdfplumber)
- [Regular expressions in Python](https://docs.python.org/3/library/re.html)
- [CSV format specification](https://tools.ietf.org/html/rfc4180)

---

**Questions?** Open an issue on GitHub or check the main project README.
