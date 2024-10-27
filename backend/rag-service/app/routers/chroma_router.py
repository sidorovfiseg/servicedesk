from typing import List

from fastapi import APIRouter, Query

from schemas.chroma import SearchRequest
from utils.chroma_utils import search, top_chunks

chroma_router = APIRouter(
    prefix="/chroma_router",
    tags=["chroma"],
)


@chroma_router.post(
    "/rag_search",
)
async def rag_search(
    request: SearchRequest,
    encoding_model: str = Query(
        "gigachat", enum=("gigachat", "local_all_12", "openai")
    ),
    n_results: int = Query(10),
    include_embeddings: bool = Query(False),
    ids: List[str] = Query([], alias="id"),
):
    res = await search(request, encoding_model, n_results, include_embeddings, ids)
    return res


@chroma_router.post(
    "/top_n",
)
async def top_n(
    encoding_model: str = Query(
        "gigachat", enum=("gigachat", "local_all_12", "openai")
    ),
    n_results: int = Query(10),
    offset: int = Query(0),
    include_embeddings: bool = Query(False),
):
    res = await top_chunks(encoding_model, n_results, offset, include_embeddings)
    return res
