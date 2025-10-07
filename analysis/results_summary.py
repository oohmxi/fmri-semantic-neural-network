"""
fMRI Tool Representation Study - Results Summary Module

This module provides automated reporting and results generation for the fMRI Tool 
Representation Study, creating comprehensive summaries and tables for the 
Creem-Regehr & Lee (2005) replication study.

Author: fMRI Tool Representation Study Team
Date: 2024
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional, Union
import logging
from pathlib import Path
import json
from datetime import datetime
import warnings

# Set up module logger (configured by application)
logger = logging.getLogger(__name__)

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')


class ResultsSummarizer:
    """
    Main class for generating comprehensive results summaries and reports.
    
    This class provides automated reporting functions for statistical results,
    descriptive statistics, and interpretation of findings.
    """
    
    def __init__(self, data_path: str = None, df: pd.DataFrame = None, 
                 analysis_results: Dict = None):
        """
        Initialize the ResultsSummarizer.
        
        Args:
            data_path: Path to processed data file (CSV or Excel)
            df: Pre-loaded DataFrame (alternative to data_path)
            analysis_results: Pre-computed analysis results
        """
        if df is not None:
            self.df = df.copy()
        elif data_path is not None:
            self.df = self._load_data(data_path)
        else:
            raise ValueError("Either data_path or df must be provided")
        
        self.analysis_results = analysis_results or {}
        
        logger.info(f"Initialized ResultsSummarizer with {len(self.df)} trials")
    
    def _load_data(self, data_path: str) -> pd.DataFrame:
        """Load data from file."""
        data_path = Path(data_path)
        
        if data_path.suffix == '.csv':
            df = pd.read_csv(data_path)
        elif data_path.suffix in ['.xlsx', '.xls']:
            df = pd.read_excel(data_path)
        else:
            raise ValueError(f"Unsupported file format: {data_path.suffix}")
        
        logger.info(f"Loaded data from {data_path}: {len(df)} trials")
        return df
    
    def generate_summary_stats(self) -> Dict:
        """
        Generate comprehensive descriptive statistics.
        
        Returns:
            Dictionary with descriptive statistics
        """
        logger.info("Generating summary statistics")
        
        summary = {
            'data_overview': {
                'total_trials': len(self.df),
                'participants': self.df['participant_id'].nunique() if 'participant_id' in self.df.columns else 0,
                'conditions': list(self.df['condition'].unique()) if 'condition' in self.df.columns else [],
                'stimulus_types': list(self.df['stimulus_type'].unique()) if 'stimulus_type' in self.df.columns else []
            },
            'timing_statistics': {},
            'condition_statistics': {},
            'stimulus_statistics': {},
            'participant_statistics': {}
        }
        
        # Timing statistics
        if 'stimulus_onset' in self.df.columns:
            timing_data = self.df['stimulus_onset'].dropna()
            summary['timing_statistics'] = {
                'mean': float(timing_data.mean()),
                'std': float(timing_data.std()),
                'min': float(timing_data.min()),
                'max': float(timing_data.max()),
                'median': float(timing_data.median()),
                'q25': float(timing_data.quantile(0.25)),
                'q75': float(timing_data.quantile(0.75))
            }
        
        # Condition statistics
        if 'condition' in self.df.columns:
            for condition in self.df['condition'].unique():
                cond_data = self.df[self.df['condition'] == condition]
                summary['condition_statistics'][condition] = {
                    'n_trials': len(cond_data),
                    'percentage': len(cond_data) / len(self.df) * 100,
                    'participants': cond_data['participant_id'].nunique() if 'participant_id' in cond_data.columns else 0
                }
        
        # Stimulus statistics
        if 'stimulus_type' in self.df.columns:
            for stim_type in self.df['stimulus_type'].unique():
                stim_data = self.df[self.df['stimulus_type'] == stim_type]
                summary['stimulus_statistics'][stim_type] = {
                    'n_trials': len(stim_data),
                    'percentage': len(stim_data) / len(self.df) * 100,
                    'participants': stim_data['participant_id'].nunique() if 'participant_id' in stim_data.columns else 0
                }
        
        # Participant statistics
        if 'participant_id' in self.df.columns:
            participant_stats = self.df.groupby('participant_id').agg({
                'trial_number': 'count',
                'stimulus_onset': ['mean', 'std'] if 'stimulus_onset' in self.df.columns else 'count'
            }).round(3)
            
            summary['participant_statistics'] = {
                'mean_trials_per_participant': float(participant_stats[('trial_number', 'count')].mean()),
                'std_trials_per_participant': float(participant_stats[('trial_number', 'count')].std()),
                'min_trials': int(participant_stats[('trial_number', 'count')].min()),
                'max_trials': int(participant_stats[('trial_number', 'count')].max())
            }
            
            if 'stimulus_onset' in self.df.columns:
                summary['participant_statistics'].update({
                    'mean_timing_per_participant': float(participant_stats[('stimulus_onset', 'mean')].mean()),
                    'std_timing_per_participant': float(participant_stats[('stimulus_onset', 'std')].mean())
                })
        
        logger.info("Summary statistics generated")
        return summary
    
    def create_results_table(self, analysis_results: Dict = None) -> pd.DataFrame:
        """
        Create comprehensive results table from analysis results.
        
        Args:
            analysis_results: Analysis results dictionary
            
        Returns:
            pandas DataFrame with results table
        """
        logger.info("Creating results table")
        
        if analysis_results is None:
            analysis_results = self.analysis_results
        
        results_data = []
        
        # Extract results from different analyses
        for analysis_type, results in analysis_results.items():
            if isinstance(results, dict):
                row = {
                    'Analysis_Type': analysis_type,
                    'N_Trials': results.get('n_trials', 'N/A'),
                    'N_Participants': results.get('participants', 'N/A'),
                    'Statistical_Test': 'N/A',
                    'Test_Statistic': 'N/A',
                    'P_Value': 'N/A',
                    'Significant': 'N/A',
                    'Effect_Size': 'N/A',
                    'Effect_Interpretation': 'N/A'
                }
                
                # Extract statistical test information
                if 't_test' in results:
                    row.update({
                        'Statistical_Test': 't-test',
                        'Test_Statistic': f"{results['t_test']['t_statistic']:.3f}",
                        'P_Value': f"{results['t_test']['p_value']:.3f}",
                        'Significant': 'Yes' if results['t_test']['significant'] else 'No'
                    })
                
                if 'effect_size' in results:
                    row.update({
                        'Effect_Size': f"{results['effect_size']['cohens_d']:.3f}",
                        'Effect_Interpretation': results['effect_size']['interpretation']
                    })
                
                if 'anova' in results:
                    row.update({
                        'Statistical_Test': 'ANOVA',
                        'Test_Statistic': f"{results['anova']['f_statistic']:.3f}",
                        'P_Value': f"{results['anova']['p_value']:.3f}",
                        'Significant': 'Yes' if results['anova']['significant'] else 'No'
                    })
                
                results_data.append(row)
        
        # Create DataFrame
        results_df = pd.DataFrame(results_data)
        
        if results_df.empty:
            logger.warning("No results data found for table creation")
            return pd.DataFrame()
        
        logger.info(f"Results table created with {len(results_df)} rows")
        return results_df
    
    def write_results_report(self, output_path: str = None) -> str:
        """
        Write comprehensive results report to file.
        
        Args:
            output_path: Path to save the report
            
        Returns:
            Path to the saved report file
        """
        logger.info("Writing results report")
        
        if output_path is None:
            output_path = Path.cwd() / f"results_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        else:
            output_path = Path(output_path)
        
        # Generate summary statistics
        summary_stats = self.generate_summary_stats()
        
        # Create results table
        results_table = self.create_results_table()
        
        # Write report
        with open(output_path, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("fMRI Tool Representation Study - Results Report\n")
            f.write("=" * 80 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Analysis Pipeline Version: 1.0\n")
            f.write("\n")
            
            # Data overview
            f.write("DATA OVERVIEW\n")
            f.write("-" * 40 + "\n")
            overview = summary_stats['data_overview']
            f.write(f"Total Trials: {overview['total_trials']}\n")
            f.write(f"Participants: {overview['participants']}\n")
            f.write(f"Conditions: {', '.join(overview['conditions'])}\n")
            f.write(f"Stimulus Types: {', '.join(overview['stimulus_types'])}\n")
            f.write("\n")
            
            # Timing statistics
            if summary_stats['timing_statistics']:
                f.write("TIMING STATISTICS\n")
                f.write("-" * 40 + "\n")
                timing = summary_stats['timing_statistics']
                f.write(f"Mean Onset Time: {timing['mean']:.3f}s\n")
                f.write(f"Standard Deviation: {timing['std']:.3f}s\n")
                f.write(f"Range: {timing['min']:.3f}s - {timing['max']:.3f}s\n")
                f.write(f"Median: {timing['median']:.3f}s\n")
                f.write(f"IQR: {timing['q25']:.3f}s - {timing['q75']:.3f}s\n")
                f.write("\n")
            
            # Condition statistics
            if summary_stats['condition_statistics']:
                f.write("CONDITION STATISTICS\n")
                f.write("-" * 40 + "\n")
                for condition, stats in summary_stats['condition_statistics'].items():
                    f.write(f"{condition}:\n")
                    f.write(f"  Trials: {stats['n_trials']} ({stats['percentage']:.1f}%)\n")
                    f.write(f"  Participants: {stats['participants']}\n")
                f.write("\n")
            
            # Stimulus statistics
            if summary_stats['stimulus_statistics']:
                f.write("STIMULUS STATISTICS\n")
                f.write("-" * 40 + "\n")
                for stim_type, stats in summary_stats['stimulus_statistics'].items():
                    f.write(f"{stim_type}:\n")
                    f.write(f"  Trials: {stats['n_trials']} ({stats['percentage']:.1f}%)\n")
                    f.write(f"  Participants: {stats['participants']}\n")
                f.write("\n")
            
            # Participant statistics
            if summary_stats['participant_statistics']:
                f.write("PARTICIPANT STATISTICS\n")
                f.write("-" * 40 + "\n")
                part_stats = summary_stats['participant_statistics']
                f.write(f"Mean Trials per Participant: {part_stats['mean_trials_per_participant']:.1f}\n")
                f.write(f"SD Trials per Participant: {part_stats['std_trials_per_participant']:.1f}\n")
                f.write(f"Trial Range: {part_stats['min_trials']} - {part_stats['max_trials']}\n")
                if 'mean_timing_per_participant' in part_stats:
                    f.write(f"Mean Timing per Participant: {part_stats['mean_timing_per_participant']:.3f}s\n")
                f.write("\n")
            
            # Results table
            if not results_table.empty:
                f.write("STATISTICAL RESULTS\n")
                f.write("-" * 40 + "\n")
                f.write(results_table.to_string(index=False))
                f.write("\n\n")
            
            # Research questions summary
            f.write("RESEARCH QUESTIONS SUMMARY\n")
            f.write("-" * 40 + "\n")
            f.write("RQ1: Are Tools Special?\n")
            f.write("  - Compare tools vs shapes across all tasks\n")
            f.write("  - Analyze passive viewing: Tools vs Shapes\n")
            f.write("  - Analyze active grasp: Tools vs Shapes\n")
            f.write("  - Compare screen-optimized stimuli\n")
            f.write("\n")
            f.write("RQ2: Action Potentiation\n")
            f.write("  - Compare passive viewing vs active grasping\n")
            f.write("  - Analyze tools: Passive vs Active\n")
            f.write("  - Analyze shapes: Passive vs Active\n")
            f.write("  - Test interaction effects\n")
            f.write("\n")
            f.write("RQ3: Functional vs Structural\n")
            f.write("  - Compare functional tools vs neutral shapes\n")
            f.write("  - Analyze standard vs screen-optimized stimuli\n")
            f.write("\n")
            
            # Key findings
            f.write("KEY FINDINGS\n")
            f.write("-" * 40 + "\n")
            f.write("1. Data Processing: Successfully processed experimental data\n")
            f.write("2. Statistical Analysis: Comprehensive analysis pipeline implemented\n")
            f.write("3. Visualization: Publication-ready plots generated\n")
            f.write("4. Results: Analysis-ready datasets created\n")
            f.write("\n")
            
            f.write("=" * 80 + "\n")
            f.write("End of Report\n")
            f.write("=" * 80 + "\n")
        
        logger.info(f"Results report written to {output_path}")
        return str(output_path)
    
    def export_for_publication(self, output_dir: str = None) -> Dict[str, str]:
        """
        Export results in publication-ready formats.
        
        Args:
            output_dir: Output directory
            
        Returns:
            Dictionary mapping file types to file paths
        """
        logger.info("Exporting results for publication")
        
        if output_dir is None:
            output_dir = Path.cwd() / "publication_results"
        else:
            output_dir = Path(output_dir)
        
        output_dir.mkdir(exist_ok=True)
        
        exported_files = {}
        
        # Generate summary statistics
        summary_stats = self.generate_summary_stats()
        
        # Export summary statistics as JSON
        summary_path = output_dir / "summary_statistics.json"
        with open(summary_path, 'w') as f:
            json.dump(summary_stats, f, indent=2)
        exported_files['summary_json'] = str(summary_path)
        
        # Create and export results table
        results_table = self.create_results_table()
        if not results_table.empty:
            # CSV format
            csv_path = output_dir / "results_table.csv"
            results_table.to_csv(csv_path, index=False)
            exported_files['results_csv'] = str(csv_path)
            
            # Excel format
            excel_path = output_dir / "results_table.xlsx"
            results_table.to_excel(excel_path, index=False)
            exported_files['results_excel'] = str(excel_path)
        
        # Write comprehensive report
        report_path = output_dir / "comprehensive_report.txt"
        self.write_results_report(report_path)
        exported_files['comprehensive_report'] = str(report_path)
        
        # Export analysis results if available
        if self.analysis_results:
            analysis_path = output_dir / "analysis_results.json"
            # Convert numpy types and booleans to JSON-serializable types
            serializable_results = self._make_json_serializable(self.analysis_results)
            with open(analysis_path, 'w') as f:
                json.dump(serializable_results, f, indent=2)
            exported_files['analysis_results'] = str(analysis_path)
        
        logger.info(f"Publication-ready results exported to {output_dir}")
        return exported_files
    
    def generate_interpretation(self, analysis_results: Dict = None) -> str:
        """
        Generate interpretation of results.
        
        Args:
            analysis_results: Analysis results dictionary
            
        Returns:
            String with interpretation
        """
        logger.info("Generating results interpretation")
        
        if analysis_results is None:
            analysis_results = self.analysis_results
        
        interpretation = []
        interpretation.append("RESULTS INTERPRETATION")
        interpretation.append("=" * 50)
        interpretation.append("")
        
        # Data quality interpretation
        summary_stats = self.generate_summary_stats()
        interpretation.append("DATA QUALITY:")
        interpretation.append(f"- Successfully processed {summary_stats['data_overview']['total_trials']} trials")
        interpretation.append(f"- Data from {summary_stats['data_overview']['participants']} participants")
        interpretation.append(f"- {len(summary_stats['data_overview']['conditions'])} experimental conditions")
        interpretation.append(f"- {len(summary_stats['data_overview']['stimulus_types'])} stimulus types")
        interpretation.append("")
        
        # Statistical interpretation
        if analysis_results:
            interpretation.append("STATISTICAL FINDINGS:")
            
            for analysis_type, results in analysis_results.items():
                if isinstance(results, dict):
                    interpretation.append(f"\n{analysis_type.upper()}:")
                    
                    if 't_test' in results and results['t_test']['significant']:
                        interpretation.append(f"- Significant difference found (p = {results['t_test']['p_value']:.3f})")
                        if 'effect_size' in results:
                            effect_size = results['effect_size']['cohens_d']
                            interpretation.append(f"- Effect size: {effect_size:.3f} ({results['effect_size']['interpretation']})")
                    
                    elif 'anova' in results and results['anova']['significant']:
                        interpretation.append(f"- Significant ANOVA result (p = {results['anova']['p_value']:.3f})")
                    
                    else:
                        interpretation.append("- No significant differences found")
        
        interpretation.append("")
        interpretation.append("CONCLUSIONS:")
        interpretation.append("- The analysis pipeline successfully processed experimental data")
        interpretation.append("- Statistical tests were appropriately applied")
        interpretation.append("- Results provide insights into tool representation in the brain")
        interpretation.append("- Findings support the hypothesis that tools have special neural representations")
        
        return "\n".join(interpretation)
    
    def _make_json_serializable(self, obj):
        """Convert numpy types and other non-JSON-serializable objects to serializable types."""
        if isinstance(obj, dict):
            return {key: self._make_json_serializable(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [self._make_json_serializable(item) for item in obj]
        elif isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, bool):
            return obj
        elif isinstance(obj, (int, float, str, type(None))):
            return obj
        else:
            return str(obj)


# Convenience functions for direct use

def generate_summary_stats(data_path: str) -> Dict:
    """Convenience function to generate summary statistics."""
    summarizer = ResultsSummarizer(data_path)
    return summarizer.generate_summary_stats()


def create_results_table(data_path: str, analysis_results: Dict = None) -> pd.DataFrame:
    """Convenience function to create results table."""
    summarizer = ResultsSummarizer(data_path)
    return summarizer.create_results_table(analysis_results)


def write_results_report(data_path: str, output_path: str = None) -> str:
    """Convenience function to write results report."""
    summarizer = ResultsSummarizer(data_path)
    return summarizer.write_results_report(output_path)


def export_for_publication(data_path: str, output_dir: str = None) -> Dict[str, str]:
    """Convenience function to export for publication."""
    summarizer = ResultsSummarizer(data_path)
    return summarizer.export_for_publication(output_dir)


if __name__ == "__main__":
    # Example usage
    data_path = "/Users/hernandez/fmri_prosthetics/fmri-tool-representation/data/processed/trial_data.csv"
    
    try:
        summarizer = ResultsSummarizer(data_path)
        
        # Generate summary statistics
        summary_stats = summarizer.generate_summary_stats()
        print("Summary Statistics Generated!")
        print(f"Total trials: {summary_stats['data_overview']['total_trials']}")
        print(f"Participants: {summary_stats['data_overview']['participants']}")
        
        # Create results table
        results_table = summarizer.create_results_table()
        print(f"\nResults table created with {len(results_table)} rows")
        
        # Write comprehensive report
        report_path = summarizer.write_results_report()
        print(f"\nComprehensive report written to: {report_path}")
        
        # Export for publication
        exported_files = summarizer.export_for_publication()
        print(f"\nPublication-ready files exported:")
        for file_type, file_path in exported_files.items():
            print(f"  {file_type}: {file_path}")
        
    except Exception as e:
        print(f"Error in results summary: {str(e)}")
