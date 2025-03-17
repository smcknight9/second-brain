"""
Schemas for journal entries.

This module defines the data models for journal entry operations.
"""

from pydantic import BaseModel

class JournalEntryCreate(BaseModel):
    """
    Schema for creating a new journal entry.

    Attributes:
        title (str): The title of the journal entry.
        content (str): The content of the journal entry.
    """
    title: str
    content: str
