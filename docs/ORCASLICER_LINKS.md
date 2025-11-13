# OrcaSlicer Settings Reference Map

This file maps the recommendations in the app to specific OrcaSlicer settings with documentation links.

## Settings Links Database

### Quality Settings
- **Layer Height**: https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#layer-height
- **Wall Loops**: https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#wall-loops
- **Infill Percentage**: https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#infill
- **Infill Pattern**: https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#infill-pattern

### Temperature Settings
- **Temperature**: https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#temperature
- **Nozzle Temperature**: https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#temperature
- **Bed Temperature**: https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#bed-temperature

### Speed Settings
- **Print Speed**: https://github.com/SoftFever/OrcaSlicer/wiki/Speed
- **Speed (All)**: https://github.com/SoftFever/OrcaSlicer/wiki/Speed
- **Outer Wall Speed**: https://github.com/SoftFever/OrcaSlicer/wiki/Speed#outer-wall-speed
- **Inner Wall Speed**: https://github.com/SoftFever/OrcaSlicer/wiki/Speed#inner-wall-speed
- **Sparse Infill Speed**: https://github.com/SoftFever/OrcaSlicer/wiki/Speed#sparse-infill-speed
- **Speed: Sparse Infill**: https://github.com/SoftFever/OrcaSlicer/wiki/Speed#sparse-infill-speed
- **Speed: Inner Wall**: https://github.com/SoftFever/OrcaSlicer/wiki/Speed#inner-wall-speed
- **Speed: Outer Wall**: https://github.com/SoftFever/OrcaSlicer/wiki/Speed#outer-wall-speed
- **Acceleration**: https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#acceleration

### Advanced Settings
- **Line Width**: https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#line-width
- **Line Width (Inner/Infill)**: https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#line-width
- **Infill/Wall Overlap**: https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#infill-wall-overlap
- **Wall Generator**: https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#arachne
- **Seam Position**: https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#seam
- **Ironing**: https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#ironing
- **Shrinkage**: https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#shrinkage
- **Shrinkage Compensation**: https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#shrinkage

### Retraction Settings
- **Retraction**: https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#retraction
- **Z-Hop**: https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#z-hop

### Support Settings
- **Support**: https://github.com/SoftFever/OrcaSlicer/wiki/Supports
- **Tree Supports**: https://github.com/SoftFever/OrcaSlicer/wiki/Supports#tree-supports

### Cooling Settings
- **Cooling**: https://github.com/SoftFever/OrcaSlicer/wiki/Cooling
- **Part Cooling Fan**: https://github.com/SoftFever/OrcaSlicer/wiki/Cooling

## JavaScript Mapping Object

```javascript
const orcaSlicerLinks = {
    // Direct setting name matches
    "Layer Height": "https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#layer-height",
    "Wall Loops": "https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#wall-loops",
    "Infill %": "https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#infill",
    "Infill Pattern": "https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#infill-pattern",
    "Temperature": "https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#temperature",
    "Print Speed": "https://github.com/SoftFever/OrcaSlicer/wiki/Speed",
    "Print Speed (All)": "https://github.com/SoftFever/OrcaSlicer/wiki/Speed",
    "Speed: Outer Wall": "https://github.com/SoftFever/OrcaSlicer/wiki/Speed#outer-wall-speed",
    "Speed: Inner Wall": "https://github.com/SoftFever/OrcaSlicer/wiki/Speed#inner-wall-speed",
    "Speed: Sparse Infill": "https://github.com/SoftFever/OrcaSlicer/wiki/Speed#sparse-infill-speed",
    "Acceleration": "https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#acceleration",
    "Line Width (Inner/Infill)": "https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#line-width",
    "Infill/Wall Overlap": "https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#infill-wall-overlap",
    "Wall Generator": "https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#arachne",
    "Seam Position": "https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#seam",
    "Ironing": "https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#ironing",
    "Shrinkage": "https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#shrinkage",
    
    // Fallback for generic terms
    "_default": "https://github.com/SoftFever/OrcaSlicer/wiki/Calibration"
};
```

## Usage in App

When creating setting cards, include a link:

```javascript
function createSettingCard(setting, goal) {
    const settingName = setting.setting;
    const link = orcaSlicerLinks[settingName] || orcaSlicerLinks["_default"];
    
    // Add link to card HTML
    const linkHTML = `
        <a href="${link}" 
           target="_blank" 
           rel="noopener noreferrer"
           class="text-blue-400 hover:text-blue-300 text-xs">
            📖 View in OrcaSlicer Docs →
        </a>
    `;
    
    // Include in card...
}
```
