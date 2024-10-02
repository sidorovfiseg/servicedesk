from pydantic import BaseModel
from fastapi import Query

class SaveDataRequest(BaseModel):
    encoding_model: str = Query('gigachat', enum=('gigachat', 'local_all_12', 'openai'))
    documents: list[str]
    metadatas: list[dict]