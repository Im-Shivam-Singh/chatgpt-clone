from sentence_transformers import SentenceTransformer

from app.embeddings.providers.base import BaseProvider
from app.settings import get_settings


class HuggingFaceProvider(BaseProvider):

    _models: dict[str, SentenceTransformer] = {}

    def __init__(self, model_name: str):
        self.settings = get_settings()
        if model_name not in self._models:
            print(f"Loading model: {model_name}")
            self._models[model_name] = SentenceTransformer(model_name)

        self.model = self._models[model_name]

    def embed(self, text: str) -> list[float]:
        return self.model.encode(
            text,
            normalize_embeddings=True,
            convert_to_numpy=True,
        ).tolist()

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        return self.model.encode(
            texts,
            batch_size=self.settings.embedding_batch_size,
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=True,
        ).tolist()