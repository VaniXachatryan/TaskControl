from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.repositories.work_center_repository_interface import IWorkCenterRepository
from src.domain.entities.work_center import WorkCenter
from src.infrastructure.common.base_repository import BaseRepository


class WorkCenterRepository(BaseRepository, IWorkCenterRepository):

    def __init__(self, session: AsyncSession):
        super().__init__(session=session, entity=WorkCenter)

    async def get_by_code(self, code: str) -> WorkCenter | None:
        query = select(WorkCenter).where(WorkCenter.code == code)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_or_create_by_code(self, code: str) -> WorkCenter:
        query = select(WorkCenter).where(WorkCenter.code == code)
        result = await self.session.execute(query)
        result = result.scalar_one_or_none()

        if result is None:
            new_work_center: WorkCenter = WorkCenter(code=code)
            self.session.add(new_work_center)
            await self.session.flush()
            result = new_work_center

        return result
