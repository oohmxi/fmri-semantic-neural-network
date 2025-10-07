"""
fMRI Tool Representation Study - Brain Image Processing Module

This module handles processing and integration of brain activation images from AFNI analysis
into the visualization pipeline for the fMRI Tool Representation Study.

Author: fMRI Tool Representation Study Team
Date: 2024
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import logging
from PIL import Image
import shutil

# Set up module logger (configured by application)
logger = logging.getLogger(__name__)


class BrainImageProcessor:
    """
    Main class for processing brain activation images from AFNI analysis.
    
    This class handles loading, processing, and organizing brain images for integration
    into the visualization pipeline.
    """
    
    def __init__(self, data_root: str):
        """
        Initialize the BrainImageProcessor.
        
        Args:
            data_root: Path to the root data directory
        """
        self.data_root = Path(data_root)
        self.raw_data_path = self.data_root / "raw"
        self.processed_data_path = self.data_root / "processed"
        
        # Brain image mapping based on experimental conditions
        self.brain_image_mapping = {
            'clench': {
                'filename': 'clench_afni.png',
                'condition': 'Clench Localizer',
                'description': 'Finger clenching task - M1 activation',
                'regions': ['Primary Motor Cortex (M1)', 'Brodmann Area 4', 'Brodmann Area 6'],
                'mni_coords': {'x': -40, 'y': 22, 'z': 62},
                'stats': {'threshold': 3.7037, 'p': 2.3e-4, 'q': 0.0047}
            },
            'imagined_grasp': {
                'filename': 'IGshape_tool_vs_PVshape_tool_GLT#0_Tstat.png',
                'condition': 'Imagined Grasp (Tools + Shapes)',
                'description': 'Imagined grasping task - combined tools and shapes',
                'regions': ['Left superior frontal gyrus', 'Parietal lobe', 'LOC (Lateral Occipital Complex)'],
                'mni_coords': [
                    {'x': 24, 'y': -58, 'z': 22},  # Superior frontal gyrus
                    {'x': 24, 'y': 50, 'z': 54},   # Parietal lobe
                    {'x': 24, 'y': 90, 'z': 24}    # LOC
                ],
                'stats': [
                    {'threshold': 3.5391, 'p': 0.0016, 'q': 0.0199},
                    {'threshold': 3.5391, 'p': 0.0016, 'q': 0.0199},
                    {'threshold': 3.1687, 'p': 0.0016, 'q': 0.0199}
                ]
            },
            'passive_viewing': {
                'filename': 'results.png',
                'condition': 'Passive Viewing: Tool vs Shape',
                'description': 'Passive viewing contrast - tools vs shapes',
                'regions': ['LOC; V1; V2; BA 18/17', 'Left Pre/Postcentral Gyrus; BA 3-5'],
                'mni_coords': [
                    {'x': 22, 'y': 100, 'z': -2},  # Visual cortex
                    {'x': 10, 'y': 44, 'z': 70}    # Pre/postcentral gyrus
                ],
                'stats': [
                    {'threshold': 3.5802, 'p': 3.7e-4, 'q': 0.0111},
                    {'threshold': 3.5802, 'p': 3.7e-4, 'q': 0.0111}
                ]
            },
            'imagined_vs_passive': {
                'filename': 'Screen Shot 2020-04-21 at 4.01.26 AM.png',
                'condition': 'Average Imagined Grasp vs Passive Viewing',
                'description': 'Contrast between imagined grasp and passive viewing',
                'regions': ['Left superior frontal gyrus', 'Brodmann Area 6', 'Left superior parietal lobe'],
                'mni_coords': [
                    {'x': 22, 'y': -54, 'z': 18},  # Superior frontal gyrus
                    {'x': 22, 'y': 10, 'z': 68},    # BA 6
                    {'x': 22, 'y': 48, 'z': 68}     # Superior parietal lobe
                ],
                'stats': [
                    {'threshold': 3.5391, 'p': 4.4e-4, 'q': 0.0533},
                    {'threshold': 3.5391, 'p': 4.4e-4, 'q': 0.0533},
                    {'threshold': 3.5391, 'p': 4.4e-4, 'q': 0.0533}
                ]
            }
        }
        
        logger.info("Initialized BrainImageProcessor")
    
    def load_brain_images(self) -> Dict[str, Dict]:
        """
        Load and process all brain activation images.
        
        Returns:
            Dictionary containing processed brain image data
        """
        logger.info("Loading brain activation images...")
        
        brain_data = {}
        
        for condition, info in self.brain_image_mapping.items():
            image_path = self.raw_data_path / info['filename']
            
            if image_path.exists():
                try:
                    # Load image
                    image = Image.open(image_path)
                    
                    # Store image data
                    brain_data[condition] = {
                        'image': image,
                        'path': str(image_path),
                        'condition': info['condition'],
                        'description': info['description'],
                        'regions': info['regions'],
                        'mni_coords': info['mni_coords'],
                        'stats': info['stats'],
                        'filename': info['filename']
                    }
                    
                    logger.info(f"✓ Loaded {condition}: {info['condition']}")
                    
                except Exception as e:
                    logger.error(f"Error loading {info['filename']}: {str(e)}")
            else:
                logger.info(f"Image not found (skipping): {image_path}")
        
        if len(brain_data) > 0:
            logger.info(f"Successfully loaded {len(brain_data)} brain images")
        else:
            logger.info("No brain images found - using demo mode with simulated data")
        return brain_data
    
    def create_brain_image_summary(self, brain_data: Dict[str, Dict]) -> str:
        """
        Create a summary of brain image data.
        
        Args:
            brain_data: Dictionary containing brain image data
            
        Returns:
            String summary of brain image data
        """
        summary = []
        summary.append("BRAIN IMAGE PROCESSING SUMMARY")
        summary.append("=" * 50)
        summary.append("")
        
        for condition, data in brain_data.items():
            summary.append(f"{data['condition'].upper()}:")
            summary.append(f"  Description: {data['description']}")
            summary.append(f"  Brain Regions: {', '.join(data['regions'])}")
            
            if isinstance(data['mni_coords'], list):
                summary.append(f"  MNI Coordinates:")
                for i, coords in enumerate(data['mni_coords']):
                    summary.append(f"    {data['regions'][i]}: ({coords['x']}, {coords['y']}, {coords['z']})")
            else:
                coords = data['mni_coords']
                summary.append(f"  MNI Coordinates: ({coords['x']}, {coords['y']}, {coords['z']})")
            
            summary.append("")
        
        return "\n".join(summary)
    
    def export_brain_images(self, brain_data: Dict[str, Dict], output_dir: str = None) -> Dict[str, str]:
        """
        Export brain images to organized directory structure.
        
        Args:
            brain_data: Dictionary containing brain image data
            output_dir: Output directory (defaults to processed/brain_images)
            
        Returns:
            Dictionary mapping conditions to exported file paths
        """
        if output_dir is None:
            output_dir = self.processed_data_path / "brain_images"
        else:
            output_dir = Path(output_dir)
        
        output_dir.mkdir(exist_ok=True)
        
        exported_files = {}
        
        for condition, data in brain_data.items():
            # Create condition-specific filename
            filename = f"{condition}_brain_activation.png"
            output_path = output_dir / filename
            
            try:
                # Copy and save image
                data['image'].save(output_path, 'PNG')
                exported_files[condition] = str(output_path)
                logger.info(f"✓ Exported {condition} brain image: {output_path}")
                
            except Exception as e:
                logger.error(f"Error exporting {condition} brain image: {str(e)}")
        
        return exported_files
    
    def generate_statistical_tables(self, brain_data: Dict[str, Dict]) -> Dict[str, List[Dict]]:
        """
        Generate statistical tables for each brain activation condition.
        
        Args:
            brain_data: Dictionary containing brain image data
            
        Returns:
            Dictionary mapping conditions to statistical tables
        """
        logger.info("Generating statistical tables for brain activations...")
        
        statistical_tables = {}
        
        for condition, data in brain_data.items():
            table_data = []
            
            regions = data['regions']
            coords = data['mni_coords']
            stats = data['stats']
            
            # Handle both single and multiple regions
            if isinstance(coords, list):
                for i, region in enumerate(regions):
                    coord = coords[i]
                    stat = stats[i]
                    
                    table_data.append({
                        'region': region,
                        'mni_x': coord['x'],
                        'mni_y': coord['y'],
                        'mni_z': coord['z'],
                        'threshold': stat['threshold'],
                        'p_value': stat['p'],
                        'q_value': stat['q']
                    })
            else:
                # Single region
                table_data.append({
                    'region': regions[0],
                    'mni_x': coords['x'],
                    'mni_y': coords['y'],
                    'mni_z': coords['z'],
                    'threshold': stats['threshold'],
                    'p_value': stats['p'],
                    'q_value': stats['q']
                })
            
            statistical_tables[condition] = table_data
            logger.info(f"✓ Generated statistical table for {condition}")
        
        return statistical_tables
    
    def process_all_brain_data(self) -> Dict:
        """
        Process all brain image data and return comprehensive results.
        
        Returns:
            Dictionary containing all processed brain data
        """
        logger.info("Processing all brain image data...")
        
        # Load brain images
        brain_data = self.load_brain_images()
        
        # Create summary
        summary = self.create_brain_image_summary(brain_data)
        
        # Export images
        exported_files = self.export_brain_images(brain_data)
        
        # Generate statistical tables
        statistical_tables = self.generate_statistical_tables(brain_data)
        
        # Compile results
        results = {
            'brain_data': brain_data,
            'summary': summary,
            'exported_files': exported_files,
            'statistical_tables': statistical_tables,
            'total_images': len(brain_data)
        }
        
        logger.info(f"Brain image processing complete: {len(brain_data)} images processed")
        return results


# Convenience functions for direct use

def process_brain_images(data_root: str) -> Dict:
    """Convenience function to process brain images."""
    processor = BrainImageProcessor(data_root)
    return processor.process_all_brain_data()


if __name__ == "__main__":
    # Example usage
    data_root = "/Users/hernandez/fmri_prosthetics/fmri-tool-representation/data"
    
    try:
        processor = BrainImageProcessor(data_root)
        results = processor.process_all_brain_data()
        
        print("Brain Image Processing Complete!")
        print(f"Processed {results['total_images']} brain images")
        print("\nSummary:")
        print(results['summary'])
        
        print("\nExported files:")
        for condition, file_path in results['exported_files'].items():
            print(f"  {condition}: {file_path}")
        
    except Exception as e:
        print(f"Error in brain image processing: {str(e)}")
