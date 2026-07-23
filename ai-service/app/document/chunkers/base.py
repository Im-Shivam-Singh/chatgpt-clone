from abc import ABC, abstractmethod
from .models import Chunk

class Chunker(ABC):
    
    @abstractmethod
    def split(self, text: str) -> list[Chunk]:
        pass