from pydantic import BaseModel

class JournalEntryCreate(BaseModel):
    title: str
    content: str