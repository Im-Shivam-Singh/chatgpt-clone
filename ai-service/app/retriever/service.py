from app.vectordb.service import VectorStoreService
from app.vectordb.models import RetrievedChunk

from app.embeddings.service import EmbeddingService 

class RetrieverService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store_service = VectorStoreService()

    def retrieve(
            self, 
            query: str, 
            k: int = 5
    ) -> list[RetrievedChunk]:
        embedding = self.embedding_service.embed(query)
        return self.vector_store_service.search(embedding, k)