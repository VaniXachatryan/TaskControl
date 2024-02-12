from pydantic import BaseModel, Field


class WorkCenterScheme(BaseModel):
    id: int = Field(..., description="ID рабочей станции")
    code: str = Field(..., description="Название/идентификатор рабочей станции")
