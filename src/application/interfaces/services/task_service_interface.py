from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

from returns.result import Result

from src.application.common.results.task_result import TaskResultWithProductIdsResult
from src.domain.entities.task import Task


class ITaskService(ABC):
    @abstractmethod
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
        pass

    @abstractmethod
    async def get_by_id_with_product_id(self, task_id: str) \
            -> Result[TaskResultWithProductIdsResult, str]:
        pass
