from abc import ABC, abstractmethod

from sqlalchemy import select

from src.domain.entities.brigade import Brigade
from src.infrastructure.common.base_repository import IRepository


class IBrigadeRepository(IRepository, ABC):

    @abstractmethod
    async def get_by_title(self, title: str) -> Brigade | None:
        pass
