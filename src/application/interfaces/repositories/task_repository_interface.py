from abc import ABC, abstractmethod

from src.application.interfaces.repositories.repository_interface import IRepository
from src.domain.entities.task import Task


class ITaskRepository(IRepository, ABC):

    @abstractmethod
    async def get_by_batch_id(self, batch_id: int) -> Task | None:
        pass
