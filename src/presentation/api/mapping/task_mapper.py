from src.domain.entities.task import Task
from src.presentation.api.schemas.batch_scheme import BatchScheme
from src.presentation.api.schemas.brigade_scheme import BrigadeScheme
from src.presentation.api.schemas.line_scheme import LineScheme
from src.presentation.api.schemas.shift_scheme import ShiftScheme
from src.presentation.api.schemas.task_scheme import TaskScheme
from src.presentation.api.schemas.work_center_scheme import WorkCenterScheme


def task_to_task_scheme_add(entity: Task) -> TaskScheme:
    return TaskScheme(is_closed=entity.is_closed,
                      title=entity.title,
                      line=LineScheme(id=entity.line.id, code=entity.line.code),
                      work_center=WorkCenterScheme(id=entity.work_center.id, code=entity.work_center.code),
                      shift=ShiftScheme(id=entity.shift.id, number=entity.shift.number, start_at=entity.shift.start_at, end_at=entity.shift.end_at),
                      brigade=BrigadeScheme(id=entity.brigade.id, title=entity.brigade.title),
                      batch=BatchScheme(id=entity.brigade.id, number=entity.batch.number, date=entity.batch.date),
                      nomenclature=entity.nomenclature,
                      ekn_code=entity.ekn_code,
                      closed_at=entity.closed_at)
