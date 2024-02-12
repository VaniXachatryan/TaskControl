from abc import ABC, abstractmethod

from src.domain.entities.work_center import WorkCenter
from src.infrastructure.common.base_repository import IRepository


class IWorkCenterRepository(IRepository, ABC):

    @abstractmethod
    async def get_by_code(self, code: str) -> WorkCenter:
        pass
