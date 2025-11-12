# OrcaSlicer Settings Recommender

A web application that provides intelligent 3D printing slicer settings recommendations based on material selection and print priorities. This tool helps users optimize their OrcaSlicer settings by balancing competing objectives like strength, speed, surface quality, and dimensional accuracy.

## 🎯 Project Overview

This application synthesizes research on FDM 3D printing parameters and material properties to provide expert-level guidance on OrcaSlicer settings. Users can:

- **Select from 28 materials** spanning standard to high-performance (PLA variants, PETG, ABS, Nylon, PC, TPU, PEEK, PEKK, and more)
- **Receive intelligent material warnings** for special requirements (hardened nozzle, enclosure, drying, ventilation, etc.)
  - **Mechanical Strength** (Tensile Z-axis, XY-plane, Flexural, Compressive)
  - **Build Time** (Print speed optimization)
  - **Surface Quality** (Roughness/aesthetic finish)
  - **Dimensional Accuracy** (Precision)

## ✨ Key Features

### 🎨 Intelligent Material Warning System
**NEW in November 2025!**

The application now includes a comprehensive warning system that automatically displays material-specific requirements and considerations:

- **10 Warning Types:**
  - 🔧 **Hardened Nozzle Required** - For abrasive materials (carbon fiber, glass fiber)
  - 🏠 **Enclosure Recommended** - For materials sensitive to drafts and temperature
  - 💧 **Hygroscopic Material** - Requires drying before printing
  - 💨 **Releases Fumes** - Ventilation required for safety
  - ⚠️ **Difficult to Print** - Requires careful calibration
  - 📉 **Prone to Creep** - Not suitable for sustained load applications
  - ☀️ **UV Resistant** - Excellent for outdoor applications
  - ⚙️ **Low Friction** - Ideal for mechanical parts and bearings
  - 🧪 **Chemical Resistance** - Suitable for harsh environments
  - 🔥 **Annealable** - Can be heat-treated for improved properties

- **Interactive UI:**
  - Color-coded alerts (red/orange/yellow for warnings, blue/green for info)
  - Dismissible warning cards with smooth animations
  - Collapsible sections (individual cards + "Collapse All" button)
  - Help guide links for each warning type
  - Automatic display on material selection

### 📊 Comprehensive Material Database

**28 Materials** organized by performance tier:

**Standard Materials (9):**
- PLA, PLA Plus, High-Temp PLA, PLA Carbon Fiber
- PLA variants: Wood-filled, Metal-filled, Silk, Glow-in-the-dark
- PP (Polypropylene)

**Engineering Materials (10):**
- PETG, PETG Carbon Fiber, PET
- ABS, ASA, HIPS
- PC-ABS Blend, Polycarbonate
- Nylon, Nylon Carbon Fiber, Nylon Glass Fiber

**Functional Materials (3):**
- TPU 95A, TPU 85A (flexible materials)
- PVA, PVB (support materials)

**High-Performance Materials (6):**
- PEEK, PEKK, PPSU
- ULTEM 9085
- (Additional high-temp variants coming soon)

## 🏗️ Current Architecture

### Technology Stack
- **Python Scripts**: UV package manager for data processing and synchronization

### File Structure
```
.
├── orcaslicer_assistant.html    # Main application (single-page app, 1839 lines)
├── data/
│   ├── material_db.csv           # Material properties database (29 materials)
│   └── materials.json            # Material settings and properties
├── scripts/
│   ├── sync_materials.py         # Sync CSV to HTML/JSON
│   ├── tds_extractor.py          # Extract data from TDS PDFs
│   └── merge_extracted_to_csv.py # Merge TDS data into CSV
├── tests/
│   └── test_merge_extracted.py   # Unit tests for merge script
├── research/                     # Academic papers on FDM printing
│   └── *.pdf                    # Research papers (gitignored)
├── pyproject.toml               # Python dependencies (UV)
├── .gitignore
├── README.md
└── TODO.md                      # Development roadmap
```

## 📊 Data Sources

### Material Database
The application includes comprehensive data on:
- **28 materials** spanning standard to high-performance grades
- **Material properties**: Tensile strength, modulus, elongation, HDT, glass transition temperature, density
- **Material characteristics**: 10+ boolean flags for special requirements
  - `hygroscopic`: Requires drying before use
  - `requires_enclosure`: Needs controlled temperature environment
  - `requires_hardened_nozzle`: Abrasive materials
  - `releases_fumes`: Requires ventilation
  - `uv_resistant`: Suitable for outdoor use
  - `difficult_to_print`: Needs careful calibration
  - `prone_to_creep`: Time-dependent deformation
  - `low_friction`: Good for mechanical parts
  - `chemical_resistance`: Resistant to solvents/chemicals
  - `annealable`: Can be heat-treated post-printing

### Knowledge Base
Settings recommendations are based on:

### Research Foundation
The `research/` folder contains 20+ academic papers covering:

## 🚀 Usage

### Quick Start: Deploy to Vercel (Recommended)
**⚡ Get your app live in 15 minutes!**

1. Follow the step-by-step guide in **[VERCEL_DEPLOYMENT.md](./VERCEL_DEPLOYMENT.md)**
2. Deploy the static HTML app (no backend needed)
3. Set up Google Analytics to track users and affiliate clicks
4. Optimize for SEO (sitemap, OG image, YouTube integration)
5. Start generating revenue immediately!

**Benefits of Deployment:**
- ✅ Live 24/7 on Vercel's global CDN (free tier)
- ✅ Automatic HTTPS and SSL
- ✅ Custom domain support: **settings.minimal3dp.com** ✅ DEPLOYED
- ✅ DNS managed by Cloudflare for fast, reliable access
- ✅ Zero-config deployment
- ✅ SEO optimized for "best slicer settings for 3d printing"
- ✅ YouTube traffic integration
- ✅ Revenue generation from affiliate links

**SEO & Marketing:**
- See **[SEO_STRATEGY.md](./SEO_STRATEGY.md)** for comprehensive SEO plan
- Target keyword: "best slicer settings for 3d printing" (from YouTube Analytics)
- YouTube channel: [youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw](https://youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw)
- Video companion content strategy
- Material landing pages roadmap

### Web App (Local Development)
1. Clone the repository
2. Open `orcaslicer_assistant.html` in a modern web browser
3. No build process or server required!
4. Select a material and adjust priority sliders
5. View intelligent warnings specific to your material choice
6. Get detailed setting recommendations

### Python Scripts (Data Management)
1. Install UV: `curl -LsSf https://astral.sh/uv/install.sh | sh` (or `brew install uv`)
2. Sync dependencies: `uv sync`
3. Run scripts:
   ```bash
   # Sync material database to HTML
   uv run scripts/sync_materials.py --output data/materials_sync.js
   
   # Extract data from TDS PDFs
   uv run scripts/tds_extractor.py --input tds/ --output output/
   
   # Run unit tests
   uv run pytest tests/
   ```

See `scripts/README.md` for detailed script usage.

## 🧠 How It Works

### 1. Material Selection
Users select from 28 materials, which loads:
- Baseline temperature and speed settings
- Material characteristics and special requirements
- Automatic warning display for material-specific considerations

### 2. Priority Ranking
Users adjust sliders (0-100) for each objective:

### 3. Conflict Detection
The system identifies common conflicts:

### 4. Recommendations
For each high-priority goal, the system provides:

### 5. Material Warnings
**NEW!** Intelligent warnings appear automatically based on material characteristics:
- **Critical warnings** (red/orange): Immediate attention required
- **Caution warnings** (yellow/purple): Important considerations
- **Informational** (blue/green): Helpful tips and capabilities
- Each warning includes a help link to educational resources
- Warnings can be dismissed or collapsed as needed

## �️ Development Setup

### Prerequisites

### Setup
```bash
# Clone the repository
git clone https://github.com/minimal3dp/orcaslicer_expert_assistant.git
cd orcaslicer_expert_assistant

# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh  # macOS/Linux
# or: brew install uv

# Sync Python dependencies
uv sync

# Test the scripts
uv run scripts/sync_materials.py --help

# Run unit tests
uv run pytest tests/
```

### Project Structure
```
.
├── orcaslicer_assistant.html    # Main web app (standalone)
├── data/
│   ├── material_db.csv           # Master material database
│   └── materials.json            # Material settings for other uses
├── scripts/                      # Python utilities
│   ├── tds_extractor.py         # Extract data from TDS PDFs
│   ├── sync_materials.py        # Sync CSV to HTML/JSON
│   ├── merge_extracted_to_csv.py # Merge TDS extraction into CSV
│   └── README.md                # Script documentation
├── tests/                       # Unit tests
│   └── test_merge_extracted.py
├── research/                     # Academic papers (gitignored)
├── pyproject.toml               # Python dependencies (UV)
├── README.md                    # This file
└── TODO.md                      # Development roadmap
```

## �🔬 Technical Details

### Material Properties Tracked

### Material Characteristics (Boolean Flags)
- Hygroscopic (requires drying)
- Requires enclosure
- Requires hardened nozzle
- Releases fumes
- UV resistant
- Difficult to print
- Prone to creep
- Low friction coefficient
- Chemical resistance
- Annealable

### Slicer Settings Covered

## 📈 Future Enhancements (See TODO.md)

### High Priority
- Material search/filter functionality in dropdown
- Material tier badges (Standard/Engineering/High-Performance)
- localStorage for persistent warning dismissals
- Brand-specific material variants (3DXTech, eSUN, ColorFabb)
- Comprehensive data quality audit (HDT, Tg, shrinkage data)

### Planned Features
- Printer capability validation
- Material comparison tool

See `TODO.md` for complete development roadmap.

## 🤝 Contributing

This project synthesizes research from academic literature and practical 3D printing experience. Contributions are welcome:
- TDS (Technical Data Sheets) for new materials
- Bug reports and feature requests

## 📚 Research Attribution

This tool is based on extensive research into FDM printing parameters. Key areas:

See `research/` folder for complete paper list.

## ⚠️ Disclaimer

These recommendations are starting points based on research and best practices. Always:
- Follow material-specific warnings and safety guidelines
- Ensure adequate ventilation for materials that release fumes
- Use appropriate nozzles for abrasive materials

## 📄 License

[Specify your license here - e.g., MIT, GPL, etc.]

## 🔗 Related Resources

- [UV Package Manager](https://github.com/astral-sh/uv) - Fast Python package manager

## 📊 Project Status

**Version**: 0.3 (Warning System + SEO Optimization)  
**Materials**: 28 (expanded from 12)  
**Warning Types**: 10 with interactive UI  
**Last Updated**: November 12, 2025  
**Status**: Actively developed, production-ready  
**SEO Status**: Optimized for "best slicer settings for 3d printing"

### Recent Updates (November 2025)
- ✅ **Material database expanded 2.3×** (12 → 28 materials)
- ✅ **Intelligent warning system** with 10 warning types
- ✅ **Interactive UI** with dismissible/collapsible cards
- ✅ **Help guide links** for educational resources
- ✅ **Material characteristics** tracked via boolean flags
- ✅ **Event-driven warnings** on material selection
- ✅ **SEO optimization** for target keyword (Nov 12, 2025)
  - Title tag: "Best Slicer Settings for 3D Printing"
  - Meta descriptions with material keywords
  - Schema.org structured data (WebApplication)
  - Open Graph tags for social sharing
  - YouTube channel integration
- ✅ **YouTube strategy** documented in SEO_STRATEGY.md


**Made with ❤️ for the 3D printing community**
