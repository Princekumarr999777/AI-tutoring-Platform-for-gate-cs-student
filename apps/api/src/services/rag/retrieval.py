from dataclasses import dataclass
from typing import Protocol
@dataclass
class RetrievedChunk:
    text: str
    source: str
    score: float
class VectorStore(Protocol):
    async def search(self, query: str, limit: int = 5) -> list[RetrievedChunk]: ...
async def retrieve(query: str, store: VectorStore, limit: int = 5) -> list[RetrievedChunk]:
    return await store.search(query, limit)
