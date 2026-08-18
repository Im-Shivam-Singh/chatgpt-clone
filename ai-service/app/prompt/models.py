from dataclasses import dataclass

from app.llm.models import ChatMessage


@dataclass(slots=True)
class Prompt:
    messages: list[ChatMessage]