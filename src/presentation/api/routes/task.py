from datetime import datetime
from typing import Optional, List

from fastapi import APIRouter, Response, status
from returns.result import Result, Success, Failure

from src.application.common.results.task_result import TaskResultWithProductIdsResult, TaskResult
from src.domain.common.errors.task_errors import TaskErrors
from src.presentation.api.common.models.error_response import ErrorResponse
from src.presentation.api.depends import TaskServiceDepend
from src.presentation.api.mapper.task_mapper import (task_result_to_task_scheme,
                                                     task_with_product_ids_result_to_task_with_product_scheme)
from src.presentation.api.schemas.task_scheme import TaskSchemeAdd, TaskSchemeUpdate, TaskSchemeFilter

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/create", status_code=201)
async def create_task(task_service: TaskServiceDepend, scheme: TaskSchemeAdd):
    result: Result[TaskResult, str] = await task_service.add(
        is_closed=scheme.is_closed,
        task_title=scheme.title,
        line_code=scheme.line_code,
        shift=scheme.shift,
        brigade_title=scheme.brigade,
        batch_number=scheme.batch_number,
        batch_date=scheme.batch_date,
        nomenclature=scheme.nomenclature,
        ekn_code=scheme.ekn_code,
        work_center_code=scheme.work_center_code,
        shift_start_date=scheme.shift_start_date,
        shift_end_date=scheme.shift_end_date
    )

    match result:
        case Success(value):
            return task_result_to_task_scheme(value)


@router.get("/get_with_products", status_code=200)
async def get_by_id(task_service: TaskServiceDepend, id: int, response: Response):
    result: Result[TaskResultWithProductIdsResult, str] = await task_service.get_by_id_with_product_id(task_id=id)

    match result:
        case Success(value):
            return task_with_product_ids_result_to_task_with_product_scheme(value)

        case Failure(TaskErrors.not_found):
            response.status_code = status.HTTP_404_NOT_FOUND
            return ErrorResponse(status_code=404, detail="Сменное задание не найдено.")


@router.patch("/update")
async def update_task(task_service: TaskServiceDepend, scheme: TaskSchemeUpdate, id: int, response: Response):
    result: Result[TaskResult, str] = await task_service.update(
        task_id=id,
        is_closed=scheme.is_closed,
        task_title=scheme.title,
        line_code=scheme.line_code,
        shift=scheme.shift,
        brigade_title=scheme.brigade,
        batch_number=scheme.batch_number,
        batch_date=scheme.batch_date,
        nomenclature=scheme.nomenclature,
        ekn_code=scheme.ekn_code,
        work_center_code=scheme.work_center_code,
        shift_start_date=scheme.shift_start_date,
        shift_end_date=scheme.shift_end_date
    )

    match result:
        case Success(value):
            return task_result_to_task_scheme(value)

        case Failure(TaskErrors.not_found):
            response.status_code = status.HTTP_404_NOT_FOUND
            return ErrorResponse(status_code=404, detail="Сменное задание не найдено.")


@router.get("/get_by_filters")
async def update_task(task_service: TaskServiceDepend,
                      is_closed: Optional[bool] = None, line: Optional[str] = None,
                      task_title: Optional[str] = None, shift: Optional[str] = None, brigade: Optional[str] = None,
                      batch_number: Optional[int] = None, batch_date: Optional[datetime] = None,
                      nomenclature: Optional[str] = None, ekn_code: Optional[str] = None,
                      work_center: Optional[str] = None, shift_start_date: Optional[datetime] = None,
                      shift_end_date: Optional[datetime] = None,
                      count: int = 15, page: int = 1):
    result: Result[List[TaskResult], str] = await task_service.get_by_filters(
        is_closed=is_closed,
        task_title=task_title,
        line_code=line,
        shift_number=shift,
        brigade_title=brigade,
        batch_number=batch_number,
        batch_date=batch_date,
        nomenclature=nomenclature,
        ekn_code=ekn_code,
        work_center_code=work_center,
        shift_start_date=shift_start_date,
        shift_end_date=shift_end_date,
        count=count,
        page=page
    )

    match result:
        case Success(value):
            return value