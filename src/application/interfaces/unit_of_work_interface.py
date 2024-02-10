from abc import abstractmethod, ABC
from typing import Type

from src.application.interfaces.repositories.task_repository_interface import ITaskRepository


class IUnitOfWork(ABC):
    tasks: Type[ITaskRepository]

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...
