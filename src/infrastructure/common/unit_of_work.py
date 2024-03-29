from src.application.interfaces.repositories.batch_repository_interface import IBatchRepository
from src.application.interfaces.repositories.brigade_repository_interface import IBrigadeRepository
from src.application.interfaces.repositories.line_repository_interface import ILineRepository
from src.application.interfaces.repositories.product_repository_interface import IProductRepository
from src.application.interfaces.repositories.shift_repository_interface import IShiftRepository
from src.application.interfaces.repositories.work_center_repository_interface import IWorkCenterRepository
from src.application.interfaces.repositories.task_repository_interface import ITaskRepository
from src.application.interfaces.unit_of_work_interface import IUnitOfWork
from src.infrastructure.configurations.database import async_session_maker
from src.infrastructure.repositories.batch_repository import BatchRepository
from src.infrastructure.repositories.brigade_repository import BrigadeRepository
from src.infrastructure.repositories.line_repository import LineRepository
from src.infrastructure.repositories.product_repository import ProductRepository
from src.infrastructure.repositories.shift_repository import ShiftRepository
from src.infrastructure.repositories.task_repository import TaskRepository
from src.infrastructure.repositories.work_center_repository import WorkCenterRepository


class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.tasks: ITaskRepository = TaskRepository(self.session)
        self.batches: IBatchRepository = BatchRepository(self.session)
        self.lines: ILineRepository = LineRepository(self.session)
        self.work_centers: IWorkCenterRepository = WorkCenterRepository(self.session)
        self.brigades: IBrigadeRepository = BrigadeRepository(self.session)
        self.shifts: IShiftRepository = ShiftRepository(self.session)
        self.products: IProductRepository = ProductRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def flush(self):
        await self.session.flush()

    async def rollback(self):
        await self.session.rollback()
