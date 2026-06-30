from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title:       str
    author:      Optional[str] = None
    description: Optional[str] = None
    price:       Optional[float] = None
    image_url:   Optional[str] = None
    genre:       Optional[str] = None
    stock:       Optional[int] = 0

class BookCreate(BookBase):
    title: str  # required on create

class BookUpdate(BaseModel):
    title:       Optional[str] = None
    author:      Optional[str] = None
    description: Optional[str] = None
    price:       Optional[float] = None
    image_url:   Optional[str] = None
    genre:       Optional[str] = None
    stock:       Optional[int] = None

class BookOut(BookBase):
    id: int

    class Config:
        from_attributes = True