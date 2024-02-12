from http import HTTPStatus

from fastapi import APIRouter
from returns.result import Result, Failure, Success
from starlette.responses import JSONResponse

from src.domain.common.errors.batch_errors import BatchErrors
from src.domain.common.errors.brigade_errors import BrigadeErrors
from src.domain.common.errors.line_errors import LineErrors
from src.domain.common.errors.work_center_errors import WorkCenterErrors
from src.domain.entities.task import Task
from src.presentation.api.depends import TaskServiceDepend
from src.presentation.api.mapping.task_mapper import task_to_task_scheme_add
from src.presentation.api.models.responses import get_response
from src.presentation.api.schemas.task_scheme import TaskSchemeAdd

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/create", status_code=201)
async def create_task(task_service: TaskServiceDepend, schema: TaskSchemeAdd):
    result: Result[Task, str] = await task_service.add(
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
        case Failure(BatchErrors.not_found):
            return JSONResponse(content=get_response("Партия не найдена"), status_code=HTTPStatus.CONFLICT)
        case Failure(BrigadeErrors.not_found):
            return JSONResponse(content=get_response("Бригада не найдена"), status_code=HTTPStatus.CONFLICT)
        case Failure(WorkCenterErrors.not_found):
            return JSONResponse(content=get_response("Рабочий центр не найден"), status_code=HTTPStatus.CONFLICT)
        case Failure(BatchErrors.task_not_found_for_batch):
            return JSONResponse(content=get_response("Данная партия сущестует, но у нее нет задания"),
                                status_code=HTTPStatus.CONFLICT)
        case Failure(LineErrors.not_found):
            return JSONResponse(content=get_response("Линия не найдена"), status_code=HTTPStatus.CONFLICT)
        case Success(value):
            return task_to_task_scheme_add(value.to_read_model())

