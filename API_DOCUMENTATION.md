# API Documentation - Student A POS System

## Overview

This document provides comprehensive API documentation for the Student A Mobile POS System backend. The API is built with FastAPI and provides RESTful endpoints for product management.

## Base URL

```
http://localhost:8000
```

## Authentication

Currently, the API does not implement authentication (development phase). All endpoints are publicly accessible.

## API Endpoints

### Products

#### Get Products List
**GET** `/products/`

Retrieve a paginated list of products with optional filtering.

**Query Parameters:**
- `skip` (int, optional): Number of products to skip (default: 0)
- `limit` (int, optional): Number of products to return (default: 100, max: 1000)
- `category` (string, optional): Filter by product category
- `search` (string, optional): Search in product name and description
- `available_only` (boolean, optional): Show only available products (default: true)

**Response:**
```json
{
  "products": [
    {
      "id": 1,
      "name": "Laptop Pro",
      "description": "High-performance laptop",
      "price": 1299.99,
      "category": "Electronics",
      "is_available": true,
      "created_at": "2024-10-02T10:00:00Z",
      "updated_at": "2024-10-02T10:00:00Z"
    }
  ],
  "total": 1,
  "page": 1,
  "size": 100,
  "pages": 1
}
```

**Example Request:**
```bash
curl -X GET "http://localhost:8000/products/?skip=0&limit=10&category=Electronics&search=laptop"
```

#### Get Product by ID
**GET** `/products/{product_id}`

Retrieve a specific product by its ID.

**Path Parameters:**
- `product_id` (int): The ID of the product

**Response:**
```json
{
  "id": 1,
  "name": "Laptop Pro",
  "description": "High-performance laptop",
  "price": 1299.99,
  "category": "Electronics",
  "is_available": true,
  "created_at": "2024-10-02T10:00:00Z",
  "updated_at": "2024-10-02T10:00:00Z"
}
```

**Example Request:**
```bash
curl -X GET "http://localhost:8000/products/1"
```

#### Create Product
**POST** `/products/`

Create a new product.

**Request Body:**
```json
{
  "name": "Laptop Pro",
  "description": "High-performance laptop",
  "price": 1299.99,
  "category": "Electronics",
  "is_available": true
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "name": "Laptop Pro",
  "description": "High-performance laptop",
  "price": 1299.99,
  "category": "Electronics",
  "is_available": true,
  "created_at": "2024-10-02T10:00:00Z",
  "updated_at": "2024-10-02T10:00:00Z"
}
```

**Example Request:**
```bash
curl -X POST "http://localhost:8000/products/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop Pro",
    "description": "High-performance laptop",
    "price": 1299.99,
    "category": "Electronics",
    "is_available": true
  }'
```

#### Update Product
**PUT** `/products/{product_id}`

Update an existing product.

**Path Parameters:**
- `product_id` (int): The ID of the product to update

**Request Body:**
```json
{
  "name": "Laptop Pro Updated",
  "description": "Updated high-performance laptop",
  "price": 1399.99,
  "category": "Electronics",
  "is_available": true
}
```

**Response:**
```json
{
  "id": 1,
  "name": "Laptop Pro Updated",
  "description": "Updated high-performance laptop",
  "price": 1399.99,
  "category": "Electronics",
  "is_available": true,
  "created_at": "2024-10-02T10:00:00Z",
  "updated_at": "2024-10-02T11:00:00Z"
}
```

**Example Request:**
```bash
curl -X PUT "http://localhost:8000/products/1" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop Pro Updated",
    "description": "Updated high-performance laptop",
    "price": 1399.99,
    "category": "Electronics",
    "is_available": true
  }'
```

#### Delete Product
**DELETE** `/products/{product_id}`

Delete a product.

**Path Parameters:**
- `product_id` (int): The ID of the product to delete

**Response:** 204 No Content

**Example Request:**
```bash
curl -X DELETE "http://localhost:8000/products/1"
```

#### Get Categories
**GET** `/products/categories/list`

Get a list of all unique product categories.

**Response:**
```json
["Electronics", "Clothing", "Books", "Home & Garden"]
```

**Example Request:**
```bash
curl -X GET "http://localhost:8000/products/categories/list"
```

#### Get Product Statistics
**GET** `/products/stats/overview`

Get product statistics overview.

**Response:**
```json
{
  "total_products": 150,
  "available_products": 145,
  "unavailable_products": 5,
  "categories": ["Electronics", "Clothing", "Books"],
  "average_price": 89.50,
  "total_value": 13425.00
}
```

**Example Request:**
```bash
curl -X GET "http://localhost:8000/products/stats/overview"
```

#### Toggle Product Availability
**PATCH** `/products/{product_id}/availability`

Toggle product availability status.

**Path Parameters:**
- `product_id` (int): The ID of the product

**Query Parameters:**
- `is_available` (boolean): Product availability status

**Response:**
```json
{
  "id": 1,
  "name": "Laptop Pro",
  "description": "High-performance laptop",
  "price": 1299.99,
  "category": "Electronics",
  "is_available": false,
  "created_at": "2024-10-02T10:00:00Z",
  "updated_at": "2024-10-02T12:00:00Z"
}
```

**Example Request:**
```bash
curl -X PATCH "http://localhost:8000/products/1/availability?is_available=false"
```

## Data Models

### Product
```json
{
  "id": "integer",
  "name": "string",
  "description": "string",
  "price": "number (decimal)",
  "category": "string",
  "is_available": "boolean",
  "created_at": "datetime (ISO 8601)",
  "updated_at": "datetime (ISO 8601)"
}
```

### ProductListResponse
```json
{
  "products": "array of Product objects",
  "total": "integer (total count)",
  "page": "integer (current page)",
  "size": "integer (page size)",
  "pages": "integer (total pages)"
}
```

### ProductStats
```json
{
  "total_products": "integer",
  "available_products": "integer",
  "unavailable_products": "integer",
  "categories": "array of strings",
  "average_price": "number (decimal)",
  "total_value": "number (decimal)"
}
```

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Product with this name already exists"
}
```

### 404 Not Found
```json
{
  "detail": "Product not found"
}
```

### 422 Validation Error
```json
{
  "detail": [
    {
      "loc": ["body", "price"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

## Rate Limiting

Currently, no rate limiting is implemented. This will be added in future versions.

## CORS

CORS is configured to allow requests from any origin during development. Production configuration should restrict this appropriately.

## Testing

### Using curl
All examples above include curl commands for testing the API endpoints.

### Using Postman
Import the API collection or use the provided curl commands in Postman.

### Using Python requests
```python
import requests

# Get products
response = requests.get("http://localhost:8000/products/")
products = response.json()

# Create product
new_product = {
    "name": "Test Product",
    "description": "Test Description",
    "price": 99.99,
    "category": "Test",
    "is_available": True
}
response = requests.post("http://localhost:8000/products/", json=new_product)
```

## OpenAPI/Swagger Documentation

The API includes automatic OpenAPI/Swagger documentation available at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`

## Development Notes

- All timestamps are in UTC
- Price values are stored as decimal with 2 decimal places
- Product names must be unique
- Category filtering is case-sensitive
- Search is case-insensitive and searches both name and description fields

---

**Last Updated**: October 2024  
**API Version**: 1.0.0  
**Base URL**: http://localhost:8000
