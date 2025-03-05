from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.journal import JournalEntry

router = APIRouter()

@router.post("/add_entry/")
def add_entry(content: str, db: Session = Depends(get_db)):
    entry = JournalEntry(content=content)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return {"message": "Journal entry added!", "id": entry.id}

@router.get("/entries/")
def get_entries(db: Session = Depends(get_db)):
    return db.query(JournalEntry).all()

