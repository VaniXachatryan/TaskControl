from pydantic import BaseModel, Field


class LineScheme(BaseModel):
    id: int = Field(..., description="ID линии")
    code: str = Field(..., description="Название/код линии")
