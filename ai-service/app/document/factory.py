from pathlib import Path
from urllib.parse import urlparse

from app.document.readers import PDFReader


class DocumentFactory:
    _READERS = {
        ".pdf": PDFReader,
    }

    @classmethod
    def get_reader(cls, file_path: str | Path):

        if isinstance(file_path, Path):
            extension = file_path.suffix.lower()

        else:
            parsed_url = urlparse(file_path)

            if parsed_url.scheme in ("http", "https"):
                extension = Path(parsed_url.path).suffix.lower()
            else:
                extension = Path(file_path).suffix.lower()

        reader_cls = cls._READERS.get(extension)

        if not reader_cls:
            raise ValueError(
                f"No reader registered for file extension: {extension}"
            )

        return reader_cls()