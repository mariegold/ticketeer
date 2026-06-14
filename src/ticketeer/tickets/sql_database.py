import sqlite3
from typing import TYPE_CHECKING

from ticketeer.tickets.base import BaseDatabase

if TYPE_CHECKING:
    from pathlib import Path


class SQLiteDatabase(BaseDatabase):
    """SQLite-backed database. Connects read-only via URI."""

    _MAX_ROWS = 5000

    def __init__(self, db_path: Path, table: str = "tickets") -> None:
        self._table = table
        self._conn = sqlite3.connect(f"file:{db_path!s}?mode=ro", uri=True)
        self._conn.row_factory = sqlite3.Row  # Enables dict conversion while preserving column names

    def execute(self, sql: str) -> list[dict]:
        cursor = self._conn.execute(sql)
        return [dict(row) for row in cursor.fetchmany(self._MAX_ROWS)]

    def get_schema(self) -> str:
        cursor = self._conn.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name=?", (self._table,))
        row = cursor.fetchone()
        return row[0] if row else ""

    def get_sample_rows(self, n: int = 5) -> list[dict]:
        cursor = self._conn.execute(f"SELECT * FROM {self._table} LIMIT {int(n)}")  # noqa: S608
        return [dict(row) for row in cursor.fetchall()]

    def close(self) -> None:
        self._conn.close()
