# Web Experiment - Neural Representation of Tools

This directory contains a **working web-based version** of the fMRI Tool Representation Study.

## Files

- `simple_experiment.html` - **Main experiment file** (self-contained HTML with embedded JavaScript)
- `resources/` - Contains all stimulus images (40 total)

## Quick Start

1. **Open `simple_experiment.html`** in any modern web browser
2. **Enter participant ID** (defaults to "test001")
3. **Click "Begin Experiment"** or press SPACEBAR
4. **Complete all four conditions**:
   - Scrambled Tools (8 images)
   - Tools (8 images)
   - Scrambled Shapes (8 images)
   - Shapes (8 images)

### Demo Mode
- **Press SPACEBAR** during the experiment to toggle demo mode on/off
- **Demo mode** runs trials much faster (1s stimulus, 0.5s intervals)
- **Perfect for demonstrations** and testing the experiment structure
- **Press SPACEBAR again** to return to normal timing

## Features

- ✅ **Self-contained**: No external dependencies or CDN libraries
- ✅ **Cross-browser compatible**: Works in Chrome, Firefox, Safari, Edge
- ✅ **32 stimulus images**: 8 images per condition from fMRI study
- ✅ **Proper timing**: 2-second stimulus presentation with 10-second interstimulus intervals
- ✅ **Demo mode**: Press SPACEBAR to toggle faster timing for demonstrations
- ✅ **Randomization**: Images shuffled within each condition
- ✅ **Data logging**: All responses logged to browser console
- ✅ **Responsive design**: Adapts to different screen sizes

## Experimental Design

- **Stimulus Duration**: 2 seconds per image
- **Interstimulus Interval**: 10 seconds with fixation cross
- **Randomization**: Random order within each condition
- **Block Sequence**: Scrambled Tools → Tools → Scrambled Shapes → Shapes
- **Images per Block**: 8 images per condition
- **Total Duration**: ~10 minutes

## Data Collection

The experiment automatically logs:
- Participant ID
- Start time
- All trial data (condition, image, trial number, timestamp)
- Complete experiment data available in browser console

## Deployment Options

- **Local testing**: Open file directly in browser
- **Live Server**: Use VS Code Live Server extension
- **Web server**: Deploy to any web hosting service
- **GitHub Pages**: Host for free on GitHub

## Relationship to fMRI Study

This web version replicates the core experimental design:
- Same stimulus images
- Same condition structure  
- Same timing parameters
- Behavioral validation of stimuli

Perfect for:
- **Pilot testing** before fMRI sessions
- **Behavioral validation** of stimuli
- **Remote data collection**
- **Public demonstrations** of research
- **Teaching** experimental design

## Technical Details

- **Pure HTML/CSS/JavaScript**: No external libraries required
- **No CORS issues**: All resources load locally
- **No module dependencies**: Works in all browsers
- **Lightweight**: Single file, fast loading