from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.configurations.database import BaseModel


class Batch(BaseModel):
    __tablename__ = "batches"

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(unique=True)
    date: Mapped[datetime]