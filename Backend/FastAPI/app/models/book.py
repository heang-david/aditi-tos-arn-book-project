from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Book(Base):
    __tablename__ = "books"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String, nullable=False)
    author      = Column(String)
    description = Column(String)
    price       = Column(Float)
    image_url   = Column(String)
    genre       = Column(String)
    stock       = Column(Integer, default=0)