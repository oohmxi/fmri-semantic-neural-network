"""
fMRI Tool Representation Study - Test Configuration

This module provides test configuration and utilities for the fMRI Tool Representation Study.

Author: fMRI Tool Representation Study Team
Date: 2024
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import tempfile
import shutil


@pytest.fixture(scope="session")
def test_data_dir():
    """Create a temporary directory for test data."""
    temp_dir = tempfile.mkdtemp()
    yield Path(temp_dir)
    shutil.rmtree(temp_dir)


@pytest.fixture
def sample_trial_data():
    """Create sample trial data for testing."""
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


@pytest.fixture
def sample_analysis_results():
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


@pytest.fixture
def mock_brain_images():
    """Create mock brain image data for testing."""
    return {
        'clench': {
            'path': 'mock_clench_image.png',
            'mni_coordinates': [-40, 22, 62],
            'statistical_threshold': 3.7037,
            'p_value': 2.3e-4
        },
        'imagined_grasp': {
            'path': 'mock_ig_image.png',
            'mni_coordinates': [-58, 22, 22],
            'statistical_threshold': 3.5391,
            'p_value': 0.0016
        },
        'passive_viewing': {
            'path': 'mock_pv_image.png',
            'mni_coordinates': [22, 100, -2],
            'statistical_threshold': 3.5802,
            'p_value': 3.7e-4
        }
    }


# Test markers for different test categories
pytest_plugins = []


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )
    config.addinivalue_line(
        "markers", "brain_images: mark test as requiring brain image data"
    )


# Test utilities
class TestDataGenerator:
    """Utility class for generating test data."""
    
    @staticmethod
    def create_trial_data(n_trials=100, participant_id='S01'):
        """Create trial data for testing."""
        np.random.seed(42)
        
        data = {
            'participant_id': [participant_id] * n_trials,
            'condition': np.random.choice(['passive_viewing', 'imagined_grasp'], n_trials),
            'stimulus_type': np.random.choice(['tool', 'shape', 'SCRtool', 'SCRshape'], n_trials),
            'run_number': np.random.choice([1, 2, 3], n_trials),
            'response_time': np.random.normal(300, 50, n_trials),
            'accuracy': np.random.choice([0, 1], n_trials),
            'onset_time': np.random.uniform(100, 500, n_trials)
        }
        
        return pd.DataFrame(data)
    
    @staticmethod
    def create_analysis_results():
        """Create analysis results for testing."""
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


# Test assertions
def assert_dataframe_structure(df, expected_columns):
    """Assert DataFrame has expected structure."""
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    for col in expected_columns:
        assert col in df.columns


def assert_statistical_results(results):
    """Assert statistical results have expected structure."""
    assert isinstance(results, dict)
    assert 't_test' in results
    assert 'effect_size' in results
    assert 'descriptive_stats' in results
    
    t_test = results['t_test']
    assert 'statistic' in t_test
    assert 'p_value' in t_test
    assert 'significant' in t_test


def assert_brain_image_data(image_data):
    """Assert brain image data has expected structure."""
    assert isinstance(image_data, dict)
    assert 'path' in image_data
    assert 'mni_coordinates' in image_data
    assert 'statistical_threshold' in image_data
    assert 'p_value' in image_data
    
    coords = image_data['mni_coordinates']
    assert len(coords) == 3
    assert all(isinstance(x, (int, float)) for x in coords)
