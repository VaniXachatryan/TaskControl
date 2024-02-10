from sqlalchemy.orm import Mapped

from src.infrastructure.configurations.database import BaseModel


class WorkCenter(BaseModel):
    __tablename__ = "work_centers"

    title: Mapped[str]