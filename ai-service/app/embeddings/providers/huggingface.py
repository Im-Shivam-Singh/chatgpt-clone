from typing import List
from sentence_transformers import SentenceTransformer


from app.embeddings.providers.base import BaseProvider


class HuggingFaceProvider(BaseProvider):
    """
    HuggingFace embedding provider.
    """

    def __init__(self, model_name: str):
        print(f"Loading model: {model_name}")
        self.model = SentenceTransformer(model_name)

    def embed(self, text: str) -> List[float]:
        vector = self.model.encode(
            text,
            normalize_embeddings=True
        )
        return vector.tolist()

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        vectors = self.model.encode(
            texts,
            batch_size=32,
            normalize_embeddings=True
        )
        return vectors.tolist()