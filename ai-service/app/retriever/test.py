from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from app.retriever.service import RetrieverService


retriever = RetrieverService()

results = retriever.retrieve(
    "What is ChatGPT?"
)

for result in results:
    print(result)