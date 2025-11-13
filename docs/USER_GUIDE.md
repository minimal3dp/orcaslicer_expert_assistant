# OrcaSlicer Settings Recommender - User Guide

**Welcome to the OrcaSlicer Settings Recommender!** This guide will help you get the best print quality, strength, and speed from your 3D printer.

---

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [Understanding the Sliders](#understanding-the-sliders)
3. [Material Selection Guide](#material-selection-guide)
4. [Reading Material Warnings](#reading-material-warnings)
5. [Interpreting Recommendations](#interpreting-recommendations)
6. [Common Use Cases](#common-use-cases)
7. [Troubleshooting](#troubleshooting)
8. [OrcaSlicer Settings Reference](#orcaslicer-settings-reference)

---

## 🚀 Quick Start

### Step 1: Select Your Material
1. Click the **Material** dropdown
2. Choose the filament you're using (e.g., "PLA", "PETG", "ABS")
3. Read any material warnings that appear

### Step 2: Set Your Priorities
Move the sliders based on what matters most for your print:
- **Mechanical Strength**: How strong does it need to be?
- **Build Time**: How fast do you need it?
- **Surface Quality**: How good should it look?
- **Dimensional Accuracy**: How precise must dimensions be?

### Step 3: Click "Generate Recommendations"
You'll get specific settings to adjust in OrcaSlicer!

### Example: Strong Functional Part
- Material: **PLA Plus**
- Strength: **90%** (choose "XY-Plane Strength")
- Build Time: **20%**
- Surface Quality: **30%**
- Accuracy: **70%**

Result: Strong, dimensionally accurate part with 4-6 wall loops and precise outer wall settings.

---

## 🎚️ Understanding the Sliders

### Mechanical Strength (0-100%)

**What it controls:** How strong your printed part will be.

**When to increase:**
- Functional parts (tools, brackets, gears)
- Parts under load or stress
- Outdoor parts exposed to weather

**When to decrease:**
- Decorative items
- Prototypes for fit-checking only
- Speed is more important

**Choose Strength Type (if >70%):**
- **Z-Axis (Layer) Strength**: For vertical loads and pulling forces between layers
- **XY-Plane Strength**: For forces parallel to the print bed (most common)
- **Flexural Strength**: For parts that will bend or flex
- **Compressive Strength**: For parts under crushing/compression loads

**OrcaSlicer Settings Affected:**
- [Wall Loops](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#wall-loops) - More walls = stronger
- [Infill Percentage](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#infill) - More infill = stronger
- [Layer Height](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#layer-height) - Lower = better layer adhesion
- [Temperature](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#temperature) - Hotter = better fusion

---

### Build Time / Speed (0-100%)

**What it controls:** How fast your print will complete.

**When to increase:**
- Prototypes and iterations
- Large prints that would otherwise take days
- When appearance doesn't matter
- Testing fit before final print

**When to decrease:**
- Final prints requiring quality
- Small intricate details
- When using difficult materials

**Trade-offs:**
- ⚡ Higher speed = rougher surface, less detail
- ⚡ Higher speed = weaker layer adhesion
- ⚡ Higher speed = potential for artifacts (ringing, ghosting)

**OrcaSlicer Settings Affected:**
- [Layer Height](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#layer-height) - Higher = faster
- [Speed: Sparse Infill](https://github.com/SoftFever/OrcaSlicer/wiki/Speed) - Can be 150-300+ mm/s
- [Speed: Inner Wall](https://github.com/SoftFever/OrcaSlicer/wiki/Speed) - Faster than outer wall
- [Infill Pattern](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#infill-pattern) - Lightning is fastest
- [Acceleration](https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#acceleration) - Higher = faster

---

### Surface Quality (0-100%)

**What it controls:** How smooth and detailed your print looks.

**When to increase:**
- Display pieces and models
- Parts with visible surfaces
- Miniatures and figurines
- Smooth cosmetic finishes
- When layer lines should be minimal

**When to decrease:**
- Hidden parts or internal components
- Rough draft prototypes
- When speed matters more

**Trade-offs:**
- ✨ Higher quality = dramatically longer print times
- ✨ Lower layer heights reveal more detail but take much longer

**OrcaSlicer Settings Affected:**
- [Layer Height](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#layer-height) - Lower = smoother (0.08-0.12mm)
- [Speed: Outer Wall](https://github.com/SoftFever/OrcaSlicer/wiki/Speed) - Slower = cleaner (40-60 mm/s)
- [Seam Position](https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#seam) - Hide the "zipper"
- [Wall Generator](https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#arachne) - Arachne for details
- [Ironing](https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#ironing) - Glass-smooth top surfaces

---

### Dimensional Accuracy (0-100%)

**What it controls:** How precisely your print matches the design dimensions.

**When to increase:**
- Parts that must fit together (snap-fits, threads)
- Mechanical assemblies
- Replacement parts
- Threaded holes and screws
- Engineering prototypes

**When to decrease:**
- Artistic/organic shapes
- When tolerances don't matter
- Decorative items

**Trade-offs:**
- 🎯 Higher accuracy requires slower speeds
- 🎯 Material shrinkage must be compensated
- 🎯 Requires well-calibrated printer

**OrcaSlicer Settings Affected:**
- [Shrinkage Compensation](https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#shrinkage) - Critical for ABS/ASA/PC
- [Speed: Outer Wall](https://github.com/SoftFever/OrcaSlicer/wiki/Speed) - Very slow (30-50 mm/s)
- [Wall Generator](https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#arachne) - Arachne for precision
- [Layer Height](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#layer-height) - Lower for curved surfaces

---

## 🧵 Material Selection Guide

### Standard Materials (Easy to Print)

#### PLA - Best for Beginners ⭐
- **Best for:** Prototypes, decorative items, learning
- **Pros:** Easy to print, no smell, biodegradable, affordable
- **Cons:** Low heat resistance (60°C), not UV resistant, brittle
- **Tips:** No heated bed required, works on open printers

#### PLA Plus / PLA+
- **Best for:** Stronger functional parts, better than standard PLA
- **Pros:** 2-3× stronger than PLA, less brittle, better layer adhesion
- **Cons:** Still low heat resistance, not outdoor rated
- **Tips:** Great upgrade from standard PLA, similar ease of printing

#### High-Temp PLA (HTPLA)
- **Best for:** Parts that need modest heat resistance
- **Pros:** Can be annealed to 100-110°C HDT, stronger than PLA+
- **Cons:** Requires annealing process, more expensive
- **Tips:** Anneal at 100°C for 30-60 minutes for best results

#### PLA Carbon Fiber (PLA-CF)
- **Best for:** Stiff, rigid parts with matte finish
- **Pros:** Very stiff, minimal warping, matte aesthetic
- **Cons:** Abrasive (needs hardened nozzle), weaker than regular PLA
- **Tips:** ⚠️ Use 0.4mm+ hardened steel nozzle, reduce flow 5-10%

#### PLA Wood-Filled
- **Best for:** Decorative items with wood appearance
- **Pros:** Authentic wood look and smell, can be sanded/stained
- **Cons:** Clogs small nozzles, inconsistent diameter
- **Tips:** Use 0.5mm+ nozzle, vary temperature for color changes

---

### Engineering Materials (Moderate Difficulty)

#### PETG - Workhorse Material ⭐
- **Best for:** Functional parts, outdoor use, food-safe applications
- **Pros:** Strong, impact-resistant, chemical resistant, UV resistant
- **Cons:** Stringing issues, can stick to nozzle, harder to print bridges
- **Tips:** Print 5-10°C hotter than PLA, use Z-hop for travel moves

#### PETG Carbon Fiber (PETG-CF)
- **Best for:** Stiff engineering parts with better heat resistance
- **Pros:** Very stiff, better heat resistance than PETG, chemical resistant
- **Cons:** Abrasive, requires hardened nozzle, expensive
- **Tips:** ⚠️ Hardened nozzle required, 240-260°C

#### ABS - Industrial Standard
- **Best for:** Heat-resistant functional parts, automotive
- **Pros:** High heat resistance (100°C), impact resistant, smooth finish
- **Cons:** Warps badly, toxic fumes, requires enclosure
- **Tips:** ⚠️ Enclosed printer required, print at 100°C bed, ventilation needed

#### ASA - Outdoor Champion
- **Best for:** Outdoor parts, UV exposure, weathering
- **Pros:** Excellent UV resistance, similar to ABS, doesn't yellow
- **Cons:** Same as ABS (warping, fumes, enclosure)
- **Tips:** ⚠️ Like ABS but for outdoors, chamber temp 50-70°C ideal

#### Nylon (PA6 / PA12)
- **Best for:** Gears, bearings, mechanical parts, living hinges
- **Pros:** Very tough, flexible, low friction, chemical resistant
- **Cons:** Very hygroscopic (absorbs water), requires drying
- **Tips:** ⚠️ Must dry 4-6 hours at 70°C before use, use glue stick for adhesion

#### Nylon Carbon Fiber (Nylon-CF)
- **Best for:** High-strength mechanical parts, tooling
- **Pros:** Extremely strong, stiff, and heat resistant
- **Cons:** Abrasive, hygroscopic, requires drying + hardened nozzle
- **Tips:** ⚠️ Dry, hardened nozzle, 260-280°C, enclosure recommended

---

### Flexible Materials (Specialized)

#### TPU 95A - Flexible Standard
- **Best for:** Phone cases, gaskets, seals, dampers
- **Pros:** Rubber-like flexibility, impact resistant, chemical resistant
- **Cons:** Slow printing required, can jam in Bowden setups
- **Tips:** Print at 20-40 mm/s, direct drive extruder ideal

#### TPU 85A - Very Flexible
- **Best for:** Very soft parts, extreme flexibility
- **Pros:** Very soft and stretchy, excellent shock absorption
- **Cons:** Even slower printing, very difficult in Bowden
- **Tips:** 15-30 mm/s max, direct drive nearly required

---

### High-Performance Materials (Advanced)

#### Polycarbonate (PC)
- **Best for:** Bulletproof shields, safety parts, high-impact
- **Pros:** Extremely tough, 140°C heat resistance, transparent
- **Cons:** Requires 270-290°C, needs enclosure, hygroscopic
- **Tips:** ⚠️ Dry thoroughly, enclosure required, all-metal hotend

#### PEEK / PEKK
- **Best for:** Aerospace, medical implants, extreme environments
- **Pros:** 250-300°C heat resistance, biocompatible, chemical resistant
- **Cons:** Requires 360-400°C nozzle, very expensive ($200-400/kg)
- **Tips:** ⚠️ Requires specialty high-temp printer, chamber heat essential

#### PPSU (Polyphenylsulfone)
- **Best for:** Medical devices, sterilization, food contact
- **Pros:** Sterilizable (autoclave safe), biocompatible, chemical resistant
- **Cons:** Requires 340-380°C, very expensive
- **Tips:** ⚠️ Medical-grade applications, specialty printer required

---

### Support Materials

#### PVA - Water Soluble
- **Best for:** Complex support structures with PLA/PETG
- **Pros:** Dissolves completely in water, no residue
- **Cons:** Very hygroscopic, expensive, slow to dissolve
- **Tips:** ⚠️ Store in desiccant, warm water (40°C) dissolves faster

#### PVB - IPA Smoothable
- **Best for:** Smooth transparent parts, dissolvable supports
- **Pros:** Can be smoothed with isopropyl alcohol, transparent
- **Cons:** Fumes from IPA smoothing, hygroscopic
- **Tips:** Smooth in sealed container with IPA vapors

#### HIPS - Limonene Soluble
- **Best for:** ABS support material
- **Pros:** Dissolves in limonene (citrus solvent), prints like ABS
- **Cons:** Requires enclosure, fumes, slower to dissolve than PVA
- **Tips:** Pair with ABS/ASA for best results

---

## ⚠️ Reading Material Warnings

When you select a material, warnings may appear. Here's what they mean:

### 🔧 Hardened Nozzle Required
**Materials:** Carbon fiber, glass fiber, metal-filled filaments

**Why:** These materials contain abrasive particles that will wear out brass nozzles in hours.

**Solution:** Use hardened steel, ruby-tipped, or tungsten carbide nozzles.

**Learn more:** [Hardened Nozzle Guide](https://all3dp.com/2/hardened-nozzle-3d-printing/)

---

### 🏠 Enclosure Required/Recommended
**Materials:** ABS, ASA, Nylon, PC, high-performance materials

**Why:** These materials shrink as they cool, causing warping and layer separation.

**Solution:** Print in an enclosure with chamber temperature 50-70°C.

**Learn more:** [DIY Enclosure Guide](https://www.printables.com/model/130780-ikea-lack-enclosure)

---

### 💧 Hygroscopic - Must Be Dried
**Materials:** Nylon, PETG, PVA, TPU, PC, ABS (slight)

**Why:** These materials absorb moisture from the air, causing bubbling, stringing, and weak prints.

**Solution:** Dry filament at 60-80°C for 4-6 hours before use. Store in desiccant.

**Signs of wet filament:**
- Popping/crackling sounds during printing
- Excessive stringing
- Rough surface finish
- Brittle parts

**Learn more:** [Filament Drying Guide](https://all3dp.com/2/how-to-dry-filament-pla-abs-nylon/)

---

### 💨 Releases Fumes - Ventilation Required
**Materials:** ABS, ASA, Nylon, PC, high-performance materials

**Why:** These materials release potentially harmful volatile organic compounds (VOCs) when heated.

**Solution:** 
- Print in well-ventilated area or with active filtration
- Use HEPA + activated carbon filters
- Consider printing in garage or outdoor area

**Learn more:** [3D Printing Air Filtration](https://www.reddit.com/r/3Dprinting/wiki/filtration/)

---

### ⚠️ Difficult to Print
**Materials:** ABS, ASA, Nylon, PC, PEEK, flexible materials

**Why:** These materials require careful calibration and tuning.

**Tips:**
- Start with well-tuned printer
- Follow manufacturer recommendations exactly
- Use test prints to dial in settings
- Be patient - expect failed prints while learning

**Learn more:** [Printer Calibration Guide](https://teachingtechyt.github.io/calibration.html)

---

### 📉 Prone to Creep
**Materials:** PLA, Nylon, PETG (all thermoplastics to some degree)

**What it means:** Part will slowly deform under sustained load over time.

**When to avoid:** 
- Parts under constant tension or compression
- Threaded connections holding heavy loads
- Bearing mounts with side loads

**Alternatives:** Use PC, PEEK, or metal for sustained loads.

---

### ☀️ UV Resistant
**Materials:** ASA, PETG, Nylon, ABS (moderate)

**What it means:** Won't degrade or become brittle in sunlight.

**Best for:**
- Outdoor planters, signs, decorations
- Automotive parts (under-hood tolerant with ASA/Nylon)
- Garden tools and fixtures

**Learn more:** [UV-Resistant Materials](https://all3dp.com/2/uv-resistant-3d-printing-filament/)

---

### ⚙️ Low Friction
**Materials:** Nylon, PETG (moderate), PC

**What it means:** Self-lubricating properties, reduces wear on moving parts.

**Best for:**
- Gears, bearings, bushings
- Sliding rails and tracks
- Living hinges
- Mechanical linkages

---

### 🧪 Chemical Resistance
**Materials:** PETG, Nylon, PP, PC, PEEK, PPSU

**Resists:** Oils, solvents, acids (varies by material)

**Best for:**
- Automotive/mechanical parts exposed to oils
- Chemical handling containers
- Industrial applications

**Learn more:** [Chemical Resistance Chart](https://omnexus.specialchem.com/polymer-properties/properties/chemical-resistance)

---

### 🔥 Annealable
**Materials:** PLA, PETG, Nylon, PC

**What it means:** Can be heat-treated after printing to increase strength and heat resistance.

**How to anneal:**
1. Print the part normally
2. Place in oven at material-specific temperature (typically 80-120°C)
3. Hold for 30-60 minutes
4. Cool slowly to room temperature

**Results:** 
- Increased HDT (heat deflection temperature)
- Higher strength
- Part will shrink 1-3% (account for this in design)

**Learn more:** [Annealing Guide by CNC Kitchen](https://www.cnckitchen.com/blog/annealing-of-3d-printed-parts)

---

## 📖 Interpreting Recommendations

### Goal Sections
Recommendations are organized by your priorities:
- **Tensile Strength (Z-Axis)** - Layer adhesion
- **XY-Plane Strength** - In-plane strength
- **Build Time (Speed)** - Print speed optimization
- **Surface Quality** - Aesthetic finish
- **Dimensional Accuracy** - Precision

### Settings Cards
Each setting card shows:
- **Setting Name**: What to adjust in OrcaSlicer
- **Recommended Value**: Specific number or range
- **Explanation**: Why this helps your goal
- **Trade-off**: What you're giving up

### Conflict Warnings
If your goals conflict, you'll see expert advice on compromises:
- **Strength vs. Speed**: Can't maximize both
- **Quality vs. Speed**: Higher quality = slower
- **Accuracy vs. Speed**: Precision requires slow, careful movements

---

## 💡 Common Use Cases

### 1. Display Model / Miniature
**Goal:** Best possible appearance

**Settings:**
- Strength: 20%
- Build Time: 10%
- Surface Quality: 95%
- Accuracy: 50%

**Material:** PLA or PLA Silk

**Key Changes:**
- Layer height: 0.08-0.12mm
- Outer wall speed: 40 mm/s
- Enable ironing for top surfaces

---

### 2. Functional Bracket / Mount
**Goal:** Strong and precise

**Settings:**
- Strength: 90% (XY-Plane)
- Build Time: 30%
- Surface Quality: 20%
- Accuracy: 80%

**Material:** PLA Plus, PETG, or ABS

**Key Changes:**
- 5-6 wall loops
- 30% gyroid infill
- Slow outer walls (40 mm/s)
- Check shrinkage compensation

---

### 3. Rapid Prototype for Fit Check
**Goal:** Fast iteration

**Settings:**
- Strength: 10%
- Build Time: 95%
- Surface Quality: 10%
- Accuracy: 60%

**Material:** PLA (fastest)

**Key Changes:**
- Layer height: 0.28-0.32mm
- Infill: Lightning or 10%
- Inner walls: 150+ mm/s
- Sparse infill: 250+ mm/s

---

### 4. Outdoor Part (Plant Hanger, Sign)
**Goal:** Weather resistant

**Settings:**
- Strength: 70% (XY-Plane)
- Build Time: 40%
- Surface Quality: 40%
- Accuracy: 50%

**Material:** ASA (best) or PETG (good)

**Key Changes:**
- 4-5 wall loops
- 20-30% infill
- Use enclosure for ASA
- Consider slightly higher temperature for better fusion

---

### 5. Flexible Seal / Gasket
**Goal:** Flexibility and durability

**Settings:**
- Strength: 60% (Flexural)
- Build Time: 20%
- Surface Quality: 30%
- Accuracy: 70%

**Material:** TPU 95A

**Key Changes:**
- Print very slowly (20-30 mm/s all speeds)
- 2-3 wall loops
- 10-20% infill (more = stiffer)
- Direct drive extruder strongly recommended

---

### 6. High-Temperature Part
**Goal:** Heat resistance

**Settings:**
- Strength: 80% (depends on use)
- Build Time: 30%
- Surface Quality: 40%
- Accuracy: 70%

**Material:** ABS, ASA, or PC

**Key Changes:**
- Enclosure required
- Bed temp: 100-110°C
- Chamber temp: 50-70°C
- Consider annealing for even higher HDT

---

### 7. Threaded Insert / Precise Assembly
**Goal:** Dimensional precision

**Settings:**
- Strength: 60% (XY-Plane)
- Build Time: 20%
- Surface Quality: 30%
- Accuracy: 95%

**Material:** PLA Plus or PETG

**Key Changes:**
- Outer wall speed: 30-40 mm/s
- Calibrate shrinkage compensation
- Use Arachne wall generator
- Print pilot holes slightly undersized, drill to final size

---

## 🔧 Troubleshooting

### "My part is weak and breaking easily"
**Possible causes:**
1. **Wet filament** - Dry your filament (especially Nylon, PETG, TPU)
2. **Low infill** - Increase to 20-30% for functional parts
3. **Not enough walls** - Use 3-4 minimum, 5-6 for strength
4. **Temperature too low** - Increase nozzle temp by +5°C increments
5. **Print speed too fast** - Slow down for better layer adhesion
6. **Wrong strength type** - Match strength type to the load direction

---

### "Print is taking forever!"
**Solutions:**
1. **Increase layer height** - 0.20mm or 0.28mm instead of 0.12mm
2. **Use Lightning infill** - Fastest pattern (but no structural support)
3. **Speed up infill** - 150-250 mm/s for sparse infill
4. **Reduce infill** - 10-15% for non-structural parts
5. **Increase acceleration** - If your printer can handle it (5000-10000 mm/s²)
6. **Choose speed** - Set Build Time slider to 80-90%

---

### "Surface looks terrible / lots of layer lines"
**Solutions:**
1. **Reduce layer height** - 0.12mm or 0.08mm for quality
2. **Slow outer wall speed** - 40-50 mm/s maximum
3. **Enable ironing** - For glass-smooth top layers
4. **Check seam placement** - Use "Aligned" or "Back" seam, or paint it
5. **Dry filament** - Wet filament causes rough surfaces
6. **Calibrate flow rate** - Over-extrusion causes blobs

---

### "Holes/threads don't fit"
**Solutions:**
1. **Calibrate shrinkage** - Especially for ABS, ASA, PC (99.4-99.7%)
2. **Slow down outer walls** - 30-40 mm/s for precision
3. **Print holes smaller** - Drill/ream to final size
4. **Horizontal expansion** - Compensate for "elephant's foot"
5. **Use Arachne** - Better at maintaining target dimensions
6. **XY compensation** - Negative value to shrink outer perimeter slightly

---

### "Warping and corners lifting"
**Solutions:**
1. **Material issue** - ABS/ASA/Nylon require enclosure
2. **Bed adhesion** - Use glue stick, hairspray, or PEI sheet
3. **Bed temperature** - Increase to material recommendations
4. **Draft shield** - Enable in OrcaSlicer to reduce cooling
5. **Brim or raft** - Add extra adhesion surface
6. **Enclosure** - Critical for high-shrinkage materials

---

### "Stringing and blobs everywhere"
**Solutions:**
1. **Wet filament** - Dry immediately, especially PETG/Nylon
2. **Temperature too high** - Reduce by -5°C increments
3. **Retraction settings** - Increase retraction distance (0.5-2mm for direct drive)
4. **Enable Z-hop** - Lifts nozzle during travel moves
5. **Reduce travel speed** - Slower travels reduce ooze
6. **Wipe while retracting** - Enable in OrcaSlicer

---

### "Material-specific issues"
- **Nylon won't stick** - Use glue stick on glass/PEI, 70-80°C bed
- **TPU jams in extruder** - Reduce speed to 20-30 mm/s, check extruder tension
- **PLA getting brittle** - Old/wet PLA degrades, replace spool
- **PETG sticking to nozzle** - Reduce temperature -5°C, enable Z-hop
- **ABS delaminating** - Enclosure required, increase chamber temp
- **Carbon fiber clogging** - Use larger nozzle (0.5mm+), hardened steel

---

## 📚 OrcaSlicer Settings Reference

### Core Settings

#### [Layer Height](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#layer-height)
- **Location:** Print Settings > Quality
- **Range:** 0.08mm - 0.32mm (max 75% of nozzle diameter)
- **Impact:**
  - Lower = better quality, stronger Z-axis, MUCH slower
  - Higher = faster prints, visible layer lines, weaker Z-axis
- **Recommendation:** 0.20mm for balanced, 0.12mm for quality, 0.28mm for speed

#### [Wall Loops (Perimeters)](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#wall-loops)
- **Location:** Print Settings > Strength
- **Range:** 2-8+ loops
- **Impact:** Primary driver of XY-plane strength
- **Recommendation:** 2-3 for decorative, 4-5 for functional, 6-8 for maximum strength

#### [Infill Percentage](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#infill)
- **Location:** Print Settings > Strength
- **Range:** 0% - 100%
- **Impact:**
  - 10-15%: Standard, good for most parts
  - 30-50%: Functional parts with good strength
  - 60-80%: Maximum compressive strength
- **Recommendation:** 15% for most, 30% for functional, 80% for compressive loads

#### [Infill Pattern](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#infill-pattern)
- **Location:** Print Settings > Strength
- **Common Patterns:**
  - **Lightning:** Fastest, no structural support (visual models only)
  - **Gyroid:** Strong multi-directional, good for most parts
  - **Grid/Cubic:** Best for vertical loads and compression
  - **Rectilinear:** Fast, adequate strength
  - **Honeycomb:** Strong but slow
- **Recommendation:** Gyroid for strength, Lightning for speed

---

### Temperature Settings

#### [Nozzle Temperature](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#temperature)
- **Location:** Filament Settings > Temperature
- **Material Ranges:**
  - PLA: 190-220°C
  - PLA+: 205-225°C
  - PETG: 230-250°C
  - ABS: 230-250°C
  - ASA: 240-260°C
  - Nylon: 240-270°C
  - TPU: 220-240°C
  - PC: 270-310°C
- **Impact:** Higher = better layer fusion, more stringing

#### [Bed Temperature](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#bed-temperature)
- **Location:** Filament Settings > Temperature
- **Material Ranges:**
  - PLA: 50-60°C (or none)
  - PETG: 70-80°C
  - ABS/ASA: 100-110°C
  - Nylon: 70-90°C
  - PC: 110-130°C

---

### Speed Settings

#### [Speed: Outer Wall](https://github.com/SoftFever/OrcaSlicer/wiki/Speed)
- **Location:** Print Settings > Speed
- **Range:** 30-80 mm/s
- **Impact:** Most visible surface, slow for quality/accuracy
- **Recommendation:** 40-60 mm/s for quality, 30-40 mm/s for precision

#### [Speed: Inner Wall](https://github.com/SoftFever/OrcaSlicer/wiki/Speed)
- **Location:** Print Settings > Speed
- **Range:** 60-150 mm/s
- **Impact:** Hidden, can be much faster than outer wall
- **Recommendation:** 2-3× outer wall speed

#### [Speed: Sparse Infill](https://github.com/SoftFever/OrcaSlicer/wiki/Speed)
- **Location:** Print Settings > Speed
- **Range:** 80-300+ mm/s
- **Impact:** Hidden, can be VERY fast
- **Recommendation:** 150-250 mm/s on capable printers

#### [Acceleration](https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#acceleration)
- **Location:** Print Settings > Speed > Acceleration
- **Range:** 1000-10000+ mm/s²
- **Impact:** How quickly printer reaches target speed
- **Recommendation:** 3000-5000 mm/s² conservative, 7000-10000 mm/s² for speed

---

### Advanced Settings

#### [Line Width](https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#line-width)
- **Location:** Print Settings > Advanced > Extrusion Width
- **Range:** 100-125% of nozzle diameter
- **Impact:** Wider = better fusion, stronger parts
- **Recommendation:** 110-120% for strength (e.g., 0.48mm on 0.4mm nozzle)

#### [Wall Generator: Arachne](https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#arachne)
- **Location:** Print Settings > Advanced > Wall Generator
- **Options:** Classic or Arachne
- **Impact:** Arachne uses variable line width for better detail and accuracy
- **Recommendation:** Arachne for quality/accuracy, Classic for speed

#### [Seam Position](https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#seam)
- **Location:** Print Settings > Advanced > Seam
- **Options:**
  - Random: Distributed around object
  - Aligned: Creates vertical "zipper" line
  - Back/Rear: Hides seam at back
  - **Seam Painting:** Manual control (best)
- **Recommendation:** Aligned for easy cleanup, Rear to hide, Paint for control

#### [Ironing](https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#ironing)
- **Location:** Print Settings > Advanced > Ironing
- **Impact:** Flattens top surfaces for glass-smooth finish
- **Trade-off:** Adds significant time
- **Recommendation:** Enable for display pieces, disable for functional

#### [Shrinkage Compensation](https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#shrinkage)
- **Location:** Filament Settings > Advanced > Shrinkage
- **Format:** Percentage (e.g., 99.5% = 0.5% shrinkage)
- **Material Values:**
  - PLA: 100% (no compensation)
  - PETG: 99.8%
  - ABS: 99.4-99.6%
  - ASA: 99.4-99.6%
  - Nylon: 99.3-99.5%
  - PC: 99.3-99.5%
- **Recommendation:** Calibrate with test prints

---

### Retraction Settings

#### [Retraction Distance](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration#retraction)
- **Location:** Filament Settings > Retraction
- **Direct Drive:** 0.5-1.5mm
- **Bowden:** 4-8mm
- **Impact:** Too little = stringing, too much = clogs
- **Recommendation:** Start with manufacturer defaults, adjust by 0.2mm increments

#### [Z-Hop](https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings#z-hop)
- **Location:** Print Settings > Advanced > Z-hop
- **Range:** 0.2-0.6mm
- **Impact:** Lifts nozzle during travel to prevent knocking prints
- **Recommendation:** Enable for PETG, flexible materials, complex geometry

---

### Support Settings

#### [Support Type](https://github.com/SoftFever/OrcaSlicer/wiki/Supports)
- **Normal:** Standard breakaway supports
- **Tree:** Organic supports, easier removal, less scarring
- **Recommendation:** Tree for complex models, Normal for simple overhangs

#### [Support Material](https://github.com/SoftFever/OrcaSlicer/wiki/Multi-Material#support-interface)
- **Same material:** Standard
- **PVA:** Water-soluble (with PLA/PETG)
- **HIPS:** Limonene-soluble (with ABS)
- **Recommendation:** Soluble supports for complex internal structures

---

### Cooling Settings

#### [Part Cooling Fan](https://github.com/SoftFever/OrcaSlicer/wiki/Cooling)
- **Location:** Filament Settings > Cooling
- **Material Guidelines:**
  - PLA: 100% (aggressive cooling)
  - PETG: 30-50% (moderate cooling)
  - ABS/ASA: 0-20% (minimal cooling)
  - Nylon: 0-10% (minimal cooling)
  - TPU: 30-60% (moderate cooling)
- **Impact:** Too much cooling = warping/layer delamination, too little = drooping overhangs

---

## 🔗 Additional Resources

### Official OrcaSlicer Documentation
- [OrcaSlicer Wiki](https://github.com/SoftFever/OrcaSlicer/wiki)
- [Calibration Guide](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration)
- [Advanced Settings](https://github.com/SoftFever/OrcaSlicer/wiki/Advanced-Settings)

### Calibration Tools
- [Teaching Tech Calibration](https://teachingtechyt.github.io/calibration.html) - Comprehensive calibration for all printers
- [Ellis' Print Tuning Guide](https://ellis3dp.com/Print-Tuning-Guide/) - Advanced tuning for Voron/Klipper
- [CNC Kitchen Testing](https://www.cnckitchen.com/) - Scientific testing of materials and settings

### Material Guides
- [Simplify3D Material Guide](https://www.simplify3d.com/resources/materials-guide/)
- [All3DP Material Guides](https://all3dp.com/1/3d-printer-filament-types-3d-printing-3d-filament/)
- [Prusa Material Table](https://help.prusa3d.com/materials)

### Community Resources
- [r/3Dprinting Wiki](https://www.reddit.com/r/3Dprinting/wiki/index)
- [r/FixMyPrint](https://www.reddit.com/r/FixMyPrint/) - Troubleshooting help
- [OrcaSlicer GitHub Issues](https://github.com/SoftFever/OrcaSlicer/issues) - Report bugs, request features

---

## 📞 Need More Help?

If you have questions or suggestions for this tool:
- **GitHub Issues:** [Report bugs or request features](https://github.com/minimal3dp/orcaslicer_expert_assistant/issues)
- **Community:** Share your results and tips with other users

---

**Made with ❤️ for the 3D printing community**

*Last updated: November 12, 2025*
