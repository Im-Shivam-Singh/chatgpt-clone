from app.settings import get_settings


class LLMFactory:

    @staticmethod
    def get_provider():
        settings = get_settings()

        match settings.llm_provider:
            case "ollama":
                from app.llm.providers.ollama import OllamaLLMProvider

                return OllamaLLMProvider(
                    base_url=settings.ollama_base_url,
                    api_key=settings.ollama_api_key,
                )
            case "github":
                from app.llm.providers.github import GithubLLMProvider

                return GithubLLMProvider(
                    token=settings.model_token,
                    model=settings.llm_model,
                )

            case _:
                raise ValueError(
                    f"Unsupported provider: {settings.llm_provider}"
                )