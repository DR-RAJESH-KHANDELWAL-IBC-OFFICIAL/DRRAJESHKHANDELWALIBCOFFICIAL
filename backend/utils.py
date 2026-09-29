
"""
👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑
Backend utility functions.
"""

from datetime import datetime, timezone
from uuid import uuid4


def get_utc_now() -> str:
    """Return the current UTC timestamp."""
    return datetime.now(timezone.utc).isoformat()


def normalize_text(value: str) -> str:
    """Normalize text by trimming and collapsing whitespace."""
    return " ".join(value.strip().split())


def generate_identifier() -> str:
    """Generate a unique identifier."""
    return str(uuid4())
