"""
Indexer module for journal entries.

This module provides a function to index a journal entry by sending it to
a Weaviate instance. It includes retry logic to handle transient failures.
"""

import time
import logging
from requests.exceptions import RequestException
from .weaviate_client import WeaviateClient



logger = logging.getLogger(__name__)

def index_journal_entry(entry_id: str, content: str, retries=3, delay=2):
    """
    Index a journal entry into Weaviate with retry logic.

    This function attempts to send the journal entry to Weaviate for indexing.
    If the request fails due to a RequestException, it will retry up to a
    specified number of times, waiting longer between each attempt.

    Args:
        entry_id (str): The ID of the journal entry.
        content (str): The content of the journal entry.
        retries (int, optional): Number of retries in case of failure. Defaults to 3.
        delay (int, optional): Delay (in seconds) between retries. Defaults to 2.

    Returns:
        None

    Side Effects:
        Logs information about success or failure.
    """
    for attempt in range(retries):
        try:
            WeaviateClient().send_entry_to_weaviate(entry_id, content)
            logger.info("Successfully indexed entry %s", entry_id)
            return
        except RequestException as req_exec:
            logger.warning("Weaviate indexing attempt %d failed: %s", attempt + 1, req_exec)
            time.sleep(delay ** attempt)
    logger.error("Failed to index journal entry %s after %d attempts.", entry_id, retries)
