"""
Configuration module.

This module defines application settings using Pydantic's BaseSettings.
The settings are loaded from environment variables and/or a .env file.
"""

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.

    Attributes:
        DATABASE_URL (str): The database connection URL.
    """
    DATABASE_URL: str = "postgresql://user:password@secondbrain:5432/secondbrain"

    class Config:
        """
        Pydantic configuration for Settings.

        Specifies the .env file to load environment variables from.
        """
        env_file = "../../../.env"

settings = Settings()
