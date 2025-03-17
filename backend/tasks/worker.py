"""
Worker module for sending journal entries to Weaviate.

This module defines a function to send a journal entry to a Weaviate instance.
It uses the WeaviateClient to create an entry and logs an error if the operation fails.
"""

import logging
from services.weaviate_client import WeaviateClient

logger = logging.getLogger(__name__)

def send_entry_to_weaviate(entry_id: int, content: str):
    """
    Send a journal entry to Weaviate.

    This function attempts to create a new entry in Weaviate using the provided
    entry_id and content. In case of an error during the process, it logs the error.

    Args:
        entry_id (int): The ID of the journal entry.
        content (str): The content of the journal entry.

    Returns:
        None
    """
    try:
        weaviate_client = WeaviateClient()
        weaviate_client.create_entry(id=str(entry_id), content=content)
    except Exception as excep:  # Consider catching more specific exceptions
        logger.error("Error sending entry to Weaviate: %s", excep)
