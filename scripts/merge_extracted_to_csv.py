#!/usr/bin/env python3
"""
Merge Extracted TDS Data into Material Database CSV

This script reads output/extracted_materials.json and merges high-confidence
temperature data into data/material_db.csv. It flags entries for manual review
based on confidence scores and data conflicts.

Usage:
    python scripts/merge_extracted_to_csv.py [--dry-run] [--min-confidence 0.3]
    
Options:
    --dry-run           Show what would be updated without modifying files
    --min-confidence    Minimum confidence score to auto-merge (default: 0.3)
    --review-output     Path to save review flagged items (default: output/merge_review.json)
"""

import json
import csv
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict
import sys


@dataclass
class MergeCandidate:
    """Represents a material extraction that's a candidate for merging."""
    source_name: str
    confidence: float
    nozzle_temp_min: Optional[float]
    nozzle_temp_max: Optional[float]
    nozzle_temp_recommended: Optional[float]
    bed_temp_min: Optional[float]
    bed_temp_max: Optional[float]
    print_speed: Optional[float]
    requires_hardened_nozzle: Optional[bool]
    requires_enclosure: Optional[bool]
    brand: str
    extraction_notes: List[str]
    
    def has_useful_data(self) -> bool:
        """Check if this extraction has any useful data to merge."""
        return any([
            self.nozzle_temp_min is not None,
            self.nozzle_temp_max is not None,
            self.nozzle_temp_recommended is not None,
            self.bed_temp_min is not None,
            self.bed_temp_max is not None,
            self.print_speed is not None,
            self.requires_hardened_nozzle is not None,
            self.requires_enclosure is not None,
        ])


@dataclass
class ReviewItem:
    """Item flagged for manual review."""
    material_name: str
    reason: str
    extracted_data: Dict
    current_csv_data: Optional[Dict] = None
    recommendation: str = ""


class MaterialMerger:
    """Handles merging extracted TDS data into material CSV."""
    
    def __init__(self, min_confidence: float = 0.3):
        self.min_confidence = min_confidence
        self.review_items: List[ReviewItem] = []
        self.merge_stats = {
            'total_extracted': 0,
            'high_confidence': 0,
            'merged': 0,
            'new_materials': 0,
            'updated_materials': 0,
            'flagged_for_review': 0,
            'skipped_low_confidence': 0,
            'skipped_no_data': 0,
        }
    
    def load_extracted_materials(self, json_path: Path) -> Dict:
        """Load extracted materials from JSON."""
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def load_csv_materials(self, csv_path: Path) -> Tuple[List[str], List[Dict]]:
        """Load existing material database from CSV."""
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
            materials = list(reader)
        return headers, materials
    
    def find_csv_match(self, extracted_name: str, csv_materials: List[Dict]) -> Optional[Dict]:
        """Try to match an extracted material name to a CSV row."""
        # Direct match
        for mat in csv_materials:
            if mat['Material'].lower() == extracted_name.lower():
                return mat
        
        # Fuzzy match on key terms (PLA, PETG, ABS, etc.)
        extracted_clean = extracted_name.lower()
        material_types = ['pla', 'petg', 'abs', 'asa', 'nylon', 'pa6', 'pa12', 'tpu', 'pc', 'peek', 'pekk', 'pei', 'ultem']
        
        for mat_type in material_types:
            if mat_type in extracted_clean:
                for mat in csv_materials:
                    if mat_type in mat['Material'].lower():
                        # Found a potential match, flag for review
                        return None  # Return None to trigger review
        
        return None
    
    def create_merge_candidate(self, name: str, data: Dict) -> MergeCandidate:
        """Convert extracted JSON entry to MergeCandidate."""
        return MergeCandidate(
            source_name=name,
            confidence=data.get('confidence_score', 0.0),
            nozzle_temp_min=data.get('nozzle_temp_min'),
            nozzle_temp_max=data.get('nozzle_temp_max'),
            nozzle_temp_recommended=data.get('nozzle_temp_recommended'),
            bed_temp_min=data.get('bed_temp_min'),
            bed_temp_max=data.get('bed_temp_max'),
            print_speed=data.get('print_speed_recommended'),
            requires_hardened_nozzle=data.get('requires_hardened_nozzle'),
            requires_enclosure=data.get('requires_enclosure'),
            brand=data.get('brand', ''),
            extraction_notes=data.get('extraction_notes', [])
        )
    
    def should_update_field(self, current_val: str, new_val: Optional[float]) -> bool:
        """Determine if a CSV field should be updated with extracted value."""
        if new_val is None:
            return False
        
        # Empty or zero in CSV - safe to update
        if not current_val or current_val.strip() == '' or current_val == '0':
            return True
        
        # Has existing data - flag for review
        return False
    
    def merge_material(self, candidate: MergeCandidate, csv_row: Optional[Dict]) -> Tuple[bool, Optional[Dict], str]:
        """
        Merge a candidate into CSV data.
        
        Returns:
            (should_merge, updated_row, reason)
        """
        # Skip low confidence
        if candidate.confidence < self.min_confidence:
            self.merge_stats['skipped_low_confidence'] += 1
            return False, None, f"Low confidence: {candidate.confidence:.1%}"
        
        # Skip if no useful data
        if not candidate.has_useful_data():
            self.merge_stats['skipped_no_data'] += 1
            return False, None, "No useful data to merge"
        
        # New material - flag for review
        if csv_row is None:
            self.review_items.append(ReviewItem(
                material_name=candidate.source_name,
                reason="New material not in CSV",
                extracted_data=asdict(candidate),
                recommendation="Consider adding as new row after verifying material type and cluster"
            ))
            self.merge_stats['flagged_for_review'] += 1
            return False, None, "New material - flagged for review"
        
        # Update existing material
        updated_row = csv_row.copy()
        changes = []
        
        # Update nozzle temps
        if candidate.nozzle_temp_min and self.should_update_field(csv_row['Nozzle_Temp_C_Min'], candidate.nozzle_temp_min):
            updated_row['Nozzle_Temp_C_Min'] = str(int(candidate.nozzle_temp_min))
            changes.append(f"Nozzle min: {candidate.nozzle_temp_min}°C")
        
        if candidate.nozzle_temp_max and self.should_update_field(csv_row['Nozzle_Temp_C_Max'], candidate.nozzle_temp_max):
            updated_row['Nozzle_Temp_C_Max'] = str(int(candidate.nozzle_temp_max))
            changes.append(f"Nozzle max: {candidate.nozzle_temp_max}°C")
        
        # Update bed temps
        if candidate.bed_temp_min and self.should_update_field(csv_row['Bed_Temp_C_Min'], candidate.bed_temp_min):
            updated_row['Bed_Temp_C_Min'] = str(int(candidate.bed_temp_min))
            changes.append(f"Bed min: {candidate.bed_temp_min}°C")
        
        if candidate.bed_temp_max and self.should_update_field(csv_row['Bed_Temp_C_Max'], candidate.bed_temp_max):
            updated_row['Bed_Temp_C_Max'] = str(int(candidate.bed_temp_max))
            changes.append(f"Bed max: {candidate.bed_temp_max}°C")
        
        # Update hardened nozzle requirement
        if candidate.requires_hardened_nozzle is not None:
            current_val = csv_row.get('Requires_Hardened_Nozzle', '').lower()
            if current_val == '' or current_val == 'false':
                updated_row['Requires_Hardened_Nozzle'] = 'true' if candidate.requires_hardened_nozzle else 'false'
                changes.append(f"Hardened nozzle: {candidate.requires_hardened_nozzle}")
        
        # Update enclosure requirement
        if candidate.requires_enclosure is not None:
            current_val = csv_row.get('Requires_Enclosure', '').lower()
            if current_val == '' or current_val == 'false':
                updated_row['Requires_Enclosure'] = 'true' if candidate.requires_enclosure else 'false'
                changes.append(f"Enclosure: {candidate.requires_enclosure}")
        
        if not changes:
            return False, None, "No fields needed updating"
        
        # Flag for review if multiple changes or critical fields
        if len(changes) > 2 or candidate.confidence < 0.5:
            self.review_items.append(ReviewItem(
                material_name=csv_row['Material'],
                reason=f"Multiple changes with {candidate.confidence:.1%} confidence",
                extracted_data=asdict(candidate),
                current_csv_data=csv_row,
                recommendation=f"Review changes: {', '.join(changes)}"
            ))
            self.merge_stats['flagged_for_review'] += 1
            return False, None, "Flagged for review - multiple changes"
        
        self.merge_stats['merged'] += 1
        self.merge_stats['updated_materials'] += 1
        return True, updated_row, f"Merged: {', '.join(changes)}"
    
    def run_merge(self, extracted_json: Path, csv_path: Path, dry_run: bool = True) -> Dict:
        """Run the merge process."""
        print(f"Loading extracted materials from {extracted_json}...")
        extracted = self.load_extracted_materials(extracted_json)
        self.merge_stats['total_extracted'] = len(extracted)
        
        print(f"Loading CSV database from {csv_path}...")
        headers, csv_materials = self.load_csv_materials(csv_path)
        
        print(f"\nProcessing {len(extracted)} extracted materials...")
        print(f"Minimum confidence threshold: {self.min_confidence:.0%}")
        print(f"Mode: {'DRY RUN' if dry_run else 'LIVE UPDATE'}\n")
        
        updated_materials = csv_materials.copy()
        
        # Process high-confidence materials first
        high_confidence = [(name, data) for name, data in extracted.items() 
                          if data['confidence_score'] >= self.min_confidence]
        self.merge_stats['high_confidence'] = len(high_confidence)
        
        for name, data in high_confidence:
            candidate = self.create_merge_candidate(name, data)
            csv_match = self.find_csv_match(name, csv_materials)
            
            should_merge, updated_row, reason = self.merge_material(candidate, csv_match)
            
            if should_merge and updated_row:
                # Find and update the row
                for i, mat in enumerate(updated_materials):
                    if mat['Material'] == csv_match['Material']:
                        updated_materials[i] = updated_row
                        print(f"✓ Updated: {csv_match['Material']} - {reason}")
                        break
            else:
                print(f"⊗ Skipped: {name[:50]}... - {reason}")
        
        # Write updated CSV if not dry run
        if not dry_run and self.merge_stats['merged'] > 0:
            self.write_csv(csv_path, headers, updated_materials)
            print(f"\n✓ Wrote updated CSV to {csv_path}")
        
        return self.merge_stats
    
    def write_csv(self, csv_path: Path, headers: List[str], materials: List[Dict]):
        """Write materials back to CSV."""
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(materials)
    
    def save_review_items(self, output_path: Path):
        """Save items flagged for review to JSON."""
        review_data = {
            'review_items': [asdict(item) for item in self.review_items],
            'stats': self.merge_stats,
            'instructions': (
                "These items require manual review before merging. "
                "Check for material name matches, verify confidence scores, "
                "and validate temperature ranges against manufacturer specs."
            )
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(review_data, f, indent=2)
        
        print(f"\n✓ Saved {len(self.review_items)} review items to {output_path}")
    
    def print_summary(self):
        """Print merge summary statistics."""
        print("\n" + "="*60)
        print("MERGE SUMMARY")
        print("="*60)
        print(f"Total extracted materials:      {self.merge_stats['total_extracted']}")
        print(f"High confidence (≥{self.min_confidence:.0%}):       {self.merge_stats['high_confidence']}")
        print(f"Successfully merged:            {self.merge_stats['merged']}")
        print(f"  - Updated existing materials: {self.merge_stats['updated_materials']}")
        print(f"  - New materials added:        {self.merge_stats['new_materials']}")
        print(f"Flagged for review:             {self.merge_stats['flagged_for_review']}")
        print(f"Skipped (low confidence):       {self.merge_stats['skipped_low_confidence']}")
        print(f"Skipped (no useful data):       {self.merge_stats['skipped_no_data']}")
        print("="*60)


def main():
    parser = argparse.ArgumentParser(
        description='Merge extracted TDS data into material CSV database'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be updated without modifying files'
    )
    parser.add_argument(
        '--min-confidence',
        type=float,
        default=0.3,
        help='Minimum confidence score to auto-merge (default: 0.3)'
    )
    parser.add_argument(
        '--review-output',
        type=Path,
        default=Path('output/merge_review.json'),
        help='Path to save review flagged items'
    )
    
    args = parser.parse_args()
    
    # Set up paths
    project_root = Path(__file__).parent.parent
    extracted_json = project_root / 'output' / 'extracted_materials.json'
    csv_path = project_root / 'data' / 'material_db.csv'
    
    # Validate paths
    if not extracted_json.exists():
        print(f"Error: Extracted materials file not found: {extracted_json}")
        sys.exit(1)
    
    if not csv_path.exists():
        print(f"Error: Material CSV not found: {csv_path}")
        sys.exit(1)
    
    # Run merge
    merger = MaterialMerger(min_confidence=args.min_confidence)
    stats = merger.run_merge(extracted_json, csv_path, dry_run=args.dry_run)
    
    # Save review items
    if merger.review_items:
        merger.save_review_items(args.review_output)
    
    # Print summary
    merger.print_summary()
    
    if args.dry_run:
        print("\n⚠ DRY RUN MODE - No files were modified")
        print("Run without --dry-run to apply changes")


if __name__ == '__main__':
    main()
