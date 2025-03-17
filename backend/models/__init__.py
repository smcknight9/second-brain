"""
Models package.

This package contains all ORM models for the application. It re-exports
the Base declarative class and the JournalEntry model for easy import.
"""

from .base import Base
from .journal import JournalEntry

__all__ = ["Base", "JournalEntry"]
