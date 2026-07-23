from app.document.chunkers.base import Chunker
from app.document.chunkers.models import Chunk


class FixedChunker(Chunker):

    def __init__(
        self,
        chunk_size: int,
        chunk_overlap: int,
    ) -> None:
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, text: str) -> list[Chunk]:

        chunks: list[Chunk] = []

        start = 0
        index = 0

        while start < len(text):

            end = start + self.chunk_size

            chunks.append(
                Chunk(
                    index=index,
                    text=text[start:end],
                )
            )

            start += self.chunk_size - self.chunk_overlap
            index += 1

        return chunks