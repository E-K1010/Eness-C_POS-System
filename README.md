# Student A - Mobile POS System

A comprehensive Mobile Point of Sale (POS) system for Mpepo Kitchen with E-Invoicing integration, featuring a Flutter mobile application and Python FastAPI backend.

## 🚀 Quick Start

### Prerequisites
- Flutter SDK 3.0+
- Python 3.8+
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/E-K1010/studenta-project.git
cd studenta-project

# Backend setup
cd backend
pip install fastapi uvicorn sqlalchemy pydantic
uvicorn app.main:app --reload

# Mobile app setup
cd ../mobile_app
flutter pub get
flutter run
```

## 📱 Features

### Mobile Application
- **Product Management**: Browse, search, and filter products
- **Shopping Cart**: Add/remove items with quantity management
- **Tax & Discounts**: Automatic tax calculations and discount application
- **Receipt Generation**: PDF receipts with QR codes
- **Offline Support**: Queue transactions when offline with auto-sync

### Backend API
- **Product CRUD**: Complete product management endpoints
- **Advanced Filtering**: Search, category filtering, and pagination
- **Statistics**: Product analytics and overview
- **RESTful Design**: Clean, documented API endpoints

## 🏗️ Project Structure

```
studenta-project/
├── mobile_app/                 # Flutter mobile application
│   ├── lib/
│   │   ├── features/
│   │   │   ├── products/       # Product listing and management
│   │   │   ├── cart/           # Shopping cart functionality
│   │   │   ├── receipts/       # Receipt generation
│   │   │   └── offline/        # Offline queue management
│   │   ├── models/             # Data models
│   │   └── providers/          # State management
│   └── pubspec.yaml
├── backend/                    # Python FastAPI backend
│   └── app/
│       ├── api/                # API endpoints
│       ├── models/             # Database models
│       └── schemas/            # Pydantic schemas
└── PROJECT_DOCUMENTATION.md    # Comprehensive documentation
```

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/products/` | List products with filtering |
| GET | `/products/{id}` | Get specific product |
| POST | `/products/` | Create new product |
| PUT | `/products/{id}` | Update product |
| DELETE | `/products/{id}` | Delete product |
| GET | `/products/categories/list` | Get all categories |
| GET | `/products/stats/overview` | Get product statistics |

## 📊 Key Responsibilities

- ✅ **Mobile POS Core Features**: Product listing, cart management, tax/discount calculations
- ✅ **Receipt Generation**: PDF receipt creation with QR codes
- ✅ **Offline Support**: Transaction queue and retry mechanism
- ✅ **Backend API**: Complete CRUD endpoints for products
- ✅ **API Documentation**: Comprehensive OpenAPI/Swagger specification

## 🛠️ Technology Stack

**Frontend:**
- Flutter 3.0+ with Dart
- Provider for state management
- HTTP/Dio for API communication
- SQLite for local storage
- PDF generation and QR codes

**Backend:**
- Python 3.8+ with FastAPI
- SQLAlchemy ORM
- Pydantic for data validation
- SQLite database

## 📚 Documentation

- **[PROJECT_DOCUMENTATION.md](./PROJECT_DOCUMENTATION.md)** - Comprehensive project documentation
- **[API Documentation](./backend/app/api/products.py)** - Detailed API endpoint documentation
- **[Setup Guide](./PROJECT_DOCUMENTATION.md#installation--setup)** - Installation and configuration

## 🧪 Testing

```bash
# Backend testing
cd backend
python -m pytest

# Mobile app testing
cd mobile_app
flutter test
```

## 🚀 Deployment

The system is designed for easy deployment with Docker support and environment configuration.

## 📞 Support

For questions or issues, please refer to the [PROJECT_DOCUMENTATION.md](./PROJECT_DOCUMENTATION.md) or create an issue in the repository.

---

**Repository**: https://github.com/E-K1010/studenta-project  
**Last Updated**: October 2024  
**Version**: 1.0.0
