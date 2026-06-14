import json
import logging
from typing import TYPE_CHECKING

from ticketeer.knowledge_base.chunking import Chunk
from ticketeer.knowledge_base.vector_store import VectorStore

if TYPE_CHECKING:
    from pathlib import Path

    from ticketeer.knowledge_base.chunking import BaseChunker
    from ticketeer.knowledge_base.embedding import OpenAIEmbedder
    from ticketeer.settings import RetrievalSettings

logger = logging.getLogger(__name__)


class KnowledgeBaseService:
    """Reads and chunks KB files, manages the vector store lifecycle, and exposes search."""

    def __init__(
        self,
        chunker: BaseChunker,
        embedder: OpenAIEmbedder,
        path: Path,
        settings: RetrievalSettings,
        *,
        filename: str = "knowledge_base.json",  # stored inside path so it stays alongside the articles it indexes
    ) -> None:
        self._path = path
        self._index_path = path / filename
        self._chunker = chunker
        self._embedder = embedder
        self.top_k = settings.top_k
        self.similarity_threshold = settings.similarity_threshold
        self._store: VectorStore = self._initialise()

    def _initialise(self) -> VectorStore:
        if self._index_path.exists():
            try:
                logger.info("Loading knowledge base index from cache")
                return self._load()
            except ValueError as exc:
                # only model mismatch raises ValueError; other errors (corruption) should surface
                logger.warning("%s : Rebuilding", exc)
        return self._build()

    def _build(self) -> VectorStore:
        logger.info("Building knowledge base")
        chunks = self._chunks()
        store = VectorStore.from_chunks(chunks=chunks, embedder=self._embedder)
        self._save(store)
        return store

    def _save(self, store: VectorStore) -> None:
        data = {
            "model": self._embedder.model,
            "entries": [{"chunk": chunk.model_dump(), "vector": vector} for chunk, vector in store.entries()],
        }
        self._index_path.write_text(json.dumps(data))

    def _load(self) -> VectorStore:
        data = json.loads(self._index_path.read_text())
        # loading an index built with a different model produces meaningless similarity scores
        if data.get("model") != self._embedder.model:
            msg = (
                f"Index was built with model '{data.get('model')}' "
                f"but embedder uses '{self._embedder.model}' — delete {self._index_path} to rebuild."
            )
            raise ValueError(msg)
        store = VectorStore(self._embedder)
        for entry in data["entries"]:
            store.add(Chunk(**entry["chunk"]), entry["vector"])
        return store

    def _chunks(self) -> list[Chunk]:
        result: list[Chunk] = []
        dirs = [self._path, *sorted(p for p in self._path.rglob("*") if p.is_dir())]
        for directory in dirs:
            for md_file in sorted(directory.glob("*.md")):
                text = md_file.read_text(encoding="utf-8")
                chunks = self._chunker.chunk(text, str(md_file))
                result.extend(chunks)
        return result

    def search(self, query: str) -> list[Chunk]:
        logger.debug("Running similarity search with query: %s", query)
        return self._store.similarity_search(query=query, k=self.top_k, threshold=self.similarity_threshold)

    @staticmethod
    def format_results(chunks: list[Chunk]) -> str:
        if not chunks:
            logger.warning("No relevant knowledge base articles found")
            return "No relevant knowledge base articles found."

        parts = []
        for i, chunk in enumerate(chunks, 1):
            header = f"[{i}] Source: {chunk.source}"
            parts.append(f"{header}\n{chunk.text}")
        return "\n\n---\n\n".join(parts)
