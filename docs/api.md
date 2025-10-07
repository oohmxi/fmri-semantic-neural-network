# API Reference

This document provides comprehensive API documentation for all modules in the fMRI Tool Representation Study analysis pipeline.

## Table of Contents

1. [DataProcessor](api.md#dataprocessor)
2. [StatisticalAnalyzer](api.md#statisticalanalyzer)
3. [DataVisualizer](api.md#datavisualizer)
4. [ResultsSummarizer](api.md#resultssummarizer)
5. [BrainImageProcessor](api.md#brainimageprocessor)

---

## DataProcessor

The `DataProcessor` class handles extraction, cleaning, and organization of experimental data from PsychoPy logs and AFNI condition timing files.

### Class Definition

```python
class DataProcessor:
    """Main class for processing fMRI Tool Representation Study data."""
```

### Constructor

```python
def __init__(self, data_root: str):
    """
    Initialize the DataProcessor.
    
    Args:
        data_root: Path to the root data directory
        
    Raises:
        ValueError: If data_root is invalid
        FileNotFoundError: If required directories don't exist
    """
```

### Methods

#### `create_trial_dataframe(participant_id: str) -> pd.DataFrame`

Creates a comprehensive trial dataframe for the specified participant.

**Parameters:**
- `participant_id` (str): Participant identifier (e.g., 'S01')

**Returns:**
- `pd.DataFrame`: Trial data with columns:
  - `participant_id`: Participant identifier
  - `condition`: Experimental condition (passive_viewing, imagined_grasp, clench)
  - `stimulus_type`: Type of stimulus (tool, shape, SCRtool, SCRshape, localizer)
  - `run_number`: Experimental run number (1, 2, 3)
  - `trial_number`: Trial number within run
  - `onset_time`: Stimulus onset time in seconds
  - `response_time`: Response time in milliseconds
  - `accuracy`: Response accuracy (0 or 1)

**Raises:**
- `FileNotFoundError`: If participant data not found
- `ValueError`: If data validation fails

**Example:**
```python
processor = DataProcessor('data')
df = processor.create_trial_dataframe('S01')
print(f"Processed {len(df)} trials for participant S01")
```

#### `generate_data_quality_report(df: pd.DataFrame) -> dict`

Generates a comprehensive data quality report.

**Parameters:**
- `df` (pd.DataFrame): Trial dataframe

**Returns:**
- `dict`: Quality report with:
  - `data_overview`: Basic statistics
  - `timing_statistics`: Timing analysis
  - `condition_statistics`: Condition breakdown
  - `stimulus_statistics`: Stimulus type analysis
  - `participant_statistics`: Participant-level statistics
  - `quality_checks`: Validation results

**Example:**
```python
quality_report = processor.generate_data_quality_report(df)
print(f"Data quality score: {quality_report['quality_score']}")
```

#### `export_processed_data(df: pd.DataFrame) -> dict`

Exports processed data to multiple formats.

**Parameters:**
- `df` (pd.DataFrame): Trial dataframe

**Returns:**
- `dict`: Dictionary with file paths:
  - `csv`: Path to CSV export
  - `excel`: Path to Excel export
  - `quality_report`: Path to quality report

**Example:**
```python
exported_files = processor.export_processed_data(df)
print(f"Exported to: {exported_files['csv']}")
```

---

## StatisticalAnalyzer

The `StatisticalAnalyzer` class provides comprehensive statistical analysis functions for testing research questions.

### Class Definition

```python
class StatisticalAnalyzer:
    """Statistical analysis for fMRI Tool Representation Study."""
```

### Constructor

```python
def __init__(self, df: pd.DataFrame):
    """
    Initialize the StatisticalAnalyzer.
    
    Args:
        df: Trial dataframe from DataProcessor
        
    Raises:
        ValueError: If dataframe is invalid or empty
    """
```

### Methods

#### `compare_tools_vs_shapes() -> dict`

Performs statistical comparison between tools and shapes conditions.

**Returns:**
- `dict`: Analysis results with:
  - `t_test`: T-test results (statistic, p_value, significant)
  - `effect_size`: Cohen's d and eta-squared
  - `descriptive_stats`: Mean, std, n for each condition
  - `confidence_intervals`: 95% confidence intervals

**Example:**
```python
analyzer = StatisticalAnalyzer(df)
results = analyzer.compare_tools_vs_shapes()
print(f"Tools vs Shapes: t={results['t_test']['statistic']:.3f}, p={results['t_test']['p_value']:.3f}")
```

#### `analyze_action_potentiation() -> dict`

Analyzes action potentiation by comparing imagined grasp vs passive viewing.

**Returns:**
- `dict`: Analysis results with:
  - `imagined_grasp`: Statistics for imagined grasp condition
  - `passive_viewing`: Statistics for passive viewing condition
  - `comparison`: Statistical comparison results
  - `effect_size`: Effect size measures

**Example:**
```python
results = analyzer.analyze_action_potentiation()
print(f"Action potentiation effect: {results['comparison']['effect_size']}")
```

#### `analyze_motor_network() -> dict`

Analyzes motor network activation patterns.

**Returns:**
- `dict`: Analysis results with:
  - `clench_condition`: Motor localizer statistics
  - `activation_patterns`: Brain activation patterns
  - `statistical_results`: Statistical test results
  - `mni_coordinates`: MNI coordinates of significant activations

**Example:**
```python
results = analyzer.analyze_motor_network()
print(f"Motor activation at MNI: {results['mni_coordinates']}")
```

#### `generate_comprehensive_report() -> dict`

Generates comprehensive statistical report addressing all research questions.

**Returns:**
- `dict`: Complete analysis report with:
  - `research_questions`: Results for each research question
  - `summary_statistics`: Overall statistics
  - `effect_sizes`: Effect size calculations
  - `statistical_tests`: All statistical tests performed
  - `interpretation`: Results interpretation

**Example:**
```python
report = analyzer.generate_comprehensive_report()
print(f"Research Question 1: {report['research_questions']['rq1']['summary']}")
```

---

## DataVisualizer

The `DataVisualizer` class creates publication-ready plots and visualizations.

### Class Definition

```python
class DataVisualizer:
    """Visualization for fMRI Tool Representation Study."""
```

### Constructor

```python
def __init__(self, df: pd.DataFrame):
    """
    Initialize the DataVisualizer.
    
    Args:
        df: Trial dataframe from DataProcessor
        
    Raises:
        ValueError: If dataframe is invalid or empty
    """
```

### Methods

#### `create_behavioral_results_plot(output_path: Path) -> Path`

Creates behavioral results visualization.

**Parameters:**
- `output_path` (Path): Output file path for the plot

**Returns:**
- `Path`: Path to saved plot file

**Example:**
```python
visualizer = DataVisualizer(df)
plot_path = visualizer.create_behavioral_results_plot(Path('plots/behavioral_results.png'))
```

#### `create_timing_analysis_plot(output_path: Path) -> Path`

Creates timing analysis visualization.

**Parameters:**
- `output_path` (Path): Output file path for the plot

**Returns:**
- `Path`: Path to saved plot file

**Example:**
```python
plot_path = visualizer.create_timing_analysis_plot(Path('plots/timing_analysis.png'))
```

#### `export_all_plots(output_dir: Path) -> dict`

Exports all visualization plots.

**Parameters:**
- `output_dir` (Path): Directory to save plots

**Returns:**
- `dict`: Dictionary with plot types and file paths

**Example:**
```python
plots = visualizer.export_all_plots(Path('plots/'))
print(f"Created {len(plots)} plots")
```

---

## ResultsSummarizer

The `ResultsSummarizer` class compiles and exports comprehensive results.

### Class Definition

```python
class ResultsSummarizer:
    """Results compilation and export for fMRI Tool Representation Study."""
```

### Constructor

```python
def __init__(self, df: pd.DataFrame, analysis_results: dict):
    """
    Initialize the ResultsSummarizer.
    
    Args:
        df: Trial dataframe from DataProcessor
        analysis_results: Results from StatisticalAnalyzer
        
    Raises:
        ValueError: If inputs are invalid
    """
```

### Methods

#### `generate_summary_stats() -> dict`

Generates comprehensive summary statistics.

**Returns:**
- `dict`: Summary statistics with:
  - `data_overview`: Basic data statistics
  - `timing_statistics`: Timing analysis
  - `condition_statistics`: Condition breakdown
  - `stimulus_statistics`: Stimulus analysis
  - `participant_statistics`: Participant statistics

**Example:**
```python
summarizer = ResultsSummarizer(df, analysis_results)
stats = summarizer.generate_summary_stats()
print(f"Total trials: {stats['data_overview']['total_trials']}")
```

#### `create_results_table() -> pd.DataFrame`

Creates comprehensive results table.

**Returns:**
- `pd.DataFrame`: Results table with statistical results

**Example:**
```python
table = summarizer.create_results_table()
print(table.head())
```

#### `export_for_publication(output_dir: Path) -> dict`

Exports publication-ready results.

**Parameters:**
- `output_dir` (Path): Directory for publication files

**Returns:**
- `dict`: Dictionary with exported file paths

**Example:**
```python
pub_files = summarizer.export_for_publication(Path('publication/'))
print(f"Exported {len(pub_files)} publication files")
```

#### `write_results_report(output_path: Path) -> Path`

Writes comprehensive results report.

**Parameters:**
- `output_path` (Path): Output file path

**Returns:**
- `Path`: Path to written report

**Example:**
```python
report_path = summarizer.write_results_report(Path('comprehensive_report.txt'))
```

---

## BrainImageProcessor

The `BrainImageProcessor` class handles brain image processing and integration.

### Class Definition

```python
class BrainImageProcessor:
    """Brain image processing for fMRI Tool Representation Study."""
```

### Constructor

```python
def __init__(self, data_root: str):
    """
    Initialize the BrainImageProcessor.
    
    Args:
        data_root: Path to the root data directory
        
    Raises:
        ValueError: If data_root is invalid
        FileNotFoundError: If brain images directory doesn't exist
    """
```

### Methods

#### `process_all_brain_data() -> dict`

Processes all brain activation images.

**Returns:**
- `dict`: Processing results with:
  - `total_images`: Number of images processed
  - `image_data`: Individual image data
  - `summary`: Processing summary
  - `statistics`: Image statistics

**Example:**
```python
processor = BrainImageProcessor('data')
results = processor.process_all_brain_data()
print(f"Processed {results['total_images']} brain images")
```

#### `_create_brain_activation_summary() -> dict`

Creates summary of brain activation patterns.

**Returns:**
- `dict`: Activation summary with MNI coordinates and statistical thresholds

**Example:**
```python
summary = processor._create_brain_activation_summary()
print(f"Motor activation: {summary['motor_localizer']['mni_coordinates']}")
```

---

## Utility Functions

### Data Validation

```python
def validate_trial_data(df: pd.DataFrame) -> bool:
    """
    Validate trial dataframe structure and content.
    
    Args:
        df: Trial dataframe to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
```

### Statistical Utilities

```python
def calculate_effect_size(group1: np.ndarray, group2: np.ndarray) -> dict:
    """
    Calculate effect size measures.
    
    Args:
        group1: First group data
        group2: Second group data
        
    Returns:
        dict: Effect size measures (Cohen's d, eta-squared)
    """
```

### File I/O Utilities

```python
def export_dataframe(df: pd.DataFrame, file_path: Path, format: str = 'csv') -> Path:
    """
    Export dataframe to specified format.
    
    Args:
        df: Dataframe to export
        file_path: Output file path
        format: Export format ('csv', 'excel', 'json')
        
    Returns:
        Path: Path to exported file
    """
```

---

## Error Handling

All classes and functions include comprehensive error handling:

### Common Exceptions

- `ValueError`: Invalid input parameters
- `FileNotFoundError`: Missing files or directories
- `DataError`: Invalid or corrupted data
- `AnalysisError`: Statistical analysis failures

### Error Recovery

- Automatic data validation and correction
- Graceful degradation for missing data
- Comprehensive error logging
- User-friendly error messages

---

## Performance Considerations

### Memory Usage
- Efficient data structures and algorithms
- Lazy loading for large datasets
- Memory cleanup after processing

### Processing Speed
- Vectorized operations using NumPy/Pandas
- Parallel processing where applicable
- Caching for repeated operations

### Scalability
- Modular design for easy extension
- Configurable parameters for different scales
- Support for batch processing

---

*This API reference provides comprehensive documentation for all modules in the fMRI Tool Representation Study. For usage examples and tutorials, please refer to the User Guide.*
