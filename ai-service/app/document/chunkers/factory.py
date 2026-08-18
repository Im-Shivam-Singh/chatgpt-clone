from app.document.chunkers.fixed import FixedChunker
from app.settings import get_settings


class ChunkerFactory:

    RAG_FIXED_CHUNKING = "fixed"

    @classmethod
    def get(cls, strategy: str):
        settings = get_settings()
        match strategy:
            case cls.RAG_FIXED_CHUNKING:
                return FixedChunker(
                    chunk_size=settings.rag_chunk_size,
                    chunk_overlap=settings.rag_chunk_overlap
                )
            case _:
                raise ValueError(f"Unknown chunking strategy: {strategy}")