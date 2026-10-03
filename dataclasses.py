from dataclasses import dataclass
from datetime import date


@dataclass
class Duration:
    hours: int
    minutes: int
    seconds: int

@dataclass
class Session:
    session_id: int                              # NEW: unikt id för passet
    description: str
    date: date
    distance: float
    duration: Duration
    tags: set[str]                               # NEW: taggar som är kopplade till passet

@dataclass(order=True)
class DistanceEntry:
    distance: float                              # sorteras först efter distans
    session_id: int

@dataclass
class TrainingDiary:
    months: list[MonthList]                      # 120 MonthList-objekt, ett per månad
    sessions_by_id: dict[int, Session]           # id till pass
    tag_index: dict[str, set[int]]               # tagg till id:et
    distance_index: list[DistanceEntry]          # sorterad lista
    next_id: int = 1