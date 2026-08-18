def main():
    from app.rag.service import RAGService
    rag = RAGService()

    response = rag.chat(
       question="who is alchemist?",
        model="gpt-oss:20b",
        temperature=0.2,
        top_k=10,
        top_p=0.9,
        max_tokens=500,
    )

    print(response.to_dict())

def test_search():
    from azure.core.credentials import AzureKeyCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.models import VectorizedQuery
    from sentence_transformers import SentenceTransformer

    from app.settings import get_settings

    settings = get_settings()

    print("=" * 80)
    print(f"Endpoint : {settings.azure_search_endpoint}")
    print(f"Index    : {settings.azure_search_index}")
    print(f"Key set? : {bool(settings.azure_search_key)}")
    print("=" * 80)

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    search_client = SearchClient(
        endpoint=settings.azure_search_endpoint,
        index_name=settings.azure_search_index,
        credential=AzureKeyCredential(settings.azure_search_key),
    )

    query = input("Enter query: ").strip()

    embedding = model.encode(query).tolist()

    print(f"\nEmbedding Dimension: {len(embedding)}")

    vector_query = VectorizedQuery(
        vector=embedding,
        fields="embedding",
        k_nearest_neighbors=5,
    )

    results = search_client.search(
        search_text=None,
        vector_queries=[vector_query],
        select=[
            "document_id",
            "chunk_index",
            "page",
            "content",
        ],
    )

    print("=" * 80)

    for i, doc in enumerate(results, start=1):
        print(f"Result #{i}")
        print(f"Score    : {doc['@search.score']:.4f}")
        print(f"Document : {doc['document_id']}")
        print(f"Chunk    : {doc['chunk_index']}")
        print(f"Page     : {doc['page']}")
        print("-" * 80)
        print(doc["content"][:500])
        print("=" * 80)

if __name__ == "__main__":
    import sys
    from pathlib import Path
    PROJECT_ROOT = Path(__file__).resolve().parents[3]
    sys.path.insert(0, str(PROJECT_ROOT))
    main()