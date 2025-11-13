# Quick Start Guide

**Get perfect prints in 3 simple steps!**

---

## Step 1: Choose Your Material 🧵

Click the dropdown and select your filament:
- **Beginners:** Start with **PLA**
- **Functional parts:** Try **PLA Plus** or **PETG**
- **Outdoor use:** Use **ASA**
- **Flexible:** Choose **TPU 95A**

⚠️ **Read any warnings** that appear! They tell you important requirements like:
- Hardened nozzle needed
- Must dry filament first
- Enclosure required
- Ventilation recommended

---

## Step 2: Set Your Priorities 🎚️

Move the sliders to tell the tool what matters most:

### 🔨 Mechanical Strength (0-100%)
**Higher = Stronger parts**
- Set to 80-90% for functional parts, tools, brackets
- Set to 20-30% for decorative items, display models
- If >70%, choose the type of strength you need

### ⚡ Build Time / Speed (0-100%)
**Higher = Faster prints**
- Set to 80-90% for rapid prototyping, quick drafts
- Set to 20-30% for final prints, quality parts

### ✨ Surface Quality (0-100%)
**Higher = Smoother, better looking**
- Set to 80-90% for display models, miniatures, smooth surfaces
- Set to 20-30% for hidden parts, internal components

### 🎯 Dimensional Accuracy (0-100%)
**Higher = More precise dimensions**
- Set to 80-90% for parts that must fit together, threaded holes, assemblies
- Set to 20-30% for decorative/artistic pieces

💡 **Tip:** You can't maximize everything! The tool will warn you about conflicts.

---

## Step 3: Generate & Apply Settings ⚙️

1. Click **"Generate Recommendations"**
2. Read the recommendations for your chosen goals
3. Open **OrcaSlicer** on your computer
4. Apply the suggested settings to your profile

---

## 📖 Reading Results

### Material Baseline
Shows your selected material's starting temperatures and notes.

### Conflict Warnings (if any)
Tells you when goals compete (e.g., strength vs speed) and how to compromise.

### Setting Recommendations
For each goal, you'll see cards like:

```
┌─────────────────────────────────┐
│ Layer Height                    │
│ Value: 0.12 - 0.16mm           │
│                                 │
│ Why: Lower layers = stronger   │
│ Trade-off: Much slower         │
│ [View in OrcaSlicer →]        │
└─────────────────────────────────┘
```

Click the link to learn more about that setting!

---

## 🎯 Quick Examples

### Example 1: Beautiful Display Model
- Material: **PLA Silk**
- Strength: **20%**
- Speed: **20%**
- Surface Quality: **95%**
- Accuracy: **40%**

**Result:** Super smooth with 0.08mm layers, slow outer walls, ironing enabled

---

### Example 2: Strong Functional Bracket
- Material: **PETG**
- Strength: **90%** (XY-Plane)
- Speed: **30%**
- Surface Quality: **20%**
- Accuracy: **80%**

**Result:** 5 walls, 30% infill, precise dimensions for mounting holes

---

### Example 3: Fast Prototype
- Material: **PLA**
- Strength: **10%**
- Speed: **95%**
- Surface Quality: **10%**
- Accuracy: **60%**

**Result:** 0.28mm layers, Lightning infill, high speeds (3× faster than normal)

---

## ❓ Common Questions

**Q: Why are some sliders conflicting?**  
A: You can't maximize strength AND speed at the same time. Choose what matters most.

**Q: Do I need to apply ALL the recommendations?**  
A: No! Apply the ones for your prioritized goals (>70% slider value).

**Q: What if my printer can't do these speeds?**  
A: Lower the speed recommendations to what your printer can handle safely.

**Q: Can I save my settings?**  
A: Yes! In OrcaSlicer, save your tuned settings as a custom preset/profile.

---

## 🆘 Troubleshooting

**"Print failed / part is weak"**
- Check if filament needs drying (see material warnings)
- Increase temperature by +5°C
- Slow down print speed
- Add more walls or infill

**"Taking way too long"**
- Increase layer height to 0.20mm or 0.28mm
- Use Lightning infill instead of Gyroid
- Speed up infill and inner walls
- Reduce infill percentage to 10-15%

**"Dimensions are wrong / holes don't fit"**
- Slow down outer wall to 30-40 mm/s
- Enable shrinkage compensation for ABS/ASA/Nylon
- Print test parts and measure
- Consider drilling holes to final size

---

## 📚 Learn More

- **[Full User Guide](USER_GUIDE.md)** - Complete documentation
- **[Material Guide](USER_GUIDE.md#material-selection-guide)** - All 28 materials explained
- **[Settings Reference](USER_GUIDE.md#orcaslicer-settings-reference)** - Every setting explained
- **[OrcaSlicer Wiki](https://github.com/SoftFever/OrcaSlicer/wiki)** - Official documentation

---

**Happy Printing! 🎉**
