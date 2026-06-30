from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate
from typing import Optional

def fetch_all(db: Session, genre: Optional[str] = None) -> list[Book]:
    query = db.query(Book)
    if genre:
        query = query.filter(Book.genre == genre)
    return query.all()

def fetch_by_id(db: Session, book_id: int) -> Optional[Book]:
    return db.query(Book).filter(Book.id == book_id).first()

def create(db: Session, data: BookCreate) -> Book:
    book = Book(**data.model_dump())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def update(db: Session, book_id: int, data: BookUpdate) -> Optional[Book]:
    book = fetch_by_id(db, book_id)
    if not book:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(book, field, value)
    db.commit()
    db.refresh(book)
    return book

def delete(db: Session, book_id: int) -> bool:
    book = fetch_by_id(db, book_id)
    if not book:
        return False
    db.delete(book)
    db.commit()
    return True