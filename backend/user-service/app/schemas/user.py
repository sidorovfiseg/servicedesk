from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    password: str
    is_verified: bool = False
    is_google_authenticated: bool = False


class UserCreate(UserBase):
    pass


class UserAuth(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    email: EmailStr


class UserUpdate(BaseModel):
    is_verified: Optional[bool] = None
    new_password: Optional[str] = None


class User(UserBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True
