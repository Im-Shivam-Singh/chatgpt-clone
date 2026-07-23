from abc import ABC, abstractmethod

from app.vectordb.models import VectorDocument


class BaseVectorStore(ABC):

    @abstractmethod
    def create_index(self) -> None:
        """Create the vector index if it does not exist."""
        raise NotImplementedError

    @abstractmethod
    def upsert(self, documents: list[VectorDocument]) -> None:
        """Insert or update vector documents."""
        raise NotImplementedError

    @abstractmethod
    def search(
        self,
        embedding: list[float],
        top_k: int = 5,
    ) -> list[VectorDocument]:
        """Return the nearest vector documents."""
        raise NotImplementedError