from typing import Annotated

from fastapi import Depends

from src.application.depends import get_task_service, get_product_service
from src.application.interfaces.services.product_service_interface import IProductService
from src.application.interfaces.services.task_service_interface import ITaskService
from src.application.interfaces.unit_of_work_interface import IUnitOfWork
from src.infrastructure.depends import get_unit_of_work


# Unit of Work
unit_of_work: IUnitOfWork = get_unit_of_work()


# Services
TaskServiceDepend = Annotated[ITaskService, Depends(lambda: get_task_service(unit_of_work))]
ProductServiceDepend = Annotated[IProductService, Depends(lambda: get_product_service(unit_of_work))]
