from dataclasses import dataclass
from datetime import date as onlydate


@dataclass
class BatchResult:
    id: int
    number: int
    date: onlydate
