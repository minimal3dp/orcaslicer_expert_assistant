#!/usr/bin/env python3
"""
CSV to HTML Material Data Synchronizer

This script reads material_db.csv and generates the JavaScript materialsData
object that can be inserted into orcaslicer_assistant.html

Usage:
    python sync_materials.py
    python sync_materials.py --output materials_js_snippet.js
"""

import csv
import json
import argparse
from pathlib import Path
from typing import Dict, Any


def csv_to_materials_dict(csv_path: Path) -> Dict[str, Any]:
    """Convert CSV material database to JavaScript-compatible dict"""
    
    materials = {}
    
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            material_name = row['Material']
            
            # Clean up the name for JavaScript key
            # Convert "PLA (Standard)" -> "PLA"
            # Convert "PETG - Carbon Fiber" -> "PETG_CF"
            js_key = material_name
            
            # Handle parenthetical descriptors
            if '(' in js_key:
                js_key = js_key.split('(')[0].strip()
            
            # Handle descriptors after dash
            if ' - ' in js_key:
                parts = js_key.split(' - ')
                base = parts[0].strip()
                modifier = parts[1].strip()
                
                # Common abbreviations
                if 'Carbon Fiber' in modifier:
                    js_key = f"{base}_CF"
                elif 'Glass Fiber' in modifier:
                    js_key = f"{base}_GF"
                elif 'Wood' in modifier:
                    js_key = f"{base}_Wood"
                elif 'Metal' in modifier:
                    js_key = f"{base}_Metal"
                else:
                    # Just append
                    js_key = f"{base}_{modifier.replace(' ', '_')}"
            
            # Special cases
            if js_key == "TPU 95A (Flexible)":
                js_key = "TPU_95A"
            elif js_key == "TPU 85A (Soft Flexible)":
                js_key = "TPU_85A"
            elif js_key == "ULTEM 9085 (PEI)":
                js_key = "ULTEM_9085"
            elif js_key == "Polycarbonate (PC)":
                js_key = "PC"
            elif js_key == "PP (Polypropylene)":
                js_key = "PP"
            elif js_key == "Nylon (PA6)":
                js_key = "PA6"
            elif js_key == "Nylon (PA12)":
                js_key = "PA12"
            elif js_key == "Nylon - Carbon Fiber (PA12-CF)":
                js_key = "PA12_CF"
            elif js_key == "Nylon - Glass Fiber (PA-GF)":
                js_key = "PA_GF"
            elif "PLA+" in js_key or "Tough PLA" in js_key:
                js_key = "PLA_Plus"
            elif "HTPLA" in js_key:
                js_key = "HTPLA"
            
            # Remove remaining parentheses and special chars
            js_key = js_key.replace('(', '').replace(')', '').replace('/', '_')
            js_key = js_key.replace(' ', '_').strip()
            
            # Build material object
            material_obj = {
                "common": {
                    "nozzle_temperature": _safe_int(row, 'Nozzle_Temp_C_Min', 
                                                    (int(row['Nozzle_Temp_C_Min']) + int(row['Nozzle_Temp_C_Max'])) // 2 
                                                    if row['Nozzle_Temp_C_Min'] and row['Nozzle_Temp_C_Max'] else None),
                    "nozzle_temp_min": _safe_int(row, 'Nozzle_Temp_C_Min'),
                    "nozzle_temp_max": _safe_int(row, 'Nozzle_Temp_C_Max'),
                    "bed_temperature": _safe_int(row, 'Bed_Temp_C_Min', 
                                                 (int(row['Bed_Temp_C_Min']) + int(row['Bed_Temp_C_Max'])) // 2
                                                 if row['Bed_Temp_C_Min'] and row['Bed_Temp_C_Max'] else None),
                    "bed_temp_min": _safe_int(row, 'Bed_Temp_C_Min'),
                    "bed_temp_max": _safe_int(row, 'Bed_Temp_C_Max'),
                    "print_speed": 50,  # Default, not in CSV
                    "fan_speed": _estimate_fan_speed(material_name),
                },
                "properties": {
                    "tensile_strength_MPa": _safe_float(row, 'Strength_XY_MPa'),
                    "tensile_strength_z_MPa": _safe_float(row, 'Strength_Z_MPa'),
                    "tensile_modulus_MPa": _safe_float(row, 'Stiffness_Modulus_MPa'),
                    "elongation_at_break_pct": None,  # Not in CSV
                    "impact_strength_kJ_m2": _safe_float(row, 'Toughness_Impact_kJ_m2'),
                    "HDT_C": _safe_float(row, 'Heat_Resistance_HDT_C'),
                    "density_g_cm3": _safe_float(row, 'Density_g_cm3'),
                },
                "characteristics": {
                    "cluster": row.get('Cluster', ''),
                    "uv_resistant": _safe_bool(row, 'UV_Resistant'),
                    "hygroscopic": _safe_bool(row, 'Hygroscopic'),
                    "prone_to_creep": _safe_bool(row, 'Prone_to_Creep'),
                    "requires_enclosure": _safe_bool(row, 'Requires_Enclosure'),
                    "releases_fumes": _safe_bool(row, 'Releases_Fumes'),
                    "requires_hardened_nozzle": _safe_bool(row, 'Requires_Hardened_Nozzle'),
                    "low_friction": _safe_bool(row, 'Low_Friction'),
                    "annealable": _safe_bool(row, 'Annealable_for_HDT'),
                    "chemical_resistance_score": _safe_int(row, 'Chemical_Resistance_Score'),
                    "printability_score": _safe_int(row, 'Printability_Score'),
                },
                "notes": _generate_notes(row)
            }
            
            # Add annealing data if available
            if row.get('Strength_XY_MPa_Annealed'):
                material_obj["annealed"] = {
                    "tensile_strength_MPa": _safe_float(row, 'Strength_XY_MPa_Annealed'),
                    "tensile_strength_z_MPa": _safe_float(row, 'Strength_Z_MPa_Annealed'),
                    "HDT_C": _safe_float(row, 'Heat_Resistance_HDT_Annealed_C'),
                }
            
            materials[js_key] = material_obj
    
    return materials


def _safe_int(row: Dict, key: str, default=None) -> int:
    """Safely convert CSV value to int"""
    try:
        val = row.get(key, '').strip()
        if val and val != '':
            return int(float(val))
    except (ValueError, AttributeError):
        pass
    return default


def _safe_float(row: Dict, key: str, default=None) -> float:
    """Safely convert CSV value to float"""
    try:
        val = row.get(key, '').strip()
        if val and val != '':
            return float(val)
    except (ValueError, AttributeError):
        pass
    return default


def _safe_bool(row: Dict, key: str) -> bool:
    """Safely convert CSV value to bool"""
    val = row.get(key, '').strip().lower()
    return val in ('true', 'yes', '1', 'x')


def _estimate_fan_speed(material_name: str) -> int:
    """Estimate fan speed based on material type"""
    name_lower = material_name.lower()
    
    if 'pla' in name_lower and 'abs' not in name_lower:
        return 100
    elif 'petg' in name_lower or 'pet' in name_lower:
        return 50
    elif 'abs' in name_lower or 'asa' in name_lower:
        return 20
    elif 'nylon' in name_lower or 'pa' in name_lower:
        return 30
    elif 'tpu' in name_lower or 'tpe' in name_lower:
        return 80
    elif 'pc' in name_lower:
        return 30
    elif any(x in name_lower for x in ['peek', 'pekk', 'ultem', 'ppsu']):
        return 0
    else:
        return 50


def _generate_notes(row: Dict) -> str:
    """Generate descriptive notes based on properties"""
    notes = []
    material = row['Material']
    
    # Printability
    printability = _safe_int(row, 'Printability_Score')
    if printability and printability >= 8:
        notes.append("Easy to print")
    elif printability and printability <= 3:
        notes.append("Difficult to print")
    
    # Special characteristics
    if _safe_bool(row, 'UV_Resistant'):
        notes.append("UV resistant, good for outdoor use")
    
    if _safe_bool(row, 'Requires_Enclosure'):
        notes.append("Requires heated enclosure to prevent warping")
    
    if _safe_bool(row, 'Requires_Hardened_Nozzle'):
        notes.append("Requires hardened nozzle (abrasive)")
    
    if _safe_bool(row, 'Hygroscopic'):
        notes.append("Must be dried before printing")
    
    if _safe_bool(row, 'Releases_Fumes'):
        notes.append("Emits fumes - use ventilation")
    
    if _safe_bool(row, 'Prone_to_Creep'):
        notes.append("Prone to creep under constant load")
    
    if _safe_bool(row, 'Low_Friction'):
        notes.append("Low friction, good for mechanical parts")
    
    chem_resist = _safe_int(row, 'Chemical_Resistance_Score')
    if chem_resist and chem_resist >= 2:
        notes.append("Good chemical resistance")
    
    # Strength notes
    strength = _safe_float(row, 'Strength_XY_MPa')
    if strength and strength >= 70:
        notes.append("High strength")
    elif strength and strength <= 20:
        notes.append("Low strength, flexible")
    
    # Temperature resistance
    hdt = _safe_float(row, 'Heat_Resistance_HDT_C')
    if hdt and hdt >= 150:
        notes.append("Excellent high-temperature performance")
    elif hdt and hdt >= 90:
        notes.append("Good heat resistance")
    elif hdt and hdt <= 60:
        notes.append("Low heat resistance")
    
    return ". ".join(notes) + "." if notes else "General purpose material."


def generate_js_code(materials: Dict[str, Any], compact: bool = False) -> str:
    """Generate JavaScript code for materialsData object"""
    
    if compact:
        # Compact JSON (for production)
        json_str = json.dumps(materials, separators=(',', ':'))
    else:
        # Pretty JSON (for development)
        json_str = json.dumps(materials, indent=4)
    
    js_code = f"const materialsData = {json_str};"
    
    return js_code


def main():
    parser = argparse.ArgumentParser(
        description="Sync CSV material database to JavaScript format"
    )
    parser.add_argument(
        '--csv',
        type=Path,
        default=Path('data/material_db.csv'),
        help='Path to CSV file (default: data/material_db.csv)'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('data/materials_sync.js'),
        help='Output JavaScript file (default: data/materials_sync.js)'
    )
    parser.add_argument(
        '--compact',
        action='store_true',
        help='Generate compact JSON (no formatting)'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON instead of JavaScript'
    )
    
    args = parser.parse_args()
    
    if not args.csv.exists():
        print(f"ERROR: CSV file not found: {args.csv}")
        return 1
    
    print(f"Reading CSV: {args.csv}")
    materials = csv_to_materials_dict(args.csv)
    
    print(f"Processed {len(materials)} materials")
    
    if args.json:
        # Output as pure JSON
        output_str = json.dumps(materials, indent=2 if not args.compact else None)
        args.output = args.output.with_suffix('.json')
    else:
        # Output as JavaScript
        output_str = generate_js_code(materials, compact=args.compact)
    
    # Write to file
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w') as f:
        f.write(output_str)
    
    print(f"✓ Written to: {args.output}")
    
    # Print summary
    print("\nMaterial Summary:")
    print("-" * 50)
    
    clusters = {}
    for name, data in materials.items():
        cluster = data['characteristics'].get('cluster', 'Unknown')
        clusters[cluster] = clusters.get(cluster, 0) + 1
    
    for cluster, count in sorted(clusters.items()):
        print(f"  {cluster}: {count} materials")
    
    print("\nNext steps:")
    print("1. Review the generated file for accuracy")
    print("2. Copy the materialsData object into orcaslicer_assistant.html")
    print("3. Update the material selector population logic if needed")
    print("\nTo use in HTML:")
    print(f"  - Open: {args.output}")
    print(f"  - Copy the entire materialsData object")
    print(f"  - Replace the existing materialsData in orcaslicer_assistant.html (around line 163)")
    
    return 0


if __name__ == "__main__":
    exit(main())
