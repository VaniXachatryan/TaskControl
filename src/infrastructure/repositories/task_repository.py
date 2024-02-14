from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.repositories.task_repository_interface import ITaskRepository
from src.domain.entities.task import Task
from src.infrastructure.common.base_repository import BaseRepository


class TaskRepository(BaseRepository, ITaskRepository):

    def __init__(self, session: AsyncSession):
        super().__init__(session=session, entity=Task)

    async def get_by_batch_id(self, batch_id: int) -> Task | None:
        query = select(Task).where(Task.batch_id == batch_id).limit(1)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
