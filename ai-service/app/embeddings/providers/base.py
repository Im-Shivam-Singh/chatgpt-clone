from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Base class for embedding providers.
    """

    @abstractmethod
    def embed(self, text: str) -> list[float]:
        """
        Generate embeddings for the given text.

        Args:
            text (str): The input text to generate embeddings for.
        """
        pass

    @abstractmethod
    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """
        Generate embeddings for a batch of texts.

        Args:
            texts (List[str]): A list of input texts to generate embeddings for.
        """
        pass