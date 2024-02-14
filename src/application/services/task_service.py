from datetime import datetime
from typing import Optional

from returns.result import Result, Success, Failure

from src.application.common.results.batch_result import BatchResult
from src.application.common.results.brigade_result import BrigadeResult
from src.application.common.results.line_result import LineResult
from src.application.common.results.shift_result import ShiftResult
from src.application.common.results.task_result import TaskResultWithProductIdsResult, TaskResult
from src.application.common.results.work_center_result import WorkCenterResult
from src.application.interfaces.services.task_service_interface import ITaskService
from src.application.interfaces.unit_of_work_interface import IUnitOfWork
from src.domain.common.errors.task_errors import TaskErrors
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
    ) -> Result[TaskResult, str]:

        batch_date = batch_date.replace(tzinfo=None)
        shift_start_date = shift_start_date.replace(tzinfo=None)
        shift_end_date = shift_end_date.replace(tzinfo=None)
        line: Line = await self.uow.lines.get_or_create_by_code(code=line_code)
        batch: Batch = await self.uow.batches.get_or_create_by_number_and_date(number=batch_number, date=batch_date,
                                                                               line_id=line.id)
        work_center: WorkCenter = await self.uow.work_centers.get_or_create_by_code(code=work_center_code)
        shift: Shift = await self.uow.shifts.get_or_create_by_number(start_at=shift_start_date,
                                                                     end_at=shift_end_date, number=shift)
        brigade: Brigade = await self.uow.brigades.get_or_create_by_title(title=brigade_title)

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

        if task.id is None:
            await self.uow.tasks.create(entity=task)
        else:
            await self.uow.tasks.update(entity=task)

        await self.uow.commit()

        return Success(TaskResult(
            id=task.id or 0,
            is_closed=task.is_closed,
            title=task.title,
            line=LineResult(id=line.id, code=line.code),
            shift=ShiftResult(id=shift.id, number=shift.number,
                              start_at=shift.start_at, end_at=shift.end_at),
            brigade=BrigadeResult(id=brigade.id, title=brigade.title),
            batch=BatchResult(id=batch.id, number=batch.number, date=batch.date),
            nomenclature=task.nomenclature,
            ekn_code=task.ekn_code,
            work_center=WorkCenterResult(id=work_center.id, code=work_center.code)
        ))

    async def get_by_id_with_product_id(self, task_id: str) -> Result[TaskResultWithProductIdsResult, str]:

        task: Task | None = await self.uow.tasks.get_by_id(entity_id=task_id)
        if task is None:
            return Failure(TaskErrors.not_found)

        products = await self.uow.products.get_ids_list_by_batch_id(batch_id=task.batch_id)

        result: TaskResultWithProductIdsResult = TaskResultWithProductIdsResult(
            id=task.id,
            is_closed=task.is_closed,
            title=task.title,
            line=LineResult(id=task.line.id, code=task.line.code),
            shift=ShiftResult(id=task.shift.id, number=task.shift.number,
                              start_at=task.shift.start_at, end_at=task.shift.end_at),
            brigade=BrigadeResult(id=task.brigade.id, title=task.brigade.title),
            batch=BatchResult(id=task.batch.id, number=task.batch.number, date=task.batch.date),
            nomenclature=task.nomenclature,
            ekn_code=task.ekn_code,
            work_center=WorkCenterResult(id=task.work_center.id, code=task.work_center.code),
            products=products
        )

        return Success(result)
