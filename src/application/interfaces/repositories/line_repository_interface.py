from abc import ABC, abstractmethod

from src.application.interfaces.repositories.repository_interface import IRepository
from src.domain.entities.line import Line

class ILineRepository(IRepository, ABC):

    @abstractmethod
    async def get_by_code(self, code: str) -> Line | None:
        pass

    async def get_or_create_by_code(self, code: str) -> Line | None:
        pass
