"""
Journal service module.

This module defines a service function to create a new journal entry.
It handles creating the journal entry, saving it to the database, and indexing it into weaviate.
"""

from backend.models.journal import JournalEntry
from backend.services.indexer import index_journal_entry


def create_journal_entry(db_session, title: str, content: str):
    """
    Create a new journal entry and index it.

    This function creates a new JournalEntry instance adds it to the database session, 
    commits the transaction, and then triggers indexing of the journal entry via the 
    index_journal_entry function.

    Args:
        db_session: The database session used for adding the entry.
        title (str): The title of the journal entry.
        content (str): The content of the journal entry.

    Returns:
        JournalEntry: The created journal entry instance.
    """
    entry = JournalEntry(title=title, content=content) 
    db_session.add(entry)
    db_session.commit()
    db_session.refresh(entry)

    # Index entry into Weaviate with the uuid
    index_journal_entry(entry.id, entry.content)

    return entry
