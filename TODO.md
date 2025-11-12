# TODO: OrcaSlicer Settings Recommender - Integration Plan

**Last Updated:** November 11, 2025  
**Status:** Material Database Enhancement Phase

---

## 🎯 PHASE 1: QUICK WINS - Foundation (Week 1)
**Goal:** Add 6-8 high-confidence materials with verified temperature data
**Estimated Time:** 4-6 hours

### Group 1A: Extract & Validate Top Materials (2 hours)
- [ ] Review `output/extracted_materials.json` for top 6 materials:
  - [ ] OBC 905 (62% confidence)
  - [ ] NylonX 2019 (54% confidence)
  - [ ] Flexible TPU 98A (54% confidence)
  - [ ] PLA Prusament (38% confidence)
  - [ ] PolyTerra PLA (38% confidence)
  - [ ] SILK PLA (46% confidence)
- [ ] Verify extracted temperatures against source TDS PDFs
- [ ] Check for any missing critical data (HDT, shrinkage, etc.)

### Group 1B: Update Material Database (2 hours)
- [ ] Add new materials to `data/material_db.csv`:
  - [ ] Add OBC 905 as new material
  - [ ] Add NylonX 2019 (keep original name; verify carbon-fibre/filled status before renaming)
  - [ ] Add Flexible TPU 98A, 92A, 85A variants
  - [ ] Add PLA Prusament as PLA variant
  - [ ] Add PolyTerra PLA as PLA variant
  - [ ] Add SILK PLA as PLA variant
- [ ] Update `data/materials.json` with same materials
- [ ] Document data sources in extraction notes
- [ ] Create `scripts/merge_extracted_to_csv.py` to semi-automate merging `output/extracted_materials.json` into `data/material_db.csv` with validation and review flags
- [ ] Add unit tests for the merge/validation script (small set of sample JSON -> CSV cases)

### Group 1C: Test & Validate (1 hour)
- [ ] Test application with new materials
- [ ] Verify recommendations are generated correctly
- [ ] Check that all material properties display properly
- [ ] Validate temperature ranges are reasonable
- [ ] **CHECKPOINT:** Commit changes, tag as v0.2-materials-phase1

---

## 🔧 PHASE 2: ENGINEERING MATERIALS (Weeks 2-3)
**Goal:** Add CarbonX composite series and PETG variants
**Estimated Time:** 6-8 hours

### Group 2A: CarbonX Composite Series (3 hours)
- [ ] Extract and validate CarbonX materials (31% confidence each):
  - [ ] CarbonX CF-PETG (245°C, 60°C bed)
  - [ ] CarbonX CF-ABS (230°C, 110°C bed)
  - [ ] CarbonX CF-PA12 (285°C, 110°C bed)
  - [ ] CarbonX CF-PC (300°C, 140°C bed)
  - [ ] CarbonX CF-ASA (250°C, 110°C bed)
- [ ] Verify hardened nozzle detection for all CF materials
- [ ] Supplement with manufacturer website data if needed
- [ ] Add to database as new "Engineering" cluster materials

### Group 2B: PETG & ABS Variants (2 hours)
- [ ] Add PETG variants:
  - [ ] 3DXPRO LG PETG (255°C, 70°C bed)
  - [ ] Update existing PETG with better data
- [ ] Add ABS variants:
  - [ ] 3DXMAX ABS (225°C, 110°C bed)
  - [ ] Update existing ABS with better data
- [ ] Add ASA Extrafill (240-255°C with mechanical properties)
- [ ] Update material clusters if needed

### Group 2C: Update Application Logic (2 hours)
- [ ] Enhance hardened nozzle detection for composites
- [ ] Add enclosure requirement warnings where detected
- [ ] Update material recommendation algorithm for new materials
- [ ] Test material selection and recommendations

### Group 2D: Test & Validate (1 hour)
- [ ] Test all engineering materials
- [ ] Verify composite material warnings
- [ ] Check temperature recommendations
- [ ] Test edge cases (high-temp materials)
- [ ] **CHECKPOINT:** Commit changes, tag as v0.3-engineering-materials

---

## 🚀 PHASE 3: HIGH-PERFORMANCE MATERIALS (Week 4)
**Goal:** Add PEEK/PEKK/ULTEM family for professional users
**Estimated Time:** 8-10 hours

### Group 3A: PEEK Family (3 hours)
- [ ] Extract and validate PEEK materials:
  - [ ] Thermax PEEK (380-400°C, 130-140°C bed)
  - [ ] CarbonX CF20 PEEK (420°C, 140°C bed)
  - [ ] FIBREX GF20 PEEK (400°C, 160°C bed)
- [ ] Supplement with HDT data from manufacturer sites
- [ ] Add glass transition temperature data
- [ ] Verify drying requirements

### Group 3B: ULTEM/PEI Series (3 hours)
- [ ] Extract and validate ULTEM materials:
  - [ ] THERMAX PEI 9085 (365-385°C, 130-140°C bed)
  - [ ] THERMAX PEI 1010 (380-400°C, 130-140°C bed)
  - [ ] CarbonX CF Ultem (390°C, 140°C bed)
- [ ] Add to database as "High-Performance" cluster
- [ ] Update with annealing data if available

### Group 3C: PEKK & PC Variants (2 hours)
- [ ] Add PEKK variants:
  - [ ] Thermax PEKK-A (350°C)
  - [ ] CarbonX CF15 PEKK-A (390°C)
- [ ] Add PC variants:
  - [ ] 3DXMAX PC (275-295°C, 110-120°C bed)
  - [ ] 3DXSTAT ESD PC (295°C, 130°C bed)

### Group 3D: Application Enhancement (2 hours)
- [ ] Add high-temperature material warnings
- [ ] Enhance enclosure requirement detection
- [ ] Add printer capability checks (max temp support)
- [ ] Update UI to show material tier (Standard/Engineering/High-Performance)
- [ ] **CHECKPOINT:** Commit changes, tag as v0.4-high-performance

---

## 🎨 PHASE 4: SPECIALTY MATERIALS (Week 5)
**Goal:** Add ESD, flame-retardant, and specialty materials
**Estimated Time:** 4-6 hours

### Group 4A: ESD/Conductive Materials (2 hours)
- [ ] Add 3DXSTAT ESD series:
  - [ ] ESD PLA (210°C, 23°C bed)
  - [ ] ESD ABS (230°C, 110°C bed)
  - [ ] ESD PETG (250°C, 70°C bed)
  - [ ] ESD PVDF (275°C, 120°C bed)
- [ ] Add ESD property flag to database
- [ ] Update recommendations for electronics applications

### Group 4B: Glass Fiber Composites (2 hours)
- [ ] Add FIBREX GF series:
  - [ ] FIBREX PA12 GF30 (285°C, 110°C bed)
  - [ ] FIBREX GF PP (265°C, 85°C bed)
  - [ ] FIBREX GF ABS (245°C, 110°C bed)
- [ ] Verify hardened nozzle requirements
- [ ] Add to engineering materials cluster

### Group 4C: Test Specialty Features (1 hour)
- [ ] Test ESD material selection
- [ ] Verify specialty material warnings
- [ ] Check composite material detection
- [ ] **CHECKPOINT:** Commit changes, tag as v0.5-specialty-materials

---

## 📊 PHASE 5: DATA QUALITY IMPROVEMENT (Week 6)
**Goal:** Enhance existing materials with better data
**Estimated Time:** 6-8 hours

### Group 5A: Update Existing Materials (3 hours)
- [ ] Update PLA Standard → Use PLA Prusament data
- [ ] Update PETG → Use 3DXPRO LG PETG data
- [ ] Update ABS → Use 3DXMAX ABS data
- [ ] Update Nylon → Use NylonX or AMIDEX data
- [ ] Update TPU 95A → Use Flexible 98A data
- [ ] Update PC → Use 3DXMAX PC data

### Group 5B: Add Missing Properties (3 hours)
- [ ] Research and add HDT values for top 20 materials
- [ ] Add glass transition temperatures where available
- [ ] Add shrinkage data from manufacturer websites
- [ ] Update drying requirements for hygroscopic materials
- [ ] Add annealing data for annealable materials

### Group 5C: Validate Data Quality (2 hours)
- [ ] Cross-reference all temperature data with multiple sources
- [ ] Verify mechanical properties are reasonable
- [ ] Check for inconsistencies in material properties
- [ ] Update confidence scores for all materials
- [ ] **CHECKPOINT:** Commit changes, tag as v0.6-data-quality

---

## 🔍 PHASE 6: EXTRACTOR IMPROVEMENT (Week 7-8)
**Goal:** Improve TDS extraction for future updates
**Estimated Time:** 8-10 hours

### Group 6A: Enhance Extraction Patterns (4 hours)
- [ ] Analyze failed PDFs (0% confidence)
- [ ] Add OCR support for image-based PDFs
- [ ] Add brand-specific extraction patterns:
  - [ ] 3DXTech specific patterns
  - [ ] eSUN specific patterns
  - [ ] ColorFabb/Extrafill patterns
- [ ] Improve HDT and Tg extraction
- [ ] Add shrinkage data extraction

### Group 6B: Handle Problem Cases (2 hours)
- [ ] Manually process high-priority 0% confidence PDFs:
  - [ ] PLA MATTE HS.pptx → Convert to proper PDF
  - [ ] ASA Prime.pptx → Convert to proper PDF
  - [ ] ABS Prime.pptx → Convert to proper PDF
  - [ ] EN_TDS-PC-ABS.pdf → Apply OCR
  - [ ] PETG_TechSheet_ENG.pdf → Apply OCR
- [ ] Re-run extraction on converted files

### Group 6C: Test & Document (2 hours)
- [ ] Test improved extractor on all PDFs
- [ ] Document extraction success rate
- [ ] Create guide for adding new TDS PDFs
- [ ] Update TDS_UPLOAD_GUIDE.md with best practices
- [ ] **CHECKPOINT:** Commit changes, tag as v0.7-extractor-improvements

---

## 🎨 PHASE 7: UI/UX ENHANCEMENTS (Week 9)
**Goal:** Improve user experience with expanded material library
**Estimated Time:** 6-8 hours

### Group 7A: Material Selection Enhancement (3 hours)
- [ ] Add material search/filter functionality
- [ ] Group materials by cluster in UI
- [ ] Add material tier badges (Standard/Engineering/High-Performance)
- [ ] Show specialty properties (ESD, flame-retardant, etc.)
- [ ] Add "most popular" materials section

### Group 7B: Information Display (2 hours)
- [ ] Enhance material details display
- [ ] Show confidence score for recommendations
- [ ] Add "Why this setting?" explanations
- [ ] Show data source (TDS, community, manufacturer)
- [ ] Add material comparison feature

### Group 7C: Warnings & Alerts (2 hours)
- [ ] Add hardened nozzle requirement warnings
- [ ] Add enclosure requirement notifications
- [ ] Show high-temperature material alerts
- [ ] Add drying requirement reminders
- [ ] Display material-specific tips
- [ ] **CHECKPOINT:** Commit changes, tag as v0.8-ui-enhancements

---

## 📚 PHASE 8: DOCUMENTATION & TESTING (Week 10)
**Goal:** Complete documentation and comprehensive testing
**Estimated Time:** 6-8 hours

### Group 8A: Documentation (3 hours)
- [ ] Update README.md with new material count
- [ ] Document all material properties and sources
- [ ] Create material selection guide for users
- [ ] Add troubleshooting guide for material issues
- [ ] Update QUICK_REFERENCE.md with new materials

### Group 8B: Comprehensive Testing (3 hours)
- [ ] Test all 90+ materials
- [ ] Verify all temperature recommendations
- [ ] Test edge cases (extreme temperatures, rare materials)
- [ ] Validate all special requirements (hardened nozzle, enclosure, etc.)
- [ ] Test on different browsers/devices

### Group 8C: Final Polish (2 hours)
- [ ] Fix any bugs found during testing
- [ ] Optimize performance with large material database
- [ ] Add analytics to track material usage
- [ ] Prepare release notes
- [ ] **CHECKPOINT:** Commit changes, tag as v1.0-release

---

## 🚀 PHASE 9: DEPLOYMENT & MONITORING (Week 11)
**Goal:** Deploy enhanced application and gather feedback
**Estimated Time:** 4-6 hours

### Group 9A: Deployment (2 hours)
- [ ] Deploy to production
- [ ] Update GitHub repository
- [ ] Create release on GitHub
- [ ] Update documentation website
- [ ] Announce new features

### Group 9B: Monitoring & Feedback (2 hours)
- [ ] Monitor application performance
- [ ] Track material usage statistics
- [ ] Gather user feedback
- [ ] Identify most-requested materials
- [ ] Plan next iteration

### Group 9C: Continuous Improvement (Ongoing)
- [ ] Add user-requested materials
- [ ] Update material data based on feedback
- [ ] Improve recommendations based on usage patterns
- [ ] Keep TDS database updated with new filaments

---

## 📋 BACKLOG: Future Enhancements

### Material Database
- [ ] Add support for multi-material printing recommendations
- [ ] Add material cost tracking and comparison
- [ ] Integrate with filament vendor APIs for pricing
- [ ] Add material availability tracking
- [ ] Create community material database contribution system

### Application Features
- [ ] Add printer profile system (validate material compatibility)
- [ ] Create print failure troubleshooting guide
- [ ] Add material property calculator
- [ ] Implement material substitution recommender
- [ ] Add batch material processing for multiple parts

### Data Sources
- [ ] Partner with filament manufacturers for official data
- [ ] Integrate with 3D printing community databases
- [ ] Add user-contributed settings (with moderation)
- [ ] Create automated TDS monitoring for updates
- [ ] Add scientific paper references for material properties

### Advanced Features
- [ ] Machine learning for recommendation improvement
- [ ] A/B testing for different recommendation algorithms
- [ ] Integration with OrcaSlicer API (when available)
- [ ] Mobile app version
- [ ] API for third-party integrations

---

## ✅ COMPLETED TASKS

### Initial Development
- [x] Create basic application structure
- [x] Build material database (29 materials)
- [x] Implement recommendation engine
- [x] Deploy initial version
- [x] Extract TDS data from 129 PDFs
- [x] Analyze TDS extraction results
- [x] Create TDS analysis report

---

## 📝 NOTES

### Success Metrics
- **Phase 1:** 6-8 new materials added, 100% tested
- **Phase 2:** 10-12 engineering materials added, composite detection working
- **Phase 3:** 8-10 high-performance materials added, high-temp warnings working
- **Phase 4:** 10-15 specialty materials added, property flags working
- **Phase 5:** All existing materials have verified data
- **Overall:** 90+ materials in database, 95%+ accuracy

### Time Estimates
- **Total Development Time:** 50-60 hours
- **Timeline:** 10-11 weeks (5-6 hours/week)
- **Quick Wins (Phase 1):** Can be completed in 1 weekend

### Data Quality Goals
- Nozzle temp: 100% coverage (currently 90%)
- Bed temp: 100% coverage (currently 85%)
- Print speed: 70% coverage (currently 40%)
- Mechanical properties: 60% coverage (currently 30%)
- Thermal properties: 50% coverage (currently 15%)

### Priority Order Rationale
1. **Phase 1:** Quick wins build momentum and validate approach
2. **Phase 2:** Engineering materials are highly requested
3. **Phase 3:** High-performance materials differentiate application
4. **Phase 4:** Specialty materials serve niche users
5. **Phase 5:** Data quality ensures trust and accuracy
6. **Phase 6:** Extractor improvements enable future growth
7. **Phase 7:** UI/UX makes features discoverable
8. **Phase 8:** Documentation ensures usability
9. **Phase 9:** Deployment delivers value to users

---

**Remember:** Each phase ends with a checkpoint. Test thoroughly, commit changes, and tag releases. This allows rollback if issues arise and provides clear progress milestones.

**Start with Phase 1 Group 1A today!** 🚀