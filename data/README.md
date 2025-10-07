# fMRI Tool Representation Study - Data Directory

This directory contains experimental data from the fMRI Tool Representation Study, including both raw and processed data files organized for analysis and reproducibility.

## Overview

The fMRI Tool Representation Study investigates neural representations of tools through different experimental conditions. This data directory contains all experimental files, from raw behavioral logs to processed analysis results.

## Directory Structure

```
data/
├── raw/                              # Original experimental data
│   ├── S01/                          # Subject 1 data
│   │   ├── experimental_runs/         # Core experimental data
│   │   ├── condition_files/           # Stimulus timing files
│   │   ├── afni_files/                # AFNI timing files
│   │   └── practice_runs/             # Practice sessions
│   ├── S02/                          # Subject 2 data
│   │   ├── experimental_runs/         # Core experimental data
│   │   ├── condition_files/           # Stimulus timing files
│   │   ├── afni_files/                # AFNI timing files
│   │   └── practice_runs/             # Practice sessions
│   └── archive/                       # Archived files
│       ├── practice_sessions/         # Practice runs and training
│       ├── test_runs/                 # Test/development runs
│       └── duplicates/                # Duplicate files
└── processed/                        # Cleaned and preprocessed data
    ├── brain_images/                  # Brain activation visualizations
    ├── plots/                         # Analysis plots
    ├── publication/                   # Publication-ready results
    ├── trial_data.csv                 # Consolidated trial data
    └── comprehensive_report.txt       # Analysis summary
```

## Data Types and File Formats

### Raw Data Files

- **`.csv`** - Behavioral data (trial responses, timing, accuracy)
- **`.log`** - PsychoPy experiment logs with detailed timing information
- **`.psydat`** - PsychoPy data files containing trial information and responses
- **`.txt`** - Condition timing files for AFNI analysis
- **`.xlsx`** - AFNI timing files for neuroimaging analysis

### Processed Data Files

- **`.png`** - Brain activation visualizations and plots
- **`.csv/.xlsx`** - Consolidated trial data and results tables
- **`.json`** - Analysis results and summary statistics
- **`.txt`** - Comprehensive analysis reports

## Experimental Conditions

Each subject participated in three main experimental runs:

1. **Passive Viewing (PV)** - Visual attention task where participants passively viewed tool images
2. **Imagined Grasp (IG)** - Motor imagery task where participants imagined grasping tools
3. **Clench** - Motor control task where participants performed hand clenching movements

## File Naming Conventions

### Raw Data Files
- `S##_PV_tool.txt` - Passive viewing tool condition for subject ##
- `S##_IG_SCRtool.txt` - Imagined grasp screen tool condition for subject ##
- `S##_clench.txt` - Clench task condition for subject ##

### Processed Data Files
- `*_brain_activation.png` - Brain activation maps for different conditions
- `behavioral_results.png` - Behavioral performance visualizations
- `trial_data.csv` - Consolidated trial-level data
- `analysis_results.json` - Statistical analysis results

## Data Organization

### Core Experimental Data
The primary experimental data is located in the `experimental_runs/` directories within each subject folder. These contain the clean, validated data used in published results.

### Supporting Files
- **Condition Files**: Stimulus timing and presentation parameters
- **AFNI Files**: Neuroimaging analysis timing files
- **Practice Data**: Training sessions moved to `practice_runs/` directories

### Archive Directory
The `archive/` directory preserves the complete experimental history:

- **Practice Sessions**: Training runs used to familiarize participants
- **Test Runs**: Development runs for parameter testing and validation
- **Duplicates**: Files identified during reorganization

**Note**: Archived files are preserved for reference and reproducibility but are not used in the main analysis.

## Data Privacy and Ethics

All participant data has been anonymized according to ethical guidelines:
- Personal identifiers removed and replaced with participant codes (S01, S02, etc.)
- No personally identifiable information is stored
- Data collection followed institutional review board protocols

## Usage Guidelines

### For Analysis
- **Core Data**: Use files in `experimental_runs/` directories for primary analysis
- **AFNI Analysis**: Use `.txt` and `.xlsx` timing files for neuroimaging analysis
- **Python Analysis**: Process `.csv` and `.log` files for behavioral analysis
- **Statistical Analysis**: Use processed data files in `processed/` directory

### For Reproducibility
- All raw data is preserved in original format
- Processing scripts maintain data provenance
- Archive directory provides complete experimental history

## Data Quality

- **Validation**: All experimental runs were validated for timing accuracy
- **Documentation**: Comprehensive logs maintained for each session
- **Backup**: Complete backup of original data preserved
- **Quality Reports**: Data quality assessments available in `processed/` directory

## Integration with Analysis Pipelines

The data structure is designed for seamless integration with:

- **AFNI**: Neuroimaging analysis using timing files
- **Python**: Behavioral analysis using log and CSV files
- **Statistical Software**: Processed data files for statistical analysis
- **Visualization**: Pre-generated plots and brain images

## Contact and Support

For questions about data structure, file formats, or analysis procedures, refer to the main project documentation or contact the research team.

---

*This README provides a comprehensive overview of the fMRI Tool Representation Study data. For specific analysis procedures or technical details, refer to the analysis scripts and documentation in the main project directory.*