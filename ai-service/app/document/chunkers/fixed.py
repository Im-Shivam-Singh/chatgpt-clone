from app.document.chunkers.base import Chunker
from app.document.chunkers.models import Chunk
from app.document.models import DocumentPage


class FixedChunker(Chunker):

    def __init__(
        self,
        chunk_size: int,
        chunk_overlap: int,
    ) -> None:
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, pages: list[DocumentPage]) -> list[Chunk]:

        chunks: list[Chunk] = []
        index = 0

        for page in pages:

            start = 0

            while start < len(page.text):

                end = start + self.chunk_size

                chunks.append(
                    Chunk(
                        index=index,
                        page=page.page,
                        text=page.text[start:end],
                    )
                )

                start += self.chunk_size - self.chunk_overlap
                index += 1

        return chunks