from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import mapped_column, Mapped

from src.domain.common.base_model import BaseModel


class Shift(BaseModel):
    __tablename__ = "shifts"

    start_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    end_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    number: Mapped[str]

    def to_read_model(self):
        return Shift(
            id=self.id,
            number=self.number,
            start_at=self.start_at,
            end_at=self.end_at
        )
