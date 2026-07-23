from dataclasses import dataclass


@dataclass(slots=True)
class Embedding:
    text: str
    vector: list[float]