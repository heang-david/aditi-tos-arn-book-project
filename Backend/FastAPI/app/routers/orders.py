from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.order import OrderCreate, OrderOut, OrderStatusUpdate
from app.services import order_service

router = APIRouter()

@router.post("/", response_model=OrderOut, status_code=201)
def create_order(data: OrderCreate, db: Session = Depends(get_db)):
    return order_service.create_order(db, data)

@router.get("/", response_model=list[OrderOut])
def get_orders(db: Session = Depends(get_db)):
    return order_service.fetch_all(db)

@router.get("/{order_id}", response_model=OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = order_service.fetch_by_id(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.patch("/{order_id}/status", response_model=OrderOut)
def update_order_status(
    order_id: int,
    data:     OrderStatusUpdate,
    db:       Session = Depends(get_db)
):
    order = order_service.update_status(db, order_id, data.status)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order