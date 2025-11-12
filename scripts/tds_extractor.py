#!/usr/bin/env python3
"""
TDS (Technical Data Sheet) Extractor for Filament Materials

This script extracts printing parameters and material properties from PDF TDS files,
regardless of manufacturer template format. It uses pattern matching and fuzzy
extraction to handle variations in layout and terminology.

Usage:
    python tds_extractor.py path/to/tds_folder/
    python tds_extractor.py single_tds.pdf
    
Output:
    - extracted_materials.json (structured data)
    - tds_report.txt (extraction report with confidence scores)
"""

import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
import sys

# Try to import PDF libraries (will provide instructions if missing)
try:
    import pdfplumber
except ImportError:
    print("ERROR: pdfplumber not installed")
    print("Install with: pip install pdfplumber")
    sys.exit(1)

try:
    from fuzzywuzzy import fuzz
except ImportError:
    print("WARNING: fuzzywuzzy not installed (optional but recommended)")
    print("Install with: pip install python-levenshtein fuzzywuzzy")
    FUZZY_AVAILABLE = False
else:
    FUZZY_AVAILABLE = True


@dataclass
class MaterialData:
    """Structure for extracted material data"""
    material_name: str
    brand: str = ""
    
    # Temperatures (°C)
    nozzle_temp_min: Optional[int] = None
    nozzle_temp_max: Optional[int] = None
    nozzle_temp_recommended: Optional[int] = None
    bed_temp_min: Optional[int] = None
    bed_temp_max: Optional[int] = None
    
    # Speeds (mm/s)
    print_speed_recommended: Optional[int] = None
    print_speed_max: Optional[int] = None
    
    # Mechanical Properties
    tensile_strength_MPa: Optional[float] = None
    tensile_modulus_MPa: Optional[float] = None
    elongation_at_break_pct: Optional[float] = None
    flexural_strength_MPa: Optional[float] = None
    flexural_modulus_MPa: Optional[float] = None
    impact_strength_kJ_m2: Optional[float] = None
    
    # Thermal Properties
    hdt_C: Optional[float] = None  # Heat Deflection Temperature
    vicat_softening_C: Optional[float] = None
    glass_transition_C: Optional[float] = None
    
    # Physical Properties
    density_g_cm3: Optional[float] = None
    shore_hardness: Optional[str] = None  # e.g., "95A", "85D"
    
    # Print Characteristics
    requires_enclosure: Optional[bool] = None
    requires_hardened_nozzle: Optional[bool] = None
    drying_temp_C: Optional[int] = None
    drying_time_hours: Optional[int] = None
    
    # Additional Info
    shrinkage_pct: Optional[float] = None
    recommended_layer_height_mm: Optional[str] = None
    retraction_mm: Optional[float] = None
    fan_speed_pct: Optional[int] = None
    
    # Metadata
    confidence_score: float = 0.0  # 0-1 scale
    extraction_notes: List[str] = None
    
    def __post_init__(self):
        if self.extraction_notes is None:
            self.extraction_notes = []


class TDSExtractor:
    """Extract material data from PDF technical data sheets"""
    
    # Comprehensive regex patterns for common TDS formats
    PATTERNS = {
        # Temperature patterns (°C or F)
        'nozzle_temp': [
            r'(?:nozzle|extrusion|print(?:ing)?)\s*temp(?:erature)?[:\s]*(\d{3})[°\s]*C',
            r'(?:nozzle|extrusion|print(?:ing)?)\s*temp(?:erature)?[:\s]*(\d{3})\s*[-–]\s*(\d{3})',
            r'T[_\s]*(?:Nozzle|Extrusion)[:\s]*(\d{3})',
        ],
        'bed_temp': [
            r'(?:bed|platform|plate)\s*temp(?:erature)?[:\s]*(\d{2,3})[°\s]*C',
            r'(?:bed|platform|plate)\s*temp(?:erature)?[:\s]*(\d{2,3})\s*[-–]\s*(\d{2,3})',
        ],
        
        # Speed patterns
        'print_speed': [
            r'print\s*speed[:\s]*(\d{2,3})\s*mm/s',
            r'(?:recommended\s*)?speed[:\s]*(\d{2,3})\s*mm/s',
        ],
        
        # Mechanical properties
        'tensile_strength': [
            r'tensile\s*strength[:\s]*(\d+\.?\d*)\s*MPa',
            r'ultimate\s*tensile[:\s]*(\d+\.?\d*)\s*MPa',
            r'UTS[:\s]*(\d+\.?\d*)\s*MPa',
        ],
        'tensile_modulus': [
            r'tensile\s*modulus[:\s]*(\d+\.?\d*)\s*[MG]Pa',
            r'(?:Young\'?s?\s*)?modulus[:\s]*(\d+\.?\d*)\s*[MG]Pa',
            r'E[\s-]*modulus[:\s]*(\d+\.?\d*)',
        ],
        'elongation': [
            r'elongation\s*at\s*break[:\s]*(\d+\.?\d*)\s*%',
            r'elongation[:\s]*(\d+\.?\d*)\s*%',
        ],
        
        # Thermal properties
        'hdt': [
            r'HDT[:\s]*(\d+\.?\d*)[°\s]*C',
            r'heat\s*deflection\s*temp[:\s]*(\d+\.?\d*)',
            r'deflection\s*temp[:\s]*(\d+\.?\d*)',
        ],
        'glass_transition': [
            r'Tg[:\s]*(\d+\.?\d*)[°\s]*C',
            r'glass\s*transition[:\s]*(\d+\.?\d*)',
        ],
        
        # Physical properties
        'density': [
            r'density[:\s]*(\d\.\d+)\s*g/cm[³3]',
            r'specific\s*gravity[:\s]*(\d\.\d+)',
        ],
        'shore_hardness': [
            r'shore\s*(?:hardness)?[:\s]*(\d{2}[AD])',
            r'hardness[:\s]*(\d{2}[AD])',
        ],
        
        # Drying requirements
        'drying': [
            r'dry(?:ing)?[:\s]*(\d{2,3})[°\s]*C[,\s]*(\d{1,2})\s*(?:hrs?|hours?)',
            r'(\d{2,3})[°\s]*C\s*for\s*(\d{1,2})\s*(?:hrs?|hours?)',
        ],
        
        # Other properties
        'shrinkage': [
            r'shrinkage[:\s]*(\d\.\d+)\s*%',
        ],
        'retraction': [
            r'retraction[:\s]*(\d\.\d+)\s*mm',
        ],
    }
    
    # Keywords that indicate special requirements
    KEYWORDS = {
        'enclosure': ['enclosure', 'enclosed', 'chamber', 'warping prone'],
        'hardened_nozzle': ['hardened nozzle', 'abrasive', 'carbon fiber', 'glass fiber', 'brass nozzle not recommended'],
        'hygroscopic': ['hygroscopic', 'absorbs moisture', 'must be dried', 'dry before use'],
    }
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.extraction_stats = {
            'files_processed': 0,
            'successful_extractions': 0,
            'failed_extractions': 0,
            'partial_extractions': 0,
        }
    
    def extract_from_pdf(self, pdf_path: Path) -> MaterialData:
        """Extract material data from a single PDF file"""
        if self.verbose:
            print(f"\n{'='*60}")
            print(f"Processing: {pdf_path.name}")
            print(f"{'='*60}")
        
        material = MaterialData(
            material_name=self._extract_material_name_from_filename(pdf_path),
            brand=self._extract_brand_from_filename(pdf_path)
        )
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                # Extract text from all pages
                full_text = ""
                for page_num, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    if text:
                        full_text += text + "\n"
                        if self.verbose:
                            print(f"  Page {page_num + 1}: {len(text)} characters")
                
                if not full_text:
                    material.extraction_notes.append("No text extracted from PDF")
                    return material
                
                # Run all extraction patterns
                self._extract_temperatures(full_text, material)
                self._extract_speeds(full_text, material)
                self._extract_mechanical_properties(full_text, material)
                self._extract_thermal_properties(full_text, material)
                self._extract_physical_properties(full_text, material)
                self._extract_print_characteristics(full_text, material)
                
                # Calculate confidence score
                material.confidence_score = self._calculate_confidence(material)
                
                if self.verbose:
                    self._print_extraction_summary(material)
                
        except Exception as e:
            material.extraction_notes.append(f"Error: {str(e)}")
            if self.verbose:
                print(f"  ERROR: {e}")
        
        return material
    
    def _extract_material_name_from_filename(self, path: Path) -> str:
        """Extract material name from filename"""
        # Remove common prefixes/suffixes
        name = path.stem
        name = re.sub(r'[-_]TDS$', '', name, flags=re.IGNORECASE)
        name = re.sub(r'[-_]datasheet$', '', name, flags=re.IGNORECASE)
        name = re.sub(r'^tds[-_]', '', name, flags=re.IGNORECASE)
        return name.replace('_', ' ').replace('-', ' ').strip()
    
    def _extract_brand_from_filename(self, path: Path) -> str:
        """Try to extract brand from filename or parent folder"""
        # Check parent folder name
        parent = path.parent.name.lower()
        known_brands = ['polymaker', 'prusament', 'esun', 'hatchbox', 'bambu', 
                       'overture', 'sunlu', '3dxtech', 'matterhackers']
        
        for brand in known_brands:
            if brand in parent:
                return brand.title()
        
        # Check filename
        filename_lower = path.stem.lower()
        for brand in known_brands:
            if brand in filename_lower:
                return brand.title()
        
        return ""
    
    def _extract_temperatures(self, text: str, material: MaterialData):
        """Extract temperature settings"""
        for pattern in self.PATTERNS['nozzle_temp']:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                if len(match.groups()) == 1:
                    temp = int(match.group(1))
                    material.nozzle_temp_recommended = temp
                    material.extraction_notes.append(f"Found nozzle temp: {temp}°C")
                elif len(match.groups()) == 2:
                    material.nozzle_temp_min = int(match.group(1))
                    material.nozzle_temp_max = int(match.group(2))
                    material.extraction_notes.append(
                        f"Found nozzle temp range: {material.nozzle_temp_min}-{material.nozzle_temp_max}°C"
                    )
                break
        
        for pattern in self.PATTERNS['bed_temp']:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                if len(match.groups()) == 1:
                    material.bed_temp_min = int(match.group(1))
                    material.extraction_notes.append(f"Found bed temp: {material.bed_temp_min}°C")
                elif len(match.groups()) == 2:
                    material.bed_temp_min = int(match.group(1))
                    material.bed_temp_max = int(match.group(2))
                    material.extraction_notes.append(
                        f"Found bed temp range: {material.bed_temp_min}-{material.bed_temp_max}°C"
                    )
                break
    
    def _extract_speeds(self, text: str, material: MaterialData):
        """Extract speed settings"""
        for pattern in self.PATTERNS['print_speed']:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                material.print_speed_recommended = int(match.group(1))
                material.extraction_notes.append(f"Found print speed: {material.print_speed_recommended} mm/s")
                break
    
    def _extract_mechanical_properties(self, text: str, material: MaterialData):
        """Extract mechanical properties"""
        # Tensile strength
        for pattern in self.PATTERNS['tensile_strength']:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                material.tensile_strength_MPa = float(match.group(1))
                material.extraction_notes.append(f"Found tensile strength: {material.tensile_strength_MPa} MPa")
                break
        
        # Tensile modulus
        for pattern in self.PATTERNS['tensile_modulus']:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                value = float(match.group(1))
                # Check if it's in GPa (convert to MPa)
                if 'GPa' in match.group(0):
                    value *= 1000
                material.tensile_modulus_MPa = value
                material.extraction_notes.append(f"Found tensile modulus: {material.tensile_modulus_MPa} MPa")
                break
        
        # Elongation
        for pattern in self.PATTERNS['elongation']:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                material.elongation_at_break_pct = float(match.group(1))
                material.extraction_notes.append(f"Found elongation: {material.elongation_at_break_pct}%")
                break
    
    def _extract_thermal_properties(self, text: str, material: MaterialData):
        """Extract thermal properties"""
        # HDT
        for pattern in self.PATTERNS['hdt']:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                material.hdt_C = float(match.group(1))
                material.extraction_notes.append(f"Found HDT: {material.hdt_C}°C")
                break
        
        # Glass transition
        for pattern in self.PATTERNS['glass_transition']:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                material.glass_transition_C = float(match.group(1))
                material.extraction_notes.append(f"Found Tg: {material.glass_transition_C}°C")
                break
    
    def _extract_physical_properties(self, text: str, material: MaterialData):
        """Extract physical properties"""
        # Density
        for pattern in self.PATTERNS['density']:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                material.density_g_cm3 = float(match.group(1))
                material.extraction_notes.append(f"Found density: {material.density_g_cm3} g/cm³")
                break
        
        # Shore hardness
        for pattern in self.PATTERNS['shore_hardness']:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                material.shore_hardness = match.group(1)
                material.extraction_notes.append(f"Found shore hardness: {material.shore_hardness}")
                break
    
    def _extract_print_characteristics(self, text: str, material: MaterialData):
        """Extract print characteristics based on keywords"""
        text_lower = text.lower()
        
        # Check for enclosure requirement
        if any(keyword in text_lower for keyword in self.KEYWORDS['enclosure']):
            material.requires_enclosure = True
            material.extraction_notes.append("Detected: Requires enclosure")
        
        # Check for hardened nozzle requirement
        if any(keyword in text_lower for keyword in self.KEYWORDS['hardened_nozzle']):
            material.requires_hardened_nozzle = True
            material.extraction_notes.append("Detected: Requires hardened nozzle")
        
        # Drying requirements
        for pattern in self.PATTERNS['drying']:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                material.drying_temp_C = int(match.group(1))
                material.drying_time_hours = int(match.group(2))
                material.extraction_notes.append(
                    f"Found drying: {material.drying_temp_C}°C for {material.drying_time_hours}h"
                )
                break
    
    def _calculate_confidence(self, material: MaterialData) -> float:
        """Calculate confidence score based on extracted data completeness"""
        total_fields = 0
        filled_fields = 0
        
        # Critical fields (weight more)
        critical_fields = [
            ('nozzle_temp_recommended', 2),
            ('nozzle_temp_min', 1),
            ('bed_temp_min', 2),
            ('tensile_strength_MPa', 1),
            ('density_g_cm3', 1),
        ]
        
        for field, weight in critical_fields:
            total_fields += weight
            if getattr(material, field) is not None:
                filled_fields += weight
        
        # Optional fields (weight less)
        optional_fields = [
            'print_speed_recommended', 'tensile_modulus_MPa', 'elongation_at_break_pct',
            'hdt_C', 'glass_transition_C', 'drying_temp_C'
        ]
        
        for field in optional_fields:
            total_fields += 1
            if getattr(material, field) is not None:
                filled_fields += 1
        
        return round(filled_fields / total_fields, 2) if total_fields > 0 else 0.0
    
    def _print_extraction_summary(self, material: MaterialData):
        """Print summary of extraction"""
        print(f"\n  Material: {material.material_name}")
        if material.brand:
            print(f"  Brand: {material.brand}")
        print(f"  Confidence: {material.confidence_score * 100:.0f}%")
        print(f"  Fields extracted: {len(material.extraction_notes)}")
        
        if material.nozzle_temp_recommended or material.nozzle_temp_min:
            print(f"  ✓ Temperature data")
        if material.tensile_strength_MPa:
            print(f"  ✓ Mechanical properties")
        if material.hdt_C or material.glass_transition_C:
            print(f"  ✓ Thermal properties")
    
    def batch_extract(self, input_path: Path) -> List[MaterialData]:
        """Extract from multiple PDFs in a directory"""
        results = []
        
        if input_path.is_file():
            # Single file
            result = self.extract_from_pdf(input_path)
            results.append(result)
            self.extraction_stats['files_processed'] = 1
        else:
            # Directory
            pdf_files = list(input_path.glob("*.pdf"))
            print(f"Found {len(pdf_files)} PDF files")
            
            for pdf_file in pdf_files:
                result = self.extract_from_pdf(pdf_file)
                results.append(result)
                self.extraction_stats['files_processed'] += 1
                
                # Classify extraction success
                if result.confidence_score > 0.7:
                    self.extraction_stats['successful_extractions'] += 1
                elif result.confidence_score > 0.3:
                    self.extraction_stats['partial_extractions'] += 1
                else:
                    self.extraction_stats['failed_extractions'] += 1
        
        return results
    
    def save_results(self, materials: List[MaterialData], output_dir: Path):
        """Save extraction results to JSON and report"""
        output_dir.mkdir(exist_ok=True)
        
        # Save JSON
        json_path = output_dir / "extracted_materials.json"
        materials_dict = {m.material_name: asdict(m) for m in materials}
        
        with open(json_path, 'w') as f:
            json.dump(materials_dict, f, indent=2)
        
        print(f"\n✓ Saved JSON to: {json_path}")
        
        # Save report
        report_path = output_dir / "extraction_report.txt"
        with open(report_path, 'w') as f:
            f.write("=" * 70 + "\n")
            f.write("TDS EXTRACTION REPORT\n")
            f.write("=" * 70 + "\n\n")
            
            f.write(f"Files processed: {self.extraction_stats['files_processed']}\n")
            f.write(f"Successful (>70%): {self.extraction_stats['successful_extractions']}\n")
            f.write(f"Partial (30-70%): {self.extraction_stats['partial_extractions']}\n")
            f.write(f"Failed (<30%): {self.extraction_stats['failed_extractions']}\n\n")
            
            f.write("=" * 70 + "\n")
            f.write("DETAILED RESULTS\n")
            f.write("=" * 70 + "\n\n")
            
            for material in sorted(materials, key=lambda m: m.confidence_score, reverse=True):
                f.write(f"\n{material.material_name}\n")
                f.write(f"{'-' * len(material.material_name)}\n")
                f.write(f"Confidence: {material.confidence_score * 100:.0f}%\n")
                
                if material.brand:
                    f.write(f"Brand: {material.brand}\n")
                
                if material.nozzle_temp_recommended:
                    f.write(f"Nozzle: {material.nozzle_temp_recommended}°C\n")
                elif material.nozzle_temp_min and material.nozzle_temp_max:
                    f.write(f"Nozzle: {material.nozzle_temp_min}-{material.nozzle_temp_max}°C\n")
                
                if material.bed_temp_min:
                    if material.bed_temp_max:
                        f.write(f"Bed: {material.bed_temp_min}-{material.bed_temp_max}°C\n")
                    else:
                        f.write(f"Bed: {material.bed_temp_min}°C\n")
                
                if material.tensile_strength_MPa:
                    f.write(f"Tensile Strength: {material.tensile_strength_MPa} MPa\n")
                
                if material.extraction_notes:
                    f.write(f"\nExtraction Notes:\n")
                    for note in material.extraction_notes:
                        f.write(f"  - {note}\n")
                
                f.write("\n")
        
        print(f"✓ Saved report to: {report_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Extract material data from TDS PDF files"
    )
    parser.add_argument(
        'input',
        type=Path,
        help='PDF file or directory containing PDFs'
    )
    parser.add_argument(
        '-o', '--output',
        type=Path,
        default=Path('output'),
        help='Output directory (default: ./output)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Verbose output'
    )
    
    args = parser.parse_args()
    
    if not args.input.exists():
        print(f"ERROR: Input path does not exist: {args.input}")
        sys.exit(1)
    
    print("\n" + "=" * 70)
    print("TDS EXTRACTOR - Filament Material Data Extraction")
    print("=" * 70)
    
    extractor = TDSExtractor(verbose=args.verbose)
    materials = extractor.batch_extract(args.input)
    extractor.save_results(materials, args.output)
    
    print("\n" + "=" * 70)
    print("EXTRACTION COMPLETE")
    print("=" * 70)
    print(f"Total files: {extractor.extraction_stats['files_processed']}")
    print(f"High confidence: {extractor.extraction_stats['successful_extractions']}")
    print(f"Partial data: {extractor.extraction_stats['partial_extractions']}")
    print(f"Low confidence: {extractor.extraction_stats['failed_extractions']}")
    print()


if __name__ == "__main__":
    main()
