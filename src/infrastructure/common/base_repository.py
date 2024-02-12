from abc import abstractmethod, ABC

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.repositories.repository_interface import IRepository
from src.infrastructure.configurations.database import BaseModel


class BaseRepository(IRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, entity: model) -> None:
        self.session.add(entity)
        await self.session.flush()

    async def update(self, entity: model) -> None:
        await self.session.merge(entity)
        await self.session.flush()

    async def get_by_id(self, entity_id: int) -> BaseModel | None:
        query = select(self.model).where(self.model.id == entity_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
