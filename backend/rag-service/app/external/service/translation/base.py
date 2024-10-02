from abc import ABC, abstractmethod

class BaseTranslation(ABC):
    @abstractmethod
    def get_prompt(self, message: str) -> str:
        pass
