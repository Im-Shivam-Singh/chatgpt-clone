
def main():
    from app.llm.service import LLMService
    from app.prompt.service import PromptService

    llm_service = LLMService()

    prompt = PromptService.chat(
        question="Introduce yourself in one sentence."
    )

    print("========== PROMPT ==========")

    for message in prompt.messages:
        print(f"{message.role}: {message.content}")

    print("============================")

    response = llm_service.generate(prompt)

    print(response.to_dict())



if __name__ == "__main__":
    import sys
    from pathlib import Path
    PROJECT_ROOT = Path(__file__).resolve().parents[3]
    sys.path.insert(0, str(PROJECT_ROOT))
    main()