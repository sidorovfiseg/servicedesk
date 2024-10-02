
from abc import ABC, abstractmethod

class BaseTokenizer(ABC):
    @abstractmethod
    def encode(self, text: str) -> list[str]:
        pass

    @abstractmethod
    def decode(self, token_ids: list[str]) -> str:
        pass

    @abstractmethod
    def length(self, text: str) -> int:
        pass
