from abc import ABC, abstractmethod

from src.presentation.api.schemas.task import TaskSchema


class ITaskService(ABC):
    @abstractmethod
    async def add(self, task: TaskSchema):
        raise NotImplementedError

