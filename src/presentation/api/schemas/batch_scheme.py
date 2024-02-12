from datetime import datetime

from pydantic import BaseModel, Field


class BatchScheme(BaseModel):
    id: int = Field(..., description="ID партии")
    number: int = Field(..., description="Номер партии")
    date: datetime = Field(..., description="Дата партии")