from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.depends import get_task_service, get_product_service
from src.application.interfaces.services.product_service_interface import IProductService
from src.application.interfaces.services.task_service_interface import ITaskService
from src.application.interfaces.unit_of_work_interface import IUnitOfWork
from src.infrastructure.configurations.database import get_async_session
from src.infrastructure.depends import get_unit_of_work

async_session: AsyncSession = Depends(get_async_session)


# Unit of Work
unit_of_work: IUnitOfWork = get_unit_of_work()


# Services
TaskServiceDepend = Annotated[ITaskService, Depends(lambda: get_task_service(unit_of_work))]
ProductServiceDepend = Annotated[IProductService, Depends(lambda: get_product_service(unit_of_work))]
