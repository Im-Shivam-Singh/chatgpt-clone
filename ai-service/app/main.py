from fastapi import FastAPI

from app.api.router import api_router
from app.settings import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.name,
    version=settings.version,
)


app.include_router(api_router)