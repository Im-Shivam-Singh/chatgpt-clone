from dataclasses import dataclass, field
from typing import Any

@dataclass(slots=True)
class Chunk:
    index: int
    text: str