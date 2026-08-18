import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

def read_files():
    from app.document.factory import DocumentFactory
    files = ["sample/test.pdf"]
    for file in files:
        full = f'{PROJECT_ROOT}/app/document/tests/{file}'
        reader_cls = DocumentFactory.get_reader(full)
        print(reader_cls.read(full))

def ingestion_file():
    from app.document.service import IngestionService
    service = IngestionService()

    count = service.ingest("https://icrrd.com/public/media/15-05-2021-084550The-Alchemist-Paulo-Coelho.pdf")

    print(f"Ingested {count} chunks")


def test_create_index():
    from app.settings import get_settings
    from app.vectordb.providers.azure_ai_search import AzureAISearchVectorStore


    settings = get_settings()

    vector_store = AzureAISearchVectorStore(
        endpoint=settings.azure_search_endpoint,
        key=settings.azure_search_key,
        index_name=settings.azure_search_index,
    )

    print("=" * 80)
    print(f"Endpoint : {settings.azure_search_endpoint}")
    print(f"Index    : {settings.azure_search_index}")
    print(f"Embedding Dimension : {settings.embedding_dimension}")
    print("=" * 80)

    # Deletes existing index and creates a new one
    vector_store.create_index(recreate=True)

    print("\n✅ Index recreated successfully.")


if __name__ == "__main__":
    ingestion_file()
    # test_create_index()