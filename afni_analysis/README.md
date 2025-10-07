# AFNI Analysis

This directory contains the neuroimaging analysis pipeline using AFNI (Analysis of Functional NeuroImages).

## Directory Structure

- `screenshots/` - AFNI interface screenshots showing analysis steps
- `scripts/` - AFNI batch scripts for automated processing

## Analysis Pipeline

### Preprocessing Steps
1. **Motion Correction**: Realign volumes to reduce head motion artifacts
2. **Slice Timing Correction**: Correct for differences in slice acquisition times
3. **Spatial Smoothing**: Apply Gaussian smoothing kernel
4. **Normalization**: Transform to standard space (MNI)

### First-Level Analysis
- General Linear Model (GLM) analysis for each participant
- Contrasts comparing tools vs. shapes
- Motor network activation analysis

### Second-Level Analysis
- Group-level statistical analysis
- Random effects analysis
- Multiple comparison correction

## Screenshots

The screenshots document the analysis workflow and demonstrate proficiency with AFNI software, showing:
- Data preprocessing steps
- Statistical analysis setup
- Results visualization
- Quality control procedures

## Scripts

Automated AFNI scripts for reproducible analysis:
- `preprocessing.sh` - Complete preprocessing pipeline
- `first_level.sh` - Individual subject analysis
- `second_level.sh` - Group-level analysis

## Usage

```bash
# Run preprocessing pipeline
bash afni_analysis/scripts/preprocessing.sh

# Run first-level analysis
bash afni_analysis/scripts/first_level.sh

# Run group analysis
bash afni_analysis/scripts/second_level.sh
```
