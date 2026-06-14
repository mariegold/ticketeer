from abc import ABC, abstractmethod


class BaseDatabase(ABC):
    """Abstract base for all database backends."""

    @abstractmethod
    def execute(self, sql: str) -> list[dict]:
        """Execute a query and return rows as dicts."""

    @abstractmethod
    def get_schema(self) -> str:
        """Return a string representation of the database schema."""

    @abstractmethod
    def get_sample_rows(self, n: int = 5) -> list[dict]:
        """Return n representative rows."""

    @abstractmethod
    def close(self) -> None:
        """Release any held resources."""
