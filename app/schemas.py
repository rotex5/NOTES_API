from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime


class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class NoteResponse(NoteBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class NoteOut(BaseModel):
    Note: NoteResponse

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    phone_number: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token:str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
