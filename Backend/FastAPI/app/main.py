from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import books, orders


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

@app.get("/")
def root():
    return { "message": "Tos arn Book Store API is running" }