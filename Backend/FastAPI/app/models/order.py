from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import enum

class OrderStatus(str, enum.Enum):
    pending   = "pending"
    confirmed = "confirmed"
    shipped   = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"

class Order(Base):
    __tablename__ = "orders"

    id            = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    email         = Column(String, nullable=False)
    phone         = Column(String, nullable=False)
    address       = Column(String)
    status        = Column(Enum(OrderStatus), default=OrderStatus.pending)
    total_price   = Column(Float, nullable=False)
    created_at    = Column(DateTime, default=datetime.utcnow)

    # one order → many order items
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_items"

    id         = Column(Integer, primary_key=True, index=True)
    order_id   = Column(Integer, ForeignKey("orders.id"),  nullable=False)
    book_id    = Column(Integer, ForeignKey("books.id"),   nullable=False)
    quantity   = Column(Integer, nullable=False, default=1)
    unit_price = Column(Float,   nullable=False)

    order = relationship("Order", back_populates="items")
    book  = relationship("Book")