from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.configurations.database import BaseModel


class Batch(BaseModel):
    __tablename__ = "batches"

    number: Mapped[int] = mapped_column(unique=True)
    date: Mapped[datetime]