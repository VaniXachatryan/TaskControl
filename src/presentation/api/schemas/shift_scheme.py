from datetime import datetime
from typing import Optional

from pydantic import Field, BaseModel


class ShiftScheme(BaseModel):
    id: int = Field(..., description="ID смены")
    number: str = Field(..., description="Номер смены")
    start_at: datetime = Field(..., description="Начало смены")
    end_at: Optional[datetime] = Field(..., description="Конец смены")