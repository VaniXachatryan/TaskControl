from fastapi import APIRouter, HTTPException
from returns.result import Result, Success, Failure

from src.application.common.results.task_result import TaskResultWithProductIdsResult, TaskResult
from src.domain.common.errors.task_errors import TaskErrors
from src.presentation.api.depends import TaskServiceDepend
from src.presentation.api.mapper.task_mapper import (task_result_to_task_scheme,
                                                     task_with_product_ids_result_to_task_with_product_scheme)
from src.presentation.api.schemas.task_scheme import TaskSchemeAdd, TaskScheme, TaskWithProductIdsScheme

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/create", status_code=201)
async def create_task(task_service: TaskServiceDepend, schema: TaskSchemeAdd):
    result: Result[TaskResult, str] = await task_service.add(
        is_closed=schema.is_closed,
        task_title=schema.title,
        line_code=schema.line_code,
        shift=schema.shift,
        brigade_title=schema.brigade,
        batch_number=schema.batch_number,
        batch_date=schema.batch_date,
        nomenclature=schema.nomenclature,
        ekn_code=schema.ekn_code,
        work_center_code=schema.work_center_code,
        shift_start_date=schema.shift_start_date,
        shift_end_date=schema.shift_end_date
    )

    match result:
        case Success(value):
            return task_result_to_task_scheme(value)


@router.get("/get_with_products", status_code=200)
async def get_by_id(task_service: TaskServiceDepend, id: int):
    result: Result[TaskResultWithProductIdsResult, str] = await task_service.get_by_id_with_product_id(task_id=id)

    match result:
        case Success(value):
            return task_with_product_ids_result_to_task_with_product_scheme(value)

        case Failure(TaskErrors.not_found):
            return HTTPException(status_code=404, detail="Сменное задание не найдено.")
