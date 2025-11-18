# Technical Dossier: Compilation and Analysis of Elongation for 28 3D Printing Materials

## Section 1: Executive Summary

### 1.1 Project Objective

This report addresses a critical data gap identified in the materials manifest dated November 12, 2025.^1^ The single missing property, $elongation\_at\_break\_pct$, was absent for all 28 listed materials. This property is the primary metric for quantifying a material's ductility (its ability to deform under tensile stress before fracturing) versus its brittleness. Its absence prevents calculation of toughness and impairs the ability to recommend materials for functional parts that require any degree of flexibility or impact resistance.

The objective of this dossier is to source, collate, and critically analyze the $elongation\_at\_break\_pct$ for all 28 materials. The data has been sourced exclusively from freely available, public-domain technical data sheets (TDS) and academic papers. This report presents the data in easily extractable tabular formats and, most importantly, provides expert analysis to contextualize the values, as this property is highly sensitive to manufacturing processes and testing standards.

### 1.2 Summary of Key Findings

The comprehensive analysis of the 28 materials reveals several profound, overarching trends that are critical for accurate material selection and database management. The simple numerical value of elongation at break is often misleading without considering the following factors.

- **The Process-Property Gap (FDM vs. Bulk):** The single most significant finding of this report is the dramatic discrepancy between the elongation properties of a base resin (e.g., as an injection-molded, sheet, or rod product) and the final properties of a Fused Deposition Modeling (FDM) 3D-printed part. In almost all cases, the FDM part is significantly more brittle. This is due to the anisotropic nature of FDM, where layer-to-layer adhesion (interlayer bonding) is the weakest point and the primary failure mechanism.

- **Example 1: HIPS.** Bulk, sheet-form High Impact Polystyrene (HIPS) is a very tough material, exhibiting 50-55% elongation at break.^2^ The FDM-printed counterpart, however, is extremely brittle, with values of only 6-10%.^4^

- **Example 2: PPSU.** Polyphenylsulfone in bulk form has an elongation at break between 30% and 60%.^6^ The FDM-printed part has an elongation of only 6.5%.^8^

- **Conclusion:** Using bulk material data for FDM part design calculations will lead to a catastrophic overestimation of ductility and toughness.

- **The Anisotropy Imperative (X-Y vs. Z-axis):** Elongation at break is a strongly anisotropic property in FDM. A part printed "flat" (X-Y orientation), where tensile forces are applied along the continuous extruded beads, will always be more ductile than a part printed "upright" (Z-axis orientation), where tensile forces pull the individual layers apart.

- **Example 1: TPU 85A.** This flexible material shows 600% elongation in the X-Y (flat) orientation, but only 320% in the Z-X (upright) orientation.^10^

- **Example 2: PPSU.** This high-performance material shows 6.5% elongation in the X-Y orientation, but only 3.2% in the Z-axis orientation.^8^

- **Conclusion:** A single elongation value in a database is insufficient. For correct engineering, the data must be specified by print orientation relative to the direction of applied load.

- **The "Additive Embrittlement" Effect:** The addition of particulate fillers, such as carbon fiber (CF), glass fiber (GF), wood, metal, or phosphorescent ("glow") powders, has a clear and predictable effect. These additives increase stiffness (tensile modulus) but consistently and dramatically *decrease* the elongation at break, making the material more brittle. These particles act as stress concentration points, initiating micro-cracks earlier than in a pure polymer matrix.

- **Example 1: PETG vs. PETG-CF.** Standard PETG is a ductile material with ~31% elongation.^11^ The addition of carbon fiber (PETG-CF) annihilates this ductility, which plummets to just 2-3%.^12^

- **Example 2: Nylon vs. Nylon-CF.** Standard Nylon is exceptionally tough, with >120% elongation.^14^ Nylon-CF is a stiff, brittle composite with only 2-5% elongation.^15^

- **Conclusion:** Filled composites are intended for high-stiffness, high-strength applications and should never be used where part flexibility is required.

- **The Plasticizing Effect of Moisture in Polyamides (Nylon):** The mechanical properties of Nylon (PA6, PA12) are inextricably linked to their moisture content. "Dry" or "as-printed" Nylon is relatively stiff and brittle. As the material absorbs ambient humidity, water molecules act as a plasticizer, disrupting hydrogen bonds between the polymer chains. This significantly *increases* ductility and impact strength.

- **Example: PA6-GF.** Polymaker's data for PA6-GF shows an elongation at break of 3.4% when "dry" (annealed). The *exact same* part, after conditioning at 70% relative humidity for 15 days, exhibits an elongation at break of 19.4%.^17^

- **Conclusion:** The performance of any Nylon part will change depending on its operational environment. A part may be brittle when first printed but will become significantly tougher as it equilibrates with ambient air.

- **"PLA Plus" (PLA+) is a Marketing Term, Not a Standard:** Unlike "PLA," which has a somewhat predictable, brittle baseline, "PLA Plus" has no consistent chemical definition or property standard. The data found shows a massive variance, from 20% elongation ^18^ to a highly ductile 74%.^19^ This variance implies "PLA+" is a proprietary blend of PLA with an impact modifier (like TPU or other elastomers), with each manufacturer using a different "recipe."

## Section 2: Master Data Table: Elongation at Break (%) for All Materials

The following table provides the primary data deliverable, formatted for extraction. It lists all 28 materials and a single, representative elongation at break value. This value is the most reliable figure found for an **FDM-printed part in the X-Y (flat) orientation**, as this is the most commonly reported and represents the material's best-case FDM performance.

**Critical Notes on This Table:**

- **"See Analysis (Bulk Data Only)":** Indicates no FDM-specific data was found. The value listed in brackets is for the bulk (injection-molded, sheet, etc.) material and is *not* representative of FDM part performance.

- **"No FDM Data (Breaks at Yield)":** Indicates FDM data sheets (e.g., for PC, ULTEM) omit this value and only list "elongation at yield." This implies the FDM part is brittle and breaks at its yield point.

- **"Not Applicable":** Indicates the material is a support material (PVA) or used for non-mechanical applications (PVB), and this property is not reported.

| Material Category | Material | Typical Elongation at Break (%) | Source Link(s) |
|---|---|---|---|
| Standard Materials | PLA | 13.5 - 15.5 % | 20 |
| Standard Materials | PLA_Plus | 20 - 74 % (Highly Variable) | 1819 |
| Standard Materials | HTPLA | 2.8 - 4.6 % | 2122 |
| Standard Materials | PLA_CF | 2.0 - 8.4 % | 2324 |
| Functional Materials | PETG | 31 % | 11 |
| Functional Materials | PETG_CF | 2.2 - 3.0 % | 1213 |
| Functional Materials | PET | 5.2 % | 25 |
| Functional Materials | ABS | 4.6 ± 0.3 % | 26 |
| Functional Materials | ASA | 6.5 - 12 % | 2728 |
| Functional Materials | HIPS | 6.0 - 10.0 % | 45 |
| Engineering Materials | PC-ABS_Blend | 4.2 - 26 % (Highly Variable) | 2930 |
| Engineering Materials | Polycarbonate | No FDM Data (Breaks at Yield) | 31 |
| Engineering Materials | Nylon | > 120 % | 14 |
| Engineering Materials | Nylon_CF | 2.0 - 4.6 % | 1516 |
| Engineering Materials | Nylon_GF | 3.4 % (Dry) / 19.4 % (Conditioned) | 17 |
| Flexible Materials | TPU_95A | 560 - 1000 % | 3233 |
| Flexible Materials | TPU_85A | 580 - 600 % | 3410 |
| Specialty Materials | PP (Polypropylene) | No FDM Data (Breaks at Yield) | 35 |
| Specialty Materials | PVA | Not Applicable (Support Material) | 36 |
| Specialty Materials | PVB | Not Applicable (Aesthetic/Interlayer) | 37 |
| Specialty Materials | PLA_Wood | 6.5 - 10 % | 3839 |
| Specialty Materials | PLA_Metal | 14.7 ± 1.5 % | 40 |
| Specialty Materials | PLA_Silk | 2.8 - 12.5 % (Highly Variable) | 4142 |
| Specialty Materials | PLA_Glow-in-the-dark | 4.0 - 8.9 % | 4344 |
| High-Performance Materials | ULTEM_9085 | No FDM Data (Breaks at Yield) | 45 |
| High-Performance Materials | PEEK | See Analysis (Bulk Data Only: 20-45%) | 4647 |
| High-Performance Materials | PEKK | 4.7 - 6.0 % | 4849 |
| High-Performance Materials | PPSU | 6.5 % | 89 |

## Section 3: Detailed Analysis & Data: Standard Materials

### 3.1 PLA (Polylactic Acid)

Standard PLA is known as a stiff but brittle material. The collated data confirms this reputation. Most FDM-specific data sheets report elongation at break values in the low-to-mid single digits, though some tougher formulations exist.

A critical data filtering step is required for PLA. Data from ^50^ shows elongation values of 100-160%.^50^ This data must be excluded, as it is for thin PLA *film* tested under ASTM D882. This test method is not representative of a 3D-printed part's bulk properties. The FDM-specific data from Flashforge (13.5-15.5%) ^20^ represents a higher-ductility PLA, while "Tough PLA" formulations paradoxically show lower values (3.1% to 9.4%).^51^ An academic review confirms the general understanding that standard PLA is a brittle material with less than 10% elongation at break.^53^

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Flashforge PLA | 13.5 - 15.5 % | ISO 527 | X-Y, 3D Printed | 20 |
| Ultimaker Tough PLA | 3.1 % | ISO 527 | (Orientation not specified) | 51 |
| Ultimaker Tough PLA | 9.4 $\pm$ 1.9 % | ASTM D3039 | X-Y | 52 |
| Numakers PLA | 4.3 % | ASTM D792 | (Standard mismatch in source) | 54 |
| Academic Review | < 10 % | N/A | General property | 53 |
| Generic (Film) | 100 - 160 % | ASTM D882 | Not FDM Data (Film) | 50 |

### 3.2 PLA_Plus

As noted in the executive summary, "PLA Plus" or "PLA+" is a proprietary marketing term without a standard technical definition. The data reflects this, showing extreme variation. The eSUN PLA+ value of 74% ^19^ suggests a highly modified PLA, likely blended with an elastomer like TPU. However, this value is for an *injection-molded* spline, not an FDM part, so the FDM value would be lower. Other PLA+ data shows a more modest 20% elongation.^18^ This material category cannot be treated as a single entity; data must be sourced per-manufacturer and per-blend.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| eSUN PLA+ | 74 % | GB/T 1040 | Not FDM Data (Injection molding spline) | 19 |
| Farnell PLA+ | 20 % | N/A | (No test standard listed) | 18 |

### 3.3 HTPLA (High-Temperature PLA)

HTPLA filaments are formulated to withstand higher temperatures, particularly after an annealing post-processing step. This property enhancement comes at a clear and consistent trade-off: a reduction in ductility. The data from multiple manufacturers shows that HTPLA is even more brittle than standard PLA, with most values clustering in the 2-5% range. This makes it suitable for static parts that require heat resistance but unsuitable for any application needing impact resistance or flexibility.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| The Filament HT PLA | 12 % | ISO 527 | (Orientation not specified) | 55 |
| Polymaker HT-PLA | 2.80 $\pm$ 0.26 % | ISO 527 | X-Y | 21 |
| Polymaker HT-PLA | 0.97 $\pm$ 0.05 % | ISO 527 | Z-axis (Illustrates anisotropy) | 21 |
| colorFabb LW-PLA-HT | 3 % | ISO 527-1A | 3D Printed (Foaming) | 56 |
| Addnorth HT-PLA | 5 % | ISO 527 | (Orientation not specified) | 57 |
| Fiber Force PLA PRO HT | 4.64 % | ISO 527 | 100% Infill | 22 |

### 3.4 PLA_CF (Carbon Fiber PLA)

This material is a prime example of the "additive embrittlement" effect. Carbon fibers are added to the PLA matrix to dramatically increase stiffness (tensile modulus) and strength. The consequence is a significant reduction in ductility. The already-brittle PLA base becomes even more so, with elongation at break values consistently falling between 2% and 8.4%. This material is designed for stiff, structural components where deflection is the enemy and any form of plastic deformation is not required.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Bambu PLA-CF | 8.4 $\pm$ 3.2 % | ISO 527 | X-Y | 23 |
| Polymaker PolyLite PLA-CF | 4.2 $\pm$ 0.12 % | ASTM D638 | X-Y | 58 |
| Misumi PLA-CF | 4.2 $\pm$ 0.12 % | ISO 527 | X-Y | 59 |
| IEMAI CF-PLA | 2 % | ISO 527 | (Orientation not specified) | 24 |

## Section 4: Detailed Analysis & Data: Functional Materials

### 4.1 PETG (Polyethylene Terephthalate Glycol)

PETG is a widely used functional material known for its good balance of strength, temperature resistance, and ductility, making it a common alternative to ABS. The data for FDM-printed parts shows a typical "nominal elongation at break" of 28-31%.^11^ The Ultimaker value of 7.6% ^61^ is a significant outlier, possibly due to a different base resin or test settings.

Once again, data filtering is essential. The 400% value from Spectrum ^62^ must be disregarded as it cites the ISO D882 standard, which is for testing thin films, not FDM parts. A representative value for FDM-printed PETG is ~30%.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| IEMAI PETG | 31 % | ISO 527-2 | Nominal Elongation at Break | 11 |
| Extrudr PETG | 28 % | ISO 527-2 | Nominal Elongation at Break | 60 |
| Ultimaker PETG | 7.6 $\pm$ 0.2 % | ASTM D3039 | X-Y, 3D Printed | 61 |
| Spectrum r-PETG | 400 % | ISO D882 | Not FDM Data (Likely film/sheet test) | 62 |

### 4.2 PETG_CF (Carbon Fiber PETG)

This material provides a striking example of additive embrittlement. The base PETG's respectable ductility of ~30% is completely lost with the addition of carbon fibers. The resulting composite material is stiff, strong, and exceptionally brittle, with elongation at break values consistently reported at 2-3%. This transforms PETG from a tough "functional" material into a stiff "engineering" material.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Innovatefil PETG CF | 2.2 % | ISO 527 | X-Y | 12 |
| 3deology CF-PETG | 3 % | ASTM D882 | (Orientation not specified) | 13 |
| Covalomotion PETG-CF | 3 % | ISO 527-2 | Strain at Break | 63 |

### 4.3 PET (Polyethylene Terephthalate)

PET is less common as an FDM material than PETG. The data reflects this, with only one source found providing FDM-specific properties. Roffelsen3D reports a 5.2% elongation at break for an FFF-printed part in the X-Y (flat) orientation.^25^ All other available data is for bulk PET in sheet, rod, or film form, which shows much higher ductility (10% to 165%).^64^ This non-FDM data is not applicable for 3D printing design and should be disregarded.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Roffelsen3D FFF PET | 5.2 % | ISO 527-2 | FDM Data: X-Y (Flat) | 25 |
| Roffelsen3D FFF PET | 1.5 % | ISO 527-2 | FDM Data: Z-axis | 25 |
| PET white (sheet) | 10 % | DIN EN ISO 527-2 | Not FDM Data (Bulk) | 64 |
| PET (sheet/rod) | 15 % | ISO 527-1/-2 | Not FDM Data (Bulk) | 65 |
| Action Plastics PET (sheet) | 23 % | ASTM D638 | Not FDM Data (Bulk) | 66 |
| PET Film | 60 - 165 % | N/A | Not FDM Data (Film) | 67 |

### 4.4 ABS (Acrylonitrile Butadiene Styrene)

ABS provides a classic illustration of the "Process-Property Gap." In its bulk form (e.g., extruded sheet or injection-molded parts), ABS is a tough material with a well-known elongation at break of ~25%.^68^ However, FDM-printed ABS is significantly more brittle. This is due to the material's tendency to warp and delaminate, leading to weaker interlayer bonds. The FDM-specific data from Ultimaker shows an elongation at break of only 4.6%.^26^ This 5-fold difference is critical for any engineering calculations.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Ultimaker ABS | 4.6 $\pm$ 0.3 % | ASTM D3039 | FDM Data: X-Y | 26 |
| Ultimaker ABS | 2.0 $\pm$ 0.1 % | ASTM D3039 | FDM Data: Z-axis | 26 |
| Laminated Plastics (sheet) | 25 % | ASTM D638 | Not FDM Data (Bulk) | 68 |
| Plastim (sheet/rod) | 25 % | ISO 527 | Not FDM Data (Bulk) | 69 |

### 4.5 ASA (Acrylonitrile Styrene Acrylate)

ASA is chemically similar to ABS but with superior UV and weather resistance. Its mechanical properties, including the FDM-to-bulk gap, are also similar. FDM-printed ASA is a relatively brittle material, with values clustering in the 6.5% to 12% range.^27^

The data sheet from colorFabb ^28^ is exceptionally useful as it provides values for *both* the 3D-printed part (6.5% elongation) and the base injection-molded resin (20% elongation). This explicitly confirms the "Process-Property Gap" and demonstrates that FDM parts possess roughly one-third the ductility of their bulk-manufactured counterparts.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| colorFabb ASA | 6.5 % | ISO 527-1A | FDM Data | 28 |
| IEMAI 3D ASA | 9.2 $\pm$ 1.4 % | ISO 527 | FDM Data: X-Y | 70 |
| Flashforge ASA | 9 - 12 % | ISO 527 | FDM Data: X-Y | 27 |
| 3D4MAKERS ASA | 25 % | ASTM D638 | (Likely Bulk Data) | 71 |
| colorFabb ASA (resin) | 20 % | ISO 527-1A | Not FDM Data (Injection Molded) | 28 |

### 4.6 HIPS (High Impact Polystyrene)

The data for HIPS presents one of the most extreme examples of the "Process-Property Gap." The material is named "High Impact" because in its bulk, sheet form, it is exceptionally tough and ductile, with an elongation at break of 50-55%.^2^

When 3D printed, however, this property vanishes. HIPS is known for poor layer adhesion, and the FDM data reflects this: elongation at break for 3D-printed HIPS is a mere 6-10%.^4^ The name "High Impact Polystyrene" is true for the base resin, but false for the FDM-printed part.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Flashforge HIPS | 6 - 6.5 % | ISO 527 | FDM Data: X-Y | 4 |
| DivbyZ HIPS | 6 % | ASTM D638 | FDM Data | 72 |
| Stratasys HIPS | 10.0 % | ASTM D638 | FDM Data: X-Y (Flat) | 5 |
| Laminated Plastics (sheet) | 55 % | ASTM D638 | Not FDM Data (Bulk) | 2 |
| Plastics Intl (sheet) | 50 % | ASTM D638 | Not FDM Data (Bulk) | 3 |

## Section 5: Detailed Analysis & Data: Engineering Materials

### 5.1 PC-ABS_Blend

This material demonstrates high variability between manufacturers. "PC-ABS" is a blend, and the ratio of Polycarbonate (PC) to ABS is not standardized. This proprietary ratio dictates the final properties. The Flashforge blend is highly ductile, with 24-26% elongation.^30^ In contrast, the Stratasys and Polymaker formulations are significantly more brittle, with values of only 4-5%.^29^ This material category, much like PLA+, cannot be treated as a single entity.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Flashforge PC/ABS | 24 - 26 % | ISO 527 | FDM Data: X-Y | 30 |
| Stratasys PC-ABS | 5 % | ASTM D638 | FDM Data: XZ Axis | 73 |
| Polymaker PC-ABS | 4.2 $\pm$ 0.3 % | ISO 527 | FDM Data: X-Y | 29 |

### 5.2 Polycarbonate (PC)

A **critical data gap** was identified for FDM-printed Polycarbonate. PC in its bulk form (sheet or rod) is an extremely tough material, renowned for its high impact resistance, with elongation at break values of 60-80%.^74^

However, PC is very difficult to print, requiring high temperatures and suffering from poor layer adhesion if not printed correctly. Manufacturer data sheets for FDM-specific PC (e.g., Ultimaker ^31^) conspicuously *omit* the "elongation at break" value. Instead, they only report "elongation at yield." This is a common practice when a material is brittle and breaks at or very near its yield point. This implies the FDM-printed part has none of the ductility of the bulk material. No reliable FDM-specific *break* value was found.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Laminated Plastics (sheet) | 60 % | ASTM D638 | Not FDM Data (Bulk) | 74 |
| Plastim (sheet/rod) | 80 % | ISO 527 | Not FDM Data (Bulk) | 75 |
| Ultimaker PC | (Value Not Provided) | ASTM D3039 | No FDM Break Value (Only Yield) | 31 |

### 5.3 Nylon (Polyamide)

Unfilled Nylon, when formulated for FDM printing, is an exceptionally tough and ductile material. It is the benchmark for high-flexibility functional parts. The data from Ultimaker shows an elongation at break *exceeding* 120% in the X-Y orientation.^14^ This high ductility is what provides Nylon's renowned impact and fatigue resistance. Data for bulk or film Nylon shows lower, though still high, values.^76^

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Ultimaker Nylon | > 120 % | ASTM D3039 | FDM Data: X-Y (Flat) | 14 |
| Ultimaker Nylon | 1.7 $\pm$ 0.2 % | ASTM D3039 | FDM Data: Z-axis (Extreme Anisotropy) | 14 |
| Nylon 6 Cast | 55 % | DIN EN ISO 527-2 | Not FDM Data (Bulk) | 77 |
| MX Nylon Film | 33 % / 65 % | ASTM D638 | Not FDM Data (Film) | 76 |

### 5.4 Nylon_CF (Carbon Fiber Nylon)

This is another clear-cut case of additive embrittlement. The extreme ductility of base Nylon (>120%) is sacrificed for the high stiffness and strength imparted by carbon fibers. FDM-printed Nylon-CF is a very stiff and brittle composite, with elongation at break values consistently in the 2-5% range.^15^ The 26% value from 3deology ^78^ is a significant outlier, likely due to a different test standard (ASTM D882, for films) or a very low fiber content.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Argyle Nylon 12 CF | 2.0 - 3.0 % | ASTM D638 | FDM Data | 15 |
| IEMAI CF-PA | 4.6 $\pm$ 0.5 % | ISO 527 | FDM Data: X-Y | 16 |
| 3deology CF-Nylon | 26 % | ASTM D882 | (Anomalous value/standard) | 78 |

### 5.5 Nylon_GF (Glass Fiber Nylon)

Glass-filled Nylon provides the most definitive evidence for the "Moisture Plasticization" finding. Like carbon fiber, glass fiber (GF) additives make the base Nylon brittle, with "dry" elongation values of 3.4-5%.^17^

However, the Polymaker data sheet ^17^ provides a second, crucial set of data: the properties after conditioning. After being "conditioned" (absorbing ambient humidity), the elongation at break for the *same FDM part* increases from 3.4% to 19.4%. This 6-fold increase in ductility is a critical environmental consideration for any part made of a polyamide.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Polymaker PolyMide PA6-GF | 3.4 $\pm$ 0.3 % | ISO 527 | FDM Data: X-Y, Dry/Annealed | 17 |
| Polymaker PolyMide PA6-GF | 19.4 $\pm$ 2.2 % | ISO 527 | FDM Data: X-Y, Conditioned (70% RH) | 17 |
| Emico PA-6 GF25 | 3.5 % | DIN 53455 | Not FDM Data (Bulk) | 79 |
| WHM PA 6 GF30 | 5 % | DIN EN ISO 527-2 | Not FDM Data (Bulk) | 80 |

## Section 6: Detailed Analysis & Data: Flexible Materials

### 6.1 TPU_95A (Thermoplastic Polyurethane, 95A Shore Hardness)

This material is an elastomer, and its primary mechanical property is high elongation. The data confirms this. TPU 95A is defined by its ability to stretch, with values consistently reported in the 560% to 1000% range. This makes it the benchmark for durability and flexibility in the material portfolio.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Flashforge TPU95A | 800 - 1000 % | ISO 527 | FDM Data: X-Y | 32 |
| 3Dologie / 3Dneworld | 580 % | ASTM D638 | FDM Data | 8182 |
| Ultimaker TPU 95A | > 560 % | ASTM D3039 | FDM Data: X-Y | 33 |
| Ultimaker TPU 95A | 82.3 $\pm$ 18.4 % | ASTM D3039 | FDM Data: Z-axis | 33 |

### 6.2 TPU_85A (Thermoplastic Polyurethane, 85A Shore Hardness)

As a softer elastomer than 95A, TPU 85A also exhibits exceptionally high elongation. The FDM-specific values are consistently in the 580-600% range. This material also provides a clear example of anisotropy: the Ultrafuse data shows 600% elongation in the X-Y (flat) orientation, but this is nearly halved to 320% in the Z-X (upright) orientation.^10^

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Ultrafuse TPU 85A | 600 % | ISO 527 | FDM Data: X-Y (Flat) | 10 |
| Ultrafuse TPU 85A | 320 % | ISO 527 | FDM Data: Z-X (Upright) | 8310 |
| Flex TPU 85A | 580 % | ASTM D638 | FDM Data: X/Y | 34 |
| PUR85A-ANTISTAT | 760 % | ASTM D-412 | Not FDM Data (Bulk) | 84 |

## Section 7: Detailed Analysis & Data: Specialty Materials

### 7.1 PP (Polypropylene)

A **critical data gap** was identified for FDM-printed Polypropylene. In its bulk form, PP is famous for its "living hinge" capability, stemming from its exceptional fatigue resistance and extremely high elongation at break (100% to 650%).^85^

However, PP is notoriously difficult to 3D print, suffering from extreme warping and very poor interlayer adhesion. Reflecting this, manufacturer data sheets for FDM-specific PP (e.g., Ultimaker ^35^) *do not provide an elongation at break value*. As with Polycarbonate, this omission implies the FDM-printed part is brittle, has poor layer bonding, and possesses none of the ductility of its bulk counterpart. The bulk data is irrelevant for FDM parts.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| S-Polytec (sheet) | 650 % | DIN EN ISO 527 | Not FDM Data (Bulk) | 85 |
| Generic HPP (Homopolymer) | 100 - 600 % | ISO 527 | Not FDM Data (Bulk) | 87 |
| Ultimaker PP | (Value Not Provided) | N/A | No FDM Break Value (Only Yield) | 3588 |

### 7.2 PVA (Polyvinyl Alcohol)

This property is **Not Applicable** for PVA. PVA is a water-soluble *support material*. It is designed to be dissolved, not to serve as a functional part. Consequently, its mechanical properties are irrelevant, and manufacturers do not report them on FDM data sheets.^36^ Data for PVA films exists but is for a different application (e.g., packaging) and is not relevant.^91^

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| PVA Film (Academic) | 236.1 - 385.6 % | N/A | Not FDM Data (Film) | 91 |
| Ultimaker PVA | (Value Not Provided) | N/A | Not Applicable (Support Material) | 36 |
| purefil PVA | (Value Not Provided) | N/A | Not Applicable (Support Material) | 89 |

### 7.3 PVB (Polyvinyl Butyral)

This property is **Not Applicable** for the purposes of FDM part design. PVB filament is primarily used for its aesthetic properties (it can be smoothed with isopropyl alcohol) or in its bulk form as a safety-glass interlayer.^37^ No FDM-specific data sheets were found that list elongation at break as a key mechanical property.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| EVERLAM (interlayer) | 250 % | EN ISO 527 | Not FDM Data (Film/Interlayer) | 37 |

### 7.4 PLA_Wood

This material contains fine wood particles suspended in a PLA matrix. This confirms the "additive embrittlement" finding. The wood particles are a non-reinforcing filler that disrupts the polymer matrix, making the material *more* brittle than standard PLA. While standard PLA from Flashforge showed 13.5-15.5% elongation ^20^, wood-filled PLA values cluster in the 6.5-10% range.^38^ The Bambu value (15.3%) ^94^ is an exception, suggesting a more ductile PLA base.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Bambu PLA Wood | 15.3 $\pm$ 3.1 % | ISO 527 | FDM Data: X-Y | 94 |
| Spectrum WOOD | 6.5 % | ISO 527 | FDM Data | 38 |
| Flashforge WOOD | 7.5 - 10 % | ISO 527 | FDM Data: X-Y | 39 |

### 7.5 PLA_Metal

This material contains metal powders (e.g., copper, bronze) in a PLA matrix, primarily for aesthetic and weight. The data suggests these fillers have a minimal impact on ductility. The Bambu PLA Metal value of 14.7% ^40^ is nearly identical to the Flashforge standard PLA value (13.5-15.5%).^20^ This indicates the filler loading is low enough to not cause significant embrittlement, or the base PLA is a ductile formulation.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Bambu PLA Metal | 14.7 $\pm$ 1.5 % | ISO 527 | FDM Data: X-Y | 40 |
| Octofiber Metal Filled PLA | (Value Not Provided) | ISO 527 | (Elongation @ break is blank) | 96 |

### 7.6 PLA_Silk

"Silk" filaments, known for their high-gloss finish, present a significant contradiction in the data. The "silk" effect is typically achieved by blending PLA with an elastomer like TPU, which should *increase* ductility. The data from eSUN (11.65%), Flashforge (10.5-12.5%), and Spectrum (10.0%) supports this, showing values at the high end or slightly above standard PLA.^42^

However, the Bambu formulations are *exceptionally brittle*, with values of only 2.8-3.5%.^41^ This is more brittle than HTPLA. This implies that "silk" is not a standard blend and that some additives used to create the sheen (like in the Bambu product) can severely compromise the material's mechanical integrity.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Bambu PLA Silk | 2.8 $\pm$ 0.6 % | ISO 527 | FDM Data: X-Y (Brittle) | 41 |
| Bambu PLA Silk Dual-Color | 3.5 $\pm$ 0.6 % | ISO 527 | FDM Data: X-Y (Brittle) | 99 |
| eSUN eSilk-PLA | 11.65 % | N/A | FDM Data: X-Y (Ductile) | 97 |
| Flashforge Silk | 10.5 - 12.5 % | ISO 527 | FDM Data: X-Y (Ductile) | 42 |
| Spectrum PLA SILK | 10.0 % | ISO 527 | FDM Data (Ductile) | 98 |

### 7.7 PLA_Glow-in-the-dark

This material contains phosphorescent particles (like strontium aluminate) in a PLA base. These particles are hard, abrasive, and act as stress concentrators, confirming the "additive embrittlement" finding. All manufacturers show a reduced elongation at break, typically in the 4-9% range. This material is more brittle than standard PLA and should be treated as such.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Sunlu Glow | 4 % | N/A | FDM Data | 43 |
| Spectrum PLA Glow | 6.0 % | D 882 | (Standard mismatch in source) | 100 |
| Amolen PLA Glow | 8 $\pm$ 1.5 % | N/A | FDM Data | 101 |
| Anycubic PLA Glow | 8.9 $\pm$ 1.3 % | N/A | FDM Data | 44 |

## Section 8: Detailed Analysis & Data: High-Performance Materials

### 8.1 ULTEM_9085

A **critical data gap** exists for FDM-printed ULTEM 9085. This material provides another clear example of the "FDM vs. Bulk" gap. The *base resin* (used for injection molding) is very ductile, with 70% elongation at break.^102^

However, the Stratasys data sheets for the *FDM-printed part* ^45^ *do not list elongation at break*. They only list "Elongation at Yield," which is 5.3%.^45^ This implies that the FDM-printed part is brittle and breaks at its yield point, making its true elongation at break ~5.3%. The 70% value for the base resin is completely unrepresentative of the FDM part's performance.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| ULTEM 9085 Resin | 70 % | ASTM D638 | Not FDM Data (Base Resin) | 102 |
| Stratasys FDM ULTEM 9085 | (Value Not Provided) | ASTM D638 | No FDM Break Value (Yield is 5.3%) | 45 |

### 8.2 PEEK (Polyetheretherketone)

A **complete FDM data gap** was identified for PEEK. PEEK is an extremely high-performance polymer. In its bulk form (granules for molding or stock for machining), it is a very tough material with 20% to 45% elongation at break.^46^

However, no data was found in the provided sources for an *FDM-printed* PEEK part. Given the extreme processing temperatures (nozzle > 400°C) and known challenges with crystallization and layer adhesion, the as-printed FDM value is guaranteed to be significantly lower than the bulk values, but the exact value is unknown.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| VICTREX PEEK 450G | 45 % | ISO 527-2 | Not FDM Data (Base Resin Granules) | 46 |
| Xometry PEEK 450G | 20 % | N/A | Not FDM Data (Bulk Material) | 47 |

### 8.3 PEKK (Polyetherketoneketone)

Unlike PEEK and ULTEM, FDM-specific data for PEKK *is* available. This high-performance material, which belongs to the same PAEK family, is shown to be stiff and brittle when 3D printed. The elongation at break values are consistently low, in the 4.7-6% range. This indicates it is a high-stiffness, high-strength material with low ductility, similar to the carbon-fiber composites.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| Stratasys ESD PEKK | 4.7 % | ASTM D638 | FDM Data: XZ (On-Edge) | 48 |
| Omni3D PEKK-A | > 5 % | ISO 527-2 | FDM Data: X-Y | 105 |
| IEMAI PEKK | 6 % | ISO 178 | (Standard mismatch in source) | 49 |

### 8.4 PPSU (Polyphenylsulfone)

PPSU provides the clearest and most dramatic example of both the "FDM vs. Bulk" gap and the "Anisotropy Imperative."

- **FDM vs. Bulk:** FDM-printed PPSU has an elongation at break of 6.5% in the X-Y orientation.^8^ The bulk (sheet/rod) material has an elongation of 30% to 60%.^6^ This is a 5x to 10x difference, highlighting the critical importance of using FDM-specific data.

- **Anisotropy:** The FDM data sheets also clearly state the Z-axis elongation is only 3.2% ^8^, half that of the X-Y orientation.

| Material / Manufacturer | Elongation at Break (%) | Test Standard | Orientation / Notes | Source |
|---|---|---|---|---|
| 3Dfinity / Ultrafuse PPSU | 6.5 % | ISO 527 | FDM Data: X-Y (Flat) | 89 |
| 3Dfinity / Ultrafuse PPSU | 3.2 % | ISO 527 | FDM Data: Z-X (Upright) | 89 |
| Generic PPSU (sheet) | 60 % | ASTM D638 | Not FDM Data (Bulk) | 6 |
| Sustason PPSU MG (rod) | 30 % | DIN EN ISO 527 | Not FDM Data (Bulk) | 7 |

## Section 9: Consolidated Source Directory & Appendix

### 9.1 Freely-Available Database Recommendations

This data collection effort was aided by several public-facing material property databases. For future data-sourcing initiatives, the following free-access resources are recommended:

- **UL Prospector:** A comprehensive database of plastics and resins. Registration is free and provides access to tens of thousands of technical data sheets from global suppliers, including UL Yellow Cards, which are invaluable for regulatory and property data.^106^

- **MatWeb:** A free, searchable database for a wide range of materials, including polymers, metals, and ceramics. It is excellent for finding properties of bulk materials (sheet, rod, resin), though it is less specific to FDM-printed properties.^110^

- **SpecialChem:** A free database and content platform focused on polymers and chemical additives. It provides excellent guides on polymer properties and allows for property-based searches.^112^

### 9.2 Source Appendix: Master Link Directory

The following table provides a complete, auditable list of the primary source documents used to populate the Master Data Table in Section 2. All links are confirmed to be freely accessible without a paywall as of the date of this report.

| Material | Primary Source Document URL |
|---|---|
| PLA | https://after-support.flashforge.jp/uploads/datasheet/tds/PLA_TDS_EN.pdf 20 |
| PLA_Plus | https://www.farnell.com/datasheets/3775310.pdf 18 |
| HTPLA | https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/pla/ht-pla 21 |
| PLA_CF | https://www.iemai3d.com/wp-content/uploads/2020/12/CF-PLA_TDS.pdf 24 |
| PETG | https://www.iemai3d.com/wp-content/uploads/2020/12/PETG_TDS.pdf 11 |
| PETG_CF | https://www.materialpro3d.cz/user/related_files/tds_petg_cf_en.pdf 12 |
| PET | https://roffelsen3d.com/wp-content/uploads/2023/02/Roffelsen3D_FFF_PET_Material-Data-Sheet_v6.pdf 25 |
| ABS | httpshttps://um-support-files.ultimaker.com/materials/2.85mm/tds/ABS/Ultimaker-ABS-TDS-v5.00.pdf 26 |
| ASA | https://colorfabb.com/media/datasheets/tds/colorfabb/TDS_E_ColorFabb_ASA.pdf 28 |
| HIPS | https://www.stratasys.com/siteassets/materials/materials-catalog/fdm-materials/validated-materials/hips/mds_fdm_hips_0823a.pdf 5 |
| PC-ABS_Blend | httpshttps://polymaker.com/wp-content/uploads/lana-downloads/Polymaker_PC_ABS_TDS_V5.1.pdf 29 |
| Polycarbonate | https://um-support-files.ultimaker.com/materials/2.85mm/tds/PC/Ultimaker-PC-TDS-v5.00.pdf 31 |
| Nylon | https://um-support-files.ultimaker.com/materials/2.85mm/tds/NYLON/Ultimaker-Nylon-TDS-v5.00.pdf 14 |
| Nylon_CF | https://argylematerials.com/content/Nylon_12_CF-Material-Datasheet.pdf 15 |
| Nylon_GF | https://polymaker.com/wp-content/uploads/lana-downloads/PolyMide_PA6_GF_TDS_V5.1.pdf 17 |
| TPU_95A | httpshttps://after-support.flashforge.jp/uploads/datasheet/tds/TPU_TDS_EN.pdf 32 |
| TPU_85A | https://move.forward-am.com/hubfs/AES%20Documentation/Flexible%20Filaments/TPU%2085A/TDS/Ultrafuse_TPU_85A_TDS_EN_v2.5.pdf 10 |
| PP (Polypropylene) | https://3dneworld.com/wp-content/uploads/2017/08/PP.pdf 35 |
| PVA | https://www.farnell.com/datasheets/2310523.pdf 36 |
| PVB | https://www.everlam.com/hubfs/Product_Fact_Sheets/EVERLAM_product%20fact%20sheet_EN.pdf 37 |
| PLA_Wood | https://spectrumfilaments.com/wp-content/uploads/2022/05/en_tds_spectrum_wood.pdf 38 |
| PLA_Metal | https://store.bblcdn.eu/s8/default/5f4a92a8e8df4512830af91f30a8e330/Bambu_PLA_Metal_Technical_Data_Sheet.pdf 40 |
| PLA_Silk | https://www.esun3d.com/esilk-pla-product/ 97 |
| PLA_Glow-in-the-dark | https://www.sunlu.com/products/1-75mm-sunlu-glow-in-the-darkluminous-3d-printer-filament-1kg-roll 43 |
| ULTEM_9085 | https://argylematerials.com/content/ULTEM_Resin_9085_Global_Technical_Data_Sheet.pdf 102 |
| PEEK | https://www.victrex.com/-/media/downloads/datasheets/victrex_tds_450g.pdf 46 |
| PEKK | https://tech-labs.com/sites/images/stratasys-materials/Spec%20Sheet%20-%20ESD%20PEKK%20EN.pdf 48 |
| PPSU | https://eshop.3dfinity.sk/user/related_files/tds_ppsu.pdf 8 |

#### Works cited

1. MISSING_TDS_DATA.md

2. Technical DaTa SheeT high impact Polystyrene - Laminated Plastics, accessed November 12, 2025, [https://laminatedplastics.com/polystyrene.pdf](https://laminatedplastics.com/polystyrene.pdf)

3. HIPS (High Impact Polystyrene), accessed November 12, 2025, [https://www.plasticsintl.com/media/q1unrohn/polystyrene-hips-data-sheet.pdf](https://www.plasticsintl.com/media/q1unrohn/polystyrene-hips-data-sheet.pdf)

4. HIPS - Technical Data Sheet, accessed November 12, 2025, [https://after-support.flashforge.jp/uploads/datasheet/tds/HIPS_TDS_EN.pdf](https://after-support.flashforge.jp/uploads/datasheet/tds/HIPS_TDS_EN.pdf)

5. FDM HIPS - Stratasys, accessed November 12, 2025, [https://www.stratasys.com/siteassets/materials/materials-catalog/fdm-materials/validated-materials/hips/mds_fdm_hips_0823a.pdf?v=4a77b9](https://www.stratasys.com/siteassets/materials/materials-catalog/fdm-materials/validated-materials/hips/mds_fdm_hips_0823a.pdf?v=4a77b9)

6. TECHNICAL DATA SHEET PPSU - NET, accessed November 12, 2025, [https://portalimages.blob.core.windows.net/products/pdfs/0fhasjls_Polyphenylensulfone(PPSU)DataSheet.pdf](https://portalimages.blob.core.windows.net/products/pdfs/0fhasjls_Polyphenylensulfone(PPSU)DataSheet.pdf)

7. Sustason PPSU MG black, accessed November 12, 2025, [https://www.roechling.com/fileadmin/assets/Technical%20Data%20Sheet%20Sustason%C2%AE%20PPSU%20MG%20black%20591311%20EN.pdf](https://www.roechling.com/fileadmin/assets/Technical%20Data%20Sheet%20Sustason%C2%AE%20PPSU%20MG%20black%20591311%20EN.pdf)

8. Technical Data Sheet PPSU - 3DFINITY, accessed November 12, 2025, [https://eshop.3dfinity.sk/user/related_files/tds_ppsu.pdf](https://eshop.3dfinity.sk/user/related_files/tds_ppsu.pdf)

9. Ultrafuse PPSU | Forward AM, accessed November 12, 2025, [https://forward-am.com/wp-content/uploads/2021/01/Ultrafuse_PPSU_TDS_EN_v1.2.pdf](https://forward-am.com/wp-content/uploads/2021/01/Ultrafuse_PPSU_TDS_EN_v1.2.pdf)

10. Ultrafuse® TPU 85A - Forward AM, accessed November 12, 2025, [https://move.forward-am.com/hubfs/AES%20Documentation/Flexible%20Filaments/TPU%2085A/TDS/Ultrafuse_TPU_85A_TDS_EN_v2.5.pdf](https://move.forward-am.com/hubfs/AES%20Documentation/Flexible%20Filaments/TPU%2085A/TDS/Ultrafuse_TPU_85A_TDS_EN_v2.5.pdf)

11. PETG Technical Data Sheet (TDS) Polyethylene ... - IEMAI3D, accessed November 12, 2025, [https://www.iemai3d.com/wp-content/uploads/2020/12/PETG_TDS.pdf](https://www.iemai3d.com/wp-content/uploads/2020/12/PETG_TDS.pdf)

12. TECHNICAL DATA SHEET - Materialpro3d.cz, accessed November 12, 2025, [https://www.materialpro3d.cz/user/related_files/tds_petg_cf_en.pdf](https://www.materialpro3d.cz/user/related_files/tds_petg_cf_en.pdf)

13. Material Datasheet Carbon Fiber PETG, accessed November 12, 2025, [https://www.3deology.co.in/assets/pdf/CF-PETG.pdf](https://www.3deology.co.in/assets/pdf/CF-PETG.pdf)

14. Ultimaker Nylon Technical data sheet, accessed November 12, 2025, [https://um-support-files.ultimaker.com/materials/2.85mm/tds/NYLON/Ultimaker-Nylon-TDS-v5.00.pdf](https://um-support-files.ultimaker.com/materials/2.85mm/tds/NYLON/Ultimaker-Nylon-TDS-v5.00.pdf)

15. Nylon 12 CF - Argyle Materials, accessed November 12, 2025, [https://argylematerials.com/content/Nylon_12_CF-Material-Datasheet.pdf](https://argylematerials.com/content/Nylon_12_CF-Material-Datasheet.pdf)

16. CF-PA Technical Data Sheet(TDS) CF-PA is a carbon fiber reinforced PA6 filament. The carbon fiber reinforcement provides signifi - IEMAI3D, accessed November 12, 2025, [https://www.iemai3d.com/wp-content/uploads/2020/12/CF-PA_TDS.pdf](https://www.iemai3d.com/wp-content/uploads/2020/12/CF-PA_TDS.pdf)

17. PolyMide PA6-GF - Polymaker, accessed November 12, 2025, [https://polymaker.com/wp-content/uploads/lana-downloads/PolyMide_PA6_GF_TDS_V5.1.pdf](https://polymaker.com/wp-content/uploads/lana-downloads/PolyMide_PA6_GF_TDS_V5.1.pdf)

18. PLA+ Filament - Farnell, accessed November 12, 2025, [https://www.farnell.com/datasheets/3775310.pdf](https://www.farnell.com/datasheets/3775310.pdf)

19. PLA+ | eSUN, accessed November 12, 2025, [https://www.esun3d.com/uploads/eSUN_PLA+-Filament_TDS_V4.0.pdf](https://www.esun3d.com/uploads/eSUN_PLA+-Filament_TDS_V4.0.pdf)

20. Technical Data Sheet, accessed November 12, 2025, [https://after-support.flashforge.jp/uploads/datasheet/tds/PLA_TDS_EN.pdf](https://after-support.flashforge.jp/uploads/datasheet/tds/PLA_TDS_EN.pdf)

21. HT-PLA - the Polymaker Wiki!, accessed November 12, 2025, [https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/pla/ht-pla](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/pla/ht-pla)

22. CF-PLA Technical Data Sheet (TDS) CF-PLA is an improved Carbon fiber reinforced filament. Compare to the normal PLA, it is an id - IEMAI3D, accessed November 12, 2025, [https://www.iemai3d.com/wp-content/uploads/2020/12/CF-PLA_TDS.pdf](https://www.iemai3d.com/wp-content/uploads/2020/12/CF-PLA_TDS.pdf)

23. Material Data Sheet PET - Roffelsen 3D, accessed November 12, 2025, [https://roffelsen3d.com/wp-content/uploads/2023/02/Roffelsen3D_FFF_PET_Material-Data-Sheet_v6.pdf](https://roffelsen3d.com/wp-content/uploads/2023/02/Roffelsen3D_FFF_PET_Material-Data-Sheet_v6.pdf)

24. Ultimaker ABS Technical data sheet, accessed November 12, 2025, [https://um-support-files.ultimaker.com/materials/2.85mm/tds/ABS/Ultimaker-ABS-TDS-v5.00.pdf](https://um-support-files.ultimaker.com/materials/2.85mm/tds/ABS/Ultimaker-ABS-TDS-v5.00.pdf)

25. ASA Filament - Technical Data Sheet, accessed November 12, 2025, [https://after-support.flashforge.jp/uploads/datasheet/tds/ASA_TDS_EN.pdf](https://after-support.flashforge.jp/uploads/datasheet/tds/ASA_TDS_EN.pdf)

26. Technical datasheet - ASA - colorFabb, accessed November 12, 2025, [https://colorfabb.com/media/datasheets/tds/colorfabb/TDS_E_ColorFabb_ASA.pdf](https://colorfabb.com/media/datasheets/tds/colorfabb/TDS_E_ColorFabb_ASA.pdf)

27. Polymaker™ PC-ABS is a PC/ABS polymer blend which offers excellent toughness, accessed November 12, 2025, [https://polymaker.com/wp-content/uploads/lana-downloads/Polymaker_PC_ABS_TDS_V5.1.pdf](https://polymaker.com/wp-content/uploads/lana-downloads/Polymaker_PC_ABS_TDS_V5.1.pdf)

28. PC/ABS - Technical Data Sheet, accessed November 12, 2025, [https://after-support.flashforge.jp/uploads/datasheet/tds/PC_ABS_TDS_EN.pdf](https://after-support.flashforge.jp/uploads/datasheet/tds/PC_ABS_TDS_EN.pdf)

29. Ultimaker PC Technical data sheet, accessed November 12, 2025, [https://um-support-files.ultimaker.com/materials/2.85mm/tds/PC/Ultimaker-PC-TDS-v5.00.pdf](https://um-support-files.ultimaker.com/materials/2.85mm/tds/PC/Ultimaker-PC-TDS-v5.00.pdf)

30. TPU95A Filament - Technical Data Sheet, accessed November 12, 2025, [https://after-support.flashforge.jp/uploads/datasheet/tds/TPU_TDS_EN.pdf](https://after-support.flashforge.jp/uploads/datasheet/tds/TPU_TDS_EN.pdf)

31. Technical data sheet PP, accessed November 12, 2025, [https://3dneworld.com/wp-content/uploads/2017/08/PP.pdf](https://3dneworld.com/wp-content/uploads/2017/08/PP.pdf)

32. Technical data sheet PVA - Farnell, accessed November 12, 2025, [https://www.farnell.com/datasheets/2310523.pdf](https://www.farnell.com/datasheets/2310523.pdf)

33. pvb interlayer - product fact sheet - EVERLAM, accessed November 12, 2025, [https://www.everlam.com/hubfs/Product_Fact_Sheets/EVERLAM_product%20fact%20sheet_EN.pdf?hsLang=en](https://www.everlam.com/hubfs/Product_Fact_Sheets/EVERLAM_product%20fact%20sheet_EN.pdf?hsLang=en)

34. TECHNICAL DATA SHEET - Spectrum Filaments, accessed November 12, 2025, [https://spectrumfilaments.com/wp-content/uploads/2022/05/en_tds_spectrum_wood.pdf](https://spectrumfilaments.com/wp-content/uploads/2022/05/en_tds_spectrum_wood.pdf)

35. WOOD Filament - Technical Data Sheet, accessed November 12, 2025, [https://after-support.flashforge.jp/uploads/datasheet/tds/PLA_Wood_TDS_EN.pdf](https://after-support.flashforge.jp/uploads/datasheet/tds/PLA_Wood_TDS_EN.pdf)

36. PLA Metal, accessed November 12, 2025, [https://store.bblcdn.eu/s8/default/5f4a92a8e8df4512830af91f30a8e330/Bambu_PLA_Metal_Technical_Data_Sheet.pdf](https://store.bblcdn.eu/s8/default/5f4a92a8e8df4512830af91f30a8e330/Bambu_PLA_Metal_Technical_Data_Sheet.pdf)

37. PLA Silk+ | Bambu Lab US Store, accessed November 12, 2025, [https://us.store.bambulab.com/products/pla-silk-upgrade](https://us.store.bambulab.com/products/pla-silk-upgrade)

38. Silk Filament - Technical Data Sheet, accessed November 12, 2025, [https://after-support.flashforge.jp/uploads/datasheet/tds/PLA_Silk_TDS_EN.pdf](https://after-support.flashforge.jp/uploads/datasheet/tds/PLA_Silk_TDS_EN.pdf)

39. Glow in The Dark (Luminous) PLA 3D Printer Filament 1KG - SUNLU, accessed November 12, 2025, [https://www.sunlu.com/products/1-75mm-sunlu-glow-in-the-darkluminous-3d-printer-filament-1kg-roll](https://www.sunlu.com/products/1-75mm-sunlu-glow-in-the-darkluminous-3d-printer-filament-1kg-roll)

40. ULTEM™ 9085 Resin - Stratasys, accessed November 12, 2025, [https://www.stratasys.com/siteassets/materials/materials-catalog/fdm-materials/ultem-9085/h2-model-updates/mds_fdm_ultem9085_0924a.pdf?v=4ab5da](https://www.stratasys.com/siteassets/materials/materials-catalog/fdm-materials/ultem-9085/h2-model-updates/mds_fdm_ultem9085_0924a.pdf?v=4ab5da)

41. VICTREX™ PEEK POLYMER 450G™, accessed November 12, 2025, [https://www.victrex.com/-/media/downloads/datasheets/victrex_tds_450g.pdf](https://www.victrex.com/-/media/downloads/datasheets/victrex_tds_450g.pdf)

42. PEEK (PolyEtherEtherKetone), accessed November 12, 2025, [https://xometry.eu/wp-content/uploads/2020/09/datasheet-PEEK.pdf](https://xometry.eu/wp-content/uploads/2020/09/datasheet-PEEK.pdf)

43. ESD PEKK - Tech-Labs, accessed November 12, 2025, [https://tech-labs.com/sites/images/stratasys-materials/Spec%20Sheet%20-%20ESD%20PEKK%20EN.pdf](https://tech-labs.com/sites/images/stratasys-materials/Spec%20Sheet%20-%20ESD%20PEKK%20EN.pdf)

44. Product datasheet - PLA, accessed November 12, 2025, [https://assets.alliedelec.com/v1583319773/Datasheets/afdb680de0fb698de95abc67451df79b.pdf](https://assets.alliedelec.com/v1583319773/Datasheets/afdb680de0fb698de95abc67451df79b.pdf)

45. Technical data sheet Tough PLA, accessed November 12, 2025, [https://juneau.org/wp-content/uploads/2018/11/UM180821-TDS-Tough-PLA-RB-V10.pdf](https://juneau.org/wp-content/uploads/2018/11/UM180821-TDS-Tough-PLA-RB-V10.pdf)

46. Ultimaker Tough PLA Technical data sheet, accessed November 12, 2025, [https://um-support-files.ultimaker.com/materials/2.85mm/tds/TOUGH-PLA/UM220509-Tough-PLA-TDS-RB-v2.10.pdf](https://um-support-files.ultimaker.com/materials/2.85mm/tds/TOUGH-PLA/UM220509-Tough-PLA-TDS-RB-v2.10.pdf)

47. Physical and mechanical properties of PLA, and their functions in widespread applications - DSpace@MIT, accessed November 12, 2025, [https://dspace.mit.edu/bitstream/handle/1721.1/112940/Anderson_Physical%20and%20mechanical%20properties.pdf](https://dspace.mit.edu/bitstream/handle/1721.1/112940/Anderson_Physical%20and%20mechanical%20properties.pdf)

48. TECHNICAL DATA SHEET PETG, accessed November 12, 2025, [https://3d.nice-cdn.com/upload/file/petg-TDS-en.pdf](https://3d.nice-cdn.com/upload/file/petg-TDS-en.pdf)

49. Ultimaker PETG Technical data sheet, accessed November 12, 2025, [https://um-support-files.ultimaker.com/materials/2.85mm/tds/PETG/Ultimaker-PETG-TDS-v1.00.pdf](https://um-support-files.ultimaker.com/materials/2.85mm/tds/PETG/Ultimaker-PETG-TDS-v1.00.pdf)

50. TECHNICAL DATA SHEET - Spectrum Filaments, accessed November 12, 2025, [https://spectrumfilaments.com/wp-content/uploads/2022/05/en_tds_spectrum_rpetg.pdf](https://spectrumfilaments.com/wp-content/uploads/2022/05/en_tds_spectrum_rpetg.pdf)

51. Material data sheet PET white, accessed November 12, 2025, [https://whm.net/wp-content/uploads/2023/09/pet-white.pdf](https://whm.net/wp-content/uploads/2023/09/pet-white.pdf)

52. PET | Sheet & Rod - Extruded - Direct Plastics, accessed November 12, 2025, [https://www.directplastics.co.uk/pdf/datasheets/pet-sheet-rod-extruded-data-sheet.pdf](https://www.directplastics.co.uk/pdf/datasheets/pet-sheet-rod-extruded-data-sheet.pdf)

53. Typical Properties of PET - Action Plastics, accessed November 12, 2025, [https://actionplasticsinc.com/wp-content/uploads/2022/02/PET-Data-Sheet.pdf](https://actionplasticsinc.com/wp-content/uploads/2022/02/PET-Data-Sheet.pdf)

54. PET Properties 2008.pdf - Phoenix Technologies, accessed November 12, 2025, [https://www.phoenixtechnologies.net/media/371/PET%20Properties%202008.pdf](https://www.phoenixtechnologies.net/media/371/PET%20Properties%202008.pdf)

55. Technical DaTa SheeT aBS - Laminated Plastics, accessed November 12, 2025, [https://laminatedplastics.com/abs.pdf](https://laminatedplastics.com/abs.pdf)

56. ABS - Technical Data Sheet_r1 - Plastim Ltd, accessed November 12, 2025, [https://plastim.co.uk/wp-content/uploads/2019/07/ABS-Technical-Data-Sheet.pdf](https://plastim.co.uk/wp-content/uploads/2019/07/ABS-Technical-Data-Sheet.pdf)

57. IEMAI3D - ASA Technical Data Sheet(TDS), accessed November 12, 2025, [https://www.iemai3d.com/wp-content/uploads/2025/04/04_ASA-Filament-TDS.pdf](https://www.iemai3d.com/wp-content/uploads/2025/04/04_ASA-Filament-TDS.pdf)

58. Technical Datasheet HIPS - Divbyz, accessed November 12, 2025, [https://www.divbyz.com/wp-content/uploads/2023/11/Technical_Datasheet-_HIPS-_16_04_19.pdf](https://www.divbyz.com/wp-content/uploads/2023/11/Technical_Datasheet-_HIPS-_16_04_19.pdf)

59. PC-ABS - MediaValet, accessed November 12, 2025, [https://cdn.mediavalet.com/usva/roush/wLtK14jF2U6f3KsucshoMQ/nUFc679TyUuan5vp4Sn1dQ/Original/pc_abs_spec_sheet.pdf](https://cdn.mediavalet.com/usva/roush/wLtK14jF2U6f3KsucshoMQ/nUFc679TyUuan5vp4Sn1dQ/Original/pc_abs_spec_sheet.pdf)

60. Technical DaTa SheeT Polycarbonate - Laminated Plastics, accessed November 12, 2025, [https://laminatedplastics.com/polycarbonate.pdf](https://laminatedplastics.com/polycarbonate.pdf)

61. Polycarbonate - Technical Data Sheet - Plastim Ltd, accessed November 12, 2025, [https://plastim.co.uk/wp-content/uploads/2019/07/Polycarbonate-Technical-Data-Sheet.pdf](https://plastim.co.uk/wp-content/uploads/2019/07/Polycarbonate-Technical-Data-Sheet.pdf)

62. Technical Data Sheet MX-Nylon: Grade S6121 - MGC Advanced Polymers, Inc., accessed November 12, 2025, [https://mapnylon.com/wp-content/uploads/2021/08/Technical-Data-Sheet-S6121.pdf](https://mapnylon.com/wp-content/uploads/2021/08/Technical-Data-Sheet-S6121.pdf)

63. Nylon Cast 6 Natural - Material Data Sheet, accessed November 12, 2025, [https://www.directplastics.co.uk/pdf/datasheets/Nylon%206%20Data%20Sheet.pdf](https://www.directplastics.co.uk/pdf/datasheets/Nylon%206%20Data%20Sheet.pdf)

64. Material Datasheet Carbon Fiber Nylon, accessed November 12, 2025, [https://www.3deology.co.in/assets/pdf/CF-Nylon.pdf](https://www.3deology.co.in/assets/pdf/CF-Nylon.pdf)

65. Material Data Sheet PA-6 GF25 (Nylon-6 + 25% glass fibre) - emico, accessed November 12, 2025, [https://www.emico.com/download-file/PA6_GF25_Materialdatenblatt_emico_Englisch_11.pdf](https://www.emico.com/download-file/PA6_GF25_Materialdatenblatt_emico_Englisch_11.pdf)

66. Material data sheet PA6 GF30 black, accessed November 12, 2025, [https://whm.net/wp-content/uploads/2023/09/pa6-gf30-black.pdf](https://whm.net/wp-content/uploads/2023/09/pa6-gf30-black.pdf)

67. Technical Data Sheet Polypropylene sheets - S-Polytec, accessed November 12, 2025, [https://www.s-polytec.com/media/attachment/file/d/a/data_sheet_pp-sheets.pdf](https://www.s-polytec.com/media/attachment/file/d/a/data_sheet_pp-sheets.pdf)

68. Technical DaTa SheeT Polypropylene - Laminated Plastics, accessed November 12, 2025, [https://laminatedplastics.com/polypropylene.pdf](https://laminatedplastics.com/polypropylene.pdf)

69. TYPICAL PROPERTIES OF POLYPROPYLENE (PP) - Precision Punch & Plastics, accessed November 12, 2025, [https://precisionpunch.com/wp-content/pdf/polypropylene.pdf](https://precisionpunch.com/wp-content/pdf/polypropylene.pdf)

70. Ultimaker PP Technical data sheet, accessed November 12, 2025, [https://um-support-files.ultimaker.com/materials/2.85mm/tds/PP/Ultimaker-PP-TDS-v3.00.pdf](https://um-support-files.ultimaker.com/materials/2.85mm/tds/PP/Ultimaker-PP-TDS-v3.00.pdf)

71. Polyvinyl alcohol (PVA) - Amazon AWS, accessed November 12, 2025, [https://s3-eu-central-1.amazonaws.com/plentymarkets-public-92/pvdtyofq45f2/propertyItems/220/Material%20data%20sheet%20PVA%20purefil.pdf](https://s3-eu-central-1.amazonaws.com/plentymarkets-public-92/pvdtyofq45f2/propertyItems/220/Material%20data%20sheet%20PVA%20purefil.pdf)

72. Technical data sheet PVA, accessed November 12, 2025, [https://3dneworld.com/wp-content/uploads/2017/08/PVA.pdf](https://3dneworld.com/wp-content/uploads/2017/08/PVA.pdf)

73. Elongation at break of PVA and PVA/PLA films. - ResearchGate, accessed November 12, 2025, [https://www.researchgate.net/figure/Elongation-at-break-of-PVA-and-PVA-PLA-films_fig1_237081349](https://www.researchgate.net/figure/Elongation-at-break-of-PVA-and-PVA-PLA-films_fig1_237081349)

74. Saflex® Structural (DG) - Polyvinyl Butyral Interlayer - Eastman, accessed November 12, 2025, [https://saflex-vanceva.eastman.com/content/dam/saflex/pdf-documents/arch/saflex/technical-data-sheet/product_technical_sheet_-_saflex_structural_031720.pdf](https://saflex-vanceva.eastman.com/content/dam/saflex/pdf-documents/arch/saflex/technical-data-sheet/product_technical_sheet_-_saflex_structural_031720.pdf)

75. PVB Film is a macromolecule material produced by the polyvinyl butyral - Nex, accessed November 12, 2025, [https://nex.eco.br/media/319/pvb-film-TDS.pdf](https://nex.eco.br/media/319/pvb-film-TDS.pdf)

76. PLA Wood - Bambu Lab, accessed November 12, 2025, [https://store.bblcdn.com/s4/default/6fda0ae88e5a4e66bb5d58f2968eee42/Bambus_PLA_Wood_Technical_Data_Sheet.pdf](https://store.bblcdn.com/s4/default/6fda0ae88e5a4e66bb5d58f2968eee42/Bambus_PLA_Wood_Technical_Data_Sheet.pdf)

77. PLA Metal | Bambu Lab US Store, accessed November 12, 2025, [https://us.store.bambulab.com/products/pla-metal](https://us.store.bambulab.com/products/pla-metal)

78. PLA-Silk - eSUN, accessed November 12, 2025, [https://www.esun3d.com/esilk-pla-product/](https://www.esun3d.com/esilk-pla-product/)

79. PLA SILK - Spectrum Filaments, accessed November 12, 2025, [https://spectrumfilaments.com/wp-content/uploads/2022/05/en_tds_spectrum_pla_silk.pdf](https://spectrumfilaments.com/wp-content/uploads/2022/05/en_tds_spectrum_pla_silk.pdf)

80. Bambu Filament - PLA Silk - Additive-X, accessed November 12, 2025, [https://www.additive-x.com/shop/mpattachments/file/viewonline/id/800/product_id/2561/](https://www.additive-x.com/shop/mpattachments/file/viewonline/id/800/product_id/2561/)

81. ULTEM™ RESIN 9085 - Argyle Materials, accessed November 12, 2025, [https://argylematerials.com/content/ULTEM_Resin_9085_Global_Technical_Data_Sheet.pdf](https://argylematerials.com/content/ULTEM_Resin_9085_Global_Technical_Data_Sheet.pdf)

82. ULTEM™ 9085 Resin - Stratasys, accessed November 12, 2025, [https://www.stratasys.com/contentassets/898e7825e3e7492ab8c0370499521596/mds_fdm_ultem9085_0422a.pdf?v=49ab26](https://www.stratasys.com/contentassets/898e7825e3e7492ab8c0370499521596/mds_fdm_ultem9085_0422a.pdf?v=49ab26)

83. ULTEM™ 9085 Resin - Tech-Labs, accessed November 12, 2025, [https://tech-labs.com/sites/images/stratasys-materials/DataSheet-ULTEM-9085.pdf](https://tech-labs.com/sites/images/stratasys-materials/DataSheet-ULTEM-9085.pdf)

84. UL Prospector materials database for product formulation, accessed November 12, 2025, [https://www.ulprospector.com/marketdisruptions](https://www.ulprospector.com/marketdisruptions)

85. Plastics & Elastomers - UL Prospector, accessed November 12, 2025, [https://www.ulprospector.com/plastics/en](https://www.ulprospector.com/plastics/en)

86. Prospector® Material Discovery | UL Solutions, accessed November 12, 2025, [https://www.ul.com/software/ultrus/prospector-material-discovery](https://www.ul.com/software/ultrus/prospector-material-discovery)

87. Materials - UL Prospector, accessed November 12, 2025, [https://www.ulprospector.com/plastics/en/generics/52/materials](https://www.ulprospector.com/plastics/en/generics/52/materials)

88. MatWeb: Online Materials Information Resource, accessed November 12, 2025, [https://www.matweb.com](https://www.matweb.com)

89. Overview of materials for Polyester (Thermoset) - Rigid - MatWeb, accessed November 12, 2025, [https://www.matweb.com/search/datasheet.aspx?matguid=1d92ed366503454ba49b8a44099f90de&n=1](https://www.matweb.com/search/datasheet.aspx?matguid=1d92ed366503454ba49b8a44099f90de&n=1)

90. Elongation at Break: Formula & Technical Properties of Plastics - SpecialChem, accessed November 12, 2025, [https://www.specialchem.com/plastics/guide/elongation-at-break](https://www.specialchem.com/plastics/guide/elongation-at-break)

91. Polyethylene (PE Plastic) – Structure, Properties & Toxicity - SpecialChem, accessed November 12, 2025, [https://www.specialchem.com/plastics/guide/polyethylene-plastic](https://www.specialchem.com/plastics/guide/polyethylene-plastic)
