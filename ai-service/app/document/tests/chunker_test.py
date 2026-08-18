from pathlib import Path

from app.document.chunkers.factory import ChunkerFactory
from app.document.factory import DocumentFactory
from app.settings import get_settings

PROJECT_ROOT = Path(__file__).resolve().parents[3]

settings = get_settings()

url = f"{PROJECT_ROOT}/app/document/tests/sample/test.pdf"
reader = DocumentFactory.get_reader(Path(url))
text = reader.read(Path(url))

chunker = ChunkerFactory.get(
    strategy=settings.rag_chunk_strategy
)

chunks = chunker.split(text)

for chunk in chunks:
    print("=" * 80)
    print(chunk.index)
    print(chunk.text)