from fastapi import APIRouter

from app.rag.service import RAGService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("")
async def chat(request: dict):

    print("AI REQUEST:", request)

    question = request["question"]
    model = request["model"]
    top_k = request["top_k"]
    temperature = request["temperature"]
    top_p = request["top_p"]
    max_tokens = request["max_tokens"]

    rag = RAGService()

    for file in request.get("files", []):
        rag.ingestion_service.ingest(file.get("sas_url"))

    response = rag.chat(
        question=question,
        model=model,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        max_tokens=max_tokens,
    )

    return {
        "response": response.content,
        "model": response.model
    }


@router.get("/{id}")
async def get_chat(id: str):
    return {
        "message": f"Chat Fetched {id}"
    }