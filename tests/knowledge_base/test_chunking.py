import pytest

from ticketeer.knowledge_base.chunking import BaseChunker, SlidingWindowChunker

SOURCE = "doc.md"


class TestClean:
    @pytest.mark.parametrize(
        ("text", "expected"),
        [
            ("hello  world", "hello world"),
            ("  leading  ", "leading"),
            ("multiple   spaces   between   words", "multiple spaces between words"),
            ("already clean", "already clean"),
            ("", ""),
        ],
    )
    def test_collapses_spaces_and_strips(self, text: str, expected: str) -> None:
        assert BaseChunker.clean(text) == expected


class TestSlidingWindowChunker:
    def test_short_text_returns_single_chunk(self) -> None:
        chunker = SlidingWindowChunker(window_size=10, overlap=2)
        (chunk,) = chunker.chunk("one two three", SOURCE)
        assert chunk.source == SOURCE

    def test_exactly_window_size_returns_single_chunk(self) -> None:
        chunker = SlidingWindowChunker(window_size=4, overlap=1)
        (chunk,) = chunker.chunk("w0 w1 w2 w3", SOURCE)
        assert chunk.source == SOURCE

    def test_source_propagated_to_all_chunks(self) -> None:
        source = "other.md"
        chunker = SlidingWindowChunker(window_size=3, overlap=1)
        chunks = chunker.chunk("a b c d e f", source)
        assert all(c.source == source for c in chunks)

    def test_first_chunk_window_start_is_zero(self) -> None:
        chunker = SlidingWindowChunker(window_size=3, overlap=1)
        chunks = chunker.chunk("a b c d e f", SOURCE)
        assert chunks[0].metadata["window_start"] == 0

    def test_second_chunk_window_start_equals_step(self) -> None:
        # window=4, overlap=1 → step=3
        chunker = SlidingWindowChunker(window_size=4, overlap=1)
        chunks = chunker.chunk(" ".join(f"w{i}" for i in range(8)), SOURCE)
        step = chunker.window_size - chunker.overlap
        assert chunks[1].metadata["window_start"] == step

    @pytest.mark.parametrize(
        ("window_size", "overlap", "word_count", "expected_chunks"),
        [
            (4, 1, 5, 2),  # step=3: starts at 0, 3
            (4, 2, 8, 4),  # step=2: starts at 0, 2, 4, 6
            (3, 0, 9, 3),  # step=3: starts at 0, 3, 6
            (5, 2, 12, 4),  # step=3: starts at 0, 3, 6, 9
        ],
    )
    def test_chunk_count(self, window_size: int, overlap: int, word_count: int, expected_chunks: int) -> None:
        chunker = SlidingWindowChunker(window_size=window_size, overlap=overlap)
        text = " ".join(f"w{i}" for i in range(word_count))
        assert len(chunker.chunk(text, SOURCE)) == expected_chunks
