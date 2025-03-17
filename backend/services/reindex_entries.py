import requests
import os

# Use your environment variables or hard-code for testing
SECOND_BRAIN_API = "http://localhost:8000"
WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://localhost:8080")

def fetch_all_entries():
    """Fetch all journal entries from Second Brain."""
    url = f"{SECOND_BRAIN_API}/entries/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def index_entry_in_weaviate(entry_id: str, content: str):
    """
    Send the entry content to Weaviate for vectorization and indexing.
    Adjust the payload format as needed by your Weaviate client.
    """
    # Depending on your indexing implementation, this could be a POST to your custom endpoint,
    # or using the Weaviate REST API for objects.
    # For example, let's assume you use Weaviate's v1/objects endpoint:
    url = f"{WEAVIATE_URL}/v1/objects"
    
    # Build the payload. Here we assume your JournalEntry class only has the 'content' field.
    payload = {
        "class": "JournalEntry",
        "properties": {
            "content": content
        }
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    print(f"Indexed entry {entry_id}: {response.json()}")

def reindex_all_entries():
    """Fetch all entries and re-index them in Weaviate."""
    entries = fetch_all_entries()
    print(f"Found {len(entries)} entries to re-index.")
    for entry in entries:
        entry_id = entry.get("id")
        content = entry.get("content")
        if entry_id and content:
            try:
                index_entry_in_weaviate(entry_id, content)
            except Exception as e:
                print(f"Failed to index entry {entry_id}: {e}")

if __name__ == "__main__": #TODO change this in the future when weaviate is persistant 
    reindex_all_entries()
