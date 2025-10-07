"""
fMRI Tool Representation Study - Statistical Analysis Module

This module provides comprehensive statistical analysis functions for the fMRI Tool 
Representation Study, implementing the analysis pipeline for Creem-Regehr & Lee (2005) 
replication study on neural representations of graspable objects.

Author: fMRI Tool Representation Study Team
Date: 2024
"""

import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import ttest_rel, ttest_ind, f_oneway, chi2_contingency
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from typing import Dict, List, Tuple, Optional, Union
import logging
from pathlib import Path
import warnings

# Set up module logger (configured by application)
logger = logging.getLogger(__name__)

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')


class StatisticalAnalyzer:
    """
    Main class for statistical analysis of fMRI Tool Representation Study data.
    
    This class implements comprehensive statistical tests addressing the research
    questions from Creem-Regehr & Lee (2005) replication study.
    """
    
    def __init__(self, data_path: str = None, df: pd.DataFrame = None):
        """
        Initialize the StatisticalAnalyzer.
        
        Args:
            data_path: Path to processed data file (CSV or Excel)
            df: Pre-loaded DataFrame (alternative to data_path)
        """
        if df is not None:
            self.df = df.copy()
        elif data_path is not None:
            self.df = self._load_data(data_path)
        else:
            raise ValueError("Either data_path or df must be provided")
        
        # Initialize results storage
        self.results = {}
        self.effect_sizes = {}
        
        logger.info(f"Initialized StatisticalAnalyzer with {len(self.df)} trials")
    
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
    
    def compare_tools_vs_shapes(self, condition: str = None) -> Dict:
        """
        Compare tools vs shapes across all tasks or specific condition.
        
        Args:
            condition: Specific condition to analyze (None for all conditions)
            
        Returns:
            Dictionary with statistical results
        """
        logger.info(f"Comparing tools vs shapes for condition: {condition}")
        
        # Filter data
        if condition:
            data = self.df[self.df['condition'] == condition].copy()
        else:
            data = self.df.copy()
        
        # Define tool and shape categories (handle case variations)
        tool_categories = ['tool', 'SCRtool']
        shape_categories = ['Shape', 'SCRshape', 'shape']  # Include both cases
        
        # Create binary categories
        data['is_tool'] = data['stimulus_type'].isin(tool_categories)
        data['is_shape'] = data['stimulus_type'].isin(shape_categories)
        
        # Filter to only include tool/shape trials
        analysis_data = data[data['is_tool'] | data['is_shape']].copy()
        
        if len(analysis_data) == 0:
            logger.info("No tool/shape data found for analysis")
            return {'error': 'No tool/shape data found'}
        
        results = {
            'analysis_type': 'tools_vs_shapes',
            'condition': condition,
            'n_trials': len(analysis_data),
            'n_tools': len(analysis_data[analysis_data['is_tool']]),
            'n_shapes': len(analysis_data[analysis_data['is_shape']]),
            'participants': analysis_data['participant_id'].nunique()
        }
        
        # Descriptive statistics
        tool_stats = analysis_data[analysis_data['is_tool']].describe()
        shape_stats = analysis_data[analysis_data['is_shape']].describe()
        
        results['descriptive_stats'] = {
            'tools': tool_stats.to_dict(),
            'shapes': shape_stats.to_dict()
        }
        
        # Statistical tests
        if 'stimulus_onset' in analysis_data.columns:
            tool_onsets = analysis_data[analysis_data['is_tool']]['stimulus_onset'].dropna()
            shape_onsets = analysis_data[analysis_data['is_shape']]['stimulus_onset'].dropna()
            
            if len(tool_onsets) > 0 and len(shape_onsets) > 0:
                # Independent t-test
                t_stat, p_value = ttest_ind(tool_onsets, shape_onsets)
                results['t_test'] = {
                    't_statistic': t_stat,
                    'p_value': p_value,
                    'significant': p_value < 0.05
                }
                
                # Effect size (Cohen's d)
                pooled_std = np.sqrt(((len(tool_onsets) - 1) * tool_onsets.std()**2 + 
                                    (len(shape_onsets) - 1) * shape_onsets.std()**2) / 
                                   (len(tool_onsets) + len(shape_onsets) - 2))
                cohens_d = (tool_onsets.mean() - shape_onsets.mean()) / pooled_std
                results['effect_size'] = {
                    'cohens_d': cohens_d,
                    'interpretation': self._interpret_cohens_d(cohens_d)
                }
        
        # Within-subject analysis if multiple participants
        if results['participants'] > 1:
            within_subject_results = self._within_subject_analysis(analysis_data, 'is_tool')
            results['within_subject'] = within_subject_results
        
        logger.info(f"Tools vs shapes analysis complete: p={results.get('t_test', {}).get('p_value', 'N/A')}")
        return results
    
    def compare_task_conditions(self, stimulus_type: str = None) -> Dict:
        """
        Compare passive vs active vs motor conditions.
        
        Args:
            stimulus_type: Specific stimulus type to analyze (None for all)
            
        Returns:
            Dictionary with statistical results
        """
        logger.info(f"Comparing task conditions for stimulus type: {stimulus_type}")
        
        # Filter data
        if stimulus_type:
            data = self.df[self.df['stimulus_type'] == stimulus_type].copy()
        else:
            data = self.df.copy()
        
        # Get unique conditions
        conditions = data['condition'].unique()
        results = {
            'analysis_type': 'task_conditions',
            'stimulus_type': stimulus_type,
            'conditions': list(conditions),
            'n_trials': len(data),
            'participants': data['participant_id'].nunique()
        }
        
        if len(conditions) < 2:
            logger.info("Need at least 2 conditions for comparison")
            return {'error': 'Need at least 2 conditions for comparison'}
        
        # Descriptive statistics by condition
        condition_stats = {}
        for condition in conditions:
            cond_data = data[data['condition'] == condition]
            condition_stats[condition] = cond_data.describe().to_dict()
        
        results['descriptive_stats'] = condition_stats
        
        # Statistical tests
        if 'stimulus_onset' in data.columns:
            # Prepare data for ANOVA
            condition_groups = []
            for condition in conditions:
                group_data = data[data['condition'] == condition]['stimulus_onset'].dropna()
                if len(group_data) > 0:
                    condition_groups.append(group_data)
            
            if len(condition_groups) >= 2:
                # One-way ANOVA
                f_stat, p_value = f_oneway(*condition_groups)
                results['anova'] = {
                    'f_statistic': f_stat,
                    'p_value': p_value,
                    'significant': p_value < 0.05
                }
                
                # Post-hoc pairwise comparisons
                pairwise_results = {}
                for i, cond1 in enumerate(conditions):
                    for j, cond2 in enumerate(conditions):
                        if i < j:
                            group1 = data[data['condition'] == cond1]['stimulus_onset'].dropna()
                            group2 = data[data['condition'] == cond2]['stimulus_onset'].dropna()
                            
                            if len(group1) > 0 and len(group2) > 0:
                                t_stat, p_val = ttest_ind(group1, group2)
                                pairwise_results[f"{cond1}_vs_{cond2}"] = {
                                    't_statistic': t_stat,
                                    'p_value': p_val,
                                    'significant': p_val < 0.05
                                }
                
                results['pairwise_comparisons'] = pairwise_results
        
        logger.info(f"Task conditions analysis complete: {len(conditions)} conditions compared")
        return results
    
    def analyze_motor_activation(self) -> Dict:
        """
        Analyze motor network activation patterns.
        
        Returns:
            Dictionary with motor activation analysis results
        """
        logger.info("Analyzing motor activation patterns")
        
        # Focus on conditions that involve motor tasks
        motor_conditions = ['active_grasp', 'imagined_grasp', 'clench']
        motor_data = self.df[self.df['condition'].isin(motor_conditions)].copy()
        
        if len(motor_data) == 0:
            logger.info("No motor condition data found")
            return {'error': 'No motor condition data found'}
        
        results = {
            'analysis_type': 'motor_activation',
            'motor_conditions': list(motor_data['condition'].unique()),
            'n_trials': len(motor_data),
            'participants': motor_data['participant_id'].nunique()
        }
        
        # Compare motor vs non-motor conditions
        non_motor_data = self.df[~self.df['condition'].isin(motor_conditions)].copy()
        
        if len(non_motor_data) > 0:
            motor_vs_non_motor = self._compare_groups(
                motor_data, non_motor_data, 
                'Motor Conditions', 'Non-Motor Conditions'
            )
            results['motor_vs_non_motor'] = motor_vs_non_motor
        
        # Analyze within motor conditions
        motor_condition_comparison = self.compare_task_conditions()
        results['within_motor_conditions'] = motor_condition_comparison
        
        # Tool-specific motor analysis
        tool_motor_data = motor_data[motor_data['stimulus_type'].isin(['tool', 'SCRtool'])]
        if len(tool_motor_data) > 0:
            tool_motor_results = self._analyze_tool_motor_patterns(tool_motor_data)
            results['tool_motor_patterns'] = tool_motor_results
        
        logger.info("Motor activation analysis complete")
        return results
    
    def functional_vs_structural(self) -> Dict:
        """
        Compare functional tools vs neutral shapes.
        
        Returns:
            Dictionary with functional vs structural analysis results
        """
        logger.info("Analyzing functional vs structural differences")
        
        # Define functional and structural categories
        functional_categories = ['tool', 'SCRtool']  # Functional tools
        structural_categories = ['Shape', 'SCRshape', 'shape']  # Neutral shapes (handle case variations)
        
        # Filter data
        functional_data = self.df[self.df['stimulus_type'].isin(functional_categories)].copy()
        structural_data = self.df[self.df['stimulus_type'].isin(structural_categories)].copy()
        
        results = {
            'analysis_type': 'functional_vs_structural',
            'functional_n': len(functional_data),
            'structural_n': len(structural_data),
            'participants': self.df['participant_id'].nunique()
        }
        
        if len(functional_data) == 0 or len(structural_data) == 0:
            logger.info("Insufficient data for functional vs structural analysis")
            return {'error': 'Insufficient data for functional vs structural analysis'}
        
        # Compare functional vs structural
        comparison_results = self._compare_groups(
            functional_data, structural_data,
            'Functional Tools', 'Structural Shapes'
        )
        results['comparison'] = comparison_results
        
        # Analyze across different conditions
        condition_results = {}
        for condition in self.df['condition'].unique():
            cond_functional = functional_data[functional_data['condition'] == condition]
            cond_structural = structural_data[structural_data['condition'] == condition]
            
            if len(cond_functional) > 0 and len(cond_structural) > 0:
                cond_comparison = self._compare_groups(
                    cond_functional, cond_structural,
                    f'Functional ({condition})', f'Structural ({condition})'
                )
                condition_results[condition] = cond_comparison
        
        results['by_condition'] = condition_results
        
        logger.info("Functional vs structural analysis complete")
        return results
    
    # Research Question Analysis Methods
    
    def analyze_rq1_tools_special(self) -> Dict:
        """
        Research Question 1: Are Tools Special?
        Compare tools vs shapes across all tasks.
        """
        logger.info("Analyzing RQ1: Are Tools Special?")
        
        results = {
            'research_question': 'RQ1: Are Tools Special?',
            'hypothesis': 'Tools should show different neural activation patterns compared to shapes',
            'analyses': {}
        }
        
        # Overall tools vs shapes comparison
        overall_comparison = self.compare_tools_vs_shapes()
        results['analyses']['overall_tools_vs_shapes'] = overall_comparison
        
        # By condition analysis
        for condition in self.df['condition'].unique():
            cond_comparison = self.compare_tools_vs_shapes(condition)
            results['analyses'][f'tools_vs_shapes_{condition}'] = cond_comparison
        
        # Screen-optimized vs standard stimuli
        scr_tools = self.df[self.df['stimulus_type'] == 'SCRtool']
        scr_shapes = self.df[self.df['stimulus_type'] == 'SCRshape']
        standard_tools = self.df[self.df['stimulus_type'] == 'tool']
        standard_shapes = self.df[self.df['stimulus_type'].isin(['Shape', 'shape'])]
        
        if len(scr_tools) > 0 and len(scr_shapes) > 0:
            scr_comparison = self._compare_groups(scr_tools, scr_shapes, 'SCR Tools', 'SCR Shapes')
            results['analyses']['screen_optimized_tools_vs_shapes'] = scr_comparison
        
        if len(standard_tools) > 0 and len(standard_shapes) > 0:
            standard_comparison = self._compare_groups(standard_tools, standard_shapes, 'Standard Tools', 'Standard Shapes')
            results['analyses']['standard_tools_vs_shapes'] = standard_comparison
        
        logger.info("RQ1 analysis complete")
        return results
    
    def analyze_rq2_action_potentiation(self) -> Dict:
        """
        Research Question 2: Action Potentiation
        Compare passive viewing vs active grasping.
        """
        logger.info("Analyzing RQ2: Action Potentiation")
        
        results = {
            'research_question': 'RQ2: Action Potentiation',
            'hypothesis': 'Active grasping should enhance neural responses compared to passive viewing',
            'analyses': {}
        }
        
        # Overall passive vs active comparison
        passive_data = self.df[self.df['condition'] == 'passive_viewing']
        active_data = self.df[self.df['condition'] == 'active_grasp']
        
        if len(passive_data) > 0 and len(active_data) > 0:
            overall_comparison = self._compare_groups(passive_data, active_data, 'Passive Viewing', 'Active Grasp')
            results['analyses']['overall_passive_vs_active'] = overall_comparison
        
        # Tools: Passive vs Active
        tool_passive = passive_data[passive_data['stimulus_type'].isin(['tool', 'SCRtool'])]
        tool_active = active_data[active_data['stimulus_type'].isin(['tool', 'SCRtool'])]
        
        if len(tool_passive) > 0 and len(tool_active) > 0:
            tool_comparison = self._compare_groups(tool_passive, tool_active, 'Tools Passive', 'Tools Active')
            results['analyses']['tools_passive_vs_active'] = tool_comparison
        
        # Shapes: Passive vs Active
        shape_passive = passive_data[passive_data['stimulus_type'].isin(['Shape', 'SCRshape', 'shape'])]
        shape_active = active_data[active_data['stimulus_type'].isin(['Shape', 'SCRshape', 'shape'])]
        
        if len(shape_passive) > 0 and len(shape_active) > 0:
            shape_comparison = self._compare_groups(shape_passive, shape_active, 'Shapes Passive', 'Shapes Active')
            results['analyses']['shapes_passive_vs_active'] = shape_comparison
        
        # Interaction analysis
        interaction_results = self._analyze_interaction_effects()
        results['analyses']['interaction_effects'] = interaction_results
        
        logger.info("RQ2 analysis complete")
        return results
    
    def analyze_rq3_functional_structural(self) -> Dict:
        """
        Research Question 3: Functional vs Structural
        Compare functional tools vs neutral shapes.
        """
        logger.info("Analyzing RQ3: Functional vs Structural")
        
        results = {
            'research_question': 'RQ3: Functional vs Structural',
            'hypothesis': 'Functional tools should show different activation patterns than neutral shapes',
            'analyses': {}
        }
        
        # Overall functional vs structural
        functional_structural_results = self.functional_vs_structural()
        results['analyses']['overall_functional_vs_structural'] = functional_structural_results
        
        # Standard vs screen-optimized stimuli
        standard_functional = self.df[self.df['stimulus_type'] == 'tool']
        standard_structural = self.df[self.df['stimulus_type'].isin(['Shape', 'shape'])]
        scr_functional = self.df[self.df['stimulus_type'] == 'SCRtool']
        scr_structural = self.df[self.df['stimulus_type'] == 'SCRshape']
        
        if len(standard_functional) > 0 and len(standard_structural) > 0:
            standard_comparison = self._compare_groups(standard_functional, standard_structural, 'Standard Functional', 'Standard Structural')
            results['analyses']['standard_functional_vs_structural'] = standard_comparison
        
        if len(scr_functional) > 0 and len(scr_structural) > 0:
            scr_comparison = self._compare_groups(scr_functional, scr_structural, 'SCR Functional', 'SCR Structural')
            results['analyses']['scr_functional_vs_structural'] = scr_comparison
        
        logger.info("RQ3 analysis complete")
        return results
    
    # Helper methods
    
    def _compare_groups(self, group1: pd.DataFrame, group2: pd.DataFrame, 
                        group1_name: str, group2_name: str) -> Dict:
        """Compare two groups statistically."""
        results = {
            'group1_name': group1_name,
            'group2_name': group2_name,
            'group1_n': len(group1),
            'group2_n': len(group2)
        }
        
        if 'stimulus_onset' in group1.columns and 'stimulus_onset' in group2.columns:
            group1_onsets = group1['stimulus_onset'].dropna()
            group2_onsets = group2['stimulus_onset'].dropna()
            
            if len(group1_onsets) > 0 and len(group2_onsets) > 0:
                # Independent t-test
                t_stat, p_value = ttest_ind(group1_onsets, group2_onsets)
                results['t_test'] = {
                    't_statistic': t_stat,
                    'p_value': p_value,
                    'significant': p_value < 0.05
                }
                
                # Effect size
                pooled_std = np.sqrt(((len(group1_onsets) - 1) * group1_onsets.std()**2 + 
                                    (len(group2_onsets) - 1) * group2_onsets.std()**2) / 
                                   (len(group1_onsets) + len(group2_onsets) - 2))
                cohens_d = (group1_onsets.mean() - group2_onsets.mean()) / pooled_std
                results['effect_size'] = {
                    'cohens_d': cohens_d,
                    'interpretation': self._interpret_cohens_d(cohens_d)
                }
                
                # Descriptive statistics
                results['descriptive_stats'] = {
                    'group1': {
                        'mean': group1_onsets.mean(),
                        'std': group1_onsets.std(),
                        'median': group1_onsets.median()
                    },
                    'group2': {
                        'mean': group2_onsets.mean(),
                        'std': group2_onsets.std(),
                        'median': group2_onsets.median()
                    }
                }
        
        return results
    
    def _within_subject_analysis(self, data: pd.DataFrame, grouping_var: str) -> Dict:
        """Perform within-subject analysis."""
        results = {}
        
        if data['participant_id'].nunique() > 1:
            # Paired t-test for within-subject comparison
            participants = data['participant_id'].unique()
            
            group1_means = []
            group2_means = []
            
            for participant in participants:
                participant_data = data[data['participant_id'] == participant]
                group1_data = participant_data[participant_data[grouping_var] == True]
                group2_data = participant_data[participant_data[grouping_var] == False]
                
                if len(group1_data) > 0 and len(group2_data) > 0:
                    if 'stimulus_onset' in group1_data.columns:
                        group1_means.append(group1_data['stimulus_onset'].mean())
                        group2_means.append(group2_data['stimulus_onset'].mean())
            
            if len(group1_means) > 1 and len(group2_means) > 1:
                t_stat, p_value = ttest_rel(group1_means, group2_means)
                results['paired_t_test'] = {
                    't_statistic': t_stat,
                    'p_value': p_value,
                    'significant': p_value < 0.05,
                    'n_participants': len(group1_means)
                }
        
        return results
    
    def _analyze_tool_motor_patterns(self, tool_motor_data: pd.DataFrame) -> Dict:
        """Analyze motor patterns specific to tools."""
        results = {
            'analysis_type': 'tool_motor_patterns',
            'n_trials': len(tool_motor_data)
        }
        
        # Compare different motor conditions for tools
        motor_conditions = tool_motor_data['condition'].unique()
        if len(motor_conditions) > 1:
            condition_comparison = self.compare_task_conditions()
            results['motor_condition_comparison'] = condition_comparison
        
        return results
    
    def _analyze_interaction_effects(self) -> Dict:
        """Analyze interaction effects between stimulus type and condition."""
        results = {'analysis_type': 'interaction_effects'}
        
        # Create interaction variable
        interaction_data = self.df.copy()
        interaction_data['stimulus_category'] = interaction_data['stimulus_type'].apply(
            lambda x: 'tool' if x in ['tool', 'SCRtool'] else 'shape'
        )
        
        # Two-way ANOVA (simplified)
        if len(interaction_data) > 0:
            # This is a simplified interaction analysis
            # In a full implementation, you would use statsmodels or similar
            results['note'] = 'Simplified interaction analysis - full implementation would use two-way ANOVA'
        
        return results
    
    def _interpret_cohens_d(self, d: float) -> str:
        """Interpret Cohen's d effect size."""
        abs_d = abs(d)
        if abs_d < 0.2:
            return "negligible"
        elif abs_d < 0.5:
            return "small"
        elif abs_d < 0.8:
            return "medium"
        else:
            return "large"
    
    def generate_comprehensive_report(self) -> Dict:
        """Generate comprehensive statistical analysis report."""
        logger.info("Generating comprehensive statistical report")
        
        report = {
            'report_type': 'comprehensive_statistical_analysis',
            'data_summary': {
                'total_trials': len(self.df),
                'participants': self.df['participant_id'].nunique(),
                'conditions': list(self.df['condition'].unique()),
                'stimulus_types': list(self.df['stimulus_type'].unique())
            },
            'research_questions': {}
        }
        
        # Analyze all research questions
        report['research_questions']['rq1'] = self.analyze_rq1_tools_special()
        report['research_questions']['rq2'] = self.analyze_rq2_action_potentiation()
        report['research_questions']['rq3'] = self.analyze_rq3_functional_structural()
        
        # Additional analyses
        report['additional_analyses'] = {
            'motor_activation': self.analyze_motor_activation(),
            'functional_vs_structural': self.functional_vs_structural()
        }
        
        logger.info("Comprehensive report generated")
        return report


# Convenience functions for direct use

def analyze_tools_vs_shapes(data_path: str, condition: str = None) -> Dict:
    """Convenience function to analyze tools vs shapes."""
    analyzer = StatisticalAnalyzer(data_path)
    return analyzer.compare_tools_vs_shapes(condition)


def analyze_task_conditions(data_path: str, stimulus_type: str = None) -> Dict:
    """Convenience function to analyze task conditions."""
    analyzer = StatisticalAnalyzer(data_path)
    return analyzer.compare_task_conditions(stimulus_type)


def generate_full_analysis_report(data_path: str) -> Dict:
    """Convenience function to generate full analysis report."""
    analyzer = StatisticalAnalyzer(data_path)
    return analyzer.generate_comprehensive_report()


if __name__ == "__main__":
    # Example usage
    data_path = "/Users/hernandez/fmri_prosthetics/fmri-tool-representation/data/processed/trial_data.csv"
    
    try:
        analyzer = StatisticalAnalyzer(data_path)
        
        # Generate comprehensive report
        report = analyzer.generate_comprehensive_report()
        
        print("Statistical Analysis Complete!")
        print(f"Analyzed {report['data_summary']['total_trials']} trials")
        print(f"Participants: {report['data_summary']['participants']}")
        print(f"Conditions: {report['data_summary']['conditions']}")
        
    except Exception as e:
        print(f"Error in analysis: {str(e)}")
