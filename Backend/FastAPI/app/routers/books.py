from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.dependencies import get_db
from app.schemas.book import BookCreate, BookUpdate, BookOut
from app.services import book_service

router = APIRouter()

@router.get("/", response_model=list[BookOut])
def get_books(
    genre: Optional[str] = Query(None, description="Filter by genre"),
    db:    Session = Depends(get_db)
):
    return book_service.fetch_all(db, genre=genre)

@router.get("/{book_id}", response_model=BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = book_service.fetch_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=BookOut, status_code=201)
def create_book(data: BookCreate, db: Session = Depends(get_db)):
    return book_service.create(db, data)

@router.patch("/{book_id}", response_model=BookOut)
def update_book(book_id: int, data: BookUpdate, db: Session = Depends(get_db)):
    book = book_service.update(db, book_id, data)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted = book_service.delete(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")