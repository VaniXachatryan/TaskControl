from pydantic import BaseModel, Field


class BrigadeScheme(BaseModel):
    id: int = Field(..., description="ID бригады")
    title: str = Field(..., description="Название бригады")
