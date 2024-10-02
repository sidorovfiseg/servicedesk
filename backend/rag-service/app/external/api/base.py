
from abc import ABC, abstractmethod

class BaseAPI(ABC):
    @abstractmethod
    async def send_message(self, prompt: str, context: str = None) -> str:
        pass
