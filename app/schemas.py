from pydantic import BaseModel
from datetime import datetime


class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteResponse(NoteBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class NoteOut(BaseModel):
    Note: NoteResponse

    class Config:
        orm_mode = True
