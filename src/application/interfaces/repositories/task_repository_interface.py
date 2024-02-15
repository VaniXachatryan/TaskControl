from abc import ABC, abstractmethod
from datetime import datetime, date
from typing import List, Optional

from src.application.interfaces.repositories.repository_interface import IRepository
from src.domain.entities.task import Task


class ITaskRepository(IRepository, ABC):

    @abstractmethod
    async def get_by_batch_id(self, batch_id: int) -> Task | None:
        pass

    async def get_list_by_filters(
            self, is_closed: Optional[bool] = None, line_code: Optional[str] = None,
            task_title: Optional[str] = None, shift_number: Optional[str] = None,
            shift_start_at: Optional[datetime] = None, shift_end_at: Optional[datetime] = None,
            brigade_title: Optional[str] = None, batch_number: Optional[str] = None,
            batch_date: Optional[date] = None, nomenclature: Optional[str] = None,
            ekn_code: Optional[str] = None, work_center_code: Optional[str] = None,
            limit: int = 15, offset: int = 0
    ) -> List[Task]:
        pass
