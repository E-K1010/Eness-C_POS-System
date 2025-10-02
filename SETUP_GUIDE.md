# Setup Guide - Student A POS System

This guide will help you set up and run the Student A Mobile POS System on your local machine.

## 📋 Prerequisites

### Required Software
- **Flutter SDK 3.0+** - [Download here](https://flutter.dev/docs/get-started/install)
- **Python 3.8+** - [Download here](https://www.python.org/downloads/)
- **Git** - [Download here](https://git-scm.com/downloads)
- **Android Studio** (for mobile development) - [Download here](https://developer.android.com/studio)

### System Requirements
- **Operating System**: Windows 10/11, macOS, or Linux
- **RAM**: Minimum 8GB (16GB recommended)
- **Storage**: At least 5GB free space
- **Internet**: Required for downloading dependencies

## 🚀 Quick Setup

### 1. Clone the Repository
```bash
git clone https://github.com/E-K1010/studenta-project.git
cd studenta-project
```

### 2. Backend Setup

#### Install Python Dependencies
```bash
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn sqlalchemy pydantic python-multipart
```

#### Run the Backend Server
```bash
# Start the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# The API will be available at:
# http://localhost:8000
# Swagger UI: http://localhost:8000/docs
```

### 3. Mobile App Setup

#### Install Flutter Dependencies
```bash
cd mobile_app

# Get Flutter dependencies
flutter pub get

# Check Flutter installation
flutter doctor
```

#### Run the Mobile App
```bash
# For Android (requires Android Studio/emulator)
flutter run

# For iOS (macOS only)
flutter run -d ios

# For web (development)
flutter run -d web
```

## 🔧 Detailed Setup Instructions

### Backend Configuration

#### Database Setup
The system uses SQLite by default. No additional database setup is required.

#### Environment Variables
Create a `.env` file in the backend directory:
```env
DATABASE_URL=sqlite:///./pos_system.db
DEBUG=True
API_HOST=0.0.0.0
API_PORT=8000
```

#### API Configuration
The backend API includes:
- **Base URL**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### Mobile App Configuration

#### Flutter Environment
Ensure Flutter is properly configured:
```bash
# Check Flutter installation
flutter doctor

# Update Flutter
flutter upgrade

# Clean and get dependencies
flutter clean
flutter pub get
```

#### Android Setup
1. Install Android Studio
2. Set up Android SDK
3. Create an Android Virtual Device (AVD)
4. Enable Developer Options on your Android device (for physical device testing)

#### iOS Setup (macOS only)
1. Install Xcode from App Store
2. Install Xcode Command Line Tools
3. Accept Xcode license
4. Set up iOS Simulator

## 🧪 Testing the Setup

### Backend Testing
```bash
cd backend

# Test API endpoints
curl http://localhost:8000/products/

# Test with sample data
curl -X POST http://localhost:8000/products/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Product",
    "description": "Test Description",
    "price": 99.99,
    "category": "Test",
    "is_available": true
  }'
```

### Mobile App Testing
```bash
cd mobile_app

# Run tests
flutter test

# Check for issues
flutter analyze

# Build for testing
flutter build apk --debug
```

## 🐛 Troubleshooting

### Common Issues

#### Backend Issues

**Port Already in Use**
```bash
# Find process using port 8000
netstat -ano | findstr :8000

# Kill the process (Windows)
taskkill /PID <PID> /F

# Or use a different port
uvicorn app.main:app --reload --port 8001
```

**Database Connection Issues**
```bash
# Check if database file exists
ls -la *.db

# Recreate database
rm *.db
python -c "from app.database import create_tables; create_tables()"
```

**Python Dependencies Issues**
```bash
# Update pip
python -m pip install --upgrade pip

# Reinstall dependencies
pip install --force-reinstall fastapi uvicorn sqlalchemy pydantic
```

#### Mobile App Issues

**Flutter Doctor Issues**
```bash
# Accept Android licenses
flutter doctor --android-licenses

# Update Flutter
flutter upgrade

# Clean and reinstall
flutter clean
flutter pub get
```

**Build Issues**
```bash
# Clean build cache
flutter clean
flutter pub get

# Check for version conflicts
flutter pub deps

# Update dependencies
flutter pub upgrade
```

**Android Emulator Issues**
```bash
# List available emulators
flutter emulators

# Start emulator
flutter emulators --launch <emulator_id>

# Check connected devices
flutter devices
```

### Performance Issues

**Slow API Response**
- Check database indexing
- Monitor memory usage
- Optimize queries

**Mobile App Performance**
- Use Flutter Inspector
- Monitor memory usage
- Check for memory leaks

## 📊 Development Tools

### Recommended IDE/Editors
- **VS Code** with Flutter and Python extensions
- **Android Studio** for mobile development
- **PyCharm** for Python backend development

### Useful Extensions
- Flutter
- Dart
- Python
- REST Client
- GitLens

### Debugging Tools
- **Flutter Inspector**: Built into VS Code and Android Studio
- **API Testing**: Postman or Insomnia
- **Database**: SQLite Browser or DB Browser for SQLite

## 🔄 Development Workflow

### Git Workflow
```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Add new feature"

# Push to GitHub
git push origin feature/new-feature

# Create Pull Request on GitHub
```

### Testing Workflow
```bash
# Backend testing
cd backend
python -m pytest

# Mobile app testing
cd mobile_app
flutter test

# Integration testing
# Run both backend and mobile app
# Test API integration
```

## 📱 Deployment

### Backend Deployment
```bash
# Production server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4

# With Gunicorn (Linux/macOS)
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### Mobile App Deployment
```bash
# Android APK
flutter build apk --release

# iOS (macOS only)
flutter build ios --release
```

## 📞 Support

### Getting Help
1. Check the troubleshooting section above
2. Review the [PROJECT_DOCUMENTATION.md](./PROJECT_DOCUMENTATION.md)
3. Check the [API_DOCUMENTATION.md](./API_DOCUMENTATION.md)
4. Create an issue in the GitHub repository

### Useful Resources
- [Flutter Documentation](https://flutter.dev/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

---

**Last Updated**: October 2024  
**Setup Guide Version**: 1.0.0
