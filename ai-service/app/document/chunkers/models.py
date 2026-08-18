from dataclasses import dataclass


@dataclass(slots=True)
class Chunk:
    index: int
    text: str
    page: int | None = None