from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Application
    name: str = "Chat Service"
    version: str = "0.1.0"

    # Server
    env: str = "DEV"
    host: str = "0.0.0.0"
    port: int = 8001

    # Azure Blob Storage
    azure_storage_account_name: str
    azure_storage_account_key: str
    azure_storage_container_name: str
    azure_storage_connection_string: str

    # AI Service
    ai_service_url: str


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()