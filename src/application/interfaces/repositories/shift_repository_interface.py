from abc import ABC, abstractmethod
from datetime import datetime

from src.application.interfaces.repositories.repository_interface import IRepository
from src.domain.entities.shift import Shift


class IShiftRepository(IRepository, ABC):

    @abstractmethod
    async def get_by_number(self, number: int) -> Shift | None:
        pass

    @abstractmethod
    async def get_or_create_by_number(self, number: int, start_at: datetime, end_at: datetime = None) -> Shift:
        pass
