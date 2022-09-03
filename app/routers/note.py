from typing import List
from .. import models, schemas
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. database import get_db

router = APIRouter(
    prefix="/notes",
    tags=["notes"]
)


@router.get("/", response_model=List[schemas.NoteResponse])
def get_notes(db: Session = Depends(get_db)):
    
    notes = db.query(models.Note).all()
    
    return notes


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.NoteResponse)
def create_notes(note : schemas.NoteCreate, db: Session = Depends(get_db)):

    new_note = models.Note(**note.dict())

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note

@router.get("/{id}", response_model=schemas.NoteResponse)
def get_post(id: int, db: Session = Depends(get_db)):

    note = db.query(models.Note).filter(models.Note.id == id).first()

    if not note:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"note with id: {id} was not found")

    return note

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(id: int, db: Session = Depends(get_db)):

    note_query = db.query(models.Note).filter(models.Note.id == id)

    note = note_query.first()

    if note == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id: {id} does not exist")
    
    note_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.NoteResponse)
def update_note(id: int, updated_note: schemas.NoteCreate, db: Session = Depends(get_db)):

    note_query = db.query(models.Note).filter(models.Note.id == id)

    note = note_query.first()

    if note == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    note_query.update(updated_note.dict(), synchronize_session=False)

    db.commit()

    return note_query.first()
