import tempfile
from pathlib import Path
from urllib.parse import urlparse

import fitz
import requests

from app.document.base import Reader
from app.document.models import DocumentPage


class PDFReader(Reader):

    def read(self, source: str | Path) -> str:

        path = self._resolve_path(source)

        pdf = fitz.open(path)

        pages = []

        for i, page in enumerate(pdf):
            pages.append(
                DocumentPage(
                    page=i + 1,
                    text=page.get_text(),
                )
            )

        pdf.close()

        return pages

    def _resolve_path(self, source: str | Path) -> Path:

        if isinstance(source, Path):
            return source

        parsed = urlparse(source)

        if parsed.scheme in ("http", "https"):
            response = requests.get(source, timeout=60)
            response.raise_for_status()

            with tempfile.NamedTemporaryFile(
                suffix=".pdf",
                delete=False,
            ) as temp_file:
                temp_file.write(response.content)
                return Path(temp_file.name)

        return Path(source)