from abc import ABC, abstractmethod
from typing import List

from sqlalchemy import select

from src.domain.entities.brigade import Brigade
from src.infrastructure.common.base_repository import IRepository


class IProductRepository(IRepository, ABC):

    @abstractmethod
    async def get_ids_list_by_batch_id(self, batch_id: int) -> List[int]:
        pass
