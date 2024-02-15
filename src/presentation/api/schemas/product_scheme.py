from datetime import date

from pydantic import BaseModel, Field


class ProductScheme(BaseModel):
    code: str
    batch_number: int
    batch_date: date


class ProductSchemeAdd(BaseModel):
    code: str = Field(alias="УникальныйКодПродукта")
    batch_number: int = Field(alias="НомерПартии")
    batch_date: date = Field(alias="ДатаПартии")
