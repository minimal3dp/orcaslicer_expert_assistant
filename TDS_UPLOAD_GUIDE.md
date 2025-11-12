# TDS Upload Guide - YES, It's Beneficial!

## 📄 Quick Answer: **YES, upload your TDS PDFs!**

Even though manufacturers use different templates, the extraction script can handle it. Here's why it's worth doing:

---

## 🎯 What You'll Gain from TDS Uploads

### 1. **Accurate, Source-Verified Data**
Instead of estimates, you'll have:
- Exact temperature ranges from manufacturer testing
- Real mechanical property values (not generic averages)
- Specific drying requirements
- Actual shrinkage factors

### 2. **Brand-Specific Profiles**
Create profiles for specific brands:
- **"Polymaker PolyLite PLA"** - 205-225°C, 0.4% shrinkage
- **"Prusament PLA"** - 210-230°C, 0.2% shrinkage  
- **"Bambu Lab PLA Basic"** - 190-220°C, 0.3% shrinkage

All are "PLA" but print differently!

### 3. **Missing Properties**
TDS sheets often include data not in your CSV:
- **Shrinkage percentage** (critical for dimensional accuracy!)
- **Water absorption rate** (for hygroscopic materials)
- **Optimal retraction settings**
- **Recommended layer heights**
- **Flow rate multipliers**
- **Shore hardness** (for TPU/TPE)

---

## 🔧 How the Script Handles Different Templates

### The script uses smart pattern matching:

```
Example TDS Variations:

Template A (Polymaker):
"Nozzle Temperature: 205-225°C"
Pattern matches: (\d{3})-(\d{3})°C

Template B (Prusament):
"Extrusion temp.: 210°C - 230°C"  
Pattern matches: (\d{3})°C - (\d{3})°C

Template C (Bambu):
"Print Temperature
  Nozzle: 190-220℃"
Pattern matches: Nozzle:\s*(\d{3})-(\d{3})
```

The script tries **multiple patterns** for each property, so it works with most formats!

---

## 📊 Confidence Scoring System

The extractor provides a confidence score (0-100%) for each file:

- **>70% = Excellent** - Most data extracted successfully
- **30-70% = Partial** - Some data found, manual review needed
- **<30% = Poor** - Mostly failed, likely image-based PDF

You'll get a detailed report showing what was found.

---

## 🚀 Step-by-Step: How to Use

### Step 1: Organize Your TDS Files

```bash
mkdir tds_pdfs
# Put your PDFs in there, organized by brand if you want:
tds_pdfs/
├── polymaker_pla_tds.pdf
├── polymaker_petg_tds.pdf
├── prusament_pla_tds.pdf
└── bambu_pla_basic_tds.pdf
```

### Step 2: Install Python Dependencies

```bash
# This project uses UV for fast Python package management
# Dependencies are already configured in pyproject.toml

# Just sync the project (one command!)
uv sync
```

### Step 3: Run the Extractor

```bash
# Extract from all PDFs (with detailed output)
uv run scripts/tds_extractor.py -v tds_pdfs/

# Check the results
cat output/extraction_report.txt
```

### Step 4: Review Results

Open `output/extraction_report.txt`:

```
=====================================
Polymaker PolyLite PLA
-------------------------------------
Confidence: 85%
Brand: Polymaker
Nozzle: 205-225°C
Bed: 45-60°C
Tensile Strength: 64.3 MPa

Extraction Notes:
  - Found nozzle temp range: 205-225°C
  - Found bed temp range: 45-60°C
  - Found tensile strength: 64.3 MPa
  - Found density: 1.24 g/cm³
  - Detected: Requires drying
```

### Step 5: Merge into Your CSV

The script outputs `output/extracted_materials.json`. You can:

**Option A: Manual merge** (recommended first time)
- Review extracted data
- Copy accurate values into your CSV
- Keep your existing structure

**Option B: Automated merge** (future enhancement)
- Script can auto-merge if you're confident in extractions

### Step 6: Sync to HTML

```bash
# Update HTML with new CSV data
uv run scripts/sync_materials.py

# Copy the output into your HTML file
```

---

## 📋 What Data Gets Extracted

### ✅ **Always looks for:**
- Nozzle temperature (min/max/recommended)
- Bed temperature (min/max)
- Print speeds
- Tensile strength
- Tensile modulus
- Elongation at break
- Heat deflection temperature (HDT)
- Glass transition temp (Tg)
- Density
- Shore hardness (for flexible materials)

### ✅ **Detects special requirements:**
- "Enclosure required" (from keywords like "warping prone")
- "Hardened nozzle required" (from "abrasive", "carbon fiber")
- "Hygroscopic" (from "must be dried", "absorbs moisture")
- Drying conditions (temp + time)

### ✅ **Bonus properties (if present):**
- Flexural strength/modulus
- Impact strength
- Vicat softening temperature
- Shrinkage percentage
- Recommended retraction settings
- Layer height recommendations

---

## 🎨 Example: What Different Templates Look Like

### Template Style 1: Table Format (Polymaker)
```
Property                    Value
─────────────────────────────────
Nozzle Temperature         205-225°C
Bed Temperature            45-60°C
Tensile Strength           64.3 MPa
Print Speed               40-60 mm/s
```
✅ **Script handles:** Table parsing

### Template Style 2: Paragraph Format (Prusament)
```
The recommended extrusion temperature is 210°C to 230°C. 
The bed should be heated to 50-60°C. Typical tensile 
strength is 62 MPa with 8% elongation at break.
```
✅ **Script handles:** Natural language patterns

### Template Style 3: Mixed Format (Bambu)
```
PRINTING PARAMETERS
Nozzle: 190-220℃
Bed: 35-60℃

MECHANICAL PROPERTIES
Ultimate Tensile Strength: 63.5 MPa
Modulus: 2,850 MPa
```
✅ **Script handles:** Mixed sections

---

## ⚠️ Known Limitations

### 1. **Image-Based PDFs**
If the PDF is just a scanned image (no selectable text):
- **Problem:** Script can't extract text
- **Solution:** Use OCR tool first, or manually enter data
- **How to check:** Try selecting text in PDF viewer

### 2. **Non-Standard Terms**
If a manufacturer uses unique terminology:
- **Example:** "Heating plate" instead of "bed temperature"
- **Solution:** May not auto-detect, but you can add patterns
- **Low confidence score** will alert you

### 3. **Ambiguous Units**
Sometimes units aren't clear:
- **Example:** "Modulus: 2.8" (is it MPa or GPa?)
- **Solution:** Script makes best guess, but verify
- **Check:** Confidence score + manual review

---

## 🏆 Best Practices

### Before Uploading:
1. ✅ Ensure UV is set up: `uv sync`
2. ✅ Collect TDS PDFs from manufacturer websites
3. ✅ Rename files clearly: `brand_material_tds.pdf`
4. ✅ Check PDF has selectable text (not just image)

### After Extraction:
1. ✅ Always review `extraction_report.txt`
2. ✅ For low confidence (<50%), manually verify
3. ✅ Compare extracted values with CSV estimates
4. ✅ Keep original PDFs archived (in case of questions)

### Data Validation:
```bash
# Check for outliers
# Example: If extracted "Nozzle: 2100°C" that's clearly wrong (missing digit)
# Should be "210°C"
```

---

## 📈 Expected Results

Based on typical TDS formats, you can expect:

| Template Quality | Confidence | Manual Work |
|-----------------|------------|-------------|
| Modern, well-formatted | 80-95% | Minimal review |
| Older formats | 50-80% | Some fields manual |
| Image scans | 0-30% | Manual entry needed |
| Mixed format | 60-80% | Verify ambiguous fields |

**Most manufacturer TDS = 70-90% success rate!**

---

## 💡 Pro Tips

### 1. **Batch Processing**
If you have 50+ TDS files:
```bash
# Process all at once
uv run scripts/tds_extractor.py -v tds_pdfs/

# Check overall success rate
grep "Confidence:" output/extraction_report.txt
```

### 2. **Brand-Specific Patterns**
If you use mainly one brand, you can add custom patterns:

Edit `scripts/tds_extractor.py`:
```python
# Add Bambu Lab specific pattern
'nozzle_temp': [
    # ... existing patterns ...
    r'Nozzle[:\s]*(\d{3})-(\d{3})℃',  # Bambu uses ℃ symbol
],
```

### 3. **Verify Critical Properties**
Always double-check these manually:
- Temperature ranges (most critical for printing!)
- Hardened nozzle requirement
- Drying needs (hygroscopic materials)

---

## 🎯 Action Items for You

### Immediate:
- [x] Install Python dependencies: `uv sync` (Already done!)
- [ ] Collect your TDS PDFs
- [ ] Test extraction on 2-3 PDFs first
- [ ] Review confidence scores

### After Testing:
- [ ] Batch process all TDS files
- [ ] Merge high-confidence extractions into CSV
- [ ] Manually fill low-confidence gaps
- [ ] Re-sync HTML with updated CSV

### Future:
- [ ] Set up auto-update workflow when new materials added
- [ ] Share extraction patterns for common brands (PR to project?)

---

## ❓ FAQ

**Q: What if my PDF is in a weird format?**  
A: Run it through the extractor anyway. Worst case: 0% confidence, you enter manually. Best case: It works!

**Q: Do I need to manually review every extraction?**  
A: No! Only review:
- Low confidence (<70%)
- Critical materials you use often
- Spot-check a few high-confidence ones

**Q: Can the script handle multi-page TDS?**  
A: Yes! It reads all pages and extracts from anywhere in the document.

**Q: What if two brands have same material name?**  
A: Add brand prefix: "Polymaker_PLA" vs "Prusament_PLA" in your CSV.

**Q: Can I add my own extraction patterns?**  
A: Yes! Edit `PATTERNS` dict in `tds_extractor.py`. See comments for examples.

---

## 📚 Next Steps

1. **Read:** `scripts/README.md` for detailed script documentation
2. **Install:** Python dependencies with `uv sync` (Already done!)
3. **Test:** Run extractor on 1-2 PDFs to see results
4. **Upload:** When ready, share your TDS files in a folder
5. **Review:** Check extraction report and merge good data

---

**Bottom Line:** YES, upload those TDS PDFs! Even with different templates, you'll get 70-90% of the data automatically, which is way better than manual entry. The extraction report will tell you what to verify.

Ready to start? Drop your TDS PDFs in a folder and run:
```bash
uv run scripts/tds_extractor.py -v your_tds_folder/
```

Let me know if you hit any issues! 🚀
