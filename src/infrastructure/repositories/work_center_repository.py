from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.repositories.work_center_repository_interface import IWorkCenterRepository
from src.domain.entities.work_center import WorkCenter
from src.infrastructure.common.base_repository import BaseRepository


class WorkCenterRepository(BaseRepository, IWorkCenterRepository):
    model = WorkCenter

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_by_code(self, code: str) -> WorkCenter | None:
        query = select(self.model).where(self.model.code == code)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
