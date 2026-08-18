from app.llm.models import ChatMessage
from app.llm.service import LLMService


def main():
    service = LLMService()

    messages = [
        ChatMessage(
            role="system",
            content="You are a helpful assistant."
        ),
        ChatMessage(
            role="user",
            content="Introduce yourself in one sentence."
        ),
    ]

    response = service.generate(messages)

    print(response.to_dict())


if __name__ == "__main__":
    import sys
    from pathlib import Path
    PROJECT_ROOT = Path(__file__).resolve().parents[3]
    sys.path.insert(0, str(PROJECT_ROOT))
    main()