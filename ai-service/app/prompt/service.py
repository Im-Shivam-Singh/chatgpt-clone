from app.prompt.builder import PromptBuilder
from app.prompt.models import Prompt
from app.prompt.templates import RAG_SYSTEM_PROMPT


class PromptService:

    @staticmethod
    def rag(
        question: str,
        context: list,
    ) -> Prompt:

        context_text = "\n\n".join(
            chunk.content for chunk in context
        )


        user_prompt = f"""
            Context:
            {context_text}

            Question:
            {question}

            Answer ONLY using the context above.
        """

        return (
            PromptBuilder()
            .system(RAG_SYSTEM_PROMPT)
            .user(user_prompt)
            .build()
        )