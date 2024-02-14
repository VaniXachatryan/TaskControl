from abc import ABC, abstractmethod

from src.domain.common.base_model import BaseModel


class IRepository(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: int) -> None:
        pass

    @abstractmethod
    async def create(self, entity: BaseModel) -> BaseModel | None:
        pass

    @abstractmethod
    async def update(self, entity: BaseModel) -> BaseModel | None:
        pass
