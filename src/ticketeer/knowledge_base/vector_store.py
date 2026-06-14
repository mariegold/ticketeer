import uuid
from typing import TYPE_CHECKING, TypedDict

import numpy as np

if TYPE_CHECKING:
    from collections.abc import Iterator

    from ticketeer.knowledge_base.chunking import Chunk
    from ticketeer.knowledge_base.embedding import OpenAIEmbedder


class IndexEntry(TypedDict):
    id: str
    vector: list[float]
    chunk: Chunk


class VectorStore:
    """In-memory vector store with cosine similarity search."""

    def __init__(self, embedder: OpenAIEmbedder) -> None:
        self._embedder = embedder
        self.index: dict[str, IndexEntry] = {}
        self._matrix: np.ndarray | None = None  # lazy-built on first search, cleared on mutation
        self._ordered_ids: list[str] = []  # row i of _matrix corresponds to _ordered_ids[i]

    def __len__(self) -> int:
        return len(self.index)

    @classmethod
    def from_chunks(cls, chunks: list[Chunk], embedder: OpenAIEmbedder) -> VectorStore:
        store = cls(embedder)

        if chunks:
            # embed_batch is a single API call; avoids per-chunk round trips
            embeddings = embedder.embed_batch([c.text for c in chunks])
            for chunk, embedding in zip(chunks, embeddings, strict=True):
                store.add(chunk, embedding)

        return store

    def add(self, chunk: Chunk, embedding: list[float]) -> str:
        id_ = str(uuid.uuid4())
        self.index[id_] = {"id": id_, "vector": embedding, "chunk": chunk}
        self._matrix = None  # stale, rebuilt on next search
        return id_

    def delete(self, ids: list[str]) -> None:
        for id_ in ids:
            self.index.pop(id_, None)
        self._matrix = None  # stale, rebuilt on next search
        self._ordered_ids = []

    def get_by_ids(self, ids: list[str]) -> list[Chunk]:
        return [self.index[id_]["chunk"] for id_ in ids if id_ in self.index]

    def similarity_search(self, query: str, k: int, threshold: float = 0.0) -> list[Chunk]:
        if not self.index:
            return []

        if self._matrix is None:
            # snapshot insertion order so row indices stay stable during this search
            self._ordered_ids = list(self.index.keys())
            self._matrix = np.array(
                [self.index[id_]["vector"] for id_ in self._ordered_ids],
                dtype=np.float32,
            )

        q = np.array(self._embedder.embed(query), dtype=np.float32)
        q_norm = q / (np.linalg.norm(q) + 1e-10)  # +1e-10 guards against division by zero
        norms = np.linalg.norm(self._matrix, axis=1, keepdims=True) + 1e-10
        scores = (self._matrix / norms) @ q_norm  # cosine similarity for each row

        top_k = min(k, len(scores))
        indices = np.argsort(scores)[::-1][:top_k]  # reverse to highest-similarity-first
        return [self.index[self._ordered_ids[int(i)]]["chunk"] for i in indices if scores[int(i)] >= threshold]

    def entries(self) -> Iterator[tuple[Chunk, list[float]]]:
        return ((e["chunk"], e["vector"]) for e in self.index.values())
