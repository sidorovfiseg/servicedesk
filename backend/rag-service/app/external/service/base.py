# services/base_service.py

from abc import ABC, abstractmethod

class BaseService(ABC):
    @abstractmethod
    async def execute(self, *args, **kwargs):
        pass
