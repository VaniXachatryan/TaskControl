from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class ShiftResult:
    id: int
    number: str
    start_at: datetime
    end_at: Optional[datetime]