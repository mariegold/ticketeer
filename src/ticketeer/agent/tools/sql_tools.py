import json
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

from ticketeer.agent.tools.base import BaseTool

if TYPE_CHECKING:
    from ticketeer.tickets.base import BaseDatabase


class ExecuteSQLArgs(BaseModel):
    query: str = Field(description="A valid SQLite SELECT statement.")


class SampleDataArgs(BaseModel):
    n: int = Field(default=5, description="Number of rows to return.", ge=1, le=20)


class ExecuteSQLTool(BaseTool):
    name = "execute_sql"
    description = (
        "Run a SQL SELECT against the tickets database."
        " Returns result rows as JSON, or an error message if the query is invalid."
    )
    args_schema = ExecuteSQLArgs

    def __init__(self, db: BaseDatabase) -> None:
        self._db = db

    def run(self, query: str) -> str:
        try:
            rows = self._db.execute(query)
            return json.dumps(rows, default=str)
        except Exception as exc:  # noqa: BLE001
            return f"Error: {exc}"


class DiscoverSchemaTool(BaseTool):
    name = "discover_schema"
    description = (
        "Return the tickets table DDL and column descriptions."
        " Call this before writing SQL if unsure of column names or types."
    )

    def __init__(self, db: BaseDatabase) -> None:
        self._db = db

    def run(self) -> str:
        return self._db.get_schema()


class SampleDataTool(BaseTool):
    name = "sample_data"
    description = "Return sample rows from the tickets table to understand the data before writing a query."
    args_schema = SampleDataArgs

    def __init__(self, db: BaseDatabase) -> None:
        self._db = db

    def run(self, n: int = 5) -> str:
        rows = self._db.get_sample_rows(n)
        return json.dumps(rows, default=str, indent=2)
