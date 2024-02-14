from abc import ABC, abstractmethod

from src.application.interfaces.repositories.repository_interface import IRepository
from src.domain.entities.brigade import Brigade


class IBrigadeRepository(IRepository, ABC):

    @abstractmethod
    async def get_by_title(self, title: str) -> Brigade | None:
        pass

    @abstractmethod
    async def get_or_create_by_title(self, title: str) -> Brigade:
        pass
