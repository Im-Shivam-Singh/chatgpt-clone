from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    name: str = "AI Service"
    version: str = "0.1.0"
    
    env: str = "DEV"
    port: int = 8002
    mongodb_uri: str

    rag_chunk_strategy: str = "fixed"
    rag_chunk_size: int = 1000
    rag_chunk_overlap: int = 200

    embedding_provider: str = "huggingface"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    embedding_batch_size: int = 32

    vector_store_provider: str = "azure"
    azure_search_endpoint: str
    azure_search_key: str
    azure_search_index: str = "documents"
    embedding_dimension: int = 384
    
    llm_provider: str = "ollama"
    llm_model: str = "qwen3:4b"
    llm_temperature: float = 0.2
    llm_top_p: float = 1.0
    
    ollama_base_url: str
    ollama_api_key: str


@lru_cache
def get_settings() -> Settings:
    return Settings()