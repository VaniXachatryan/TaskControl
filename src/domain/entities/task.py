from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.domain.common.base_model import BaseModel
from src.domain.entities.brigade import Brigade
from src.domain.entities.batch import Batch
from src.domain.entities.line import Line
from src.domain.entities.shift import Shift
from src.domain.entities.work_center import WorkCenter


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

    line: Mapped[Line] = relationship(Line, lazy="joined")
    batch: Mapped[Batch] = relationship(Batch, lazy="joined")
    work_center: Mapped[WorkCenter] = relationship(WorkCenter, lazy="joined")
    shift: Mapped[Shift] = relationship(Shift, lazy="joined")
    brigade: Mapped[Brigade] = relationship(Brigade, lazy="joined")

    def to_read_model(self):
        return Task(
            id=self.id,
            title=self.title,
            is_closed=self.is_closed,
            work_center=self.work_center,
            batch=self.batch,
            line=self.line,
            shift=self.shift,
            brigade=self.brigade,
            nomenclature=self.nomenclature,
            ekn_code=self.ekn_code
        )
