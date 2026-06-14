from typing import TYPE_CHECKING

import pytest

from ticketeer.knowledge_base.chunking import Chunk
from ticketeer.knowledge_base.embedding import OpenAIEmbedder
from ticketeer.knowledge_base.vector_store import VectorStore

if TYPE_CHECKING:
    from pytest_mock import MockerFixture

QUERY = "query"
INLINE_SOURCE = "scratch.md"
UNKNOWN_ID = "nonexistent"


@pytest.fixture
def sample_chunks() -> list[Chunk]:
    return [
        Chunk(text="password reset instructions", source="faq.md", metadata={"section": "## Passwords"}),
        Chunk(text="vpn setup guide", source="vpn.md", metadata={"section": "## VPN"}),
        Chunk(text="hardware replacement policy", source="hw.md", metadata={}),
    ]


@pytest.fixture
def fake_embedder(mocker: MockerFixture) -> OpenAIEmbedder:
    embedder = mocker.MagicMock(spec=OpenAIEmbedder)
    embedder.model = "test-model"
    embedder.embed.return_value = [1.0, 0.0, 0.0]
    embedder.embed_batch.side_effect = lambda texts: [[1.0, 0.0, 0.0]] * len(texts)
    return embedder


@pytest.fixture
def populated_store(fake_embedder: OpenAIEmbedder, sample_chunks: list[Chunk]) -> VectorStore:
    """VectorStore with three chunks at orthogonal unit vectors [1,0,0], [0,1,0], [0,0,1]."""
    store = VectorStore(fake_embedder)
    for i, chunk in enumerate(sample_chunks):
        vec = [0.0, 0.0, 0.0]
        vec[i] = 1.0
        store.add(chunk, vec)
    return store


class TestAdd:
    def test_empty_store_has_len_zero(self, fake_embedder: OpenAIEmbedder) -> None:
        assert len(VectorStore(fake_embedder)) == 0

    def test_add_increments_len(self, fake_embedder: OpenAIEmbedder) -> None:
        store = VectorStore(fake_embedder)
        store.add(Chunk(text="hello", source=INLINE_SOURCE), [1.0, 0.0, 0.0])
        assert len(store) == 1

    def test_add_returns_string_id(self, fake_embedder: OpenAIEmbedder) -> None:
        store = VectorStore(fake_embedder)
        id_ = store.add(Chunk(text="hello", source=INLINE_SOURCE), [1.0, 0.0, 0.0])
        assert isinstance(id_, str)
        assert id_

    def test_add_after_search_invalidates_matrix_cache(self, populated_store: VectorStore) -> None:
        populated_store.similarity_search(QUERY, k=1)
        assert populated_store._matrix is not None
        populated_store.add(Chunk(text="new entry", source=INLINE_SOURCE), [0.5, 0.5, 0.0])
        assert populated_store._matrix is None


class TestDelete:
    def test_delete_removes_entry(self, populated_store: VectorStore, sample_chunks: list[Chunk]) -> None:
        id_ = next(iter(populated_store.index))
        populated_store.delete([id_])
        assert len(populated_store) == len(sample_chunks) - 1

    def test_delete_missing_id_is_silent(self, populated_store: VectorStore, sample_chunks: list[Chunk]) -> None:
        populated_store.delete([UNKNOWN_ID])
        assert len(populated_store) == len(sample_chunks)

    def test_delete_invalidates_matrix_cache(self, populated_store: VectorStore) -> None:
        populated_store.similarity_search(QUERY, k=1)
        populated_store.delete([next(iter(populated_store.index))])
        assert populated_store._matrix is None


class TestGetByIds:
    def test_returns_chunk_for_known_id(self, populated_store: VectorStore) -> None:
        id_ = next(iter(populated_store.index))
        result = populated_store.get_by_ids([id_])
        assert len(result) == 1
        assert isinstance(result[0], Chunk)

    def test_ignores_unknown_ids(self, populated_store: VectorStore) -> None:
        assert populated_store.get_by_ids([UNKNOWN_ID]) == []

    def test_mixed_known_and_unknown(self, populated_store: VectorStore) -> None:
        id_ = next(iter(populated_store.index))
        result = populated_store.get_by_ids([id_, UNKNOWN_ID])
        assert len(result) == 1


class TestSimilaritySearch:
    def test_empty_store_returns_empty(self, fake_embedder: OpenAIEmbedder) -> None:
        assert VectorStore(fake_embedder).similarity_search(QUERY, k=3) == []

    def test_returns_at_most_k_results(self, populated_store: VectorStore) -> None:
        k = 2
        assert len(populated_store.similarity_search(QUERY, k=k)) <= k

    def test_k_larger_than_store_returns_all(self, populated_store: VectorStore, sample_chunks: list[Chunk]) -> None:
        assert len(populated_store.similarity_search(QUERY, k=100)) == len(sample_chunks)

    def test_most_similar_chunk_ranked_first(self, fake_embedder: OpenAIEmbedder, sample_chunks: list[Chunk]) -> None:
        # fake_embedder returns [1,0,0]; chunk at [1,0,0] should rank first
        top_chunk = sample_chunks[0]
        store = VectorStore(fake_embedder)
        store.add(top_chunk, [1.0, 0.0, 0.0])  # cosine sim = 1.0
        store.add(sample_chunks[1], [0.0, 1.0, 0.0])  # cosine sim = 0.0
        store.add(sample_chunks[2], [0.0, 0.0, 1.0])  # cosine sim = 0.0
        assert store.similarity_search(QUERY, k=3)[0].text == top_chunk.text

    def test_threshold_filters_low_similarity_chunks(
        self, fake_embedder: OpenAIEmbedder, sample_chunks: list[Chunk]
    ) -> None:
        passing_chunk = sample_chunks[0]
        store = VectorStore(fake_embedder)
        store.add(passing_chunk, [1.0, 0.0, 0.0])  # similarity 1.0 — passes threshold
        store.add(sample_chunks[1], [0.0, 1.0, 0.0])  # similarity 0.0 — filtered out
        results = store.similarity_search(QUERY, k=3, threshold=0.5)
        assert len(results) == 1
        assert results[0].text == passing_chunk.text

    def test_zero_threshold_returns_all(self, populated_store: VectorStore, sample_chunks: list[Chunk]) -> None:
        assert len(populated_store.similarity_search(QUERY, k=10, threshold=0.0)) == len(sample_chunks)


class TestFromChunks:
    def test_empty_list_returns_empty_store(self, fake_embedder: OpenAIEmbedder) -> None:
        assert len(VectorStore.from_chunks([], fake_embedder)) == 0

    def test_populates_store_with_all_chunks(self, fake_embedder: OpenAIEmbedder, sample_chunks: list[Chunk]) -> None:
        store = VectorStore.from_chunks(sample_chunks, fake_embedder)
        assert len(store) == len(sample_chunks)

    def test_chunk_texts_preserved(self, fake_embedder: OpenAIEmbedder, sample_chunks: list[Chunk]) -> None:
        store = VectorStore.from_chunks(sample_chunks, fake_embedder)
        expected_texts = {c.text for c in sample_chunks}
        assert {e["chunk"].text for e in store.index.values()} == expected_texts
