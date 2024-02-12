from abc import ABC, abstractmethod
from datetime import datetime

from src.domain.entities.batch import Batch
from src.infrastructure.common.base_repository import IRepository


class IBatchRepository(IRepository, ABC):

    @abstractmethod
    async def get_by_number_and_date(self, number: int, date: datetime, line_id: int) -> Batch | None:
        pass

    @abstractmethod
    async def get_or_create_by_number_and_date(self, number: int, date: datetime, line_id: int) -> Batch:
        pass
