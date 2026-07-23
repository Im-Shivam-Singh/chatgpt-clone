from pathlib import Path
from app.document.readers import PDFReader

class DocumentFactory:
    _READERS = {
        ".pdf": PDFReader,
    }

    @classmethod
    def get_reader(cls, file_path: str):
        extension = Path(file_path).suffix.lower()
        reader_cls = cls._READERS.get(extension)
        if not reader_cls:
            raise ValueError(f"No reader registered for file extension: {extension}")
        return reader_cls()