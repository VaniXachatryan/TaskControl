from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.repositories.brigade_repository_interface import IBrigadeRepository
from src.domain.entities.brigade import Brigade
from src.infrastructure.common.base_repository import BaseRepository


class BrigadeRepository(BaseRepository, IBrigadeRepository):

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_by_title(self, title: str) -> Brigade | None:
        query = select(Brigade).where(Brigade.title == title)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
