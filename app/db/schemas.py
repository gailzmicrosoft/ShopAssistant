# Pydantic schemas for API requests and responses
#
# Pydantic is a Python library for data validation and settings management using Python type annotations.
# It automatically checks that data matches the expected types and structure, and provides helpful error messages if not.
# In FastAPI, Pydantic models (schemas) are used to validate incoming request data and serialize outgoing responses,
# making your API robust, secure, and self-documenting.
#
from pydantic import BaseModel
from typing import List, Optional
import datetime

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime.datetime
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

class CartItem(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    class Config:
        orm_mode = True

class OrderItem(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    price: float  # Price at the time of order
    class Config:
        orm_mode = True

class Order(BaseModel):
    id: int
    user_id: int
    status: str
    total: float  # Total order amount
    created_at: datetime.datetime
    items: List[OrderItem] = []
    class Config:
        orm_mode = True

class WishlistItem(BaseModel):
    id: int
    user_id: int
    product_id: int
    class Config:
        orm_mode = True

class ChatHistory(BaseModel):
    id: int
    user_id: int
    message: str
    timestamp: datetime.datetime
    class Config:
        orm_mode = True

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: Optional[datetime.datetime] = None
    street_address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    email: str
    phone: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    created_at: datetime.datetime
    class Config:
        orm_mode = True
