# Troubleshooting Guide

This guide provides solutions to common problems and issues encountered when using the fMRI Tool Representation Study analysis pipeline.

## Table of Contents

1. [Installation Issues](troubleshooting.md#installation-issues)
2. [Data Processing Problems](troubleshooting.md#data-processing-problems)
3. [Analysis Errors](troubleshooting.md#analysis-errors)
4. [Visualization Issues](troubleshooting.md#visualization-issues)
5. [Performance Problems](troubleshooting.md#performance-problems)
6. [Web Experiment Issues](troubleshooting.md#web-experiment-issues)
7. [Getting Help](troubleshooting.md#getting-help)

---

## Installation Issues

### Python Version Compatibility

**Problem:** Error messages about Python version incompatibility.

**Symptoms:**
```
Python 3.6 is not supported. Please use Python 3.7 or higher.
```

**Solution:**
1. Check your Python version:
   ```bash
   python --version
   ```
2. Install Python 3.7+ if needed
3. Use a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

### Dependency Installation Failures

**Problem:** Package installation fails with dependency conflicts.

**Symptoms:**
```
ERROR: Could not find a version that satisfies the requirement
```

**Solution:**
1. Update pip:
   ```bash
   pip install --upgrade pip
   ```
2. Install dependencies individually:
   ```bash
   pip install numpy pandas matplotlib scipy
   pip install psychopy
   ```
3. Use conda for complex dependencies:
   ```bash
   conda install numpy pandas matplotlib scipy
   pip install psychopy
   ```

### PsychoPy Installation Issues

**Problem:** PsychoPy fails to install or import.

**Symptoms:**
```
ImportError: No module named 'psychopy'
```

**Solution:**
1. Install PsychoPy with conda (recommended):
   ```bash
   conda install -c conda-forge psychopy
   ```
2. Or install from source:
   ```bash
   pip install psychopy --no-deps
   pip install numpy scipy matplotlib
   ```

---

## Data Processing Problems

### Missing Data Files

**Problem:** DataProcessor cannot find participant data files.

**Symptoms:**
```
FileNotFoundError: No S01 data found in data/raw/
```

**Solution:**
1. Check data directory structure:
   ```bash
   ls -la data/raw/S01/
   ```
2. Ensure files are in correct location:
   ```
   data/raw/S01/experimental_runs/
   data/raw/S01/condition_files/
   data/raw/S01/afni_files/
   ```
3. Check file permissions and accessibility

### Data Validation Failures

**Problem:** Data validation fails during processing.

**Symptoms:**
```
ValueError: Data validation failed: Missing required columns
```

**Solution:**
1. Check data format and structure:
   ```python
   import pandas as pd
   df = pd.read_csv('data/raw/S01/experimental_runs/S01_PV_tool.csv')
   print(df.columns)
   print(df.head())
   ```
2. Verify required columns exist:
   - `participant_id`
   - `condition`
   - `stimulus_type`
   - `run_number`
   - `onset_time`

### Timing Synchronization Issues

**Problem:** Timing data doesn't match between PsychoPy and AFNI files.

**Symptoms:**
```
Warning: Timing mismatch detected between PsychoPy and AFNI files
```

**Solution:**
1. Check timing file formats:
   ```bash
   head data/raw/S01/condition_files/S01_PV_tool.txt
   ```
2. Verify timing precision (should be in seconds)
3. Check for missing or duplicate trials

---

## Analysis Errors

### Statistical Analysis Failures

**Problem:** Statistical tests fail or produce unexpected results.

**Symptoms:**
```
ValueError: Cannot perform statistical test: insufficient data
```

**Solution:**
1. Check data completeness:
   ```python
   print(df.groupby('condition').size())
   print(df.groupby('stimulus_type').size())
   ```
2. Ensure sufficient sample sizes (minimum 10 trials per condition)
3. Check for missing values:
   ```python
   print(df.isnull().sum())
   ```

### Memory Issues During Analysis

**Problem:** Analysis fails due to memory limitations.

**Symptoms:**
```
MemoryError: Unable to allocate array
```

**Solution:**
1. Process data in smaller chunks:
   ```python
   # Process by run
   for run in df['run_number'].unique():
       run_data = df[df['run_number'] == run]
       # Process run_data
   ```
2. Increase system memory or use a machine with more RAM
3. Optimize data types:
   ```python
   df['response_time'] = df['response_time'].astype('float32')
   ```

### Brain Image Processing Errors

**Problem:** Brain image processing fails or produces errors.

**Symptoms:**
```
FileNotFoundError: Brain images not found
```

**Solution:**
1. Check brain images directory:
   ```bash
   ls -la data/processed/brain_images/
   ```
2. Ensure image files exist and are accessible
3. Check image file formats (PNG, JPG supported)

---

## Visualization Issues

### Plot Generation Failures

**Problem:** Visualization plots fail to generate or display incorrectly.

**Symptoms:**
```
RuntimeError: Failed to create plot
```

**Solution:**
1. Check matplotlib backend:
   ```python
   import matplotlib
   print(matplotlib.get_backend())
   ```
2. Set appropriate backend:
   ```python
   import matplotlib
   matplotlib.use('Agg')  # For headless environments
   ```
3. Install required dependencies:
   ```bash
   pip install plotly seaborn bokeh
   ```

### Missing Plot Elements

**Problem:** Plots are generated but missing expected elements.

**Symptoms:** Plots appear incomplete or have missing data.

**Solution:**
1. Check data availability:
   ```python
   print(df['condition'].value_counts())
   print(df['stimulus_type'].value_counts())
   ```
2. Verify plot parameters and data ranges
3. Check for data filtering issues

---

## Performance Problems

### Slow Processing Times

**Problem:** Analysis pipeline runs very slowly.

**Symptoms:** Processing takes much longer than expected (>10 minutes).

**Solution:**
1. Check system resources:
   ```bash
   top  # On Linux/Mac
   tasklist  # On Windows
   ```
2. Optimize data processing:
   ```python
   # Use efficient data types
   df['response_time'] = df['response_time'].astype('float32')
   # Process in chunks
   chunk_size = 1000
   for i in range(0, len(df), chunk_size):
       chunk = df.iloc[i:i+chunk_size]
       # Process chunk
   ```
3. Use parallel processing where applicable

### High Memory Usage

**Problem:** Analysis consumes excessive memory.

**Symptoms:** System becomes slow or crashes due to memory usage.

**Solution:**
1. Monitor memory usage:
   ```python
   import psutil
   print(f"Memory usage: {psutil.virtual_memory().percent}%")
   ```
2. Process data in smaller batches
3. Clear unused variables:
   ```python
   del large_dataframe
   import gc
   gc.collect()
   ```

---

## Web Experiment Issues

### Browser Compatibility

**Problem:** Web experiment doesn't work in certain browsers.

**Symptoms:** Experiment fails to load or display incorrectly.

**Solution:**
1. Use modern browsers (Chrome, Firefox, Safari, Edge)
2. Enable JavaScript
3. Check browser console for errors (F12)
4. Try different browser or incognito mode

### Data Collection Problems

**Problem:** Web experiment doesn't collect or save data properly.

**Symptoms:** No data appears in browser console or exported files.

**Solution:**
1. Check browser console for errors
2. Ensure JavaScript is enabled
3. Check browser storage permissions
4. Try different browser or clear cache

### Stimulus Loading Issues

**Problem:** Images don't load or display incorrectly.

**Symptoms:** Missing or broken images in experiment.

**Solution:**
1. Check image file paths and formats
2. Ensure images are in correct directory
3. Check file permissions
4. Verify image file integrity

---

## Getting Help

### Self-Diagnosis Steps

1. **Check the logs:**
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

2. **Verify installation:**
   ```python
   import sys
   print(sys.version)
   import numpy, pandas, matplotlib
   print("Dependencies OK")
   ```

3. **Test with sample data:**
   ```python
   from analysis.preprocessing import DataProcessor
   processor = DataProcessor('data')
   sample_data = processor._create_sample_trial_data('S01')
   print(f"Sample data created: {len(sample_data)} trials")
   ```

### Common Error Messages and Solutions

#### ImportError: No module named 'analysis'
**Solution:** Ensure you're running from the project root directory or add the analysis directory to Python path:
```python
import sys
sys.path.append('analysis')
```

#### ValueError: Data validation failed
**Solution:** Check your data format and ensure all required columns are present.

#### FileNotFoundError: Brain images not found
**Solution:** Ensure brain images are in the correct directory (`data/processed/brain_images/`).

#### MemoryError: Unable to allocate array
**Solution:** Process data in smaller chunks or increase system memory.

### Debugging Tips

1. **Use verbose output:**
   ```bash
   python run_analysis.py --verbose
   ```

2. **Check intermediate files:**
   ```bash
   ls -la data/processed/
   ```

3. **Test individual components:**
   ```python
   # Test data processing
   from analysis.preprocessing import DataProcessor
   processor = DataProcessor('data')
   
   # Test statistical analysis
   from analysis.statistical_analysis import StatisticalAnalyzer
   analyzer = StatisticalAnalyzer(sample_data)
   ```

4. **Use debug mode:**
   ```python
   import pdb
   pdb.set_trace()  # Set breakpoint
   ```

### Contact and Support

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For general questions and community support
- **Email**: For research collaboration inquiries
- **Documentation**: Check existing docs for detailed information

### Reporting Issues

When reporting issues, please include:

1. **System information:**
   - Operating system and version
   - Python version
   - Package versions

2. **Error details:**
   - Complete error message
   - Steps to reproduce
   - Expected vs actual behavior

3. **Data information:**
   - Data format and structure
   - Sample size and conditions
   - Any data preprocessing steps

4. **Code context:**
   - Relevant code snippets
   - Configuration settings
   - Command line arguments

---

*This troubleshooting guide covers the most common issues encountered with the fMRI Tool Representation Study. For additional support, please refer to the GitHub repository or contact the development team.*
