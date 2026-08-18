from dataclasses import dataclass


@dataclass(slots=True)
class LLMResponse:
    content: str
    model: str

    def to_dict(self):
        return {
            "content": self.content,
            "model": self.model,
        }

@dataclass(slots=True)
class ChatMessage:
    role: str
    content: str

    def to_dict(self):
        return {
            "role": self.role,
            "content": self.content,
        }