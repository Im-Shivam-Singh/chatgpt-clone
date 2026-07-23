
from abc import ABC, abstractmethod
from pathlib import Path


class Reader(ABC):

    @abstractmethod
    def read(self, file_path: Path):
        pass