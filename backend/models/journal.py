"""
Journal model.

This module defines the JournalEntry class, an ORM model for storing
journal entries in the database. Each journal entry includes an auto-incremented
ID, title, content, and a timestamp indicating when the entry was created.
"""

import uuid
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from .base import Base

class JournalEntry(Base):
    """
    ORM model for a journal entry.
    Attributes:
	    id (int): Primary key, auto-incremented.
	    content (str): The textual content of the journal entry.
	    title (str): The title of the journal entry.
	    created_at (datetime): The timestamp when the entry was created.
    """
    __tablename__ = "journal_entries"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    content = Column(Text, nullable=False)
    title = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now(), server_default=func.now())
