from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AdminLogin(BaseModel):
    username: str
    password: str

class AdminCreate(BaseModel):
    username: str
    password: str

class AdminOut(BaseModel):
    id:         int
    username:   str
    is_active:  bool
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type:   str = "bearer"
    expires_in:   int  # seconds
