from datetime import datetime, date
from typing import Optional, List, Any

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
            batch_date: date,
            nomenclature: str,
            ekn_code: str,
            work_center_code: str,
            shift_start_date: datetime,
            shift_end_date: Optional[datetime]
    ) -> (TaskResult, str):
        async with self.uow:
            line: Line = await self.uow.lines.get_or_create_by_code(code=line_code)
            batch: Batch = await self.uow.batches.get_or_create_by_number_and_date(number=batch_number, date=batch_date,
                                                                                   line_id=line.id)
            work_center: WorkCenter = await self.uow.work_centers.get_or_create_by_code(code=work_center_code)
            shift: Shift = await self.uow.shifts.get_or_create_by_number(start_at=shift_start_date,
                                                                         end_at=shift_end_date, number=shift)
            brigade: Brigade = await self.uow.brigades.get_or_create_by_title(title=brigade_title)

            task: Task = await self.uow.tasks.get_by_batch_id(batch_id=batch.id) or Task()

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

            return TaskResult(
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
            ), None

    async def get_by_id_with_product_id(self, task_id: str) -> (TaskResultWithProductIdsResult, str):
        async with self.uow:
            task: Task | None = await self.uow.tasks.get_by_id(entity_id=task_id)
            if task is None:
                return None, TaskErrors.not_found

            products = await self.uow.products.get_ids_list_by_batch_id(batch_id=task.batch_id)

            result: TaskResultWithProductIdsResult = TaskResultWithProductIdsResult(
                id=task.id,
                is_closed=task.is_closed,
                title=task.title,
                line=LineResult(id=task.batch.line.id, code=task.batch.line.code),
                shift=ShiftResult(id=task.shift.id, number=task.shift.number,
                                  start_at=task.shift.start_at, end_at=task.shift.end_at),
                brigade=BrigadeResult(id=task.brigade.id, title=task.brigade.title),
                batch=BatchResult(id=task.batch.id, number=task.batch.number, date=task.batch.date),
                nomenclature=task.nomenclature,
                ekn_code=task.ekn_code,
                work_center=WorkCenterResult(id=task.work_center.id, code=task.work_center.code),
                products=products
            )

            return result, None

    async def update(
            self,
            task_id: int,
            is_closed: Optional[bool],
            task_title: Optional[str],
            line_code: Optional[str],
            shift: Optional[str],
            brigade_title: Optional[str],
            batch_number: Optional[int],
            batch_date: Optional[datetime],
            nomenclature: Optional[str],
            ekn_code: Optional[str],
            work_center_code: Optional[str],
            shift_start_date: Optional[datetime],
            shift_end_date: Optional[datetime]
    ) -> (List[TaskResult], str):

        async with self.uow:
            task: Task | None = await self.uow.tasks.get_by_id(entity_id=task_id)

            if task is None:
                return None, TaskErrors.not_found

            batch_date = batch_date if batch_date is not None else task.batch.date
            shift_start_date = shift_start_date if shift_start_date is not None else task.shift.start_at
            shift_end_date = shift_end_date if shift_end_date is not None else task.shift.end_at

            line: Line = await self.uow.lines.get_or_create_by_code(code=line_code) if line_code else task.batch.line

            batch: Batch = await self.uow.batches.get_or_create_by_number_and_date(
                number=batch_number,
                date=batch_date,
                line_id=line.id) if batch_number and batch_date else task.batch

            work_center: WorkCenter = await self.uow.work_centers.get_or_create_by_code(
                code=work_center_code) if work_center_code else task.work_center

            shift: Shift = await self.uow.shifts.get_or_create_by_number(
                start_at=shift_start_date,
                end_at=shift_end_date,
                number=shift) if shift else task.shift

            brigade: Brigade = await self.uow.brigades.get_or_create_by_title(
                title=brigade_title) if brigade_title else task.brigade

            task.title = task_title if task_title is not None else task.title
            task.is_closed = is_closed if is_closed is not None else task.is_closed
            task.closed_at = datetime.utcnow() if task.is_closed is True else None
            task.work_center = work_center
            task.shift = shift
            task.brigade = brigade
            task.batch = batch
            task.nomenclature = nomenclature if nomenclature is not None else task.nomenclature
            task.ekn_code = ekn_code if ekn_code is not None else task.ekn_code

            await self.uow.tasks.update(entity=task)

            await self.uow.commit()

            return TaskResult(
                id=task.id,
                is_closed=task.is_closed,
                title=task.title,
                line=LineResult(id=task.batch.line.id, code=task.batch.line.code),
                shift=ShiftResult(id=task.shift.id, number=task.shift.number,
                                  start_at=task.shift.start_at, end_at=task.shift.end_at),
                brigade=BrigadeResult(id=task.brigade.id, title=task.brigade.title),
                batch=BatchResult(id=task.batch.id, number=task.batch.number, date=task.batch.date),
                nomenclature=task.nomenclature,
                ekn_code=task.ekn_code,
                work_center=WorkCenterResult(id=task.work_center.id, code=task.work_center.code)
            ), None

    async def get_by_filters(
            self, is_closed: Optional[bool] = None, line_code: Optional[str] = None,
            task_title: Optional[str] = None, shift_number: Optional[str] = None,
            brigade_title: Optional[str] = None, batch_number: Optional[int] = None,
            batch_date: Optional[datetime] = None, nomenclature: Optional[str] = None,
            ekn_code: Optional[str] = None, work_center_code: Optional[str] = None,
            shift_start_date: Optional[datetime] = None, shift_end_date: Optional[datetime] = None,
            count: int = 15, page: int = 1
    ) -> (List[TaskResult], str):
        count = 1 if count < 1 else count
        page = 1 if page < 1 else page

        async with self.uow:
            tasks = await self.uow.tasks.get_list_by_filters(
                is_closed=is_closed,
                line_code=line_code,
                task_title=task_title,
                shift_number=shift_number,
                shift_start_at=shift_start_date,
                shift_end_at=shift_end_date,
                brigade_title=brigade_title,
                batch_number=batch_number,
                batch_date=batch_date,
                nomenclature=nomenclature,
                ekn_code=ekn_code,
                work_center_code=work_center_code,
                limit=count, offset=(page-1)*count
            )

            return [TaskResult(
                id=task.id,
                is_closed=task.is_closed,
                title=task.title,
                line=LineResult(id=task.batch.line.id, code=task.batch.line.code),
                shift=ShiftResult(id=task.shift.id, number=task.shift.number,
                                  start_at=task.shift.start_at, end_at=task.shift.end_at),
                brigade=BrigadeResult(id=task.brigade.id, title=task.brigade.title),
                batch=BatchResult(id=task.batch.id, number=task.batch.number, date=task.batch.date),
                nomenclature=task.nomenclature,
                ekn_code=task.ekn_code,
                work_center=WorkCenterResult(id=task.work_center.id, code=task.work_center.code)
            ) for task in tasks], None
