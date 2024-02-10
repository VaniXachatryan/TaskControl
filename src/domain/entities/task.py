from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.configurations.database import BaseModel
from src.domain.entities.brigade import Brigade
from src.domain.entities.batch import Batch
from src.domain.entities.line import Line
from src.domain.entities.shift import Shift
from src.domain.entities.work_center import WorkCenter
from src.presentation.api.schemas.task import TaskSchemaAdd


class Task(BaseModel):
    __tablename__ = "tasks"

    line_id: Mapped[int] = mapped_column(ForeignKey(Line.id))
    title: Mapped[str]
    is_closed: Mapped[bool] = mapped_column(default=False)
    closed_at: Mapped[datetime] = mapped_column(nullable=True)
    work_center_id: Mapped[int] = mapped_column(ForeignKey(WorkCenter.id))
    shift_id: Mapped[str] = mapped_column(ForeignKey(Shift.id))
    brigade_id: Mapped[int] = mapped_column(ForeignKey(Brigade.id))
    batch_id: Mapped[int] = mapped_column(ForeignKey(Batch.id))
    nomenclature: Mapped[str]
    ekn_code: Mapped[str]

    line = relationship(Line, lazy="joined")
    batch = relationship(Batch, lazy="joined")
    work_center = relationship(WorkCenter, lazy="joined")
    shift = relationship(Shift, lazy="joined")
    brigade = relationship(Brigade, lazy="joined")

    def to_read_model(self):
        return TaskSchemaAdd(
            is_closed=self.is_closed,
            title=self.name,
            work_center=self.work_center.title,
            work_center_id=self.work_center_id,
            brigade_id=self.brigade_id,
            batch_number=self.batch.number,
            nomenclature=self.nomenclature,
            ekn_code=self.ekn_code,
            shift_id=self.shift_id,
            shift_start_date=self.shift.shift_start_date,
            shift_end_date=self.shift.shift_end_date
        )
