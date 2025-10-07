# fMRI Tool Representation Study - Technical Documentation

Welcome to the technical documentation for the fMRI Tool Representation Study. This comprehensive guide provides detailed information about the project's architecture, implementation, and usage.

## Table of Contents

1. [Project Overview](overview.md)
2. [Architecture](architecture.md)
3. [API Reference](api.md)
4. [Installation Guide](installation.md)
5. [User Guide](user-guide.md)
6. [Developer Guide](developer-guide.md)
7. [Troubleshooting](troubleshooting.md)
8. [Contributing](contributing.md)
9. [References](references.md)

## Quick Start

### Installation
```bash
git clone https://github.com/ohernandez/fmri-tool-representation.git
cd fmri-tool-representation
pip install -r requirements.txt
```

### Basic Usage
```bash
# Run complete analysis pipeline
python run_analysis.py

# Run specific analysis components
python -c "from analysis.preprocessing import DataProcessor; processor = DataProcessor('data'); print('Ready!')"
```

### Web Experiment
```bash
# Open web experiment in browser
open web_experiment/simple_experiment.html
```

## Project Structure

```
fmri-tool-representation/
├── analysis/                 # Core analysis modules
│   ├── preprocessing.py      # Data processing and validation
│   ├── statistical_analysis.py  # Statistical analysis and hypothesis testing
│   ├── visualization.py     # Plot creation and visualization
│   ├── results_summary.py   # Results compilation and reporting
│   └── brain_image_processor.py  # Brain image processing and integration
├── data/                    # Experimental data and results
│   ├── raw/                 # Original experimental data
│   └── processed/           # Cleaned and preprocessed data
├── experiments/             # PsychoPy experiment scripts
├── stimuli/                 # Image stimuli and condition files
├── afni_analysis/           # Neuroimaging processing pipeline
├── web_experiment/          # Online experiment deployment
├── tests/                   # Comprehensive test suite
├── docs/                    # Technical documentation
└── run_analysis.py         # Main analysis pipeline
```

## Key Features

### Data Engineering
- **Automated Processing**: End-to-end data processing from raw logs to publication-ready results
- **Quality Control**: Comprehensive validation and error handling
- **Reproducibility**: Version-controlled analysis with clear documentation
- **Integration**: Seamless integration of behavioral and neuroimaging data

### Statistical Analysis
- **Research Questions**: Addresses all four core research questions
- **Multiple Comparisons**: Proper correction for multiple statistical tests
- **Effect Sizes**: Cohen's d and eta-squared for practical significance
- **Case Study Design**: Single-subject analysis with extensive trial sampling

### Visualization
- **Publication-Ready**: High-quality plots suitable for academic publication
- **Interactive**: Plotly-based interactive visualizations
- **Brain Maps**: Integration of real brain activation images
- **Automated**: Automated generation of all required figures

### Web Experiment
- **Self-Contained**: Complete experimental replication in web browser
- **Cross-Platform**: Works on all modern browsers and devices
- **Data Logging**: Comprehensive data collection and export
- **Educational**: Perfect for demonstrations and teaching

## Technical Specifications

### Dependencies
- **Python**: 3.7+ (tested on 3.8, 3.9, 3.10, 3.11)
- **Core Libraries**: NumPy, Pandas, Matplotlib, SciPy, Scikit-learn
- **Visualization**: Plotly, Seaborn, Bokeh
- **Neuroimaging**: AFNI integration
- **Experiments**: PsychoPy 3.2.4

### Performance
- **Processing Time**: Complete analysis pipeline runs in < 5 minutes
- **Memory Usage**: < 2GB RAM for full dataset processing
- **Storage**: ~500MB for complete project including data and results
- **Compatibility**: Cross-platform (Windows, macOS, Linux)

### Quality Assurance
- **Test Coverage**: >80% code coverage with comprehensive test suite
- **Code Quality**: Black formatting, Flake8 linting, MyPy type checking
- **Documentation**: Complete API documentation and user guides
- **CI/CD**: Automated testing and deployment pipeline

## Research Applications

### Clinical Applications
- **Neuroprosthetics**: Brain-computer interface design for prosthetic control
- **Rehabilitation**: Motor imagery training protocols for amputees
- **Assessment**: Motor recovery evaluation tools and procedures
- **Therapy**: Action observation therapy optimization

### Scientific Contributions
- **Methodology**: Integrated behavioral and neuroimaging analysis pipeline
- **Replication**: Modern replication of Creem-Regehr & Lee (2004)
- **Open Science**: Complete data and code availability
- **Reproducibility**: Deterministic analysis with clear procedures

## Getting Help

### Documentation
- **User Guide**: Step-by-step instructions for common tasks
- **API Reference**: Complete documentation of all functions and classes
- **Troubleshooting**: Solutions to common problems and issues
- **Examples**: Code examples and usage patterns

### Support
- **GitHub Issues**: Bug reports and feature requests
- **Discussions**: General questions and community support
- **Email**: Research collaboration inquiries
- **Contributing**: Guidelines for contributing to the project

## License and Citation

This project is licensed under the MIT License. When using this software in research, please cite:

```bibtex
@software{hernandez2024fmri,
  title={fMRI Tool Representation Study: Neural Representations of Graspable Objects},
  author={Hernandez, Omar},
  year={2024},
  url={https://github.com/ohernandez/fmri-tool-representation},
  license={MIT}
}
```

## Acknowledgments

This project builds upon the foundational work of Creem-Regehr & Lee (2004) and represents a modern data engineering approach to neuroprosthetic research. Special thanks to the open-source community for the excellent tools and libraries that made this project possible.

---

*This documentation is continuously updated to reflect the latest version of the fMRI Tool Representation Study. For the most current information, please refer to the GitHub repository.*
