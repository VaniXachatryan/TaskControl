from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class ProductResult:
    id: int
    code: str
    batch_number: int
    batch_date: date
    is_aggregated: bool
    aggregated_at: datetime
