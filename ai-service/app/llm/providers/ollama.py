from openai import OpenAI

from app.llm.models import LLMResponse
from app.llm.providers.base import BaseLLMProvider
from app.prompt.models import Prompt


class OllamaLLMProvider(BaseLLMProvider):

    def __init__(
        self,
        base_url: str,
        api_key: str,
    ):
        self.client = OpenAI(
            base_url=f"{base_url}/v1",
            api_key=api_key,
        )

    def generate(
        self,
        prompt: Prompt,
        model: str,
        temperature: float,
        top_p: float,
        max_tokens: int,
    ) -> LLMResponse:

        response = self.client.chat.completions.create(
            model=model,
            messages=[
                message.to_dict()
                for message in prompt.messages
            ],
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
        )

        return LLMResponse(
            content=response.choices[0].message.content,
            model=model,
        )

    def stream(self, prompt: Prompt):
        raise NotImplementedError(
            "Streaming is not implemented yet."
        )