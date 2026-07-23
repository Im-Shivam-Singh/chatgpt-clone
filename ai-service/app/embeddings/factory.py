
from app.settings import get_settings


class EmbeddingFactory:

    @staticmethod
    def get_provider():
        settings = get_settings()
        provider = settings.embedding_provider

        match provider:
            case "huggingface":
                from app.embeddings.providers.huggingface import HuggingFaceProvider
                return HuggingFaceProvider(
                    model_name=settings.embedding_model
                )
            case _:
                raise ValueError(f"Unsupported embedding provider: {provider}")