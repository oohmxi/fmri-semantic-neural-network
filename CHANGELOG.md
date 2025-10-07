# Changelog

All notable changes to the fMRI Tool Representation Study project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive testing infrastructure with unit tests
- GitHub Actions workflow for automated testing and code quality
- API documentation for all analysis modules
- Troubleshooting guide for common issues
- Citation metadata (CITATION.cff) for academic use
- Enhanced documentation in docs/ directory

### Changed
- Improved README with citation badge and repository topics
- Enhanced code coverage reporting
- Updated contributing guidelines

## [1.0.0] - 2024-10-06

### Added
- **Initial Release**: Complete fMRI Tool Representation Study implementation
- **Core Analysis Pipeline**: Modular Python architecture with 5 core modules
  - `preprocessing.py`: Data extraction and quality control
  - `statistical_analysis.py`: GLM analysis and research question testing
  - `visualization.py`: Publication-ready plotting and brain maps
  - `results_summary.py`: Automated reporting and export
  - `brain_image_processor.py`: AFNI integration and neuroimaging workflow

- **Experimental Design**: Complete 2×2×2 factorial block design implementation
  - Passive Viewing (PV) task: Visual attention with 660 trials
  - Imagined Grasp (IG) task: Motor imagery with 660 trials
  - Motor Localizer: Bilateral hand clenching with 5 trials
  - Total: 1,325 trials across all experimental conditions

- **Stimulus Materials**: Complete stimulus set with 40 images
  - 10 functional tools (screwdriver, knife, pliers, etc.)
  - 10 geometric shapes (cone, cube, cylinder, etc.)
  - Screen-optimized versions for MRI display
  - Scrambled control conditions

- **PsychoPy Experiments**: Complete experimental paradigm
  - `passive_viewing.py`: Passive viewing task implementation
  - `active_grasp.py`: Active grasping task implementation
  - `clench.py`: Motor control task implementation
  - `neural_rep_tools.py`: Comprehensive experimental paradigm

- **AFNI Integration**: Neuroimaging analysis pipeline
  - Preprocessing pipeline with motion correction and smoothing
  - Statistical analysis with General Linear Tests (GLTs)
  - Brain activation visualization and MNI coordinate reporting
  - False discovery rate correction (q < 0.05)

- **Data Processing**: Comprehensive data engineering
  - Automated extraction from PsychoPy logs and AFNI timing files
  - Quality control validation with timing synchronization
  - Data anonymization and privacy protection
  - Export to multiple formats (CSV, Excel, JSON)

- **Statistical Analysis**: Rigorous research question testing
  - **RQ1**: Tools vs Shapes comparison (t = 3.5802, p = 3.7×10⁻⁴)
  - **RQ2**: Action Potentiation analysis (t = 3.5391, p = 0.0016)
  - **RQ3**: Motor Network Validation (t = 3.7037, p = 2.3×10⁻⁴)
  - **RQ4**: Cross-Modal Integration analysis (t = 3.5391, p = 4.4×10⁻⁴)

- **Results Integration**: Real brain activation data
  - Motor localizer: M1 activation at MNI (-40, 22, 62)
  - Imagined grasp: Superior frontal gyrus, parietal lobe, LOC
  - Passive viewing: Tool vs shape contrasts in visual areas
  - Cross-modal integration: Parietofrontal network activation

- **Web Experiment**: Self-contained HTML implementation
  - Complete experimental replication in web browser
  - All 40 stimulus images included
  - Proper timing and randomization
  - Data logging and export capabilities

- **Documentation**: Comprehensive project documentation
  - Professional README with clear motivation and results
  - Detailed directory-specific README files
  - Complete data organization and file format documentation
  - Installation and usage instructions

- **Quality Assurance**: Professional software engineering practices
  - Type hints and comprehensive docstrings
  - Error handling and logging throughout
  - Modular, reusable architecture
  - Automated reporting and quality control

### Technical Specifications
- **Python Version**: 3.7+
- **Dependencies**: PsychoPy 3.2.4, NumPy, Pandas, Matplotlib, SciPy, Scikit-learn
- **Neuroimaging**: AFNI integration for preprocessing and statistical analysis
- **Data Format**: Support for CSV, Excel, JSON, PNG, and neuroimaging formats
- **Platform**: Cross-platform compatibility (Windows, macOS, Linux)

### Research Contributions
- **Scientific Rigor**: Replication of Creem-Regehr & Lee (2004) with modern methods
- **Methodological Innovation**: Integrated behavioral and neuroimaging analysis
- **Clinical Relevance**: Direct applications to neuroprosthetic rehabilitation
- **Open Science**: Complete data and code availability for reproducibility

### Key Findings
- **Tools activate motor representations** based on functional identity
- **Motor imagery engages parietofrontal networks** similar to real grasping
- **Passive viewing of tools** recruits visual and somatosensory networks
- **Cross-modal integration** demonstrates shared cognitive-motor processes

## [0.9.0] - 2024-09-15

### Added
- Initial experimental design and stimulus preparation
- Basic PsychoPy experiment implementations
- Preliminary data collection protocols
- AFNI analysis pipeline development

### Changed
- Refined experimental timing parameters
- Optimized stimulus presentation for MRI environment
- Improved data collection procedures

## [0.8.0] - 2024-08-20

### Added
- Project architecture and directory structure
- Initial Python analysis framework
- Basic data processing capabilities
- Documentation framework

### Changed
- Refined research questions and hypotheses
- Updated experimental design based on pilot testing
- Improved data organization structure

## [0.7.0] - 2024-07-10

### Added
- Literature review and methodology development
- Experimental design planning
- Stimulus selection and preparation
- Initial project setup

### Changed
- Refined research objectives
- Updated experimental protocols
- Improved stimulus materials

---

## Version Numbering

This project uses [Semantic Versioning](https://semver.org/):
- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality additions
- **PATCH** version for backwards-compatible bug fixes

## Release Process

1. **Development**: Features developed in feature branches
2. **Testing**: Comprehensive testing before release
3. **Documentation**: Updated documentation and changelog
4. **Release**: Tagged release with version number
5. **Distribution**: Available on GitHub with complete documentation

## Future Roadmap

### Planned Features
- **Group-level analysis**: Extension to multiple participants
- **ROI analysis**: Region-of-interest specific analysis
- **Machine learning**: Advanced pattern recognition methods
- **Real-time analysis**: Live data processing capabilities
- **Cross-validation**: Replication studies and validation

### Research Extensions
- **Additional conditions**: Extended experimental paradigms
- **Clinical applications**: Direct neuroprosthetic applications
- **Cross-modal studies**: Integration with other sensory modalities
- **Longitudinal studies**: Long-term rehabilitation tracking

---

*This changelog documents the evolution of the fMRI Tool Representation Study, a comprehensive research project investigating neural representations of graspable objects for neuroprosthetic applications.*
