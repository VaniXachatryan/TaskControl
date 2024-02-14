from abc import ABC, abstractmethod

from src.application.interfaces.repositories.repository_interface import IRepository
from src.domain.entities.work_center import WorkCenter


class IWorkCenterRepository(IRepository, ABC):

    @abstractmethod
    async def get_by_code(self, code: str) -> WorkCenter | None:
        pass

    @abstractmethod
    async def get_or_create_by_code(self, code: str) -> WorkCenter:
        pass
