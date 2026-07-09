from fastapi import APIRouter

from app.api.schemas import ChatRequest, ChatResponse

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    print(request)

    return ChatResponse(
        reply="Hello from Internal Chat Service"
    )


@router.get("/{id}")
async def get_chat(id: str):
    return {"message": f"Chat Fetched {id}"}