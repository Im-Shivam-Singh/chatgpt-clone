
from app.settings import get_settings


class VectorStoreFactory:

    @staticmethod
    def get_provider():
        settings = get_settings()
        match settings.vector_store_provider:
            case "azure":
                from app.vectordb.providers import AzureAISearchVectorStore
                return AzureAISearchVectorStore(
                    endpoint=settings.azure_search_endpoint,
                    key=settings.azure_search_key,
                    index_name=settings.azure_search_index,
                )  
            case _:
                raise ValueError(f"Unsupported vector store provider: {settings.vector_store_provider}")