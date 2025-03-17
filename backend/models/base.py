"""
Base module for SQLAlchemy models.

This module creates a declarative base class that all ORM model classes
should inherit from. The Base object stores metadata about all models,
which is later used to generate database tables.
"""

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
