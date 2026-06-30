from app.database import SessionLocal

# reused across every router with Depends(get_db)
def get_db():
    db = SessionLocal()
    try:
        yield db
        print("CONNECTED TO DB")
    finally:
        db.close()
        print("DISCONNECTED TO DB")