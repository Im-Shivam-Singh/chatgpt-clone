from dataclasses import dataclass, asdict


@dataclass(slots=True)
class VectorDocument:
    id: str
    user_id: str
    document_id: str
    chunk_index: int
    page: int
    content: str
    embedding: list[float]
    score: float | None = None

    def to_dict(self) -> dict:
        data = asdict(self)
        if self.score is None:
            data.pop("score")
        return data
    

@dataclass(slots=True)
class RetrievedChunk:
    content: str
    page: int
    document_id: str
    score: float

    def to_dict(self) -> dict:
        return asdict(self)