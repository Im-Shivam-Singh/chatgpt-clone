from dataclasses import dataclass


@dataclass
class DocumentPage:
    page: int
    text: str