from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@secondbrain_db:5432/secondbrain_db"

    class Config:
        env_file = "../../../.env"


settings = Settings()
