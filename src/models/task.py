from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.configurations.database import BaseModel


class Task(BaseModel):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    is_closed: Mapped[bool] = mapped_column(default=False)
    closed_at: Mapped[datetime] = mapped_column(nullable=True)
    work_center_id: Mapped[int] = mapped_column(ForeignKey("work_centers.id"))
    shift_id: Mapped[str] = mapped_column(ForeignKey("shifts.id"))
    brigade: Mapped[str] # Бригада
    batch_id: Mapped[int] = mapped_column(ForeignKey("batches.id"))
    nomenclature: Mapped[str]
    ekn_code: Mapped[str]
