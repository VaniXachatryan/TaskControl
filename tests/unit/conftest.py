from unittest.mock import MagicMock, AsyncMock

import pytest

from src.application.depends import get_task_service
from src.application.interfaces.services.task_service_interface import ITaskService


@pytest.fixture(autouse=True, scope='function')
def unit_of_work_mock():
    return AsyncMock()


@pytest.fixture(autouse=True, scope='module')
def task_service(unit_of_work: MagicMock = MagicMock()) -> ITaskService:
    return get_task_service(unit_of_work)
