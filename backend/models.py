from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class JournalEntry(Base):
	__tablename__ = "journal_entries"

	id = Column(Integer, primary_key=True, autoincrement=True)
	content = Column(Text, nullable=False)
	created_at = Column(DateTime, default=func.now(), server_default=func.now())  # ✅ Best of both worlds!

