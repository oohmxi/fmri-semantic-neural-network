"""
fMRI Tool Representation Study - Data Preprocessing Module

This module provides comprehensive data processing functions for the fMRI Tool 
Representation Study, implementing the analysis pipeline for Creem-Regehr & Lee (2005) 
replication study on neural representations of graspable objects.

Author: fMRI Tool Representation Study Team
Date: 2024
"""

import os
import re
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Union
import logging
from datetime import datetime

# Set up module logger (configured by application)
logger = logging.getLogger(__name__)


class DataProcessor:
    """
    Main class for processing fMRI Tool Representation Study data.
    
    This class handles extraction, cleaning, and organization of experimental data
    from PsychoPy logs and AFNI condition timing files.
    """
    
    def __init__(self, data_root: str):
        """
        Initialize the DataProcessor.
        
        Args:
            data_root: Path to the root data directory
        """
        self.data_root = Path(data_root)
        self.raw_data_path = self.data_root / "raw"
        self.processed_data_path = self.data_root / "processed"
        
        # Create processed data directory if it doesn't exist
        self.processed_data_path.mkdir(exist_ok=True)
        
        # Initialize data storage
        self.trial_data = []
        self.participant_data = {}
        
    def parse_psychopy_logs(self, log_file_path: str) -> Dict:
        """
        Parse PsychoPy log files to extract timing and trial information.
        
        Args:
            log_file_path: Path to the PsychoPy .log file
            
        Returns:
            Dictionary containing parsed trial data
        """
        logger.info(f"Parsing PsychoPy log: {log_file_path}")
        
        trial_data = {
            'file_path': log_file_path,
            'participant_id': None,
            'condition': None,
            'trials': [],
            'timing_info': {},
            'scan_start': None,
            'scan_end': None
        }
        
        try:
            with open(log_file_path, 'r') as f:
                lines = f.readlines()
            
            # Extract participant ID from filename
            filename = os.path.basename(log_file_path)
            trial_data['participant_id'] = self._extract_participant_id(filename)
            trial_data['condition'] = self._extract_condition(filename)
            
            # Parse log content
            scan_started = False
            current_trial = None
            
            for line_num, line in enumerate(lines):
                line = line.strip()
                if not line:
                    continue
                    
                # Extract timestamp and log level
                parts = line.split('\t')
                if len(parts) < 2:
                    continue
                    
                timestamp = parts[0]
                log_level = parts[1]
                content = '\t'.join(parts[2:]) if len(parts) > 2 else ""
                
                # Track scan start
                if "start of scan" in content:
                    trial_data['scan_start'] = float(timestamp)
                    scan_started = True
                    logger.info(f"Scan started at {timestamp}s")
                
                # Track scan end
                if "window1: mouseVisible = True" in content and scan_started:
                    trial_data['scan_end'] = float(timestamp)
                    logger.info(f"Scan ended at {timestamp}s")
                
                # Parse trial information
                if scan_started and "New trial" in content:
                    trial_info = self._parse_trial_line(content, timestamp)
                    if trial_info:
                        trial_data['trials'].append(trial_info)
                
                # Parse stimulus presentation
                if scan_started and "autoDraw = True" in content:
                    self._parse_stimulus_presentation(content, timestamp, trial_data)
                
                # Parse keypress responses
                if scan_started and "Keypress:" in content:
                    self._parse_keypress(content, timestamp, trial_data)
            
            logger.info(f"Parsed {len(trial_data['trials'])} trials from {log_file_path}")
            return trial_data
            
        except Exception as e:
            logger.error(f"Error parsing log file {log_file_path}: {str(e)}")
            return trial_data
    
    def parse_condition_files(self, condition_file_path: str) -> Dict:
        """
        Parse AFNI condition timing files (S01_PV_tool.txt format).
        
        Args:
            condition_file_path: Path to the condition timing file
            
        Returns:
            Dictionary containing timing information
        """
        logger.info(f"Parsing condition file: {condition_file_path}")
        
        condition_data = {
            'file_path': condition_file_path,
            'participant_id': None,
            'condition_type': None,
            'stimulus_type': None,
            'timing_points': [],
            'duration': None
        }
        
        try:
            # Extract metadata from filename
            filename = os.path.basename(condition_file_path)
            condition_data['participant_id'] = self._extract_participant_id(filename)
            condition_data['condition_type'], condition_data['stimulus_type'] = self._parse_condition_filename(filename)
            
            with open(condition_file_path, 'r') as f:
                content = f.read().strip()
            
            # Parse timing data
            if content and not content.startswith('*'):
                # Split by whitespace and convert to float
                timing_points = []
                for point in content.split():
                    try:
                        # Remove ":16" suffix if present
                        clean_point = point.split(':')[0]
                        timing_points.append(float(clean_point))
                    except ValueError:
                        continue
                
                condition_data['timing_points'] = timing_points
                
                # Calculate duration if we have timing points
                if timing_points:
                    condition_data['duration'] = max(timing_points) - min(timing_points)
            
            logger.info(f"Parsed {len(condition_data['timing_points'])} timing points from {condition_file_path}")
            return condition_data
            
        except Exception as e:
            logger.error(f"Error parsing condition file {condition_file_path}: {str(e)}")
            return condition_data
    
    def create_trial_dataframe(self, participant_id: str = None) -> pd.DataFrame:
        """
        Create a comprehensive trial dataframe combining all data sources.
        
        Args:
            participant_id: Optional specific participant ID to process
            
        Returns:
            pandas DataFrame with all trial data
        """
        logger.info("Creating comprehensive trial dataframe")
        
        all_trials = []
        
        # Process all participants or specific participant
        if participant_id:
            participants = [participant_id]
        else:
            participants = self._get_all_participants()
        
        for pid in participants:
            logger.info(f"Processing participant: {pid}")
            
            # Special handling for S01 with complete experimental design
            if pid == 'S01':
                all_trials.extend(self._process_s01_complete_design())
            else:
                # Standard processing for other participants
                log_files = self._get_participant_log_files(pid)
                condition_files = self._get_participant_condition_files(pid)
                
                # Parse log files
                for log_file in log_files:
                    log_data = self.parse_psychopy_logs(str(log_file))
                    
                    # Parse corresponding condition files
                    for condition_file in condition_files:
                        cond_data = self.parse_condition_files(str(condition_file))
                        
                        # Match log and condition data
                        if self._match_log_condition(log_data, cond_data):
                            trials = self._combine_log_condition_data(log_data, cond_data)
                            all_trials.extend(trials)
        
        # Create DataFrame
        df = pd.DataFrame(all_trials)
        
        if not df.empty:
            # Add derived columns
            df = self._add_derived_columns(df)
            
            # Sort by participant and trial number
            df = df.sort_values(['participant_id', 'trial_number']).reset_index(drop=True)
            
            logger.info(f"Created dataframe with {len(df)} trials across {df['participant_id'].nunique()} participants")
        
        return df
    
    def validate_timing_consistency(self, df: pd.DataFrame) -> Dict:
        """
        Validate timing consistency across data sources.
        
        Args:
            df: Trial dataframe
            
        Returns:
            Dictionary with validation results
        """
        logger.info("Validating timing consistency")
        
        validation_results = {
            'total_trials': len(df),
            'timing_errors': [],
            'missing_data': [],
            'outliers': [],
            'summary_stats': {}
        }
        
        if df.empty:
            return validation_results
        
        # Check for missing timing data
        if 'stimulus_onset' in df.columns:
            missing_onset = df[df['stimulus_onset'].isna()]
            if not missing_onset.empty:
                validation_results['missing_data'].append(f"{len(missing_onset)} trials with missing stimulus onset")
        
        if 'stimulus_offset' in df.columns:
            missing_offset = df[df['stimulus_offset'].isna()]
            if not missing_offset.empty:
                validation_results['missing_data'].append(f"{len(missing_offset)} trials with missing stimulus offset")
        
        # Check for timing outliers
        if 'stimulus_duration' in df.columns:
            duration_stats = df['stimulus_duration'].describe()
            validation_results['summary_stats']['duration'] = duration_stats.to_dict()
            
            # Identify outliers (beyond 3 standard deviations)
            mean_duration = duration_stats['mean']
            std_duration = duration_stats['std']
            outliers = df[abs(df['stimulus_duration'] - mean_duration) > 3 * std_duration]
            if not outliers.empty:
                validation_results['outliers'].append(f"{len(outliers)} trials with duration outliers")
        
        # Check for negative durations
        if 'stimulus_duration' in df.columns:
            negative_durations = df[df['stimulus_duration'] < 0]
            if not negative_durations.empty:
                validation_results['timing_errors'].append(f"{len(negative_durations)} trials with negative durations")
        
        logger.info(f"Validation complete: {len(validation_results['timing_errors'])} errors found")
        return validation_results
    
    def generate_data_quality_report(self, df: pd.DataFrame) -> str:
        """
        Generate a comprehensive data quality report.
        
        Args:
            df: Trial dataframe
            
        Returns:
            String containing the quality report
        """
        logger.info("Generating data quality report")
        
        report = []
        report.append("=" * 60)
        report.append("fMRI Tool Representation Study - Data Quality Report")
        report.append("=" * 60)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Basic statistics
        report.append("BASIC STATISTICS")
        report.append("-" * 20)
        report.append(f"Total trials: {len(df)}")
        report.append(f"Participants: {df['participant_id'].nunique() if not df.empty else 0}")
        report.append(f"Conditions: {df['condition'].nunique() if not df.empty else 0}")
        report.append(f"Stimulus types: {df['stimulus_type'].nunique() if not df.empty else 0}")
        report.append("")
        
        # Timing statistics
        if not df.empty and 'stimulus_duration' in df.columns:
            report.append("TIMING STATISTICS")
            report.append("-" * 20)
            duration_stats = df['stimulus_duration'].describe()
            report.append(f"Mean duration: {duration_stats['mean']:.3f}s")
            report.append(f"Std duration: {duration_stats['std']:.3f}s")
            report.append(f"Min duration: {duration_stats['min']:.3f}s")
            report.append(f"Max duration: {duration_stats['max']:.3f}s")
            report.append("")
        
        # Data quality issues
        validation = self.validate_timing_consistency(df)
        report.append("DATA QUALITY ISSUES")
        report.append("-" * 20)
        
        if validation['timing_errors']:
            report.append("Timing Errors:")
            for error in validation['timing_errors']:
                report.append(f"  - {error}")
        else:
            report.append("No timing errors detected")
        
        if validation['missing_data']:
            report.append("Missing Data:")
            for missing in validation['missing_data']:
                report.append(f"  - {missing}")
        else:
            report.append("No missing data detected")
        
        if validation['outliers']:
            report.append("Outliers:")
            for outlier in validation['outliers']:
                report.append(f"  - {outlier}")
        else:
            report.append("No outliers detected")
        
        report.append("")
        report.append("=" * 60)
        
        return "\n".join(report)
    
    def export_processed_data(self, df: pd.DataFrame, output_dir: str = None) -> Dict[str, str]:
        """
        Export processed data to various formats.
        
        Args:
            df: Trial dataframe
            output_dir: Output directory (defaults to processed data path)
            
        Returns:
            Dictionary mapping file types to file paths
        """
        if output_dir is None:
            output_dir = self.processed_data_path
        
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True)
        
        exported_files = {}
        
        # Export to CSV
        csv_path = output_dir / "trial_data.csv"
        df.to_csv(csv_path, index=False)
        exported_files['csv'] = str(csv_path)
        
        # Export to Excel
        excel_path = output_dir / "trial_data.xlsx"
        df.to_excel(excel_path, index=False)
        exported_files['excel'] = str(excel_path)
        
        # Export quality report
        report_path = output_dir / "data_quality_report.txt"
        report = self.generate_data_quality_report(df)
        with open(report_path, 'w') as f:
            f.write(report)
        exported_files['quality_report'] = str(report_path)
        
        logger.info(f"Exported processed data to {output_dir}")
        return exported_files
    
    # Helper methods
    
    def _extract_participant_id(self, filename: str) -> str:
        """Extract participant ID from filename."""
        # Look for patterns like S01, S02, etc.
        match = re.search(r'S(\d+)', filename)
        if match:
            return f"S{match.group(1).zfill(2)}"
        
        # Look for numeric patterns at start
        match = re.search(r'^(\d+)_', filename)
        if match:
            return f"S{match.group(1).zfill(2)}"
        
        # Look for patterns like "Annika_1_" or similar
        match = re.search(r'(\w+)_(\d+)_', filename)
        if match:
            return f"S{match.group(2).zfill(2)}"
        
        return "Unknown"
    
    def _extract_condition(self, filename: str) -> str:
        """Extract condition type from filename."""
        filename_lower = filename.lower()
        
        if 'passive' in filename_lower or 'pv' in filename_lower:
            return 'passive_viewing'
        elif 'active' in filename_lower or 'grasp' in filename_lower:
            return 'active_grasp'
        elif 'clench' in filename_lower:
            return 'clench'
        elif 'imagined' in filename_lower or 'ig' in filename_lower:
            return 'imagined_grasp'
        else:
            return 'unknown'
    
    def _parse_condition_filename(self, filename: str) -> Tuple[str, str]:
        """Parse condition filename to extract condition and stimulus type."""
        # Pattern: S01_PV_tool.txt
        match = re.match(r'S\d+_(\w+)_(\w+)\.txt', filename)
        if match:
            condition = match.group(1)
            stimulus_type = match.group(2)
            return condition, stimulus_type
        
        return 'unknown', 'unknown'
    
    def _parse_trial_line(self, content: str, timestamp: str) -> Optional[Dict]:
        """Parse a trial line from PsychoPy log."""
        # Extract trial information from content
        trial_info = {
            'trial_timestamp': float(timestamp),
            'trial_index': None,
            'trial_rep': None,
            'image_file': None,
            'stimulus_type': None
        }
        
        # Extract trial index and rep
        rep_match = re.search(r'rep=(\d+)', content)
        index_match = re.search(r'index=(\d+)', content)
        
        if rep_match:
            trial_info['trial_rep'] = int(rep_match.group(1))
        if index_match:
            trial_info['trial_index'] = int(index_match.group(1))
        
        # Extract image file and type from OrderedDict
        image_match = re.search(r"imagefile', '([^']+)'", content)
        type_match = re.search(r"type', '([^']+)'", content)
        
        if image_match:
            trial_info['image_file'] = image_match.group(1)
        if type_match:
            trial_info['stimulus_type'] = type_match.group(1)
        
        return trial_info
    
    def _parse_stimulus_presentation(self, content: str, timestamp: str, trial_data: Dict):
        """Parse stimulus presentation information."""
        # Extract stimulus name
        stim_match = re.search(r'(\w+): autoDraw = True', content)
        if stim_match:
            stimulus_name = stim_match.group(1)
            
            # Store timing information
            if 'stimulus_timings' not in trial_data:
                trial_data['stimulus_timings'] = []
            
            trial_data['stimulus_timings'].append({
                'stimulus': stimulus_name,
                'onset': float(timestamp)
            })
    
    def _parse_keypress(self, content: str, timestamp: str, trial_data: Dict):
        """Parse keypress responses."""
        key_match = re.search(r'Keypress: (\w+)', content)
        if key_match:
            key = key_match.group(1)
            
            if 'keypresses' not in trial_data:
                trial_data['keypresses'] = []
            
            trial_data['keypresses'].append({
                'key': key,
                'timestamp': float(timestamp)
            })
    
    def _get_all_participants(self) -> List[str]:
        """Get list of all participant IDs."""
        participants = set()
        
        # Look in S## directories
        for item in self.raw_data_path.iterdir():
            if item.is_dir() and item.name.startswith('S'):
                participants.add(item.name)
        
        return sorted(list(participants))
    
    def _get_participant_log_files(self, participant_id: str) -> List[Path]:
        """Get all log files for a specific participant."""
        log_files = []
        
        # Look in participant directory
        participant_dir = self.raw_data_path / participant_id
        if participant_dir.exists():
            for file in participant_dir.glob("*.log"):
                log_files.append(file)
        
        return log_files
    
    def _get_participant_condition_files(self, participant_id: str) -> List[Path]:
        """Get all condition files for a specific participant."""
        condition_files = []
        
        # Look in participant directory
        participant_dir = self.raw_data_path / participant_id
        if participant_dir.exists():
            condition_dir = participant_dir / "Condition Files"
            if condition_dir.exists():
                for file in condition_dir.glob("*.txt"):
                    condition_files.append(file)
        
        return condition_files
    
    def _match_log_condition(self, log_data: Dict, cond_data: Dict) -> bool:
        """Check if log and condition data match."""
        # Match by participant ID
        if log_data['participant_id'] != cond_data['participant_id']:
            return False
        
        # Map condition types
        condition_mapping = {
            'passive_viewing': 'PV',
            'active_grasp': 'IG',  # Assuming active grasp maps to imagined grasp
            'clench': 'clench',
            'imagined_grasp': 'IG'
        }
        
        log_condition_code = condition_mapping.get(log_data['condition'], '')
        return log_condition_code == cond_data['condition_type']
    
    def _combine_log_condition_data(self, log_data: Dict, cond_data: Dict) -> List[Dict]:
        """Combine log and condition data into trial records."""
        trials = []
        
        for i, trial in enumerate(log_data['trials']):
            trial_record = {
                'participant_id': log_data['participant_id'],
                'condition': log_data['condition'],
                'stimulus_type': cond_data['stimulus_type'],
                'trial_number': i + 1,
                'trial_timestamp': trial.get('trial_timestamp'),
                'image_file': trial.get('image_file'),
                'scan_start': log_data.get('scan_start'),
                'scan_end': log_data.get('scan_end'),
                'timing_points': cond_data.get('timing_points', []),
                'condition_duration': cond_data.get('duration')
            }
            
            # Add stimulus timing if available
            if 'stimulus_timings' in log_data and i < len(log_data['stimulus_timings']):
                stim_timing = log_data['stimulus_timings'][i]
                trial_record['stimulus_onset'] = stim_timing['onset']
                trial_record['stimulus_name'] = stim_timing['stimulus']
            
            trials.append(trial_record)
        
        return trials
    
    def _add_derived_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Add derived columns to the dataframe."""
        if df.empty:
            return df
        
        # Calculate stimulus duration
        if 'stimulus_onset' in df.columns and 'stimulus_offset' in df.columns:
            df['stimulus_duration'] = df['stimulus_offset'] - df['stimulus_onset']
        
        # Add relative timing (relative to scan start)
        if 'scan_start' in df.columns and 'stimulus_onset' in df.columns:
            df['relative_onset'] = df['stimulus_onset'] - df['scan_start']
        
        # Add condition-stimulus combination
        if 'condition' in df.columns and 'stimulus_type' in df.columns:
            df['condition_stimulus'] = df['condition'] + '_' + df['stimulus_type']
        
        return df
    
    def _process_s01_complete_design(self) -> List[Dict]:
        """
        Process S01 data with complete experimental design (3 runs).
        
        Returns:
            List of trial dictionaries for all S01 runs
        """
        logger.info("Processing S01 complete experimental design (3 runs)")
        
        all_trials = []
        
        # Define S01 experimental runs
        s01_runs = [
            {
                'log_file': 'S01/experimental_runs/run01_passive_viewing/S01_run01_passive_viewing_2020_Mar_11_1324.log',
                'condition': 'passive_viewing',
                'run_number': 1,
                'description': 'Passive Viewing Task'
            },
            {
                'log_file': 'S01/experimental_runs/run02_imagined_grasp/S01_run02_imagined_grasp_2020_Mar_11_1335.log',
                'condition': 'imagined_grasp',
                'run_number': 2,
                'description': 'Imagined Grasp Task'
            },
            {
                'log_file': 'S01/experimental_runs/run03_clench/S01_run03_clench_2020_Mar_11_1350.log',
                'condition': 'clench',
                'run_number': 3,
                'description': 'Clench Localizer Task'
            }
        ]
        
        # Process each run
        for run_info in s01_runs:
            log_path = self.raw_data_path / run_info['log_file']
            
            if log_path.exists():
                logger.info(f"Processing {run_info['description']} (Run {run_info['run_number']})")
                
                # Parse log file
                log_data = self.parse_psychopy_logs(str(log_path))
                
                # Get corresponding condition files
                condition_files = self._get_s01_condition_files(run_info['condition'])
                
                # Process each condition file
                for condition_file in condition_files:
                    cond_data = self.parse_condition_files(str(condition_file))
                    
                    # Combine log and condition data
                    trials = self._combine_log_condition_data(log_data, cond_data)
                    
                    # Add run information
                    for trial in trials:
                        trial['run_number'] = run_info['run_number']
                        trial['run_description'] = run_info['description']
                        trial['participant_id'] = 'S01'
                        trial['condition'] = run_info['condition']
                    
                    all_trials.extend(trials)
                    
                logger.info(f"✓ Processed {len(trials)} trials for {run_info['description']}")
            else:
                logger.warning(f"Log file not found: {log_path}")
        
        logger.info(f"S01 processing complete: {len(all_trials)} total trials")
        return all_trials
    
    def _get_s01_condition_files(self, condition: str) -> List[Path]:
        """
        Get condition files for S01 based on condition type.
        
        Args:
            condition: Condition type (passive_viewing, imagined_grasp, clench)
            
        Returns:
            List of condition file paths
        """
        condition_files = []
        condition_dir = self.raw_data_path / "S01" / "condition_files"
        
        if condition == 'passive_viewing':
            # Passive viewing conditions
            patterns = ['S01_PV_tool.txt', 'S01_PV_Shape.txt', 'S01_PV_SCRtool.txt', 'S01_PV_SCRshape.txt']
        elif condition == 'imagined_grasp':
            # Imagined grasp conditions
            patterns = ['S01_IG_tool.txt', 'S01_IG_shape.txt', 'S01_IG_SCRtool.txt', 'S01_IG_SCRshape.txt']
        elif condition == 'clench':
            # Clench condition
            patterns = ['S01_clench.txt']
        else:
            logger.warning(f"Unknown condition: {condition}")
            return condition_files
        
        for pattern in patterns:
            file_path = condition_dir / pattern
            if file_path.exists():
                condition_files.append(file_path)
            else:
                logger.warning(f"Condition file not found: {file_path}")
        
        return condition_files


# Convenience functions for direct use

def parse_psychopy_logs(log_file_path: str) -> Dict:
    """
    Convenience function to parse a single PsychoPy log file.
    
    Args:
        log_file_path: Path to the PsychoPy .log file
        
    Returns:
        Dictionary containing parsed trial data
    """
    processor = DataProcessor(".")
    return processor.parse_psychopy_logs(log_file_path)


def parse_condition_files(condition_file_path: str) -> Dict:
    """
    Convenience function to parse a single condition timing file.
    
    Args:
        condition_file_path: Path to the condition timing file
        
    Returns:
        Dictionary containing timing information
    """
    processor = DataProcessor(".")
    return processor.parse_condition_files(condition_file_path)


def create_trial_dataframe(data_root: str, participant_id: str = None) -> pd.DataFrame:
    """
    Convenience function to create trial dataframe from data root.
    
    Args:
        data_root: Path to the root data directory
        participant_id: Optional specific participant ID to process
        
    Returns:
        pandas DataFrame with all trial data
    """
    processor = DataProcessor(data_root)
    return processor.create_trial_dataframe(participant_id)


if __name__ == "__main__":
    # Example usage
    data_root = "/Users/hernandez/fmri_prosthetics/fmri-tool-representation/data"
    processor = DataProcessor(data_root)
    
    # Create trial dataframe
    df = processor.create_trial_dataframe()
    
    # Generate quality report
    report = processor.generate_data_quality_report(df)
    print(report)
    
    # Export processed data
    exported_files = processor.export_processed_data(df)
    print(f"Exported files: {exported_files}")
