from fastapi import APIRouter

from app.api.v1.chat import router as chat_router

api_router = APIRouter(prefix="/api")

api_router.include_router(
    chat_router,
    prefix="/v1",
    tags=["Chat"],
)