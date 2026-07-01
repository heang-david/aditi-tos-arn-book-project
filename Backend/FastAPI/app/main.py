from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import books, orders, admin
from app.models import admin as _admin_model  # ensures table is created


# create all tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title       = "Tos arn Book Store API",
    description = "Backend API for Tos arn Book Store",
    version     = "1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins     = ["http://localhost:5173"],  # Vue dev server
    allow_credentials = True,
    allow_methods     = ["*"],
    allow_headers     = ["*"],
)

app.include_router(books.router,  prefix="/api/books",  tags=["Books"])
app.include_router(orders.router, prefix="/api/orders", tags=["Orders"])
app.include_router(admin.router,  prefix="/api/admin",  tags=["Admin"])

@app.on_event("startup")
def seed_default_admin():
    """Create a default admin account if none exists."""
    from app.database import SessionLocal
    from app.services.admin_service import get_by_username, create_admin
    from app.schemas.admin import AdminCreate
    db = SessionLocal()
    try:
        if not get_by_username(db, "admin"):
            create_admin(db, AdminCreate(username="admin", password="admin123"))
            print("✅ Default admin created  →  username: admin  |  password: admin123")
    finally:
        db.close()

@app.get("/")
def root():
    return { "message": "Tos arn Book Store API is running" }