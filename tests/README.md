# fMRI Tool Representation Study - Testing

This directory contains comprehensive test suites for the fMRI Tool Representation Study analysis pipeline.

## Test Structure

```
tests/
├── conftest.py              # Test configuration and fixtures
├── test_analysis.py         # Main test suite for analysis modules
├── run_tests.py            # Test runner utilities
└── README.md               # This file
```

## Test Categories

### Unit Tests
- **DataProcessor**: Data loading, validation, and export
- **StatisticalAnalyzer**: Statistical analysis and hypothesis testing
- **DataVisualizer**: Plot creation and visualization
- **ResultsSummarizer**: Results compilation and reporting
- **BrainImageProcessor**: Brain image processing and integration

### Integration Tests
- **Complete Pipeline**: End-to-end analysis workflow
- **Data Flow**: Integration between all components
- **Export Pipeline**: Complete results generation

### Test Markers
- `@pytest.mark.unit`: Unit tests
- `@pytest.mark.integration`: Integration tests
- `@pytest.mark.slow`: Slow-running tests
- `@pytest.mark.brain_images`: Tests requiring brain image data

## Running Tests

### Prerequisites
```bash
# Install test dependencies
pip install pytest pytest-cov pytest-html

# Install project dependencies
pip install -r requirements.txt
```

### Basic Test Execution
```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_analysis.py

# Run specific test class
pytest tests/test_analysis.py::TestDataProcessor
```

### Test Categories
```bash
# Run only unit tests
pytest tests/ -m unit

# Run only integration tests
pytest tests/ -m integration

# Run tests excluding slow ones
pytest tests/ -m "not slow"
```

### Coverage Analysis
```bash
# Run with coverage
pytest tests/ --cov=analysis --cov-report=html

# Coverage with terminal output
pytest tests/ --cov=analysis --cov-report=term-missing

# Coverage threshold
pytest tests/ --cov=analysis --cov-fail-under=80
```

### Test Reports
```bash
# Generate HTML test report
pytest tests/ --html=test_report.html --self-contained-html

# Generate JUnit XML report
pytest tests/ --junitxml=test_results.xml

# Generate comprehensive report
python tests/run_tests.py report
```

## Test Utilities

### Test Runner Script
```bash
# Run different test suites
python tests/run_tests.py unit        # Unit tests only
python tests/run_tests.py integration # Integration tests only
python tests/run_tests.py all         # All tests with coverage
python tests/run_tests.py report     # Generate comprehensive report
```

### Test Fixtures
- `sample_trial_data`: Sample experimental data
- `sample_analysis_results`: Sample analysis results
- `mock_brain_images`: Mock brain image data
- `test_data_dir`: Temporary directory for test data

## Test Data

### Sample Data Generation
Tests use synthetic data that mimics the structure of real experimental data:

- **Participant Data**: S01 representative subject
- **Conditions**: Passive viewing, imagined grasp, clench
- **Stimulus Types**: Tools, shapes, scrambled versions
- **Timing Data**: Realistic response times and onset times
- **Statistical Properties**: Appropriate distributions and correlations

### Mock Data
- **Brain Images**: Mock brain activation maps
- **Statistical Results**: Realistic p-values and effect sizes
- **Analysis Outputs**: Complete analysis result structures

## Test Configuration

### pytest.ini
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
markers =
    unit: Unit tests
    integration: Integration tests
    slow: Slow running tests
    brain_images: Tests requiring brain image data
```

### Coverage Configuration
```ini
[coverage:run]
source = analysis
omit = 
    */tests/*
    */venv/*
    */__pycache__/*

[coverage:report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
```

## Continuous Integration

### GitHub Actions
Tests are automatically run on:
- **Pull Requests**: Full test suite with coverage
- **Main Branch**: Complete testing and reporting
- **Releases**: Comprehensive validation

### Local CI Simulation
```bash
# Simulate CI environment
pytest tests/ --cov=analysis --cov-report=xml --junitxml=test_results.xml
```

## Test Quality Standards

### Coverage Requirements
- **Minimum Coverage**: 80% for all modules
- **Critical Functions**: 100% coverage for core analysis functions
- **Edge Cases**: Comprehensive testing of error conditions

### Performance Standards
- **Unit Tests**: < 1 second per test
- **Integration Tests**: < 10 seconds per test
- **Complete Suite**: < 5 minutes total

### Test Documentation
- **Test Names**: Descriptive and clear
- **Test Docstrings**: Explain test purpose and expected behavior
- **Assertions**: Specific and meaningful
- **Error Messages**: Helpful debugging information

## Debugging Tests

### Common Issues
1. **Import Errors**: Ensure analysis modules are in Python path
2. **Data Path Issues**: Check test data directory setup
3. **Mock Failures**: Verify mock configurations
4. **Timing Issues**: Use appropriate timeouts for slow operations

### Debug Commands
```bash
# Run with debugging
pytest tests/ -v -s --pdb

# Run specific failing test
pytest tests/test_analysis.py::TestDataProcessor::test_initialization -v -s

# Show test collection
pytest tests/ --collect-only
```

## Contributing Tests

### Adding New Tests
1. **Follow Naming Conventions**: `test_*.py` files, `Test*` classes, `test_*` functions
2. **Use Appropriate Markers**: Mark tests with relevant categories
3. **Include Fixtures**: Use existing fixtures or create new ones
4. **Document Tests**: Add docstrings explaining test purpose
5. **Test Edge Cases**: Include boundary conditions and error cases

### Test Best Practices
- **Isolation**: Tests should not depend on each other
- **Deterministic**: Use fixed random seeds for reproducible results
- **Fast**: Keep tests as fast as possible
- **Clear**: Use descriptive names and clear assertions
- **Maintainable**: Keep tests simple and focused

---

*This test suite ensures the reliability and reproducibility of the fMRI Tool Representation Study analysis pipeline.*
