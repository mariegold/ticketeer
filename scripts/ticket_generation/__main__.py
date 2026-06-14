"""Generate synthetic IT support tickets into a SQLite database."""

import argparse
from pathlib import Path

from ticket_generation.constants import SEED
from ticket_generation.db import create_db, insert_tickets, verify
from ticket_generation.metadata import generate_metadata
from ticket_generation.text import generate_text_fields

# Resolved relative to this file so the script works from any working directory
DEFAULT_DB = Path(__file__).parent.parent.parent / "data" / "sqlite" / "tickets.db"
DEFAULT_COUNT = 200


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate synthetic IT support tickets.")
    parser.add_argument("--db-path", default=str(DEFAULT_DB))
    parser.add_argument("--count", type=int, default=DEFAULT_COUNT)
    args = parser.parse_args()

    db_path = Path(args.db_path)
    # Two-pass generation: metadata first (structure), then free-text fields
    records = generate_text_fields(generate_metadata(args.count, SEED), SEED)

    conn = create_db(db_path)
    conn.execute("DELETE FROM tickets")  # idempotent: safe to re-run
    insert_tickets(conn, records)
    verify(conn, args.count)
    conn.close()

    print(f"Generated {args.count} tickets ({db_path})")


if __name__ == "__main__":
    main()
