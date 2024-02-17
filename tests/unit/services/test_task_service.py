from datetime import date, datetime
from typing import Optional
from unittest.mock import MagicMock, AsyncMock

import pytest

from src.application.common.results.batch_result import BatchResult
from src.application.common.results.brigade_result import BrigadeResult
from src.application.common.results.line_result import LineResult
from src.application.common.results.shift_result import ShiftResult
from src.application.common.results.task_result import TaskResult, TaskResultWithProductIdsResult
from src.application.common.results.work_center_result import WorkCenterResult
from src.domain.common.errors.task_errors import TaskErrors
from src.domain.entities.batch import Batch
from src.domain.entities.brigade import Brigade
from src.domain.entities.line import Line
from src.domain.entities.shift import Shift
from src.domain.entities.task import Task
from src.domain.entities.work_center import WorkCenter


@pytest.fixture(autouse=True, scope="class")
def data():
    print("Initialize data")
    line: Line | None = Line(id=1, code='wQ21eDS')
    batch: Batch = Batch(id=1, line=line, number='44231', date=date(2024, 0o2, 17))
    work_center: WorkCenter = WorkCenter(id=1, code='WC1')
    brigade: Brigade = Brigade(id=1, title='Бригада 1')
    shift: Shift = Shift(id=1, start_at=datetime(2024, 0o2, 17, 12, 00, 00),
                         end_at=None, number='T1')
    task: Task = Task(id=1, batch=batch, work_center=work_center, shift=shift,
                      brigade=brigade, title='Test task title', is_closed=False,
                      nomenclature='Test nomenclature', ekn_code='EKN_CODE_TEST')

    yield line, batch, work_center, brigade, shift, task


@pytest.mark.usefixtures('data')
class TestTaskService:

    @pytest.mark.parametrize(
        'is_closed, task_title, line_code, shift_number, '
        'brigade_title, batch_number, batch_date, '
        'nomenclature, ekn_code, work_center_code, shift_start_date,'
        'shift_end_date',
        [
            (True, 'Test task title 1', 'ZQS1eG4', 'T1', 'Бригада 3', '412754',
             date(2024, 0o2, 17), 'Test nomenclature', 'EKN_CODE_TEST',
             'WC1', datetime(2024, 0o2, 17, 12, 00, 00),
             datetime(2024, 0o2, 18, 00, 00, 00)),

            (None, 'Test task title 2', None, 2, 13, 3123,
             date(2024, 0o2, 17), 'Test nomenclature 2', 'EKN_CODE_TEST',
             'WC1', datetime(2024, 0o2, 17, 12, 00, 00),
             datetime(2024, 0o2, 18, 00, 00, 00))
        ])
    async def test_add_task_should_be_value(
            self,
            is_closed: bool,
            task_title: str,
            line_code: str,
            shift_number: str,
            brigade_title: str,
            batch_number: int,
            batch_date: date,
            nomenclature: str,
            ekn_code: str,
            work_center_code: str,
            shift_start_date: datetime,
            shift_end_date: Optional[datetime],
            task_service,
            unit_of_work_mock,
            data,
            mocker):
        # Arrange
        (line, batch, work_center, brigade, shift, task) = data

        unit_of_work_mock.lines.get_or_create_by_code.return_value = line
        unit_of_work_mock.work_centers.get_or_create_by_code.return_value = work_center
        unit_of_work_mock.batches.get_or_create_by_number_and_date.return_value = batch
        unit_of_work_mock.shifts.get_or_create_by_number.return_value = shift
        unit_of_work_mock.brigades.get_or_create_by_title.return_value = brigade
        unit_of_work_mock.tasks.get_by_batch_id.return_value = task

        value: TaskResult | None = None

        # Act
        async with mocker.patch.object(task_service, 'uow', unit_of_work_mock):
            value, error = await task_service.add(is_closed=is_closed, nomenclature=nomenclature, ekn_code=ekn_code,
                                                  task_title=task_title, line_code=line_code, shift=shift_number,
                                                  brigade_title=brigade_title, batch_number=batch_number,
                                                  batch_date=batch_date, work_center_code=work_center_code,
                                                  shift_start_date=shift_start_date, shift_end_date=shift_end_date)

        # Assert
        assert (value, error) == (TaskResult(
            id=task.id or 0,
            is_closed=task.is_closed,
            title=task.title,
            line=LineResult(id=line.id, code=line.code),
            shift=ShiftResult(id=shift.id, number=shift.number,
                              start_at=shift.start_at, end_at=shift.end_at),
            brigade=BrigadeResult(id=brigade.id, title=brigade.title),
            batch=BatchResult(id=batch.id, number=batch.number, date=batch.date),
            nomenclature=task.nomenclature,
            ekn_code=task.ekn_code,
            work_center=WorkCenterResult(id=work_center.id, code=work_center.code)
        ), None)

    @pytest.mark.parametrize(
        'task_id, expected_result',
        [(1, 'good'), (2, 'task_not_found')])
    async def test_get_by_id_with_product_id(
            self,
            task_id: int,
            expected_result: str,
            task_service,
            unit_of_work_mock,
            data,
            mocker):
        # Arrange
        (line, batch, work_center, brigade, shift, task) = data

        product_ids = [1, 2, 3, 4, 5]

        if expected_result == 'task_not_found':
            unit_of_work_mock.tasks.get_by_id.return_value = None
        elif expected_result == 'good':
            unit_of_work_mock.products.get_ids_list_by_batch_id.return_value = product_ids
            unit_of_work_mock.tasks.get_by_id.return_value = task

        value: TaskResultWithProductIdsResult | None = None

        # Act
        async with mocker.patch.object(task_service, 'uow', unit_of_work_mock):
            value, error = await task_service.get_by_id_with_product_id(task_id=task_id)

        # Assert
        if expected_result == 'good':
            assert value == TaskResultWithProductIdsResult(
                id=task.id,
                is_closed=task.is_closed,
                title=task.title,
                line=LineResult(id=task.batch.line.id, code=task.batch.line.code),
                shift=ShiftResult(id=task.shift.id, number=task.shift.number,
                                  start_at=task.shift.start_at, end_at=task.shift.end_at),
                brigade=BrigadeResult(id=task.brigade.id, title=task.brigade.title),
                batch=BatchResult(id=task.batch.id, number=task.batch.number, date=task.batch.date),
                nomenclature=task.nomenclature,
                ekn_code=task.ekn_code,
                work_center=WorkCenterResult(id=task.work_center.id, code=task.work_center.code),
                products=product_ids
            )

        if expected_result == 'task_not_found':
            assert (value, error) == (None, TaskErrors.not_found)

