"""
Weaviate client module.

This module defines a client for interacting with a Weaviate instance.
It provides functionality to send journal entry data to Weaviate for indexing.
"""

import os
import requests

class WeaviateClient:
    """
    Client for interacting with Weaviate.

    Attributes:
        BASE_URL (str): The base URL for the Weaviate instance.
    """
    BASE_URL = os.getenv("WEAVIATE_URL", "http://weaviate:8080")

    @classmethod
    def send_entry_to_weaviate(cls, entry_id: str, content: str):
        """
        Send a journal entry to Weaviate for indexing.

        Constructs a payload from the given journal entry data and sends a POST
        request to the Weaviate instance. Raises an exception if the request fails.

        Args:
            entry_id (str): The ID of the journal entry.
            content (str): The content of the journal entry.

        Returns:
            dict: The JSON response from the Weaviate instance.

        Raises:
            Exception: If there is an error sending the entry to Weaviate.
        """
        url = f"{cls.BASE_URL}/v1/objects"
        payload = {
            "class": "JournalEntry",
            "id": str(entry_id), # convert to str
            "properties": {
                "content": content
            }
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception("Error indexing journal entry: {e}")
