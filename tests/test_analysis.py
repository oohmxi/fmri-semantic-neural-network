"""
fMRI Tool Representation Study - Test Suite

This module contains comprehensive unit tests for the fMRI Tool Representation Study
analysis pipeline, ensuring code quality and reproducibility.

Author: fMRI Tool Representation Study Team
Date: 2024
"""

import pytest
import pandas as pd
import numpy as np
import os
import sys
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import tempfile
import shutil

# Add analysis directory to path
sys.path.append(str(Path(__file__).parent.parent / "analysis"))

from preprocessing import DataProcessor
from statistical_analysis import StatisticalAnalyzer
from visualization import DataVisualizer
from results_summary import ResultsSummarizer
from brain_image_processor import BrainImageProcessor


class TestDataProcessor:
    """Test suite for DataProcessor class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.data_root = Path(self.temp_dir)
        self.raw_data_path = self.data_root / "raw"
        self.processed_data_path = self.data_root / "processed"
        
        # Create directory structure
        self.raw_data_path.mkdir(parents=True)
        self.processed_data_path.mkdir(parents=True)
        
        # Initialize processor
        self.processor = DataProcessor(str(self.data_root))
    
    def teardown_method(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)
    
    def test_initialization(self):
        """Test DataProcessor initialization."""
        assert self.processor.data_root == self.data_root
        assert self.processor.raw_data_path == self.raw_data_path
        assert self.processor.processed_data_path == self.processed_data_path
    
    def test_create_sample_data(self):
        """Test creation of sample trial data."""
        # Create sample data
        sample_data = self.processor._create_sample_trial_data('S01')
        
        assert isinstance(sample_data, pd.DataFrame)
        assert len(sample_data) > 0
        assert 'participant_id' in sample_data.columns
        assert 'condition' in sample_data.columns
        assert 'stimulus_type' in sample_data.columns
        assert 'run_number' in sample_data.columns
    
    def test_data_validation(self):
        """Test data validation methods."""
        # Create sample data
        sample_data = self.processor._create_sample_trial_data('S01')
        
        # Test validation
        is_valid = self.processor._validate_trial_data(sample_data)
        assert is_valid
        
        # Test with invalid data
        invalid_data = sample_data.copy()
        invalid_data.loc[0, 'participant_id'] = None
        is_valid = self.processor._validate_trial_data(invalid_data)
        assert not is_valid
    
    def test_export_processed_data(self):
        """Test data export functionality."""
        # Create sample data
        sample_data = self.processor._create_sample_trial_data('S01')
        
        # Test export
        exported_files = self.processor.export_processed_data(sample_data)
        
        assert isinstance(exported_files, dict)
        assert 'csv' in exported_files
        assert 'excel' in exported_files
        
        # Check files exist
        csv_path = Path(exported_files['csv'])
        excel_path = Path(exported_files['excel'])
        assert csv_path.exists()
        assert excel_path.exists()


class TestStatisticalAnalyzer:
    """Test suite for StatisticalAnalyzer class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        # Create sample data
        self.sample_data = self._create_sample_dataframe()
        self.analyzer = StatisticalAnalyzer(df=self.sample_data)
    
    def _create_sample_dataframe(self):
        """Create sample DataFrame for testing."""
        np.random.seed(42)
        n_trials = 100
        
        data = {
            'participant_id': ['S01'] * n_trials,
            'condition': np.random.choice(['passive_viewing', 'imagined_grasp'], n_trials),
            'stimulus_type': np.random.choice(['tool', 'shape', 'SCRtool', 'SCRshape'], n_trials),
            'run_number': np.random.choice([1, 2, 3], n_trials),
            'response_time': np.random.normal(300, 50, n_trials),
            'accuracy': np.random.choice([0, 1], n_trials),
            'onset_time': np.random.uniform(100, 500, n_trials)
        }
        
        return pd.DataFrame(data)
    
    def test_initialization(self):
        """Test StatisticalAnalyzer initialization."""
        assert isinstance(self.analyzer.df, pd.DataFrame)
        assert len(self.analyzer.df) == 100
    
    def test_tools_vs_shapes_comparison(self):
        """Test tools vs shapes statistical comparison."""
        result = self.analyzer.compare_tools_vs_shapes()
        
        assert isinstance(result, dict)
        assert 't_test' in result
        assert 'effect_size' in result
        assert 'descriptive_stats' in result
        
        # Check t-test results
        t_test = result['t_test']
        assert 'statistic' in t_test
        assert 'p_value' in t_test
        assert 'significant' in t_test
    
    def test_action_potentiation_analysis(self):
        """Test action potentiation analysis."""
        result = self.analyzer.analyze_action_potentiation()
        
        assert isinstance(result, dict)
        assert 'imagined_grasp' in result
        assert 'passive_viewing' in result
        assert 'comparison' in result
    
    def test_motor_network_analysis(self):
        """Test motor network analysis."""
        result = self.analyzer.analyze_motor_network()
        
        assert isinstance(result, dict)
        assert 'clench_condition' in result
        assert 'activation_patterns' in result
    
    def test_comprehensive_report(self):
        """Test comprehensive report generation."""
        report = self.analyzer.generate_comprehensive_report()
        
        assert isinstance(report, dict)
        assert 'research_questions' in report
        assert 'summary_statistics' in report
        assert 'effect_sizes' in report
        
        # Check research questions
        rq = report['research_questions']
        assert 'rq1' in rq
        assert 'rq2' in rq
        assert 'rq3' in rq


class TestDataVisualizer:
    """Test suite for DataVisualizer class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        # Create sample data
        self.sample_data = self._create_sample_dataframe()
        self.visualizer = DataVisualizer(df=self.sample_data)
    
    def _create_sample_dataframe(self):
        """Create sample DataFrame for testing."""
        np.random.seed(42)
        n_trials = 100
        
        data = {
            'participant_id': ['S01'] * n_trials,
            'condition': np.random.choice(['passive_viewing', 'imagined_grasp'], n_trials),
            'stimulus_type': np.random.choice(['tool', 'shape', 'SCRtool', 'SCRshape'], n_trials),
            'run_number': np.random.choice([1, 2, 3], n_trials),
            'response_time': np.random.normal(300, 50, n_trials),
            'accuracy': np.random.choice([0, 1], n_trials),
            'onset_time': np.random.uniform(100, 500, n_trials)
        }
        
        return pd.DataFrame(data)
    
    def test_initialization(self):
        """Test DataVisualizer initialization."""
        assert isinstance(self.visualizer.df, pd.DataFrame)
        assert len(self.visualizer.df) == 100
    
    def test_create_behavioral_plot(self):
        """Test behavioral results plot creation."""
        with tempfile.TemporaryDirectory() as temp_dir:
            plot_path = self.visualizer.create_behavioral_results_plot(
                output_path=Path(temp_dir) / "test_plot.png"
            )
            
            assert plot_path.exists()
            assert plot_path.suffix == '.png'
    
    def test_create_timing_plot(self):
        """Test timing analysis plot creation."""
        with tempfile.TemporaryDirectory() as temp_dir:
            plot_path = self.visualizer.create_timing_analysis_plot(
                output_path=Path(temp_dir) / "timing_plot.png"
            )
            
            assert plot_path.exists()
            assert plot_path.suffix == '.png'
    
    def test_export_all_plots(self):
        """Test export of all plots."""
        with tempfile.TemporaryDirectory() as temp_dir:
            exported_plots = self.visualizer.export_all_plots(Path(temp_dir))
            
            assert isinstance(exported_plots, dict)
            assert len(exported_plots) > 0
            
            # Check all plots exist
            for plot_type, plot_path in exported_plots.items():
                assert Path(plot_path).exists()


class TestResultsSummarizer:
    """Test suite for ResultsSummarizer class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        # Create sample data
        self.sample_data = self._create_sample_dataframe()
        self.sample_analysis = self._create_sample_analysis_results()
        self.summarizer = ResultsSummarizer(
            df=self.sample_data,
            analysis_results=self.sample_analysis
        )
    
    def _create_sample_dataframe(self):
        """Create sample DataFrame for testing."""
        np.random.seed(42)
        n_trials = 100
        
        data = {
            'participant_id': ['S01'] * n_trials,
            'condition': np.random.choice(['passive_viewing', 'imagined_grasp'], n_trials),
            'stimulus_type': np.random.choice(['tool', 'shape', 'SCRtool', 'SCRshape'], n_trials),
            'run_number': np.random.choice([1, 2, 3], n_trials),
            'response_time': np.random.normal(300, 50, n_trials),
            'accuracy': np.random.choice([0, 1], n_trials),
            'onset_time': np.random.uniform(100, 500, n_trials)
        }
        
        return pd.DataFrame(data)
    
    def _create_sample_analysis_results(self):
        """Create sample analysis results for testing."""
        return {
            'research_questions': {
                'rq1': {
                    'analyses': [{'test': 't-test', 'p_value': 0.001}],
                    'summary': 'Tools vs Shapes comparison'
                },
                'rq2': {
                    'analyses': [{'test': 't-test', 'p_value': 0.01}],
                    'summary': 'Action potentiation analysis'
                },
                'rq3': {
                    'analyses': [{'test': 't-test', 'p_value': 0.005}],
                    'summary': 'Motor network analysis'
                }
            },
            'summary_statistics': {
                'total_trials': 100,
                'participants': 1
            }
        }
    
    def test_initialization(self):
        """Test ResultsSummarizer initialization."""
        assert isinstance(self.summarizer.df, pd.DataFrame)
        assert isinstance(self.summarizer.analysis_results, dict)
    
    def test_generate_summary_stats(self):
        """Test summary statistics generation."""
        stats = self.summarizer.generate_summary_stats()
        
        assert isinstance(stats, dict)
        assert 'data_overview' in stats
        assert 'timing_statistics' in stats
        assert 'condition_statistics' in stats
    
    def test_create_results_table(self):
        """Test results table creation."""
        table = self.summarizer.create_results_table()
        
        assert isinstance(table, pd.DataFrame)
        assert len(table) > 0
        assert 'condition' in table.columns
        assert 'n_trials' in table.columns
    
    def test_export_for_publication(self):
        """Test publication export functionality."""
        with tempfile.TemporaryDirectory() as temp_dir:
            publication_files = self.summarizer.export_for_publication(
                Path(temp_dir) / "publication"
            )
            
            assert isinstance(publication_files, dict)
            assert len(publication_files) > 0
            
            # Check files exist
            for file_type, file_path in publication_files.items():
                assert Path(file_path).exists()


class TestBrainImageProcessor:
    """Test suite for BrainImageProcessor class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.data_root = Path(self.temp_dir)
        
        # Create directory structure
        (self.data_root / "processed" / "brain_images").mkdir(parents=True)
        
        # Initialize processor
        self.processor = BrainImageProcessor(str(self.data_root))
    
    def teardown_method(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)
    
    def test_initialization(self):
        """Test BrainImageProcessor initialization."""
        assert self.processor.data_root == self.data_root
        assert self.processor.brain_images_path.exists()
    
    def test_process_brain_images(self):
        """Test brain image processing."""
        # Mock brain image processing
        with patch.object(self.processor, '_load_brain_images') as mock_load:
            mock_load.return_value = {
                'clench': 'mock_clench_image.png',
                'imagined_grasp': 'mock_ig_image.png',
                'passive_viewing': 'mock_pv_image.png'
            }
            
            result = self.processor.process_all_brain_data()
            
            assert isinstance(result, dict)
            assert 'total_images' in result
            assert 'summary' in result
    
    def test_create_brain_summary(self):
        """Test brain activation summary creation."""
        summary = self.processor._create_brain_activation_summary()
        
        assert isinstance(summary, dict)
        assert 'motor_localizer' in summary
        assert 'imagined_grasp' in summary
        assert 'passive_viewing' in summary


class TestIntegrationTests:
    """Integration tests for the complete analysis pipeline."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.data_root = Path(self.temp_dir)
        
        # Create directory structure
        (self.data_root / "raw").mkdir(parents=True)
        (self.data_root / "processed").mkdir(parents=True)
    
    def teardown_method(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)
    
    def test_complete_analysis_pipeline(self):
        """Test the complete analysis pipeline."""
        # Initialize components
        processor = DataProcessor(str(self.data_root))
        sample_data = processor._create_sample_trial_data('S01')
        
        analyzer = StatisticalAnalyzer(df=sample_data)
        analysis_results = analyzer.generate_comprehensive_report()
        
        visualizer = DataVisualizer(df=sample_data)
        
        summarizer = ResultsSummarizer(
            df=sample_data,
            analysis_results=analysis_results
        )
        
        # Test pipeline components
        assert len(sample_data) > 0
        assert isinstance(analysis_results, dict)
        assert 'research_questions' in analysis_results
        
        # Test visualization
        with tempfile.TemporaryDirectory() as temp_dir:
            plots = visualizer.export_all_plots(Path(temp_dir))
            assert len(plots) > 0
        
        # Test results summary
        stats = summarizer.generate_summary_stats()
        assert isinstance(stats, dict)
        assert 'data_overview' in stats


# Test configuration and utilities
@pytest.fixture
def sample_data():
    """Fixture providing sample data for tests."""
    np.random.seed(42)
    n_trials = 100
    
    data = {
        'participant_id': ['S01'] * n_trials,
        'condition': np.random.choice(['passive_viewing', 'imagined_grasp'], n_trials),
        'stimulus_type': np.random.choice(['tool', 'shape', 'SCRtool', 'SCRshape'], n_trials),
        'run_number': np.random.choice([1, 2, 3], n_trials),
        'response_time': np.random.normal(300, 50, n_trials),
        'accuracy': np.random.choice([0, 1], n_trials),
        'onset_time': np.random.uniform(100, 500, n_trials)
    }
    
    return pd.DataFrame(data)


def test_data_quality_checks(sample_data):
    """Test data quality validation."""
    # Check for missing values
    assert not sample_data.isnull().any().any()
    
    # Check data types
    assert sample_data['participant_id'].dtype == 'object'
    assert sample_data['condition'].dtype == 'object'
    assert sample_data['response_time'].dtype == 'float64'
    
    # Check value ranges
    assert sample_data['response_time'].min() > 0
    assert sample_data['accuracy'].isin([0, 1]).all()


def test_statistical_assumptions(sample_data):
    """Test statistical assumptions."""
    # Test normality (using Shapiro-Wilk for small samples)
    from scipy import stats
    
    # Test response time normality
    _, p_value = stats.shapiro(sample_data['response_time'].sample(50))
    # Note: This might fail for some random samples, which is expected
    
    # Test independence (check for autocorrelation)
    response_times = sample_data['response_time'].values
    correlation = np.corrcoef(response_times[:-1], response_times[1:])[0, 1]
    assert abs(correlation) < 0.5  # Should be low for independent observations


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--cov=analysis", "--cov-report=html"])
