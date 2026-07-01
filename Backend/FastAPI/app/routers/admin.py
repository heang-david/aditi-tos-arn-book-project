from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.admin import AdminLogin, AdminCreate, AdminOut, Token
from app.services import admin_service
from app.config import settings

router  = APIRouter()
bearer  = HTTPBearer()


# ── Auth dependency ────────────────────────────────────────────────────────

def require_admin(
    credentials: HTTPAuthorizationCredentials = Depends(bearer),
    db: Session = Depends(get_db),
):
    token    = credentials.credentials
    username = admin_service.decode_token(token)
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
    admin = admin_service.get_by_username(db, username)
    if not admin or not admin.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Admin not found")
    return admin


# ── Routes ─────────────────────────────────────────────────────────────────

@router.post("/login", response_model=Token)
def login(data: AdminLogin, db: Session = Depends(get_db)):
    admin = admin_service.authenticate(db, data.username, data.password)
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    token = admin_service.create_access_token(subject=admin.username)
    return Token(
        access_token=token,
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )


@router.post("/", response_model=AdminOut, status_code=201)
def create_admin(
    data: AdminCreate,
    db:   Session = Depends(get_db),
    _:    object  = Depends(require_admin),   # must be logged in to create admins
):
    if admin_service.get_by_username(db, data.username):
        raise HTTPException(status_code=400, detail="Username already taken")
    return admin_service.create_admin(db, data)


@router.get("/users", response_model=list[AdminOut])
def list_admins(
    db: Session = Depends(get_db),
    _:  object  = Depends(require_admin),
):
    return admin_service.get_all(db)


@router.get("/me", response_model=AdminOut)
def me(current_admin=Depends(require_admin)):
    return current_admin
