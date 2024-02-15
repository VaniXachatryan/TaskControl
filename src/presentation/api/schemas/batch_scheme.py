from datetime import date as onlydate

from pydantic import BaseModel, Field


class BatchScheme(BaseModel):
    id: int = Field(..., description="ID партии")
    number: int = Field(..., description="Номер партии")
    date: onlydate = Field(..., description="Дата партии")