from abc import ABC, abstractmethod

from src.domain.entities.line import Line
from src.infrastructure.common.base_repository import IRepository


class ILineRepository(IRepository, ABC):

    @abstractmethod
    async def get_by_code(self, code: str) -> Line | None:
        pass
