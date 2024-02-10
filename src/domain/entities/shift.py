from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped

from src.infrastructure.configurations.database import BaseModel


class Shift(BaseModel):
    __tablename__ = "shifts"

    start_at: Mapped[datetime]
    end_at: Mapped[datetime] = mapped_column(nullable=True)