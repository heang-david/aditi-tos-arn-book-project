from sqlalchemy.orm import Session
from app.models.book import Book
from app.models.order import Order, OrderItem, OrderStatus
from app.schemas.order import OrderCreate
from typing import Optional
from fastapi import HTTPException

def create_order(db: Session, data: OrderCreate) -> Order:
    total = 0
    order_items = []

    for item in data.items:
        book = db.query(Book).filter(Book.id == item.book_id).first()
        if not book:
            raise HTTPException(
                status_code=404,
                detail=f"Book with id {item.book_id} not found"
            )
        if book.stock < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Not enough stock for '{book.title}'"
            )

        # snapshot the price at time of purchase
        total += book.price * item.quantity

        # deduct stock
        book.stock -= item.quantity

        order_items.append(OrderItem(
            book_id    = item.book_id,
            quantity   = item.quantity,
            unit_price = book.price,
        ))

    order = Order(
        customer_name = data.customer_name,
        email         = data.email,
        phone         = data.phone,
        address       = data.address,
        total_price   = round(total, 2),
        items         = order_items,
    )

    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def fetch_all(db: Session) -> list[Order]:
    return db.query(Order).all()

def fetch_by_id(db: Session, order_id: int) -> Optional[Order]:
    return db.query(Order).filter(Order.id == order_id).first()

def update_status(db: Session, order_id: int, status: OrderStatus) -> Optional[Order]:
    order = fetch_by_id(db, order_id)
    if not order:
        return None
    order.status = status
    db.commit()
    db.refresh(order)
    return order