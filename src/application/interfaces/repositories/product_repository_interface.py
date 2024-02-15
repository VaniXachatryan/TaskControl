from abc import ABC, abstractmethod
from typing import List

from src.application.interfaces.repositories.repository_interface import IRepository
from src.domain.entities.product import Product


class IProductRepository(IRepository, ABC):

    @abstractmethod
    async def get_by_code(self, code: str) -> Product | None:
        pass

    @abstractmethod
    async def get_ids_list_by_batch_id(self, batch_id: int) -> List[int]:
        pass

    @abstractmethod
    async def any_by_code(self, code: str) -> bool:
        pass
