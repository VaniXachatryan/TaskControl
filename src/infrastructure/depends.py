from src.application.interfaces.unit_of_work_interface import IUnitOfWork
from src.infrastructure.common.unit_of_work import UnitOfWork


def get_unit_of_work() -> IUnitOfWork:
    return UnitOfWork()
