# Experiments

This directory contains the PsychoPy experiment scripts for the fMRI Tool Representation Study.

## Experiment Files

- `passive_viewing.py` - Passive viewing task where participants view images while maintaining fixation
- `active_grasp.py` - Active grasping task where participants imagine grasping objects
- `clench.py` - Motor control task with actual hand clenching movements
- `neural_rep_tools.py` - Comprehensive experimental paradigm combining all conditions

## Usage

Each experiment can be run independently:

```bash
python experiments/passive_viewing.py
python experiments/active_grasp.py
python experiments/clench.py
python experiments/neural_rep_tools.py
```

## Technical Details

- **PsychoPy Version**: 3.2.4
- **Display Resolution**: 1024x768
- **Timing Precision**: 1ms tolerance
- **Scanner Sync**: Hardware synchronization with 't' key
- **fMRI Parameters**: TR = 2.0s, 30 volumes per run

## Stimulus Timing

- **Stimulus Duration**: 2 seconds
- **Rest Duration**: 10 seconds
- **Block Design**: Optimized for fMRI analysis
- **Randomization**: Random selection of 8 stimuli per condition
