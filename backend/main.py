from fastapi import FastAPI
from backend.database import engine, get_db, Base
from backend.api.endpoints import router
from backend.core.config import settings

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(router)
