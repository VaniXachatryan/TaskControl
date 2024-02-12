from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped

from src.infrastructure.configurations.database import BaseModel


class Shift(BaseModel):
    __tablename__ = "shifts"

    start_at: Mapped[datetime]
    end_at: Mapped[datetime] = mapped_column(nullable=True)
    number: Mapped[str]

    def to_read_model(self):
        return {
            "id": self.id,
            "start_at": self.start_at,
            "end_at": self.end_at,
        }