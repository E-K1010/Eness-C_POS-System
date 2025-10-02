from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models.product import Product
from app.schemas.product import (
    ProductCreate, 
    ProductUpdate, 
    ProductResponse, 
    ProductListResponse,
    ProductStats
)

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=ProductListResponse)
async def get_products(
    skip: int = Query(0, ge=0, description="Number of products to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Number of products to return"),
    category: Optional[str] = Query(None, description="Filter by category"),
    search: Optional[str] = Query(None, description="Search in name and description"),
    available_only: bool = Query(True, description="Show only available products"),
    db: Session = Depends(get_db)
):
    """
    Get a list of products with optional filtering and pagination.
    """
    query = db.query(Product)
    
    # Apply filters
    if available_only:
        query = query.filter(Product.is_available == True)
    
    if category:
        query = query.filter(Product.category == category)
    
    if search:
        search_term = f"%{search}%"
        query = query.filter(
            (Product.name.ilike(search_term)) | 
            (Product.description.ilike(search_term))
        )
    
    # Get total count
    total = query.count()
    
    # Apply pagination
    products = query.offset(skip).limit(limit).all()
    
    # Calculate pages
    pages = (total + limit - 1) // limit
    
    return ProductListResponse(
        products=[ProductResponse.from_orm(product) for product in products],
        total=total,
        page=(skip // limit) + 1,
        size=limit,
        pages=pages
    )

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    """
    Get a specific product by ID.
    """
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return ProductResponse.from_orm(product)

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Create a new product.
    """
    # Check if product with same name already exists
    existing_product = db.query(Product).filter(Product.name == product.name).first()
    if existing_product:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product with this name already exists"
        )
    
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    
    return ProductResponse.from_orm(db_product)

@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int, 
    product_update: ProductUpdate, 
    db: Session = Depends(get_db)
):
    """
    Update an existing product.
    """
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    # Check if new name conflicts with existing product
    if product_update.name and product_update.name != db_product.name:
        existing_product = db.query(Product).filter(
            Product.name == product_update.name,
            Product.id != product_id
        ).first()
        if existing_product:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Product with this name already exists"
            )
    
    # Update fields
    update_data = product_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_product, field, value)
    
    db.commit()
    db.refresh(db_product)
    
    return ProductResponse.from_orm(db_product)

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Delete a product.
    """
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    db.delete(db_product)
    db.commit()

@router.get("/categories/list", response_model=List[str])
async def get_categories(db: Session = Depends(get_db)):
    """
    Get a list of all unique product categories.
    """
    categories = db.query(Product.category).distinct().all()
    return [category[0] for category in categories if category[0]]

@router.get("/stats/overview", response_model=ProductStats)
async def get_product_stats(db: Session = Depends(get_db)):
    """
    Get product statistics overview.
    """
    total_products = db.query(Product).count()
    available_products = db.query(Product).filter(Product.is_available == True).count()
    unavailable_products = total_products - available_products
    
    # Get unique categories
    categories = db.query(Product.category).distinct().all()
    category_list = [cat[0] for cat in categories if cat[0]]
    
    # Calculate average price and total value
    products = db.query(Product).all()
    if products:
        average_price = sum(p.price for p in products) / len(products)
        total_value = sum(p.price for p in products)
    else:
        average_price = 0.0
        total_value = 0.0
    
    return ProductStats(
        total_products=total_products,
        available_products=available_products,
        unavailable_products=unavailable_products,
        categories=category_list,
        average_price=round(average_price, 2),
        total_value=round(total_value, 2)
    )

@router.patch("/{product_id}/availability", response_model=ProductResponse)
async def toggle_product_availability(
    product_id: int, 
    is_available: bool = Query(..., description="Product availability status"),
    db: Session = Depends(get_db)
):
    """
    Toggle product availability status.
    """
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    db_product.is_available = is_available
    db.commit()
    db.refresh(db_product)
    
    return ProductResponse.from_orm(db_product)
