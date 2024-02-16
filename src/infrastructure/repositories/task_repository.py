from datetime import datetime
from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.repositories.task_repository_interface import ITaskRepository
from src.domain.entities.batch import Batch
from src.domain.entities.brigade import Brigade
from src.domain.entities.line import Line
from src.domain.entities.shift import Shift
from src.domain.entities.task import Task
from src.domain.entities.work_center import WorkCenter
from src.infrastructure.common.base_repository import BaseRepository


class TaskRepository(BaseRepository, ITaskRepository):

    def __init__(self, session: AsyncSession):
        super().__init__(session=session, entity=Task)

    async def get_by_batch_id(self, batch_id: int) -> Task | None:
        query = select(Task).where(Task.batch_id == batch_id).limit(1)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_list_by_filters(
            self, is_closed: Optional[bool] = None, line_code: Optional[str] = None,
            task_title: Optional[str] = None, shift_number: Optional[str] = None,
            shift_start_at: Optional[datetime] = None, shift_end_at: Optional[datetime] = None,
            brigade_title: Optional[str] = None, batch_number: Optional[int] = None,
            batch_date: Optional[datetime] = None, nomenclature: Optional[str] = None,
            ekn_code: Optional[str] = None, work_center_code: Optional[str] = None,
            limit: int = 15, offset: int = 0
    ) -> List[Task]:
        query = select(Task)

        if is_closed is not None:
            query = query.where(Task.is_closed == is_closed)

        if line_code is not None:
            query = query.join(Task.line).where(Line.code == line_code)

        if task_title is not None:
            query = query.where(Task.title == task_title)

        if shift_number is not None:
            query = query.join(Task.shift).where(Shift.number == shift_number)

        if shift_start_at is not None:
            query = query.join(Task.shift).where(Shift.start_at == shift_start_at)

        if shift_end_at is not None:
            query = query.join(Task.shift).where(Shift.end_at == shift_end_at)

        if brigade_title is not None:
            query = query.join(Task.brigade).where(Brigade.title == brigade_title)

        if batch_number is not None:
            query = query.join(Task.batch).where(Batch.number == batch_number)

        if batch_date is not None:
            query = query.join(Task.batch).where(Batch.date == batch_date)

        if nomenclature is not None:
            query = query.where(Task.nomenclature == nomenclature)

        if ekn_code is not None:
            query = query.where(Task.ekn_code == ekn_code)

        if work_center_code is not None:
            query = query.join(Task.work_center).where(WorkCenter.code == work_center_code)

        query = query.offset(offset).limit(limit)

        result = await self.session.execute(query)

        return list(result.scalars().all())
