from src.application.interfaces.services.product_service_interface import IProductService
from src.application.interfaces.services.task_service_interface import ITaskService
from src.application.interfaces.unit_of_work_interface import IUnitOfWork
from src.application.services.product_service import ProductService
from src.application.services.task_service import TaskService


def get_task_service(unit_of_work: IUnitOfWork) -> ITaskService:
    return TaskService(unit_of_work)


def get_product_service(unit_of_work: IUnitOfWork) -> IProductService:
    return ProductService(unit_of_work)
