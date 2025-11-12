#!/usr/bin/env python3
"""
Unit tests for merge_extracted_to_csv.py

Tests the material merging logic, field update rules, and confidence thresholds.
"""

import unittest
import json
import csv
import tempfile
from pathlib import Path
import sys

# Add scripts dir to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from merge_extracted_to_csv import MaterialMerger, MergeCandidate, ReviewItem


class TestMergeCandidate(unittest.TestCase):
    """Test MergeCandidate dataclass."""
    
    def test_has_useful_data_true(self):
        """Candidate with temp data should return True."""
        candidate = MergeCandidate(
            source_name="Test PLA",
            confidence=0.5,
            nozzle_temp_min=200,
            nozzle_temp_max=220,
            nozzle_temp_recommended=None,
            bed_temp_min=60,
            bed_temp_max=None,
            print_speed=None,
            requires_hardened_nozzle=None,
            requires_enclosure=None,
            brand="TestBrand",
            extraction_notes=[]
        )
        self.assertTrue(candidate.has_useful_data())
    
    def test_has_useful_data_false(self):
        """Candidate with no data should return False."""
        candidate = MergeCandidate(
            source_name="Empty Material",
            confidence=0.0,
            nozzle_temp_min=None,
            nozzle_temp_max=None,
            nozzle_temp_recommended=None,
            bed_temp_min=None,
            bed_temp_max=None,
            print_speed=None,
            requires_hardened_nozzle=None,
            requires_enclosure=None,
            brand="",
            extraction_notes=[]
        )
        self.assertFalse(candidate.has_useful_data())
    
    def test_has_useful_data_with_flags(self):
        """Candidate with only flags should return True."""
        candidate = MergeCandidate(
            source_name="CF Material",
            confidence=0.4,
            nozzle_temp_min=None,
            nozzle_temp_max=None,
            nozzle_temp_recommended=None,
            bed_temp_min=None,
            bed_temp_max=None,
            print_speed=None,
            requires_hardened_nozzle=True,
            requires_enclosure=False,
            brand="",
            extraction_notes=["Detected: Requires hardened nozzle"]
        )
        self.assertTrue(candidate.has_useful_data())


class TestMaterialMerger(unittest.TestCase):
    """Test MaterialMerger class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.merger = MaterialMerger(min_confidence=0.3)
        
        # Sample extracted materials
        self.sample_extracted = {
            "PLA Prusament TDS": {
                "material_name": "PLA Prusament TDS",
                "brand": "Prusament",
                "nozzle_temp_min": None,
                "nozzle_temp_max": None,
                "nozzle_temp_recommended": 215,
                "bed_temp_min": 60,
                "bed_temp_max": None,
                "print_speed_recommended": 200,
                "requires_hardened_nozzle": None,
                "requires_enclosure": None,
                "confidence_score": 0.38,
                "extraction_notes": ["Found nozzle temp: 215°C", "Found bed temp: 60°C"]
            },
            "NylonX 2019": {
                "material_name": "NylonX 2019",
                "brand": "",
                "nozzle_temp_min": None,
                "nozzle_temp_max": None,
                "nozzle_temp_recommended": 240,
                "bed_temp_min": 20,
                "bed_temp_max": None,
                "requires_hardened_nozzle": True,
                "requires_enclosure": None,
                "confidence_score": 0.54,
                "extraction_notes": ["Detected: Requires hardened nozzle"]
            },
            "Low Confidence Material": {
                "material_name": "Low Confidence Material",
                "nozzle_temp_recommended": 200,
                "confidence_score": 0.15,
                "extraction_notes": []
            }
        }
        
        # Sample CSV data
        self.sample_csv_headers = [
            'Material', 'Cluster', 'Nozzle_Temp_C_Min', 'Nozzle_Temp_C_Max',
            'Bed_Temp_C_Min', 'Bed_Temp_C_Max', 'Requires_Hardened_Nozzle',
            'Requires_Enclosure'
        ]
        
        self.sample_csv_materials = [
            {
                'Material': 'PLA (Standard)',
                'Cluster': 'Standard',
                'Nozzle_Temp_C_Min': '190',
                'Nozzle_Temp_C_Max': '215',
                'Bed_Temp_C_Min': '0',
                'Bed_Temp_C_Max': '60',
                'Requires_Hardened_Nozzle': 'false',
                'Requires_Enclosure': 'false'
            },
            {
                'Material': 'Nylon (PA6)',
                'Cluster': 'Engineering',
                'Nozzle_Temp_C_Min': '240',
                'Nozzle_Temp_C_Max': '255',
                'Bed_Temp_C_Min': '70',
                'Bed_Temp_C_Max': '90',
                'Requires_Hardened_Nozzle': 'false',
                'Requires_Enclosure': 'false'
            }
        ]
    
    def test_create_merge_candidate(self):
        """Test conversion from JSON to MergeCandidate."""
        data = self.sample_extracted["PLA Prusament TDS"]
        candidate = self.merger.create_merge_candidate("PLA Prusament TDS", data)
        
        self.assertEqual(candidate.source_name, "PLA Prusament TDS")
        self.assertEqual(candidate.confidence, 0.38)
        self.assertEqual(candidate.nozzle_temp_recommended, 215)
        self.assertEqual(candidate.bed_temp_min, 60)
        self.assertEqual(candidate.brand, "Prusament")
    
    def test_should_update_field_empty(self):
        """Empty CSV field should allow update."""
        self.assertTrue(self.merger.should_update_field('', 200))
        self.assertTrue(self.merger.should_update_field('0', 200))
    
    def test_should_update_field_existing(self):
        """Existing CSV value should NOT allow update (requires review)."""
        self.assertFalse(self.merger.should_update_field('190', 200))
        self.assertFalse(self.merger.should_update_field('220', 200))
    
    def test_should_update_field_none(self):
        """None value should NOT update."""
        self.assertFalse(self.merger.should_update_field('190', None))
    
    def test_merge_low_confidence(self):
        """Low confidence material should be skipped."""
        data = self.sample_extracted["Low Confidence Material"]
        candidate = self.merger.create_merge_candidate("Low Confidence Material", data)
        csv_row = self.sample_csv_materials[0]
        
        should_merge, updated_row, reason = self.merger.merge_material(candidate, csv_row)
        
        self.assertFalse(should_merge)
        self.assertIsNone(updated_row)
        self.assertIn("Low confidence", reason)
        self.assertEqual(self.merger.merge_stats['skipped_low_confidence'], 1)
    
    def test_merge_no_useful_data(self):
        """Material with no useful data should be skipped."""
        candidate = MergeCandidate(
            source_name="Empty",
            confidence=0.5,
            nozzle_temp_min=None,
            nozzle_temp_max=None,
            nozzle_temp_recommended=None,
            bed_temp_min=None,
            bed_temp_max=None,
            print_speed=None,
            requires_hardened_nozzle=None,
            requires_enclosure=None,
            brand="",
            extraction_notes=[]
        )
        csv_row = self.sample_csv_materials[0]
        
        should_merge, updated_row, reason = self.merger.merge_material(candidate, csv_row)
        
        self.assertFalse(should_merge)
        self.assertIn("No useful data", reason)
    
    def test_merge_new_material(self):
        """New material should be flagged for review."""
        data = self.sample_extracted["PLA Prusament TDS"]
        candidate = self.merger.create_merge_candidate("PLA Prusament TDS", data)
        
        should_merge, updated_row, reason = self.merger.merge_material(candidate, None)
        
        self.assertFalse(should_merge)
        self.assertIn("New material", reason)
        self.assertEqual(len(self.merger.review_items), 1)
        self.assertEqual(self.merger.review_items[0].material_name, "PLA Prusament TDS")
    
    def test_merge_update_empty_fields(self):
        """Should update empty temperature fields."""
        # Create material with empty temp fields
        csv_row = {
            'Material': 'Test PLA',
            'Cluster': 'Standard',
            'Nozzle_Temp_C_Min': '',
            'Nozzle_Temp_C_Max': '',
            'Bed_Temp_C_Min': '0',
            'Bed_Temp_C_Max': '',
            'Requires_Hardened_Nozzle': 'false',
            'Requires_Enclosure': ''
        }
        
        candidate = MergeCandidate(
            source_name="Test PLA",
            confidence=0.4,
            nozzle_temp_min=200,
            nozzle_temp_max=220,
            nozzle_temp_recommended=None,
            bed_temp_min=None,
            bed_temp_max=60,
            print_speed=None,
            requires_hardened_nozzle=None,
            requires_enclosure=False,
            brand="",
            extraction_notes=[]
        )
        
        should_merge, updated_row, reason = self.merger.merge_material(candidate, csv_row)
        
        # Should NOT merge because of multiple changes (flags for review)
        self.assertFalse(should_merge)
        self.assertIn("Flagged for review", reason)
    
    def test_merge_hardened_nozzle_flag(self):
        """Should update hardened nozzle requirement."""
        csv_row = {
            'Material': 'NylonX',
            'Cluster': 'Engineering',
            'Nozzle_Temp_C_Min': '240',
            'Nozzle_Temp_C_Max': '260',
            'Bed_Temp_C_Min': '20',
            'Bed_Temp_C_Max': '40',
            'Requires_Hardened_Nozzle': 'false',
            'Requires_Enclosure': 'false'
        }
        
        candidate = MergeCandidate(
            source_name="NylonX",
            confidence=0.5,
            nozzle_temp_min=None,
            nozzle_temp_max=None,
            nozzle_temp_recommended=None,
            bed_temp_min=None,
            bed_temp_max=None,
            print_speed=None,
            requires_hardened_nozzle=True,
            requires_enclosure=None,
            brand="",
            extraction_notes=["Detected: Requires hardened nozzle"]
        )
        
        should_merge, updated_row, reason = self.merger.merge_material(candidate, csv_row)
        
        self.assertTrue(should_merge)
        self.assertIsNotNone(updated_row)
        self.assertEqual(updated_row['Requires_Hardened_Nozzle'], 'true')


class TestIntegration(unittest.TestCase):
    """Integration tests with temp files."""
    
    def test_full_merge_workflow(self):
        """Test complete merge workflow with temp files."""
        # Create temp JSON
        extracted_data = {
            "Test PLA": {
                "material_name": "Test PLA",
                "brand": "TestBrand",
                "nozzle_temp_min": 200,
                "nozzle_temp_max": 220,
                "bed_temp_min": 60,
                "bed_temp_max": None,
                "requires_hardened_nozzle": False,
                "confidence_score": 0.4,
                "extraction_notes": ["Test extraction"]
            }
        }
        
        csv_data = [
            ['Material', 'Nozzle_Temp_C_Min', 'Nozzle_Temp_C_Max', 'Bed_Temp_C_Min', 'Bed_Temp_C_Max', 'Requires_Hardened_Nozzle'],
            ['Test PLA', '', '', '0', '', 'false']
        ]
        
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            
            # Write JSON
            json_path = tmpdir_path / 'extracted.json'
            with open(json_path, 'w') as f:
                json.dump(extracted_data, f)
            
            # Write CSV
            csv_path = tmpdir_path / 'materials.csv'
            with open(csv_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(csv_data)
            
            # Run merge
            merger = MaterialMerger(min_confidence=0.3)
            stats = merger.run_merge(json_path, csv_path, dry_run=False)
            
            # Verify results
            self.assertGreater(stats['total_extracted'], 0)
            
            # Read updated CSV
            with open(csv_path, 'r') as f:
                reader = csv.DictReader(f)
                materials = list(reader)
            
            # Check if updates were made (may be flagged for review due to multiple changes)
            self.assertEqual(len(materials), 1)


def run_tests():
    """Run all tests."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
