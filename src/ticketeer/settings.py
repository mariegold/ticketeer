from pathlib import Path

from pydantic_settings import BaseSettings

_ROOT = Path(__file__).parent.parent.parent


class RetrievalSettings(BaseSettings):
    top_k: int = 3
    """Number of document chunks to retrieve."""

    similarity_threshold: float = 0.3
    """Minimum cosine similarity score for a chunk to be returned."""

    embedding_model: str = "text-embedding-3-small"
    """Embedding model from OpenAI to use."""


class ChatSettings(BaseSettings):
    model: str = "gpt-4o-mini"
    """GPT model to use."""

    temperature: float = 0.1
    """Temperature for the chat model."""


class ServiceSettings(ChatSettings, RetrievalSettings):
    openai_api_key: str = ""
    """OpenAI API key."""

    data_dir: Path = _ROOT / "data"
    """Path to the directory where the data is stored."""

    @property
    def db_path(self) -> Path:
        """Path to the directory where the in-memory structured database is stored."""
        return self.data_dir / "sqlite" / "tickets.db"

    @property
    def knowledge_base_path(self) -> Path:
        """Path to the knowledge base directory."""
        return self.data_dir / "md"
