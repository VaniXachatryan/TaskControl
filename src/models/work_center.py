from sqlalchemy.orm import Mapped, mapped_column

from src.configurations.database import BaseModel


class WorkCenter(BaseModel):
    __tablename__ = "work_centers"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]