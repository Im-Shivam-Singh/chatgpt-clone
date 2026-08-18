from app.embeddings.service import EmbeddingService
from app.vectordb.service import VectorStoreService


class RetrieverService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store_service = VectorStoreService()

    def retrieve(
        self,
        query: str,
        embedding: list[float],
        top_k: int = 5,
    ):
        return self.vector_store_service.search(
            query,
            embedding,
            top_k,
        )