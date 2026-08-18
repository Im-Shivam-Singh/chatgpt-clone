from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

from app.llm.models import ChatMessage, LLMResponse
from app.llm.providers.base import BaseLLMProvider


class GithubLLMProvider(BaseLLMProvider):

    def __init__(
        self,
        token: str,
        model: str,
    ):
        self.model = model

        self.client = ChatCompletionsClient(
            endpoint="https://models.github.ai/inference",
            credential=AzureKeyCredential(token),
        )
    
    def generate(
        self,
        messages: list[ChatMessage]
    ) -> LLMResponse:

        response = self.client.complete(
            model=self.model,
            messages=[message.to_dict() for message in messages],
            temperature=0.2,
            top_p=1.0,
        )

        return LLMResponse(
            content=response.choices[0].message.content,
            model=self.model,
        )

    def stream(
        self,
        messages: list[ChatMessage],
    ):
        raise NotImplementedError("Streaming is not implemented yet.")