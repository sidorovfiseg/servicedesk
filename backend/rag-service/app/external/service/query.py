# services/query_service.py

from external.service import BaseService
from external.api import BaseAPI

class QueryService(BaseService):
    def __init__(self, api: BaseAPI):
        self.api = api

    async def execute(self, query: str, context: str) -> str:
        return await self.api.send_message(query, context)
