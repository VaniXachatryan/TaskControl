from abc import ABC, abstractmethod
from typing import List

from src.application.interfaces.repositories.repository_interface import IRepository


class IProductRepository(IRepository, ABC):

    @abstractmethod
    async def get_ids_list_by_batch_id(self, batch_id: int) -> List[int]:
        pass