from app.llm.models import ChatMessage
from app.prompt.models import Prompt


class PromptBuilder:

    def __init__(self):
        self._messages: list[ChatMessage] = []

    def system(self, content: str):
        self._messages.append(
            ChatMessage(
                role="system",
                content=content,
            )
        )
        return self

    def user(self, content: str):
        self._messages.append(
            ChatMessage(
                role="user",
                content=content,
            )
        )
        return self

    def assistant(self, content: str):
        self._messages.append(
            ChatMessage(
                role="assistant",
                content=content,
            )
        )
        return self

    def build(self) -> Prompt:
        return Prompt(messages=self._messages)