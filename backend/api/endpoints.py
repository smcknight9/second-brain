"""
API endpoints for journal entries.

This module defines endpoints for creating and retrieving journal entries.
It leverages FastAPI for building the API, SQLAlchemy for database operations,
and background tasks to asynchronously send new entries for indexing.
"""

from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.journal import JournalEntry
from backend.schemas.journal import JournalEntryCreate
from backend.services.weaviate_client import WeaviateClient
from backend.services.journal_service import create_journal_entry

router = APIRouter()

@router.post("/add_entry/")
def add_entry(entry_data: JournalEntryCreate,
              background_tasks: BackgroundTasks,
              db_secondbrain: Session = Depends(get_db)):
    """
    Create a new journal entry and schedule its indexing.

    This endpoint creates a new journal entry in the database and schedules
    a background task to send the entry for indexing via Weaviate.

    Args:
        entry_data (JournalEntryCreate): Data containing title and content for the new entry.
        background_tasks (BackgroundTasks): Manager for scheduling background tasks.
        db_secondbrain (Session): SQLAlchemy session instance provided by dependency injection.

    Returns:
        dict: A dictionary with a success message and the new entry's ID.
    """
    entry = create_journal_entry(db_secondbrain, entry_data.title, entry_data.content)

    # Schedule the background task for Weaviate indexing.
    background_tasks.add_task(
        WeaviateClient.send_entry_to_weaviate, str(entry.id), entry.content
    )

    return {"message": "Journal entry added!", "id": entry.id}

@router.get("/entries/")
def get_entries(db_secondbrain: Session = Depends(get_db)):
    """
    Retrieve all journal entries.

    Args:
        db_secondbrain (Session): SQLAlchemy session instance provided by dependency injection.

    Returns:
        list: A list of all journal entries from the database.
    """
    return db_secondbrain.query(JournalEntry).all()

@router.get("/entries/{entry_id}/")
def get_entry(entry_id: str, db_secondbrain: Session = Depends(get_db)):
    """
    Retrieve a single journal entry by its UUID.
    """
    entry = db_secondbrain.query(JournalEntry).filter(JournalEntry.id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry
