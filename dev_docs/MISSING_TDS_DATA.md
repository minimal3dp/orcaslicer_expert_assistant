# Missing TDS (Technical Data Sheet) Values Report

**Generated:** November 12, 2025  
**Purpose:** Track missing material properties for TDS research and data enhancement  
**Total Materials:** 28

---

## Summary Statistics

### Overall Data Completeness
- **elongation_at_break_pct:** 0/28 materials (0% complete) ⚠️ **CRITICAL GAP**
- **Thermal properties:** Generally good coverage
- **Mechanical properties:** Good coverage for most materials
- **Print settings:** Excellent coverage (100%)

### Priority Levels
- 🔴 **HIGH PRIORITY:** Properties missing for >75% of materials
- 🟡 **MEDIUM PRIORITY:** Properties missing for 25-75% of materials
- 🟢 **LOW PRIORITY:** Properties missing for <25% of materials

---

## 🔴 CRITICAL: Universal Missing Properties

### elongation_at_break_pct (Missing: 28/28 materials)
**Impact:** Cannot calculate ductility vs. brittleness, affects recommendations for functional parts that need flexibility

**All materials missing this property:**
1. PLA
2. PLA_Plus
3. HTPLA
4. PLA_CF
5. PETG
6. PETG_CF
7. PET
8. ABS
9. ASA
10. HIPS
11. PC-ABS_Blend
12. Polycarbonate
13. Nylon
14. Nylon_CF
15. Nylon_GF
16. TPU_95A
17. TPU_85A
18. PP
19. PVA
20. PVB
21. PLA_Wood
22. PLA_Metal
23. PLA_Silk
24. PLA_Glow-in-the-dark
25. ULTEM_9085
26. PEEK
27. PEKK
28. PPSU

**Research Priority:** 🔴 **HIGHEST**  
**Typical Sources:** Manufacturer TDS, material testing labs, academic papers  
**Typical Values:** 
- Rigid materials (PLA, ABS): 2-8%
- Flexible materials (TPU): 300-600%
- Engineering materials (Nylon, PETG): 15-50%
- High-performance (PEEK): 20-50%

---

## Material-Specific Missing Data

### Standard Materials

#### PLA
✅ Complete - All properties present

#### PLA_Plus
✅ Complete - All properties present

#### HTPLA
✅ Complete - All properties present (including annealed data)

#### PLA_CF
✅ Complete - All properties present

---

### Functional Materials

#### PETG
✅ Complete - All properties present

#### PETG_CF
✅ Complete - All properties present

#### PET
✅ Complete - All properties present

#### ABS
✅ Complete - All properties present

#### ASA
✅ Complete - All properties present

#### HIPS
✅ Complete - All properties present

---

### Engineering Materials

#### PC-ABS_Blend
✅ Complete - All properties present

#### Polycarbonate
✅ Complete - All properties present

#### Nylon
✅ Complete - All properties present (including annealed data)

#### Nylon_CF
✅ Complete - All properties present

#### Nylon_GF
✅ Complete - All properties present

---

### Flexible Materials

#### TPU_95A
✅ Complete - All properties present

#### TPU_85A
✅ Complete - All properties present

---

### Specialty Materials

#### PP (Polypropylene)
✅ Complete - All properties present

#### PVA
✅ Complete - All properties present

#### PVB
✅ Complete - All properties present

#### PLA_Wood
✅ Complete - All properties present

#### PLA_Metal
✅ Complete - All properties present

#### PLA_Silk
✅ Complete - All properties present

#### PLA_Glow-in-the-dark
✅ Complete - All properties present

---

### High-Performance Materials

#### ULTEM_9085
✅ Complete - All properties present (including annealed data)

#### PEEK
✅ Complete - All properties present (including annealed data)

#### PEKK
✅ Complete - All properties present (including annealed data)

#### PPSU
✅ Complete - All properties present (including annealed data)

---

## Research Action Plan

### Phase 1: Elongation at Break (Highest Priority)
**Estimated Time:** 4-6 hours  
**Goal:** Fill in elongation_at_break_pct for all 28 materials

**Recommended Sources:**
1. **Manufacturer TDS:** Check official technical data sheets
   - Overture, HATCHBOX, eSUN, Polymaker websites
   - 3DXTech CarbonX series documentation
   - Stratasys ULTEM documentation
2. **Material Testing Labs:**
   - ASTM D638 tensile testing results
   - ISO 527 testing data
3. **Academic Research:**
   - Google Scholar searches for "3D printing [material] elongation"
   - ResearchGate papers on FDM material properties
4. **Community Resources:**
   - CNC Kitchen YouTube videos (Stefan Hermann testing)
   - r/3Dprinting material databases
   - Simplify3D material guides

**Strategy:**
1. Start with common materials (PLA, PETG, ABS) - easier to find data
2. Use manufacturer TDS as primary source
3. For specialty materials, reference similar base materials
4. Document ranges (min-max) where exact values vary by brand

---

### Phase 2: Additional Property Enhancement (Future)
Once elongation data is complete, consider enhancing:

1. **Tg (Glass Transition Temperature):**
   - Useful for understanding annealing behavior
   - Important for high-temp applications
   
2. **Flexural Modulus:**
   - Complements existing flexural strength data
   - Important for structural applications

3. **Shore Hardness (for TPU variants):**
   - Better characterization of flexible materials
   - Important for grip, cushioning applications

4. **Shrinkage Coefficients:**
   - Critical for dimensional accuracy
   - Varies significantly by material (especially ABS/ASA)

5. **Brand-Specific Variants:**
   - Compare properties across major brands
   - Identify best-in-class options for recommendations

---

## Data Entry Guidelines

### When Adding New Data:

1. **Always cite source:**
   ```csv
   # Example:
   PLA,elongation_at_break_pct,5.5,Source: Overture TDS Rev 2.1
   ```

2. **Use ranges when appropriate:**
   ```csv
   # If data varies by brand:
   TPU_95A,elongation_at_break_pct,450-550,Typical range for 95A TPU
   ```

3. **Mark estimated values:**
   ```csv
   # If extrapolating from similar materials:
   PLA_Wood,elongation_at_break_pct,3.5,Estimated from PLA base (typically 10-20% lower)
   ```

4. **Update this document:**
   - Move materials from "Missing" to "Complete" section
   - Update completion percentages
   - Note any data quality concerns

---

## TDS Research Resources

### Manufacturer Websites
- **Overture 3D:** https://overture3d.com/pages/technical-data
- **HATCHBOX:** https://www.hatchbox3d.com/pages/technical-specifications
- **eSUN:** https://www.esun3d.com/tds
- **Polymaker:** https://polymaker.com/datasheets
- **3DXTech:** https://www.3dxtech.com/technical-data-sheets/
- **Proto-pasta:** https://www.proto-pasta.com/pages/technical-data-sheets

### Testing Standards
- **ASTM D638:** Tensile properties of plastics
- **ISO 527:** Determination of tensile properties
- **ASTM D790:** Flexural properties
- **ISO 306:** Heat deflection temperature

### Community Resources
- **CNC Kitchen:** https://www.cnckitchen.com/ (material testing videos)
- **All3DP Material Guide:** https://all3dp.com/1/3d-printing-materials-guide-3d-printer-material/
- **SimplifD Material Settings:** https://www.simplify3d.com/resources/materials-guide/
- **MatWeb:** http://www.matweb.com/ (polymer property database)

---

## Version History

### v1.0 (November 12, 2025)
- Initial analysis of 28 materials
- Identified elongation_at_break_pct as universal gap
- All other mechanical/thermal properties present
- Excellent print settings coverage (100%)

---

## Notes

**Good News:** 
- Your material database has excellent coverage for most TDS properties!
- Print settings (temperatures, speeds, bed temps) are 100% complete
- Mechanical properties (tensile strength, modulus, impact) are comprehensive
- Thermal properties (HDT) are well-documented

**Main Gap:**
- Only missing property is `elongation_at_break_pct` (ductility measurement)
- This is a single, focused research task rather than a massive data collection effort

**Recommendation:**
- Focus research effort on elongation data first
- Consider this a Phase 5 enhancement rather than critical blocker
- Current data is sufficient for most user recommendations
- Elongation data would enhance recommendations for functional vs. decorative parts
