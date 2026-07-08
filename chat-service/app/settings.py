from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    name: str = "Chat Service"
    version: str = "0.1.0"
    
    env: str = "DEV"
    port: int = 8001
    mongodb_uri: str
    ai_agent_url: str


@lru_cache
def get_settings() -> Settings:
    return Settings()