from abc import ABC, abstractmethod
from datetime import date as onlydate

from src.application.interfaces.repositories.repository_interface import IRepository
from src.domain.entities.batch import Batch


class IBatchRepository(IRepository, ABC):

    @abstractmethod
    async def get_by_number_and_date(self, number: int, date: onlydate, line_id: int) -> Batch | None:
        pass

    @abstractmethod
    async def get_or_create_by_number_and_date(self, number: int, date: onlydate, line_id: int) -> Batch:
        pass
