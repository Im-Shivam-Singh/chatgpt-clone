import fitz
from pathlib import Path

from app.document.base import Reader

class PDFReader(Reader):

    def read(self, file_path: Path):
        pdf = fitz.open(file_path)
        pages = []
        for page in pdf:
            pages.append(page.get_text())
        pdf.close()
        return "\n".join(pages)