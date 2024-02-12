from abc import ABC, abstractmethod

from src.domain.entities.shift import Shift
from src.infrastructure.common.base_repository import IRepository


class IShiftRepository(IRepository, ABC):

    @abstractmethod
    async def get_by_number(self, number: int) -> Shift:
        pass
