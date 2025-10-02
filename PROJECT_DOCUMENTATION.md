# Student A - Mobile POS System Documentation

## 📋 Project Overview

This project implements a comprehensive Mobile Point of Sale (POS) system for Mpepo Kitchen with E-Invoicing integration. The system consists of a Flutter mobile application and a Python FastAPI backend, providing core POS features including product management, cart functionality, receipt generation, and offline transaction handling.

## 🏗️ Architecture

### System Components

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Flutter App   │◄──►│  FastAPI Backend│◄──►│   Database      │
│   (Mobile POS)  │    │   (REST API)    │    │   (SQLite)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │
         ▼
┌─────────────────┐
│  Offline Queue  │
│  (Local Storage)│
└─────────────────┘
```

### Technology Stack

**Frontend (Mobile App):**
- Flutter 3.0+
- Dart SDK
- Provider (State Management)
- HTTP/Dio (API Communication)
- SQLite (Local Storage)
- PDF Generation
- QR Code Support

**Backend (API Server):**
- Python 3.8+
- FastAPI
- SQLAlchemy (ORM)
- Pydantic (Data Validation)
- SQLite Database

## 📱 Mobile Application Features

### Core POS Features
- **Product Listing**: Browse and search products with filtering
- **Cart Management**: Add/remove items, quantity management
- **Tax & Discount Calculations**: Automatic tax computation
- **Receipt Generation**: PDF receipt creation with QR codes
- **Offline Support**: Queue transactions when offline

### Key Components

#### 1. Product Management
- **Location**: `mobile_app/lib/features/products/`
- **Files**:
  - `product_list_screen.dart` - Main product listing interface
  - `product_detail_dialog.dart` - Product details modal

#### 2. Cart System
- **Location**: `mobile_app/lib/features/cart/`
- **Files**:
  - `cart_screen.dart` - Shopping cart interface
- **Features**:
  - Add/remove items
  - Quantity adjustment
  - Tax calculations
  - Discount application

#### 3. Receipt Generation
- **Location**: `mobile_app/lib/features/receipts/`
- **Files**:
  - `receipt_generator.dart` - PDF receipt creation
- **Features**:
  - PDF generation
  - QR code integration
  - Professional formatting

#### 4. Offline Support
- **Location**: `mobile_app/lib/features/offline/`
- **Files**:
  - `offline_queue.dart` - Transaction queue management
- **Features**:
  - Local transaction storage
  - Automatic retry mechanism
  - Sync when online

### Data Models
- **Product**: Product information and pricing
- **CartItem**: Shopping cart item with quantity and calculations

### State Management
- **CartProvider**: Manages cart state and operations
- **ProductProvider**: Handles product data and API calls

## 🔧 Backend API Features

### Product Management API
- **Base URL**: `/products`
- **Authentication**: Not implemented (development phase)

#### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/products/` | List products with filtering |
| GET | `/products/{id}` | Get specific product |
| POST | `/products/` | Create new product |
| PUT | `/products/{id}` | Update product |
| DELETE | `/products/{id}` | Delete product |
| GET | `/products/categories/list` | Get all categories |
| GET | `/products/stats/overview` | Get product statistics |
| PATCH | `/products/{id}/availability` | Toggle availability |

#### API Features
- **Pagination**: Skip/limit parameters
- **Filtering**: Category and search filters
- **Search**: Name and description search
- **Statistics**: Product overview and analytics
- **Validation**: Comprehensive input validation

### Data Models

#### Product Schema
```python
{
  "id": int,
  "name": str,
  "description": str,
  "price": float,
  "category": str,
  "is_available": bool,
  "created_at": datetime,
  "updated_at": datetime
}
```

## 🚀 Installation & Setup

### Prerequisites
- Flutter SDK 3.0+
- Python 3.8+
- Git

### Backend Setup
```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install fastapi uvicorn sqlalchemy pydantic

# Run the server
uvicorn app.main:app --reload
```

### Mobile App Setup
```bash
# Navigate to mobile app directory
cd mobile_app

# Install Flutter dependencies
flutter pub get

# Run the app
flutter run
```

## 📊 Database Schema

### Products Table
```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    category VARCHAR(100),
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🔄 API Integration

### Request/Response Examples

#### Get Products
```http
GET /products/?skip=0&limit=10&category=electronics&search=laptop
```

#### Create Product
```http
POST /products/
Content-Type: application/json

{
  "name": "Laptop Pro",
  "description": "High-performance laptop",
  "price": 1299.99,
  "category": "Electronics",
  "is_available": true
}
```

## 🧪 Testing

### Backend Testing
- Unit tests for API endpoints
- Integration tests for database operations
- Validation testing for schemas

### Mobile App Testing
- Widget tests for UI components
- Integration tests for API calls
- Offline functionality testing

## 📈 Performance Considerations

### Mobile App
- **State Management**: Efficient provider-based state updates
- **Local Storage**: SQLite for offline data persistence
- **API Optimization**: Caching and request batching
- **Memory Management**: Proper disposal of resources

### Backend
- **Database Indexing**: Optimized queries for large datasets
- **Pagination**: Efficient data retrieval
- **Caching**: Response caching for frequently accessed data
- **Validation**: Input validation to prevent errors

## 🔒 Security Features

### Data Protection
- Input validation and sanitization
- SQL injection prevention
- XSS protection
- Secure API endpoints

### Offline Security
- Local data encryption
- Secure transaction queuing
- Data integrity validation

## 🚀 Deployment

### Backend Deployment
- Docker containerization
- Environment configuration
- Database migration scripts
- Health check endpoints

### Mobile App Deployment
- Android APK generation
- iOS app store preparation
- Code signing
- Release management

## 📝 Development Guidelines

### Code Standards
- **Flutter**: Follow Dart style guide
- **Python**: PEP 8 compliance
- **API**: RESTful design principles
- **Database**: Normalized schema design

### Git Workflow
- Feature branch development
- Code review process
- Automated testing
- Continuous integration

## 🐛 Troubleshooting

### Common Issues
1. **API Connection**: Check network connectivity and endpoint URLs
2. **Offline Sync**: Verify local storage and queue status
3. **PDF Generation**: Ensure proper permissions and dependencies
4. **Database**: Check connection strings and migrations

### Debug Tools
- Flutter Inspector for UI debugging
- API testing with Postman/curl
- Database inspection tools
- Log analysis and monitoring

## 📞 Support

For technical support or questions:
- Check the troubleshooting section
- Review API documentation
- Test with sample data
- Verify system requirements

## 🔄 Future Enhancements

### Planned Features
- User authentication and authorization
- Multi-store support
- Advanced reporting and analytics
- Real-time synchronization
- Cloud backup integration
- Enhanced offline capabilities

### Technical Improvements
- Performance optimization
- Security enhancements
- Scalability improvements
- Monitoring and logging
- Automated testing coverage

---

**Last Updated**: October 2024  
**Version**: 1.0.0  
**Maintainer**: Student A Development Team
