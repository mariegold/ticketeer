"""Generate structured ticket metadata (everything except free-text fields)."""

import random
from datetime import datetime, timedelta

from ticket_generation.constants import (
    CATEGORIES,
    END_DATE,
    RESOLUTION_TIME_RANGES,
    START_DATE,
    STATUS_WEIGHTS,
    STATUSES,
    TEAM_BY_CATEGORY,
    USER_WEIGHTS,
    USERS,
)


def _random_business_timestamp(rng: random.Random) -> datetime:
    t = START_DATE + timedelta(days=rng.randint(0, (END_DATE - START_DATE).days))
    if rng.random() < 0.85:  # Snap ~85% of tickets to business hours
        if t.weekday() >= 5:  # Snap weekends to the following Monday
            t += timedelta(days=7 - t.weekday())
        t = t.replace(
            hour=rng.randint(8, 17),
            minute=rng.randint(0, 59),
            second=rng.randint(0, 59)
        )
    return t


def _pick_team(category: str, rng: random.Random) -> str:
    # Each category has a primary team and a fallback (e.g. IT Ops), with defined probabilities
    teams, weights = zip(*TEAM_BY_CATEGORY[category])
    return rng.choices(list(teams), weights=list(weights), k=1)[0]


def _pick_resolution_time(category: str, rng: random.Random, *, long_outlier: bool) -> float:
    lo, hi = RESOLUTION_TIME_RANGES[category]
    # Outliers simulate unusually slow hardware resolutions (e.g. waiting for a part)
    if long_outlier:
        return round(rng.uniform(100, 150), 1)
    return round(rng.uniform(lo, hi), 1)


def generate_metadata(n: int, seed: int) -> list[dict]:
    rng = random.Random(seed)
    # Sort timestamps so ticket IDs are in chronological order
    timestamps = sorted(_random_business_timestamp(rng) for _ in range(n))

    outlier_count = 0
    records = []
    for i, ts in enumerate(timestamps):
        category = rng.choices(CATEGORIES, k=1)[0]
        status = rng.choices(STATUSES, weights=STATUS_WEIGHTS, k=1)[0]

        # A small number of resolved hardware tickets get an extreme resolution time
        long_outlier = (
            category == "hardware"
            and status == "resolved"
            and outlier_count < 3
            and rng.random() < 0.15
        )
        if long_outlier:
            outlier_count += 1

        records.append({
            "ticket_id": f"T-{i + 1:04d}",
            "created_at": ts.strftime("%Y-%m-%dT%H:%M:%S"),
            "requester_user": rng.choices(USERS, weights=USER_WEIGHTS, k=1)[0],
            "category": category,
            "status": status,
            "assigned_team": _pick_team(category, rng),
            # resolution fields are null for open/escalated tickets
            "resolution_time_hours": _pick_resolution_time(category, rng, long_outlier=long_outlier) if status == "resolved" else None,
            "subject": "",       # filled in by generate_text_fields
            "description": "",   # filled in by generate_text_fields
            "resolution": None,  # filled in by generate_text_fields
        })

    return records
