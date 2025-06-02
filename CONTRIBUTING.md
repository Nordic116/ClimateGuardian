# Contributing to ClimateGuardian 🤝

Thank you for your interest in contributing to ClimateGuardian! This project aims to democratize access to climate data and empower decision-makers with AI-driven insights.

## 🌍 How You Can Help

### Areas of Contribution
- **Climate Data Integration**: Add new datasets and improve data quality
- **AI/ML Improvements**: Enhance the RAG system and response accuracy
- **Multilingual Support**: Add translations and improve language processing
- **User Experience**: Improve the web interface and user interactions
- **Documentation**: Help others understand and use the system
- **Testing**: Write tests and improve code quality
- **Deployment**: Improve deployment processes and infrastructure

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Git
- Basic knowledge of Flask/web development
- Understanding of climate science (helpful but not required)

### Development Setup

1. **Fork the Repository**
   ```bash
   # Fork on GitHub, then clone your fork
   git clone https://github.com/your-username/ClimateGuardian.git
   cd ClimateGuardian
   ```

2. **Set Up Development Environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Install development dependencies
   pip install pytest pytest-cov black flake8 mypy
   ```

3. **Configure Environment**
   ```bash
   # Copy environment template
   cp .env.example .env
   
   # Edit .env with your credentials (optional for basic development)
   ```

4. **Initialize Development Data**
   ```bash
   python scripts/initialize_datasets.py
   ```

5. **Run Tests**
   ```bash
   python -m pytest tests/
   ```

6. **Start Development Server**
   ```bash
   python app.py
   ```

## 📝 Development Guidelines

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and small
- Use type hints where appropriate

### Code Formatting
```bash
# Format code with black
black app.py scripts/ tests/

# Check style with flake8
flake8 app.py scripts/ tests/

# Type checking with mypy
mypy app.py
```

### Testing
- Write tests for all new features
- Maintain test coverage above 80%
- Test both success and error cases
- Use descriptive test names

```bash
# Run tests
python -m pytest tests/

# Run with coverage
python -m pytest --cov=app tests/

# Run specific test
python -m pytest tests/test_app.py::test_health_check
```

## 🔄 Contribution Workflow

### 1. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes
- Write clean, well-documented code
- Add tests for new functionality
- Update documentation as needed
- Follow the existing code style

### 3. Test Your Changes
```bash
# Run all tests
python -m pytest tests/

# Test the application manually
python app.py
```

### 4. Commit Your Changes
```bash
# Stage your changes
git add .

# Commit with descriptive message
git commit -m "Add feature: brief description of what you added"
```

### 5. Push and Create Pull Request
```bash
# Push to your fork
git push origin feature/your-feature-name

# Create pull request on GitHub
```

## 📋 Pull Request Guidelines

### Before Submitting
- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] No sensitive data (API keys, etc.) in commits

### Pull Request Template
```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Other (please describe)

## Testing
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)
```

## 🐛 Bug Reports

### Before Reporting
1. Check existing issues
2. Try the latest version
3. Reproduce the bug consistently

### Bug Report Template
```markdown
**Bug Description**
Clear description of the bug.

**Steps to Reproduce**
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment**
- OS: [e.g., Windows 10]
- Browser: [e.g., Chrome 91]
- Python version: [e.g., 3.9]
```

## 💡 Feature Requests

### Feature Request Template
```markdown
**Feature Description**
Clear description of the proposed feature.

**Problem Statement**
What problem does this solve?

**Proposed Solution**
How should this feature work?

**Alternatives Considered**
Other solutions you've considered.

**Additional Context**
Any other context or screenshots.
```

## 🌐 Adding New Climate Datasets

### Dataset Integration Checklist
- [ ] Dataset has open license (CC BY, Public Domain, etc.)
- [ ] Data is reliable and regularly updated
- [ ] API or download method available
- [ ] Documentation exists for data format
- [ ] Adds value to climate analysis

### Integration Steps
1. Add dataset info to `scripts/initialize_datasets.py`
2. Create data processing functions
3. Add API endpoints if needed
4. Update documentation
5. Add tests for new functionality

## 🌍 Multilingual Support

### Adding New Languages
1. Create translation files in `translations/` directory
2. Add language detection logic
3. Update UI to support new language
4. Test with native speakers
5. Update documentation

### Translation Guidelines
- Use climate-specific terminology correctly
- Maintain consistent tone and style
- Consider cultural context
- Provide context for translators

## 📚 Documentation

### Types of Documentation
- **Code Comments**: Explain complex logic
- **Docstrings**: Document functions and classes
- **README Updates**: Keep installation/usage current
- **API Documentation**: Document all endpoints
- **User Guides**: Help end users

### Documentation Style
- Use clear, simple language
- Include examples
- Keep it up-to-date
- Consider different skill levels

## 🏆 Recognition

### Contributors
All contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

### Types of Contributions Recognized
- Code contributions
- Documentation improvements
- Bug reports and testing
- Feature suggestions
- Community support
- Translations

## 📞 Getting Help

### Communication Channels
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Email**: team@climateguardian.ai (for sensitive issues)

### Response Times
- Issues: Within 48 hours
- Pull requests: Within 72 hours
- Security issues: Within 24 hours

## 🔒 Security

### Reporting Security Issues
- **DO NOT** create public issues for security vulnerabilities
- Email security@climateguardian.ai
- Include detailed description and steps to reproduce
- We'll respond within 24 hours

### Security Guidelines
- Never commit API keys or secrets
- Use environment variables for configuration
- Follow secure coding practices
- Keep dependencies updated

## 📄 License

By contributing to ClimateGuardian, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You

Your contributions help make climate data more accessible and support global climate action. Every contribution, no matter how small, makes a difference!

---

**Questions?** Feel free to reach out through GitHub issues or email. We're here to help! 🌱