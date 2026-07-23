from pathlib import Path
import sys


def test_upload():
    from app.embeddings.service import EmbeddingService
    from app.vectordb.models import VectorDocument
    from app.vectordb.service import VectorStoreService
    embedding_service = EmbeddingService()
    vector_store = VectorStoreService()

    text = "ChatGPT is an AI assistant built by OpenAI."

    embedding = embedding_service.embed(text)

    document = VectorDocument(
        id="test-1",
        user_id="user-1",
        document_id="sample",
        chunk_index=0,
        page=1,
        content=text,
        embedding=embedding,
    )

    # vector_store.upsert([document])

    print("Upload completed.", document.to_dict())

def test_search():
    from app.embeddings.service import EmbeddingService
    from app.vectordb.service import VectorStoreService
    embedding_service = EmbeddingService()
    vector_store = VectorStoreService()

    text = "ChatGPT is an AI assistant built by OpenAI."

    embedding = embedding_service.embed(text)

    results = vector_store.search(embedding, k=5)

    print("Search completed.", results)


if __name__ == "__main__":
    PROJECT_ROOT = Path(__file__).resolve().parents[3]
    sys.path.insert(0, str(PROJECT_ROOT))
    test_search()
    