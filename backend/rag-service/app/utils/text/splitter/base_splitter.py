from abc import ABC, abstractmethod

class TextSplitter(ABC):
    def __init__(self, chunk_overlap: int, tokens_per_chunk: int):
        self.chunk_overlap = chunk_overlap
        self.tokens_per_chunk = tokens_per_chunk

    @abstractmethod
    def split_text(self, text: str) -> list[str]:
        pass