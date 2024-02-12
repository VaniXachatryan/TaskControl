from dataclasses import dataclass
from datetime import datetime


@dataclass
class BatchResult:
    id: int
    number: int
    date: datetime
