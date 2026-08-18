from app.api.router import api_router
from app.settings import get_settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

settings = get_settings()

app = FastAPI(
    title=settings.name,
    version=settings.version,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://zany-memory-956jrjjjj772jvw-3000.app.github.dev",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)