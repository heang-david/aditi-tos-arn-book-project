from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from app.models.order import OrderStatus

class OrderItemCreate(BaseModel):
    book_id:  int
    quantity: int

class OrderCreate(BaseModel):
    customer_name: str
    email:         EmailStr
    phone:         str
    address:       str
    items:         List[OrderItemCreate]

class OrderItemOut(BaseModel):
    id:         int
    book_id:    int
    quantity:   int
    unit_price: float

    class Config:
        from_attributes = True

class OrderOut(BaseModel):
    id:            int
    customer_name: str
    email:         str
    phone:         str
    address:       str
    status:        OrderStatus
    total_price:   float
    created_at:    datetime
    items:         List[OrderItemOut]

    class Config:
        from_attributes = True

class OrderStatusUpdate(BaseModel):
    status: OrderStatus