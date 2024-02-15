from src.application.common.results.task_result import TaskResultWithProductIdsResult, TaskResult
from src.presentation.api.schemas.task_scheme import TaskWithProductIdsScheme, TaskScheme


def task_with_product_ids_result_to_task_with_product_scheme(result: TaskResultWithProductIdsResult) -> TaskWithProductIdsScheme:
    return TaskWithProductIdsScheme(
        id=result.id,
        title=result.title,
        is_closed=result.is_closed,
        line=result.line.code,
        shift=result.shift.number,
        brigade=result.brigade.title,
        batch=result.batch.number,
        nomenclature=result.nomenclature,
        ekn_code=result.ekn_code,
        work_center=result.work_center.code,
        products=result.products
    )


def task_result_to_task_scheme(result: TaskResult) -> TaskScheme:
    return TaskScheme(
        id=result.id,
        title=result.title,
        is_closed=result.is_closed,
        line=result.line.code,
        shift=result.shift.number,
        brigade=result.brigade.title,
        batch=result.batch.number,
        nomenclature=result.nomenclature,
        ekn_code=result.ekn_code,
        work_center=result.work_center.code
    )