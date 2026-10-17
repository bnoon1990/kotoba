from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import IntEnum

def get_current_time() -> datetime:
    """Get the current time in UTC."""
    return datetime.now(timezone.utc)

class Grade(IntEnum):
    """Answer quality."""
    AGAIN = 1
    HARD = 2
    GOOD = 3
    EASY = 4

@dataclass
class Card:
    """A flashcard for a single word."""
    front: str
    back: str
    interval_days: int
    due: datetime = field(default_factory=get_current_time)
    created_at: datetime = field(default_factory=get_current_time)
    ease: float = 2.5
    repetitions: int = 0
    id: int | None = None
    reading: str | None = None

@dataclass(frozen = True)
class Review:
    """A review of a flashcard."""
    card_id: int
    grade: Grade
    created_at: datetime = field(default_factory=get_current_time)