# OrcaSlicer Settings Recommender

A web application that provides intelligent 3D printing slicer settings recommendations based on material selection and print priorities. This tool helps users optimize their OrcaSlicer settings by balancing competing objectives like strength, speed, surface quality, and dimensional accuracy.

## 🎯 Project Overview

This application synthesizes research on FDM 3D printing parameters and material properties to provide expert-level guidance on OrcaSlicer settings. Users can:

- Select from a comprehensive material database (PLA, PETG, ABS, Nylon, PC, TPU, etc.)
- Rank their priorities across multiple objectives:
  - **Mechanical Strength** (Tensile Z-axis, XY-plane, Flexural, Compressive)
  - **Build Time** (Print speed optimization)
  - **Surface Quality** (Roughness/aesthetic finish)
  - **Dimensional Accuracy** (Precision)
- Receive detailed setting recommendations with explanations and trade-offs
- Understand conflicts between competing goals with expert advice

## 🏗️ Current Architecture

### Technology Stack
- **Frontend**: Pure HTML5, CSS (Tailwind CSS via CDN), Vanilla JavaScript
- **Data Format**: JSON for material properties, embedded knowledge base
- **Deployment**: Static site (no backend required)

### File Structure
```
.
├── orcaslicer_assistant.html    # Main application (single-page app)
├── data/
│   ├── material_db.csv           # Material properties database
│   └── materials.json            # Material settings and properties
├── research/                     # Academic papers on FDM printing
│   └── *.pdf                    # Research papers (gitignored)
├── .gitignore
└── README.md
```

## 📊 Data Sources

### Material Database
The application includes comprehensive data on:
- **12+ common materials**: PLA, PLA-CF, PETG, PETG-CF, ABS, ASA, PC, PA6-CF, PA12-CF, ULTEM 9085, TPU-95A, TPE-85A
- **Material properties**: Tensile strength, modulus, elongation, HDT, glass transition temp, density
- **Print settings**: Temperature ranges, speeds, cooling requirements
- **Special considerations**: Hygroscopic nature, enclosure requirements, hardened nozzle needs

### Knowledge Base
Settings recommendations are based on:
- **Layer height** effects on strength, quality, and speed
- **Temperature** impact on layer adhesion and quality
- **Wall/perimeter** strategies for different strength types
- **Infill** patterns and densities for structural requirements
- **Speed profiles** for balanced quality vs. time
- **Advanced features**: Arachne engine, ironing, seam placement

### Research Foundation
The `research/` folder contains 20+ academic papers covering:
- Effects of FDM process parameters on mechanical properties
- Layer height, temperature, and speed optimization studies
- Material-specific printing characteristics
- Annealing and post-processing techniques

## 🚀 Usage

### Web App (Frontend Only)
1. Clone the repository
2. Open `orcaslicer_assistant.html` in a modern web browser
3. No build process or server required!

### Python Scripts (Data Management)
1. Install UV: `curl -LsSf https://astral.sh/uv/install.sh | sh` (or `brew install uv`)
2. Sync dependencies: `uv sync`
3. Run scripts: `uv run scripts/sync_materials.py`

See `scripts/README.md` for detailed script usage.

### Deployment Options
- GitHub Pages
- Netlify/Vercel static hosting
- Any web server (Apache, Nginx, etc.)

## 🧠 How It Works

### 1. Material Selection
Users select their filament material, which loads baseline temperature and speed settings.

### 2. Priority Ranking
Users adjust sliders (0-100) for each objective:
- Values >70 are considered "high priority"
- Multiple high priorities trigger conflict detection

### 3. Conflict Detection
The system identifies common conflicts:
- **Z-Strength vs. Speed**: Low layers (strength) vs. thick layers (speed)
- **Accuracy vs. Speed**: Slow precision vs. fast printing
- **Quality vs. Speed**: Fine details vs. rapid completion

### 4. Recommendations
For each high-priority goal, the system provides:
- **Specific setting values** (e.g., "Layer Height: 0.12-0.16mm")
- **Explanation** of why this setting matters
- **Trade-offs** to be aware of

## �️ Development Setup

### Prerequisites
- Modern web browser (Chrome, Firefox, Edge, Safari)
- **Python 3.12+** and **UV** (for data management scripts)

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
│   └── README.md                # Script documentation
├── research/                     # Academic papers (gitignored)
├── pyproject.toml               # Python dependencies (UV)
└── README.md                    # This file
```

## �🔬 Technical Details

### Material Properties Tracked
- Tensile strength (MPa) - XY and Z-axis
- Tensile modulus (stiffness)
- Elongation at break (ductility)
- Heat deflection temperature (HDT)
- Glass transition temperature (Tg)
- Impact strength
- Density
- Fatigue resistance
- Creep behavior

### Slicer Settings Covered
- Layer height and first layer
- Nozzle and bed temperatures
- Print speeds (outer wall, inner wall, infill)
- Acceleration and jerk
- Wall count and line width
- Infill percentage and pattern
- Cooling/fan speeds
- Retraction settings
- Advanced features (ironing, seam placement, wall generator)

## 📈 Future Enhancements (See TODO.md)

- Backend API for settings calculations
- User profiles and saved configurations
- OrcaSlicer profile export (.json)
- Material cost calculator
- Print time estimator
- Multi-material/MMU support
- Community-contributed profiles

## 🤝 Contributing

This project synthesizes research from academic literature and practical 3D printing experience. Contributions are welcome:
- Material property data
- Setting validation from test prints
- UI/UX improvements
- Additional conflict detection logic

## 📚 Research Attribution

This tool is based on extensive research into FDM printing parameters. Key areas:
- Layer adhesion and Z-axis strength optimization
- Speed/acceleration tuning for quality retention
- Material-specific thermal requirements
- Infill strategies for different load types

See `research/` folder for complete paper list.

## ⚠️ Disclaimer

These recommendations are starting points based on research and best practices. Always:
- Test settings with small calibration prints first
- Adjust for your specific printer hardware
- Consider your environmental conditions
- Dry hygroscopic materials before printing

## 📄 License

[Specify your license here - e.g., MIT, GPL, etc.]

## 🔗 Related Resources

- [OrcaSlicer GitHub](https://github.com/SoftFever/OrcaSlicer)
- [OrcaSlicer Documentation](https://github.com/SoftFever/OrcaSlicer/wiki)
- Material manufacturer datasheets

---

**Version**: 1.0.0  
**Last Updated**: November 2025  
**Status**: Functional prototype, actively developed
