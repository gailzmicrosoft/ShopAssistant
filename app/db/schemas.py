# Pydantic schemas for API requests and responses
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
    class Config:
        orm_mode = True

class Order(BaseModel):
    id: int
    user_id: int
    status: str
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
