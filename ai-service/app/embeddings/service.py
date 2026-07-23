from app.embeddings.factory import EmbeddingFactory


class EmbeddingService:
    def __init__(self):
        self.provider = EmbeddingFactory.get_provider()

    def embed(self, text: str):
        return self.provider.embed(text)

    def embed_batch(self, texts: list[str]):
        return self.provider.embed_batch(texts)
