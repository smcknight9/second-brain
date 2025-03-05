from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from backend.models import Base
from .database import get_db
from .models import JournalEntry


DATABASE_URL = "postgresql://user:password@db:5432/secondbrain"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.post("/add_entry/")
def add_entry(content: str, db: Session = Depends(get_db)):
    entry = JournalEntry(content=content)  # Create a new journal entry object
    db.add(entry)  # Add to the session
    db.commit()  # Commit to DB
    db.refresh(entry)  # Refresh object with DB-generated values
    return {"message": "Journal entry added!", "id": entry.id}

@app.get("/entries/")
def get_entries(db: Session = Depends(get_db)):
    entries = db.query(JournalEntry).all()
    return entries
