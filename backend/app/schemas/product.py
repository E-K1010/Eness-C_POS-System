from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255, description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., gt=0, description="Product price in TZS")
    category: str = Field(..., min_length=1, max_length=100, description="Product category")
    image_url: Optional[str] = Field(None, max_length=500, description="Product image URL")
    is_available: bool = Field(True, description="Product availability status")
    tax_rate: float = Field(18.0, ge=0, le=100, description="Tax rate as percentage")

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Product name cannot be empty')
        return v.strip()

    @validator('category')
    def category_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Product category cannot be empty')
        return v.strip()

    @validator('price')
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Product price must be greater than 0')
        return round(v, 2)

    @validator('tax_rate')
    def tax_rate_must_be_valid(cls, v):
        if v < 0 or v > 100:
            raise ValueError('Tax rate must be between 0 and 100')
        return round(v, 2)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    category: Optional[str] = Field(None, min_length=1, max_length=100)
    image_url: Optional[str] = Field(None, max_length=500)
    is_available: Optional[bool] = None
    tax_rate: Optional[float] = Field(None, ge=0, le=100)

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('Product name cannot be empty')
        return v.strip() if v else v

    @validator('category')
    def category_must_not_be_empty(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('Product category cannot be empty')
        return v.strip() if v else v

    @validator('price')
    def price_must_be_positive(cls, v):
        if v is not None and v <= 0:
            raise ValueError('Product price must be greater than 0')
        return round(v, 2) if v is not None else v

    @validator('tax_rate')
    def tax_rate_must_be_valid(cls, v):
        if v is not None and (v < 0 or v > 100):
            raise ValueError('Tax rate must be between 0 and 100')
        return round(v, 2) if v is not None else v

class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int
    page: int
    size: int
    pages: int

class ProductStats(BaseModel):
    total_products: int
    available_products: int
    unavailable_products: int
    categories: list[str]
    average_price: float
    total_value: float
