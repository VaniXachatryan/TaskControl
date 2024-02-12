from datetime import datetime
from typing import Optional

from returns.result import Result, Success, Failure

from src.application.interfaces.services.task_service_interface import ITaskService
from src.application.interfaces.unit_of_work_interface import IUnitOfWork
from src.domain.common.errors.batch_errors import BatchErrors
from src.domain.common.errors.brigade_errors import BrigadeErrors
from src.domain.common.errors.line_errors import LineErrors
from src.domain.common.errors.work_center_errors import WorkCenterErrors
from src.domain.entities.batch import Batch
from src.domain.entities.brigade import Brigade
from src.domain.entities.line import Line
from src.domain.entities.shift import Shift
from src.domain.entities.task import Task
from src.domain.entities.work_center import WorkCenter


class TaskService(ITaskService):
    def __init__(self, uow: IUnitOfWork):
        self.uow: IUnitOfWork = uow

    async def add(
            self,
            is_closed: bool,
            task_title: str,
            line_code: str,
            shift: str,
            brigade_title: str,
            batch_number: int,
            batch_date: datetime,
            nomenclature: str,
            ekn_code: str,
            work_center_code: str,
            shift_start_date: datetime,
            shift_end_date: Optional[datetime]
    ) -> Result[Task, str]:
        batch_date = batch_date.replace(tzinfo=None)
        async with self.uow:
            batch: Batch = await self.uow.batches.get_by_number_and_date(number=batch_number, date=batch_date)
            line: Line = await self.uow.lines.get_by_code(code=line_code)
            work_center: WorkCenter = await self.uow.work_centers.get_by_code(code=work_center_code)
            shift: Shift = await self.uow.shifts.get_by_number(number=shift)
            brigade: Brigade = await self.uow.brigades.get_by_title(title=brigade_title)

            if line is None:
                line: Line = Line(code=line_code)
                await self.uow.lines.create(entity=line)
                await self.uow.flush()

            if batch is None:
                batch = Batch(line_id=line.id, number=batch_number,
                                     date=batch_date)
                await self.uow.batches.create(entity=batch)

            if shift is None:
                shift = Shift(code=shift)
                await self.uow.shifts.create(entity=shift)

            if brigade is None:
                brigade = Brigade(title=brigade_title)
                await self.uow.brigades.create(entity=brigade)

            if work_center is None:
                work_center = WorkCenter(code=work_center_code)
                await self.uow.work_centers.create(entity=work_center)

            await self.uow.flush()

            task: Task = await self.uow.tasks.get_by_batch_id(batch_id=batch.id) or Task()

            task.line = line
            task.title = task_title
            task.is_closed = is_closed
            task.closed_at = None
            task.work_center = work_center
            task.shift = shift
            task.brigade = brigade
            task.batch = batch
            task.nomenclature = nomenclature
            task.ekn_code = ekn_code

            await self.uow.tasks.update(entity=task)

            await self.uow.commit()

            return Success(task)
