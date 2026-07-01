from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import Optional

from passlib.context import CryptContext
from jose import JWTError, jwt

from app.models.admin import Admin
from app.schemas.admin import AdminCreate
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ── Password helpers ────────────────────────────────────────────────────────

def hash_password(plain: str) -> str:
    return pwd_context.hash(plain)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


# ── CRUD ───────────────────────────────────────────────────────────────────

def get_by_username(db: Session, username: str) -> Optional[Admin]:
    return db.query(Admin).filter(Admin.username == username).first()

def get_all(db: Session) -> list[Admin]:
    return db.query(Admin).all()

def create_admin(db: Session, data: AdminCreate) -> Admin:
    admin = Admin(
        username        = data.username,
        hashed_password = hash_password(data.password),
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin

def authenticate(db: Session, username: str, password: str) -> Optional[Admin]:
    admin = get_by_username(db, username)
    if not admin or not admin.is_active:
        return None
    if not verify_password(password, admin.hashed_password):
        return None
    return admin


# ── JWT ────────────────────────────────────────────────────────────────────

def create_access_token(subject: str) -> str:
    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_token(token: str) -> Optional[str]:
    """Returns the username (sub) or None if invalid/expired."""
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        return payload.get("sub")
    except JWTError:
        return None
