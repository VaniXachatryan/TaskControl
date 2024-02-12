from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.domain.entities.line import Line
from src.infrastructure.configurations.database import BaseModel


class Batch(BaseModel):
    __tablename__ = "batches"

    number: Mapped[int]
    date: Mapped[datetime]
    line_id: Mapped[int] = mapped_column(ForeignKey(Line.id))

    line = relationship(Line, lazy="joined")

    def to_read_model(self):
        return Batch(
            id=self.id,
            number=self.number,
            date=self.date,
            line=self.line
        )
