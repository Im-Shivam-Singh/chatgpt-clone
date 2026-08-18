import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))


from app.embeddings.service import EmbeddingService

service = EmbeddingService()

vector = service.embed(
    "Azure AI Search is awesome."
)

print(vector)