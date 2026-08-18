from app.document.service import IngestionService
from app.embeddings.service import EmbeddingService
from app.llm.models import LLMResponse
from app.llm.service import LLMService
from app.prompt.service import PromptService
from app.retriever.service import RetrieverService


class RAGService:

    def __init__(self):
        self.ingestion_service = IngestionService()
        self.embedding_service = EmbeddingService()
        self.retriever_service = RetrieverService()
        self.prompt_service = PromptService()
        self.llm_service = LLMService()

    def chat(
        self,
        question: str,
        model: str,
        top_k: int,
        temperature: float,
        max_tokens: int,
        top_p: float,
    ) -> LLMResponse:
        """
        End-to-end RAG pipeline.

        Flow:
            Question
                ↓
            Embed Query
                ↓
            Retrieve Context
                ↓
            Build Prompt
                ↓
            Generate Answer
        """

        # Step 1: Embed the user query
        embedding = self.embedding_service.embed(question)

        # Step 2: Retrieve relevant chunks
        chunks = self.retriever_service.retrieve(
            query=question,
            embedding=embedding,
            top_k=top_k,
        )

        
        # Step 3: Build the RAG prompt
        prompt = self.prompt_service.rag(
            question=question,
            context=chunks,
        )

        import re
        from datetime import datetime
        from pathlib import Path


        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        log_dir = Path("rag_logs") / timestamp
        log_dir.mkdir(parents=True, exist_ok=True)

        # Convert question into a safe filename
        filename = re.sub(r'[<>:"/\\|?*]', '', question)
        filename = filename.strip()

        # Prevent excessively long filenames
        filename = filename[:150]

        log_file = log_dir / f"{filename}.txt"

        with open(log_file, "w", encoding="utf-8") as f:
            f.write("=" * 100 + "\n")
            f.write(f"Query: {question}\n")
            f.write(f"Timestamp: {timestamp}\n")
            f.write("=" * 100 + "\n\n")

            for i, chunk in enumerate(chunks, start=1):
                f.write(f"Result #{i}\n")
                f.write(f"Score       : {chunk.score:.4f}\n")
                f.write(f"Document ID : {chunk.document_id}\n")
                f.write(f"Page        : {chunk.page}\n")
                f.write("-" * 100 + "\n")
                f.write(chunk.content)
                f.write("\n\n" + "=" * 100 + "\n\n")

            f.write("=" * 100 + "\n")

        print(f"Debug log written to: {log_file.resolve()}")

        # Step 4: Generate the final answer
        return self.llm_service.generate(
            prompt=prompt,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p
        )