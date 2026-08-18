from .base import BaseLLMProvider


class AzureOpenAIProvider(BaseLLMProvider):

    def generate(self, prompt):
        ...