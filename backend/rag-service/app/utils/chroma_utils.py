from typing import List

import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
from fastapi import Query

from embeddings.infrastructure.embedding_functions import GigaChatEmbeddingFunction
from config.chroma_db_config import chroma_db_config
from embeddings.infrastructure.config import giga_chat_api_config

from embeddings.api.schema import SaveDataRequest, SearchRequest

gigachat_embedding_function = GigaChatEmbeddingFunction(
    credentials=giga_chat_api_config.TOKEN, scope=giga_chat_api_config.SCOPE
)

chroma_client = chromadb.HttpClient(
    host=chroma_db_config.HOST, port=chroma_db_config.PORT
)

gigachat_collection = chroma_client.get_or_create_collection(
    name="gigachat_patent_collection_1", embedding_function=gigachat_embedding_function
)


async def add_vectors_to_db(request: SaveDataRequest):
    if request.encoding_model == "gigachat":
        collection = gigachat_collection
    else:
        return "not valid encoding_model"

    try:
        documents = request.documents
        metadatas = request.metadatas
        start = collection.count()
        ids = [str(i) for i in range(start, start + len(documents))]
        collection.add(ids=ids, documents=documents, metadatas=metadatas)
    except Exception as e:
        return "save error!"

    return f"vector count = {collection.count()}"


async def search(
    request: SearchRequest,
    encoding_model: str = Query(
        "gigachat", enum=("gigachat", "local_all_12", "openai")
    ),
    n_results: int = Query(10),
    include_embeddings: bool = Query(False),
    ids: List[str] = Query([], alias="id"),
):
    if encoding_model == "gigachat":
        collection = gigachat_collection
    else:
        return "not valid encoding_model"

    where = {"id": {"$in": ids}} if ids else None
    include = ["metadatas", "documents", "distances"] + (
        ["embeddings"] if include_embeddings else []
    )
    try:
        return collection.query(
            query_texts=request.text,
            # query_embeddings=gigachat_embedding_function([request.text]),
            n_results=n_results,
            include=include,
            where=where,
        )
    except Exception as e:
        return None


async def top_chunks(
    encoding_model: str = Query(
        "gigachat", enum=("gigachat", "local_all_12", "openai")
    ),
    n_results: int = Query(10),
    offset: int = Query(0),
    include_embeddings: bool = Query(False),
):
    if encoding_model == "gigachat":
        collection = gigachat_collection
    else:
        return "invalid encoding_model"

    ids = [str(i) for i in range(offset, n_results + offset)]
    res = collection.get(
        ids=ids,
        include=["metadatas", "documents"]
        + (["embeddings"] if include_embeddings else []),
    )
    return res
