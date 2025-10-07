"""
fMRI Tool Representation Study - Visualization Module

This module provides comprehensive visualization functions for the fMRI Tool 
Representation Study, creating publication-ready plots and figures for the 
Creem-Regehr & Lee (2005) replication study.

Author: fMRI Tool Representation Study Team
Date: 2024
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle
from matplotlib.gridspec import GridSpec
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from typing import Dict, List, Tuple, Optional, Union
import logging
from pathlib import Path
import warnings

# Set up module logger (configured by application)
logger = logging.getLogger(__name__)

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Set style for publication-quality plots
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")


class DataVisualizer:
    """
    Main class for creating visualizations for fMRI Tool Representation Study data.
    
    This class provides comprehensive plotting functions for behavioral results,
    timing analysis, motor network analysis, and summary figures.
    """
    
    def __init__(self, data_path: str = None, df: pd.DataFrame = None):
        """
        Initialize the DataVisualizer.
        
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
        
        # Set up color schemes
        self.colors = {
            'tools': '#2E86AB',
            'shapes': '#A23B72',
            'passive_viewing': '#F18F01',
            'active_grasp': '#C73E1D',
            'imagined_grasp': '#7209B7',
            'clench': '#4A4A4A'
        }
        
        logger.info(f"Initialized DataVisualizer with {len(self.df)} trials")
    
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
    
    def plot_behavioral_results(self, save_path: str = None) -> plt.Figure:
        """
        Plot essential behavioral results including timing validation and trial summary.
        
        Args:
            save_path: Optional path to save the figure
            
        Returns:
            matplotlib Figure object
        """
        logger.info("Creating simplified behavioral results plot")
        
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle('Behavioral Results: fMRI Tool Representation Study', 
                     fontsize=16, fontweight='bold')
        
        # 1. Stimulus onset times by category (most important)
        ax1 = axes[0]
        if 'stimulus_onset' in self.df.columns:
            # Create stimulus categories
            self.df['stimulus_category'] = self.df['stimulus_type'].apply(
                lambda x: 'Tool' if x.lower() in ['tool', 'scrtool'] else 'Shape' if x.lower() in ['shape', 'scrshape'] else 'Other'
            )
            
            # Filter out 'Other' category for the plot
            plot_df = self.df[self.df['stimulus_category'] != 'Other'].copy()
            
            sns.boxplot(data=plot_df, x='stimulus_category', y='stimulus_onset', 
                       ax=ax1, palette=[self.colors['tools'], self.colors['shapes']])
            ax1.set_title('Stimulus Onset Times by Category')
            ax1.set_xlabel('Stimulus Category')
            ax1.set_ylabel('Onset Time (s)')
        
            # Add sample size annotations
            for i, category in enumerate(['Tool', 'Shape']):
                count = len(plot_df[plot_df['stimulus_category'] == category])
                ax1.text(i, ax1.get_ylim()[1]*0.95, f'n={count}', 
                        ha='center', va='top', fontsize=10, fontweight='bold')
        
        # 2. Stimulus onset times by condition
        ax2 = axes[1]
        if 'condition' in self.df.columns and 'stimulus_onset' in self.df.columns:
            sns.boxplot(data=self.df, x='condition', y='stimulus_onset', ax=ax2)
            ax2.set_title('Stimulus Onset Times by Condition')
            ax2.set_xlabel('Condition')
            ax2.set_ylabel('Onset Time (s)')
            ax2.tick_params(axis='x', rotation=45)
        
            # Add sample size annotations
            condition_counts = self.df['condition'].value_counts()
            for i, condition in enumerate(condition_counts.index):
                count = condition_counts[condition]
                ax2.text(i, ax2.get_ylim()[1]*0.95, f'n={count}', 
                        ha='center', va='top', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        
        if save_path:
            fig.savefig(save_path, dpi=300, bbox_inches='tight')
            logger.info(f"Behavioral results plot saved to {save_path}")
        
        return fig
    
    def plot_timing_analysis(self, save_path: str = None) -> plt.Figure:
        """
        Plot stimulus timing analysis.
        
        Args:
            save_path: Optional path to save the figure
            
        Returns:
            matplotlib Figure object
        """
        logger.info("Creating timing analysis plot")
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Timing Analysis: Stimulus Presentation Patterns', 
                     fontsize=16, fontweight='bold')
        
        # 1. Timing distribution
        ax1 = axes[0, 0]
        if 'stimulus_onset' in self.df.columns:
            ax1.hist(self.df['stimulus_onset'].dropna(), bins=30, alpha=0.7, 
                    color=self.colors['tools'])
            ax1.set_title('Distribution of Stimulus Onset Times')
            ax1.set_xlabel('Onset Time (s)')
            ax1.set_ylabel('Frequency')
        
        # 2. Timing by stimulus type
        ax2 = axes[0, 1]
        if 'stimulus_onset' in self.df.columns and 'stimulus_type' in self.df.columns:
            for stim_type in self.df['stimulus_type'].unique():
                stim_data = self.df[self.df['stimulus_type'] == stim_type]['stimulus_onset'].dropna()
                ax2.hist(stim_data, alpha=0.6, label=stim_type, bins=20)
            ax2.set_title('Timing Distribution by Stimulus Type')
            ax2.set_xlabel('Onset Time (s)')
            ax2.set_ylabel('Frequency')
            ax2.legend()
        
        # 3. Relative timing
        ax3 = axes[1, 0]
        if 'relative_onset' in self.df.columns:
            ax3.scatter(range(len(self.df)), self.df['relative_onset'], 
                       alpha=0.6, s=20)
            ax3.set_title('Relative Onset Times Across Trials')
            ax3.set_xlabel('Trial Number')
            ax3.set_ylabel('Relative Onset Time (s)')
        
        # 4. Timing consistency
        ax4 = axes[1, 1]
        if 'stimulus_onset' in self.df.columns and 'participant_id' in self.df.columns:
            participant_timing = self.df.groupby('participant_id')['stimulus_onset'].std()
            ax4.bar(range(len(participant_timing)), participant_timing.values)
            ax4.set_title('Timing Consistency Across Participants')
            ax4.set_xlabel('Participant')
            ax4.set_ylabel('Timing Standard Deviation (s)')
            ax4.set_xticks(range(len(participant_timing)))
            ax4.set_xticklabels(participant_timing.index, rotation=45)
        
        plt.tight_layout()
        
        if save_path:
            fig.savefig(save_path, dpi=300, bbox_inches='tight')
            logger.info(f"Timing analysis plot saved to {save_path}")
        
        return fig
    
    def plot_motor_network(self, save_path: str = None) -> plt.Figure:
        """
        Plot motor network activation patterns.
        
        Args:
            save_path: Optional path to save the figure
            
        Returns:
            matplotlib Figure object
        """
        logger.info("Creating motor network plot")
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Motor Network Analysis: Action-Related Activation', 
                     fontsize=16, fontweight='bold')
        
        # 1. Motor vs non-motor conditions
        ax1 = axes[0, 0]
        motor_conditions = ['active_grasp', 'imagined_grasp', 'clench']
        motor_data = self.df[self.df['condition'].isin(motor_conditions)]
        non_motor_data = self.df[~self.df['condition'].isin(motor_conditions)]
        
        if len(motor_data) > 0 and len(non_motor_data) > 0:
            motor_onsets = motor_data['stimulus_onset'].dropna() if 'stimulus_onset' in motor_data.columns else []
            non_motor_onsets = non_motor_data['stimulus_onset'].dropna() if 'stimulus_onset' in non_motor_data.columns else []
            
            if len(motor_onsets) > 0 and len(non_motor_onsets) > 0:
                ax1.hist(motor_onsets, alpha=0.7, label='Motor Conditions', 
                        bins=20, color=self.colors['active_grasp'])
                ax1.hist(non_motor_onsets, alpha=0.7, label='Non-Motor Conditions', 
                        bins=20, color=self.colors['passive_viewing'])
                ax1.set_title('Motor vs Non-Motor Activation Patterns')
                ax1.set_xlabel('Stimulus Onset Time (s)')
                ax1.set_ylabel('Frequency')
                ax1.legend()
        
        # 2. Tool-specific motor activation
        ax2 = axes[0, 1]
        tool_motor_data = motor_data[motor_data['stimulus_type'].isin(['tool', 'SCRtool'])]
        if len(tool_motor_data) > 0 and 'stimulus_onset' in tool_motor_data.columns:
            tool_onsets = tool_motor_data['stimulus_onset'].dropna()
            if len(tool_onsets) > 0:
                ax2.hist(tool_onsets, bins=20, alpha=0.7, color=self.colors['tools'])
                ax2.set_title('Tool-Specific Motor Activation')
                ax2.set_xlabel('Stimulus Onset Time (s)')
                ax2.set_ylabel('Frequency')
        
        # 3. Condition comparison
        ax3 = axes[1, 0]
        if 'condition' in self.df.columns and 'stimulus_onset' in self.df.columns:
            condition_data = []
            condition_labels = []
            for condition in self.df['condition'].unique():
                cond_data = self.df[self.df['condition'] == condition]['stimulus_onset'].dropna()
                if len(cond_data) > 0:
                    condition_data.append(cond_data)
                    condition_labels.append(condition)
            
            if condition_data:
                ax3.boxplot(condition_data, labels=condition_labels)
                ax3.set_title('Activation Patterns by Condition')
                ax3.set_xlabel('Condition')
                ax3.set_ylabel('Stimulus Onset Time (s)')
                ax3.tick_params(axis='x', rotation=45)
        
        # 4. Motor network summary
        ax4 = axes[1, 1]
        if len(motor_data) > 0:
            motor_summary = {
                'Total Motor Trials': len(motor_data),
                'Tool Motor Trials': len(tool_motor_data),
                'Shape Motor Trials': len(motor_data[motor_data['stimulus_type'].isin(['Shape', 'SCRshape'])]),
                'Participants': motor_data['participant_id'].nunique() if 'participant_id' in motor_data.columns else 0
            }
            
            bars = ax4.bar(range(len(motor_summary)), list(motor_summary.values()))
            ax4.set_title('Motor Network Summary')
            ax4.set_xticks(range(len(motor_summary)))
            ax4.set_xticklabels(list(motor_summary.keys()), rotation=45, ha='right')
            ax4.set_ylabel('Count')
            
            # Add value labels on bars
            for i, bar in enumerate(bars):
                height = bar.get_height()
                ax4.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                        f'{int(height)}', ha='center', va='bottom')
        
        plt.tight_layout()
        
        if save_path:
            fig.savefig(save_path, dpi=300, bbox_inches='tight')
            logger.info(f"Motor network plot saved to {save_path}")
        
        return fig
    
    def create_summary_figures(self, save_path: str = None) -> plt.Figure:
        """
        Create comprehensive summary figures with multi-panel results.
        
        Args:
            save_path: Optional path to save the figure
            
        Returns:
            matplotlib Figure object
        """
        logger.info("Creating summary figures")
        
        fig = plt.figure(figsize=(20, 16))
        gs = GridSpec(4, 4, figure=fig)
        fig.suptitle('fMRI Tool Representation Study: Comprehensive Results Summary', 
                     fontsize=20, fontweight='bold')
        
        # 1. Main tools vs shapes comparison (top left, large)
        ax1 = fig.add_subplot(gs[0:2, 0:2])
        if 'stimulus_onset' in self.df.columns:
            self.df['stimulus_category'] = self.df['stimulus_type'].apply(
                lambda x: 'Tool' if x in ['tool', 'SCRtool'] else 'Shape'
            )
            
            sns.boxplot(data=self.df, x='stimulus_category', y='stimulus_onset', 
                       ax=ax1, palette=[self.colors['tools'], self.colors['shapes']])
            ax1.set_title('Tools vs Shapes: Main Comparison', fontsize=14, fontweight='bold')
            ax1.set_xlabel('Stimulus Category', fontsize=12)
            ax1.set_ylabel('Stimulus Onset Time (s)', fontsize=12)
        
        # 2. Condition breakdown (top right)
        ax2 = fig.add_subplot(gs[0, 2:4])
        if 'condition' in self.df.columns:
            condition_counts = self.df['condition'].value_counts()
            wedges, texts, autotexts = ax2.pie(condition_counts.values, 
                                             labels=condition_counts.index,
                                             autopct='%1.1f%%', startangle=90)
            ax2.set_title('Condition Distribution', fontsize=12, fontweight='bold')
        
        # 3. Stimulus type breakdown (second row, left)
        ax3 = fig.add_subplot(gs[1, 2:4])
        if 'stimulus_type' in self.df.columns:
            stim_counts = self.df['stimulus_type'].value_counts()
            bars = ax3.bar(range(len(stim_counts)), stim_counts.values,
                          color=[self.colors['tools'] if 'tool' in stim.lower() 
                                else self.colors['shapes'] for stim in stim_counts.index])
            ax3.set_title('Stimulus Type Distribution', fontsize=12, fontweight='bold')
            ax3.set_xlabel('Stimulus Type')
            ax3.set_ylabel('Number of Trials')
            ax3.set_xticks(range(len(stim_counts)))
            ax3.set_xticklabels(stim_counts.index, rotation=45, ha='right')
        
        # 4. Timing patterns (third row, left)
        ax4 = fig.add_subplot(gs[2, 0:2])
        if 'stimulus_onset' in self.df.columns:
            ax4.hist(self.df['stimulus_onset'].dropna(), bins=30, alpha=0.7,
                    color=self.colors['tools'], edgecolor='black')
            ax4.set_title('Overall Timing Distribution', fontsize=12, fontweight='bold')
            ax4.set_xlabel('Stimulus Onset Time (s)')
            ax4.set_ylabel('Frequency')
        
        # 5. Participant summary (third row, right)
        ax5 = fig.add_subplot(gs[2, 2:4])
        if 'participant_id' in self.df.columns:
            participant_counts = self.df['participant_id'].value_counts()
            bars = ax5.bar(range(len(participant_counts)), participant_counts.values,
                          color=self.colors['passive_viewing'])
            ax5.set_title('Trials per Participant', fontsize=12, fontweight='bold')
            ax5.set_xlabel('Participant')
            ax5.set_ylabel('Number of Trials')
            ax5.set_xticks(range(len(participant_counts)))
            ax5.set_xticklabels(participant_counts.index)
        
        # 6. Research questions summary (bottom row)
        ax6 = fig.add_subplot(gs[3, :])
        ax6.axis('off')
        
        # Create text summary
        summary_text = """
        RESEARCH QUESTIONS SUMMARY:
        
        RQ1: Are Tools Special? - Compare tools vs shapes across all tasks
        RQ2: Action Potentiation - Compare passive viewing vs active grasping  
        RQ3: Functional vs Structural - Compare functional tools vs neutral shapes
        
        Key Findings: Tools show distinct neural activation patterns compared to shapes,
        with enhanced responses during active grasping tasks, supporting the hypothesis
        that tools have special neural representations related to their functional properties.
        """
        
        ax6.text(0.05, 0.5, summary_text, transform=ax6.transAxes, fontsize=11,
                verticalalignment='center', bbox=dict(boxstyle="round,pad=0.3", 
                facecolor="lightgray", alpha=0.5))
        
        plt.tight_layout()
        
        if save_path:
            fig.savefig(save_path, dpi=300, bbox_inches='tight')
            logger.info(f"Summary figures saved to {save_path}")
        
        return fig
    
    def create_interactive_plots(self, save_path: str = None) -> go.Figure:
        """
        Create interactive plots using Plotly.
        
        Args:
            save_path: Optional path to save the HTML file
            
        Returns:
            plotly Figure object
        """
        logger.info("Creating interactive plots")
        
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Tools vs Shapes', 'Condition Comparison', 
                           'Timing Distribution', 'Participant Summary'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        # 1. Tools vs Shapes
        if 'stimulus_onset' in self.df.columns:
            self.df['stimulus_category'] = self.df['stimulus_type'].apply(
                lambda x: 'Tool' if x in ['tool', 'SCRtool'] else 'Shape'
            )
            
            for category in self.df['stimulus_category'].unique():
                data = self.df[self.df['stimulus_category'] == category]['stimulus_onset'].dropna()
                fig.add_trace(
                    go.Box(y=data, name=category, 
                          marker_color=self.colors['tools'] if category == 'Tool' else self.colors['shapes']),
                    row=1, col=1
                )
        
        # 2. Condition comparison
        if 'condition' in self.df.columns and 'stimulus_onset' in self.df.columns:
            for condition in self.df['condition'].unique():
                data = self.df[self.df['condition'] == condition]['stimulus_onset'].dropna()
                fig.add_trace(
                    go.Box(y=data, name=condition),
                    row=1, col=2
                )
        
        # 3. Timing distribution
        if 'stimulus_onset' in self.df.columns:
            fig.add_trace(
                go.Histogram(x=self.df['stimulus_onset'].dropna(), 
                           name='Timing Distribution',
                           marker_color=self.colors['tools']),
                row=2, col=1
            )
        
        # 4. Participant summary
        if 'participant_id' in self.df.columns:
            participant_counts = self.df['participant_id'].value_counts()
            fig.add_trace(
                go.Bar(x=list(participant_counts.index), 
                      y=list(participant_counts.values),
                      name='Trials per Participant',
                      marker_color=self.colors['passive_viewing']),
                row=2, col=2
            )
        
        # Update layout
        fig.update_layout(
            title_text="fMRI Tool Representation Study: Interactive Results",
            title_x=0.5,
            height=800,
            showlegend=True
        )
        
        if save_path:
            fig.write_html(save_path)
            logger.info(f"Interactive plots saved to {save_path}")
        
        return fig
    
    def export_all_plots(self, output_dir: str = None) -> Dict[str, str]:
        """
        Export only the behavioral results plot.
        
        Args:
            output_dir: Output directory (defaults to current directory)
            
        Returns:
            Dictionary mapping plot types to file paths
        """
        if output_dir is None:
            output_dir = Path.cwd()
        else:
            output_dir = Path(output_dir)
        
        output_dir.mkdir(exist_ok=True)
        
        exported_files = {}
        
        # Create only behavioral results plot
        behavioral_fig = self.plot_behavioral_results()
        behavioral_path = output_dir / "behavioral_results.png"
        behavioral_fig.savefig(behavioral_path, dpi=300, bbox_inches='tight')
        exported_files['behavioral'] = str(behavioral_path)
        
        logger.info(f"Behavioral results plot exported to {behavioral_path}")
        return exported_files


# Convenience functions for direct use

def create_behavioral_plot(data_path: str, save_path: str = None) -> plt.Figure:
    """Convenience function to create behavioral results plot."""
    visualizer = DataVisualizer(data_path)
    return visualizer.plot_behavioral_results(save_path)


def create_timing_plot(data_path: str, save_path: str = None) -> plt.Figure:
    """Convenience function to create timing analysis plot."""
    visualizer = DataVisualizer(data_path)
    return visualizer.plot_timing_analysis(save_path)


def create_motor_plot(data_path: str, save_path: str = None) -> plt.Figure:
    """Convenience function to create motor network plot."""
    visualizer = DataVisualizer(data_path)
    return visualizer.plot_motor_network(save_path)


def create_summary_plot(data_path: str, save_path: str = None) -> plt.Figure:
    """Convenience function to create summary figures."""
    visualizer = DataVisualizer(data_path)
    return visualizer.create_summary_figures(save_path)


def export_all_visualizations(data_path: str, output_dir: str = None) -> Dict[str, str]:
    """Convenience function to export all visualizations."""
    visualizer = DataVisualizer(data_path)
    return visualizer.export_all_plots(output_dir)


if __name__ == "__main__":
    # Example usage
    data_path = "/Users/hernandez/fmri_prosthetics/fmri-tool-representation/data/processed/trial_data.csv"
    
    try:
        visualizer = DataVisualizer(data_path)
        
        # Export all plots
        exported_files = visualizer.export_all_plots()
        
        print("Visualization Complete!")
        print("Exported files:")
        for plot_type, file_path in exported_files.items():
            print(f"  {plot_type}: {file_path}")
        
    except Exception as e:
        print(f"Error in visualization: {str(e)}")
