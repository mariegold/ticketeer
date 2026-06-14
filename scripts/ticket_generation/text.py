"""Fill free-text fields (subject, description, resolution) using templates and slot values."""

import random
import re

from ticket_generation.constants import SLOT_VALUES, TEMPLATES


def _fill_slots(template: str, rng: random.Random) -> str:
    for ph in re.findall(r"\{(\w+)\}", template):
        # Replace one occurrence at a time so repeated placeholders get different values
        template = template.replace("{" + ph + "}", rng.choice(SLOT_VALUES.get(ph, [f"<{ph}>"])), 1)
    return template


def generate_text_fields(records: list[dict], seed: int) -> list[dict]:
    # seed + 1 so text draws don't correlate with the metadata RNG (which used seed)
    rng = random.Random(seed + 1)
    # Collect resolved IDs upfront for cross-reference easter eggs
    resolved_ids = [r["ticket_id"] for r in records if r["status"] == "resolved"]

    for idx, record in enumerate(records):
        tmpl = TEMPLATES[record["category"]]

        record["subject"] = _fill_slots(rng.choice(tmpl["subjects"]), rng)
        desc = _fill_slots(rng.choice(tmpl["descriptions"]), rng)

        # ~8% chance to mention a prior resolved ticket (skip first 10 to have enough history)
        if idx > 10 and rng.random() < 0.08 and resolved_ids:
            desc += f" This may be related to {rng.choice(resolved_ids[:idx])}."

        # Escalated security tickets get urgency language appended
        if record["category"] == "security" and record["status"] == "escalated":
            desc += (
                " URGENT: potential breach scenario — escalating to Security team "
                "for immediate investigation. Machine isolated from network."
            )

        record["description"] = desc

        if record["status"] == "resolved":
            record["resolution"] = _fill_slots(rng.choice(tmpl["resolutions"]), rng)

    return records
