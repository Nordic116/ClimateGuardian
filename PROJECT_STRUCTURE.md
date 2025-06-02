# ClimateGuardian Project Structure 📁

This document provides an overview of the ClimateGuardian project structure and explains the purpose of each component.

## 📂 Root Directory Structure

```
ClimateGuardian/
├── 📄 README.md                    # Main project documentation
├── 📄 LICENSE                      # MIT License
├── 📄 DEPLOYMENT.md                # Deployment guide for Render
├── 📄 CONTRIBUTING.md              # Contribution guidelines
├── 📄 PROJECT_STRUCTURE.md         # This file
├── 📄 .env.example                 # Environment variables template
├── 📄 .gitignore                   # Git ignore rules
├── 📄 requirements.txt             # Python dependencies
├── 📄 runtime.txt                  # Python version for deployment
├── 📄 Procfile                     # Process file for deployment
├── 📄 render.yaml                  # Render deployment configuration
├── 🐍 app.py                       # Main Flask application
├── 📁 templates/                   # HTML templates
├── 📁 static/                      # Static assets (CSS, JS, images)
├── 📁 scripts/                     # Utility scripts
├── 📁 tests/                       # Test suite
└── 📁 data/                        # Dataset storage and metadata
```

## 🔧 Core Application Files

### `app.py` - Main Application
- **Purpose**: Core Flask web application
- **Features**:
  - RESTful API endpoints
  - ClimateGuardian AI assistant class
  - Intent analysis and response generation
  - Session management and conversation history
  - CORS support for cross-origin requests

### `requirements.txt` - Dependencies
- **Purpose**: Python package dependencies
- **Key Packages**:
  - `Flask==3.0.0` - Web framework
  - `Flask-CORS==4.0.0` - Cross-origin resource sharing
  - `requests==2.31.0` - HTTP client library
  - `gunicorn==21.2.0` - WSGI HTTP server

### `render.yaml` - Deployment Configuration
- **Purpose**: Render platform deployment settings
- **Configuration**:
  - Build and start commands
  - Environment variables
  - Service type and plan

## 🌐 Web Interface

### `templates/index.html` - Main UI
- **Purpose**: Single-page application interface
- **Features**:
  - Responsive design with mobile support
  - Real-time chat interface
  - Example queries and feature showcase
  - Dataset information display
  - Professional climate-themed styling

### `static/` - Static Assets
- **Purpose**: CSS, JavaScript, and image files
- **Current Status**: Styles embedded in HTML for simplicity
- **Future**: Can be expanded with separate CSS/JS files

## 🔬 Scripts and Utilities

### `scripts/initialize_datasets.py` - Dataset Setup
- **Purpose**: Initialize and validate climate datasets
- **Features**:
  - Dataset metadata creation
  - API connectivity testing
  - Sample data generation
  - Environment validation
  - Initialization reporting

## 🧪 Testing

### `tests/test_app.py` - Test Suite
- **Purpose**: Comprehensive application testing
- **Test Coverage**:
  - API endpoint testing
  - Intent analysis validation
  - Query processing verification
  - Error handling checks
  - Conversation history tracking

## 📊 Data Management

### `data/` - Dataset Storage
- **Purpose**: Store dataset metadata and sample data
- **Structure**:
  ```
  data/
  ├── {dataset}_metadata.json     # Dataset information
  ├── {dataset}_sample.json       # Sample data for demo
  └── initialization_report.json  # Setup status report
  ```

### Supported Datasets
1. **ND-GAIN** - Climate vulnerability index
2. **NOAA Climate Data** - Weather and climate records
3. **OpenAQ** - Air quality measurements
4. **Climate TRACE** - Greenhouse gas emissions
5. **Climate Watch** - Climate policy tracking
6. **UN SDG 13** - Climate action indicators

## 🚀 Deployment Files

### `Procfile` - Process Definition
- **Purpose**: Define how to run the application
- **Command**: `web: gunicorn --bind 0.0.0.0:$PORT app:app`

### `runtime.txt` - Python Version
- **Purpose**: Specify Python version for deployment
- **Version**: `python-3.11.0`

### `.env.example` - Environment Template
- **Purpose**: Template for environment variables
- **Variables**:
  - `WATSONX_API_KEY` - IBM watsonx.ai API key
  - `WATSONX_PROJECT_ID` - watsonx.ai project ID
  - `IBM_CLOUD_API_KEY` - IBM Cloud API key
  - `SECRET_KEY` - Flask session secret

## 📚 Documentation

### `README.md` - Main Documentation
- **Purpose**: Comprehensive project overview
- **Sections**:
  - Project description and goals
  - Features and capabilities
  - Installation and setup
  - Usage examples
  - Architecture overview

### `DEPLOYMENT.md` - Deployment Guide
- **Purpose**: Step-by-step deployment instructions
- **Platforms**: Render (primary), with general guidelines
- **Sections**:
  - Prerequisites and setup
  - Environment configuration
  - Deployment verification
  - Troubleshooting

### `CONTRIBUTING.md` - Contribution Guide
- **Purpose**: Guidelines for contributors
- **Sections**:
  - Development setup
  - Code style and standards
  - Testing requirements
  - Pull request process

## 🔒 Security and Configuration

### `.gitignore` - Version Control
- **Purpose**: Exclude sensitive and generated files
- **Excludes**:
  - Environment files (`.env`)
  - Python cache (`__pycache__/`)
  - IDE files (`.vscode/`, `.idea/`)
  - Temporary files and logs

### Environment Variables
- **Security**: All sensitive data stored in environment variables
- **Configuration**: Separate development and production settings
- **Validation**: Environment validation in initialization script

## 🏗️ Architecture Overview

### Application Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface (HTML/JS)                 │
├─────────────────────────────────────────────────────────────┤
│                    Flask Web Application                    │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │   API Routes    │  │  ClimateGuardian │  │   Session       │ │
│  │   (/api/*)      │  │   AI Assistant   │  │  Management     │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│                    Data Layer                               │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │   Climate       │  │    Mock Data    │  │   Metadata      │ │
│  │   Datasets      │  │   (Demo Mode)   │  │   Storage       │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### API Endpoints
- `GET /` - Main application page
- `GET /api/health` - Health check
- `GET /api/datasets` - Dataset information
- `POST /api/query` - Process climate queries
- `GET /api/history` - Conversation history

## 🔄 Development Workflow

### Local Development
1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Initialize datasets: `python scripts/initialize_datasets.py`
4. Run tests: `python -m pytest tests/`
5. Start server: `python app.py`

### Production Deployment
1. Configure environment variables
2. Deploy to Render using `render.yaml`
3. Verify deployment with health checks
4. Monitor logs and performance

## 📈 Future Enhancements

### Planned Features
- Real IBM watsonx.ai integration
- Vector database for RAG
- Advanced data visualization
- Mobile application
- API rate limiting
- User authentication
- Multi-language support

### Scalability Considerations
- Database integration for persistent storage
- Caching layer for improved performance
- Load balancing for high availability
- Monitoring and alerting systems

---

**📞 Questions?** Refer to the documentation files or create an issue in the repository.