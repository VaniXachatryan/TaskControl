from src.infrastructure.configurations.database import async_session_maker
from src.application.interfaces.repositories.task_repository_interface import ITaskRepository
from src.application.interfaces.unit_of_work_interface import IUnitOfWork
from src.infrastructure.repositories.task_repository import TaskRepository


class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.tasks: ITaskRepository = TaskRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
