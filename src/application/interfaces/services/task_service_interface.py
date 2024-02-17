from abc import ABC, abstractmethod
from datetime import datetime, date
from typing import Optional, List

from src.application.common.results.task_result import TaskResultWithProductIdsResult, TaskResult


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
            batch_date: date,
            nomenclature: str,
            ekn_code: str,
            work_center_code: str,
            shift_start_date: datetime,
            shift_end_date: Optional[datetime]
    ) -> (TaskResult, str):
        pass

    @abstractmethod
    async def get_by_id_with_product_id(self, task_id: int) \
            -> (TaskResultWithProductIdsResult, str):
        pass

    @abstractmethod
    async def get_by_filters(
            self, is_closed: Optional[bool] = None, line_code: Optional[str] = None,
            task_title: Optional[str] = None, shift_number: Optional[str] = None,
            brigade_title: Optional[str] = None, batch_number: Optional[int] = None,
            batch_date: Optional[datetime] = None, nomenclature: Optional[str] = None,
            ekn_code: Optional[str] = None, work_center_code: Optional[str] = None,
            shift_start_date: Optional[datetime] = None, shift_end_date: Optional[datetime] = None,
            count: int = 15, page: int = 1
    ) -> (List[TaskResult], str):
        pass