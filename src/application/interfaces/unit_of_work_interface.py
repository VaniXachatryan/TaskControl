from abc import abstractmethod, ABC
from typing import Type

from src.application.interfaces.repositories.batch_repository_interface import IBatchRepository
from src.application.interfaces.repositories.brigade_repository_interface import IBrigadeRepository
from src.application.interfaces.repositories.line_repository_interface import ILineRepository
from src.application.interfaces.repositories.product_repository_interface import IProductRepository
from src.application.interfaces.repositories.shift_repository_interface import IShiftRepository
from src.application.interfaces.repositories.task_repository_interface import ITaskRepository
from src.application.interfaces.repositories.work_center_repository_interface import IWorkCenterRepository
from src.infrastructure.configurations.database import BaseModel


class IUnitOfWork(ABC):
    tasks: Type[ITaskRepository]
    batches: Type[IBatchRepository]
    lines: Type[ILineRepository]
    work_centers: Type[IWorkCenterRepository]
    brigades: Type[IBrigadeRepository]
    shifts: Type[IShiftRepository]
    products: Type[IProductRepository]

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def flush(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...
