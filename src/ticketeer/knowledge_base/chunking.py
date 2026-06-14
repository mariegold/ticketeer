import re

from pydantic import BaseModel


class Chunk(BaseModel):
    text: str
    source: str
    metadata: dict = {}


class BaseChunker:
    def chunk(self, text: str, source: str) -> list[Chunk]:
        raise NotImplementedError

    @staticmethod
    def clean(text: str) -> str:
        return re.sub(r" +", " ", text).strip()


class SlidingWindowChunker(BaseChunker):
    """Word-level overlapping windows."""

    def __init__(self, window_size: int = 250, overlap: int = 50) -> None:
        self.window_size = window_size
        self.overlap = overlap

    def chunk(self, text: str, source: str) -> list[Chunk]:
        words = text.split()
        if len(words) <= self.window_size:
            return [Chunk(text=self.clean(text), source=source, metadata={})]

        step = self.window_size - self.overlap
        chunks: list[Chunk] = []
        start = 0
        while start < len(words):
            window = words[start : start + self.window_size]
            chunks.append(
                Chunk(
                    text=self.clean(" ".join(window)),
                    source=source,
                    metadata={"window_start": start},  # word offset, useful for deduplication or highlighting
                )
            )
            start += step

        return chunks
