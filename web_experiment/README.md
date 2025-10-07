# Web Experiment - Neural Representation of Tools

This directory contains a **working web-based version** of the fMRI Tool Representation Study.

## Files

- `simple_experiment.html` - **Main experiment file** (self-contained HTML with embedded JavaScript)
- `resources/` - Contains all stimulus images (40 total)

## Quick Start

1. **Open `simple_experiment.html`** in any modern web browser
2. **Enter participant ID** (defaults to "test001")
3. **Click "Begin Experiment"**
4. **Complete all four conditions**:
   - Tools (10 images)
   - Shapes (10 images) 
   - Scrambled Tools (10 images)
   - Scrambled Shapes (10 images)

## Features

- ✅ **Self-contained**: No external dependencies or CDN libraries
- ✅ **Cross-browser compatible**: Works in Chrome, Firefox, Safari, Edge
- ✅ **All 40 stimulus images**: Complete set from fMRI study
- ✅ **Proper timing**: 2-second stimulus presentation with fixation cross
- ✅ **Randomization**: Images shuffled within each condition
- ✅ **Data logging**: All responses logged to browser console
- ✅ **Responsive design**: Adapts to different screen sizes

## Experimental Design

- **Stimulus Duration**: 2 seconds per image
- **Fixation Cross**: 0.5 seconds before each stimulus
- **Randomization**: Random order within each condition
- **Conditions**: 4 separate blocks (Tools, Shapes, SCR Tools, SCR Shapes)
- **Total Duration**: ~2-3 minutes

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