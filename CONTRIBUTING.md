# Contributing to fMRI Tool Representation Study

Thank you for your interest in contributing to the fMRI Tool Representation Study! This document provides guidelines for contributing to this research project.

## Project Overview

This project investigates neural representations of graspable objects using a comprehensive data engineering approach, combining Python analysis pipelines with AFNI neuroimaging workflows. The research addresses critical questions in neuroprosthetic rehabilitation and brain-computer interface design.

## How to Contribute

### Types of Contributions

We welcome contributions in the following areas:

1. **Code Improvements**
   - Bug fixes and performance optimizations
   - Additional analysis methods and statistical tests
   - Enhanced visualization capabilities
   - Code refactoring and documentation improvements

2. **Documentation**
   - Technical documentation improvements
   - Tutorial and example additions
   - API documentation enhancements
   - Troubleshooting guide updates


4. **Research Extensions**
   - Additional experimental conditions
   - New analysis methodologies
   - Cross-validation studies
   - Replication studies

### Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/fmri-tool-representation.git
   cd fmri-tool-representation
   ```

3. **Set up the development environment**:
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Install development dependencies (optional)
   # pip install black flake8 mypy
   ```

4. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Guidelines

### Code Style

- **Python**: Follow PEP 8 style guidelines
- **Documentation**: Use Google-style docstrings
- **Type hints**: Include type annotations for all functions
- **Formatting**: Use `black` for code formatting
- **Linting**: Use `flake8` for code quality checks


### Documentation Standards

- **Docstrings**: Document all public functions and classes
- **README updates**: Update relevant sections for new features
- **API docs**: Update technical documentation
- **Examples**: Provide usage examples for new functionality


## Research Contributions

### Experimental Design

When proposing new experimental conditions or analysis methods:

1. **Literature Review**: Provide relevant citations
2. **Methodology**: Describe the proposed approach
3. **Validation**: Explain how results will be validated
4. **Ethics**: Ensure compliance with research ethics guidelines

### Data Analysis Extensions

For new analysis methods:

1. **Statistical Rigor**: Use appropriate statistical tests
2. **Multiple Comparisons**: Apply proper correction methods
3. **Effect Sizes**: Report practical significance measures
4. **Reproducibility**: Ensure deterministic results

## Data Handling

### Data Privacy

- **Anonymization**: All participant data must be anonymized
- **Consent**: Ensure proper informed consent procedures
- **Storage**: Follow institutional data storage guidelines
- **Sharing**: Only share de-identified data

### Data Formats

- **Raw Data**: Preserve original experimental files
- **Processed Data**: Document all processing steps
- **Results**: Use standard formats (CSV, JSON, PNG)
- **Metadata**: Include comprehensive data descriptions

## Pull Request Process

### Before Submitting

1. **Check code style**: Run `black` and `flake8` (optional)
2. **Update documentation**: Update relevant docs
3. **Write clear commit messages**: Use conventional commit format

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Research extension

## Documentation
- [ ] Code documented
- [ ] README updated (if needed)
- [ ] API docs updated (if needed)

## Research Impact
Describe how this contributes to the research goals
```

### Review Process

1. **Code Review**: Maintainers review code quality and methodology
2. **Research Review**: Scientific accuracy and rigor verification
3. **Manual Testing**: Ensure compatibility with existing code

## Academic Contributions

### Citation Guidelines

When using this project in research:

1. **Cite the original paper**: Creem-Regehr & Lee (2004)
2. **Cite this repository**: Use the provided CITATION.cff
3. **Acknowledge contributions**: Credit all contributors
4. **Share results**: Consider contributing back findings

### Publication Support

- **Data sharing**: We encourage data sharing for replication
- **Methodology**: Detailed methods available in documentation
- **Results**: Publication-ready outputs provided
- **Collaboration**: Open to research collaborations

## Bug Reports

### Reporting Bugs

Use GitHub Issues with the following information:

1. **Environment**: Python version, OS, dependencies
2. **Steps to reproduce**: Clear reproduction steps
3. **Expected behavior**: What should happen
4. **Actual behavior**: What actually happens
5. **Error messages**: Complete error output
6. **Data**: Sample data that causes the issue (if applicable)

### Bug Report Template

```markdown
**Bug Description**
Brief description of the bug

**Environment**
- Python version: 
- OS: 
- Package versions: 

**Steps to Reproduce**
1. 
2. 
3. 

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Error Messages**
```
Error output here
```

**Additional Context**
Any other relevant information
```

## Feature Requests

### Suggesting Features

1. **Use case**: Describe the research need
2. **Implementation**: Suggest technical approach
3. **Benefits**: Explain research impact
4. **Alternatives**: Consider existing solutions

## Contact and Support

### Getting Help

- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For general questions and ideas
- **Email**: For research collaboration inquiries
- **Documentation**: Check existing docs first

### Community Guidelines

- **Be respectful**: Maintain professional communication
- **Be constructive**: Provide helpful feedback
- **Be patient**: Research projects have complex requirements
- **Be collaborative**: Work together toward research goals

## Recognition

### Contributor Recognition

Contributors will be recognized through:

1. **GitHub contributors**: Automatic recognition in repository
2. **Research acknowledgments**: Credit in publications
3. **Documentation**: Contributor list in project docs
4. **Collaboration**: Invitation to research collaborations

## License

By contributing to this project, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

**Thank you for contributing to the fMRI Tool Representation Study!**

*This project represents important research in neuroprosthetics and brain-computer interfaces. Your contributions help advance our understanding of neural representations and improve rehabilitation technologies.*
