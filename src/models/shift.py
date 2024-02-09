from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped

from src.configurations.database import BaseModel


class Shift(BaseModel):
    __tablename__ = "shifts"

    id: Mapped[int] = mapped_column(primary_key=True)
    start_at: Mapped[datetime]
    end_at: Mapped[datetime] = mapped_column(nullable=True)