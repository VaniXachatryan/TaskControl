from typing import Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.repositories.repository_interface import IRepository
from src.domain.common.base_model import BaseModel


class BaseRepository(IRepository):

    def __init__(self, session: AsyncSession, entity: Type[BaseModel]):
        self.entity: Type[BaseModel] = entity
        self.session: AsyncSession = session

    async def create(self, entity: BaseModel) -> None:
        self.session.add(entity)
        await self.session.flush()

    async def update(self, entity: BaseModel) -> None:
        await self.session.merge(entity)
        await self.session.flush()

    async def get_by_id(self, entity_id: int) -> BaseModel | None:
        query = select(self.entity).where(self.entity.id == entity_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
