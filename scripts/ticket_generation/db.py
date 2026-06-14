"""SQLite persistence: create schema, insert rows, verify row count."""

import sqlite3
from pathlib import Path

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS tickets (
    ticket_id              TEXT    NOT NULL PRIMARY KEY,
    created_at             TEXT    NOT NULL,
    requester_user         TEXT    NOT NULL,
    category               TEXT    NOT NULL,
    subject                TEXT    NOT NULL,
    description            TEXT    NOT NULL,
    status                 TEXT    NOT NULL,
    resolution             TEXT,                   -- null for open/escalated
    resolution_time_hours  REAL,                   -- null for open/escalated
    assigned_team          TEXT    NOT NULL
);
"""

INSERT_SQL = """
INSERT INTO tickets
    (ticket_id, created_at, requester_user, category, subject, description,
     status, resolution, resolution_time_hours, assigned_team)
VALUES
    (:ticket_id, :created_at, :requester_user, :category, :subject, :description,
     :status, :resolution, :resolution_time_hours, :assigned_team)
"""


def create_db(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.execute(CREATE_TABLE)
    conn.commit()
    return conn


def insert_tickets(conn: sqlite3.Connection, tickets: list[dict]) -> None:
    conn.executemany(INSERT_SQL, tickets)
    conn.commit()


def verify(conn: sqlite3.Connection, expected: int) -> None:
    total = conn.execute("SELECT COUNT(*) FROM tickets").fetchone()[0]
    assert total == expected, f"Expected {expected} tickets, got {total}"
