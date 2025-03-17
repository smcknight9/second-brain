"""
Main application entry point.

This module initializes the FastAPI application, configures the database,
and includes API endpoints. During the startup event, the module creates
all the necessary database tables as defined by the SQLAlchemy models.

Modules:
    - backend.database: Provides the SQLAlchemy engine and Base for model metadata.
    - backend.api.endpoints: Contains the API endpoint routes.
    - backend.core.config: Application configuration settings.
    - backend.models.journal: Defines the journal model used in the application.
"""

from fastapi import FastAPI
from backend.database import engine
from backend.models import Base
from backend.api.endpoints import router

app = FastAPI()

@app.on_event("startup")
def startup():
    """
    Startup event handler for FastAPI.

    This function is executed when the FastAPI application starts. It creates
    all the database tables defined in the SQLAlchemy models by invoking
    `Base.metadata.create_all(bind=engine)`.
    """
    Base.metadata.create_all(bind=engine)

app.include_router(router)
