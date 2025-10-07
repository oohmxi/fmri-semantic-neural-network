"""
fMRI Tool Representation Study - Test Suite Runner

This module provides utilities for running the complete test suite
and generating test reports for the fMRI Tool Representation Study.

Author: fMRI Tool Representation Study Team
Date: 2024
"""

import pytest
import sys
from pathlib import Path
import subprocess
import os


def run_unit_tests():
    """Run unit tests only."""
    print("Running unit tests...")
    result = pytest.main([
        "tests/test_analysis.py::TestDataProcessor",
        "tests/test_analysis.py::TestStatisticalAnalyzer", 
        "tests/test_analysis.py::TestDataVisualizer",
        "tests/test_analysis.py::TestResultsSummarizer",
        "tests/test_analysis.py::TestBrainImageProcessor",
        "-v",
        "--tb=short"
    ])
    return result


def run_integration_tests():
    """Run integration tests only."""
    print("Running integration tests...")
    result = pytest.main([
        "tests/test_analysis.py::TestIntegrationTests",
        "-v",
        "--tb=short"
    ])
    return result


def run_all_tests():
    """Run all tests with coverage."""
    print("Running complete test suite with coverage...")
    result = pytest.main([
        "tests/",
        "-v",
        "--cov=analysis",
        "--cov-report=html",
        "--cov-report=term-missing",
        "--tb=short"
    ])
    return result


def run_tests_with_markers():
    """Run tests with specific markers."""
    print("Running tests with markers...")
    result = pytest.main([
        "tests/",
        "-m", "unit",
        "-v",
        "--tb=short"
    ])
    return result


def generate_test_report():
    """Generate comprehensive test report."""
    print("Generating test report...")
    
    # Run tests with HTML report
    result = pytest.main([
        "tests/",
        "--html=test_report.html",
        "--self-contained-html",
        "--cov=analysis",
        "--cov-report=html:coverage_report",
        "-v"
    ])
    
    print(f"Test report generated: test_report.html")
    print(f"Coverage report generated: coverage_report/index.html")
    
    return result


if __name__ == "__main__":
    """Run tests based on command line arguments."""
    if len(sys.argv) > 1:
        test_type = sys.argv[1]
        
        if test_type == "unit":
            exit_code = run_unit_tests()
        elif test_type == "integration":
            exit_code = run_integration_tests()
        elif test_type == "all":
            exit_code = run_all_tests()
        elif test_type == "report":
            exit_code = generate_test_report()
        elif test_type == "markers":
            exit_code = run_tests_with_markers()
        else:
            print(f"Unknown test type: {test_type}")
            print("Available options: unit, integration, all, report, markers")
            exit_code = 1
    else:
        # Default: run all tests
        exit_code = run_all_tests()
    
    sys.exit(exit_code)
