from pydantic import BaseModel, constr

class EmbeddingRequest(BaseModel):
    id: str
    text: str  # Текст для встраивания
