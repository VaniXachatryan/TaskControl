from src.application.interfaces.services.task_service_interface import ITaskService
from src.application.interfaces.unit_of_work_interface import IUnitOfWork
from src.domain.entities.task import Task
from src.presentation.api.schemas.task import TaskSchemaAdd
# TODO: refactor schema for app layer


class TaskService(ITaskService):
    def __init__(self, uow: IUnitOfWork):
        self.uow: IUnitOfWork = uow

    async def add(self, task: TaskSchemaAdd):
        # TODO: validation
        task_model: Task = Task(
            line_id=1,
            title=task.title,
            is_closed=task.is_closed,
            closed_at=None,
            work_center_id=task.work_center_id,
            shift_id=1,
            brigade_id=1,
            batch_id=1,
            nomenclature=task.nomenclature,
            ekn_code=task.ekn_code
        )

        async with self.uow:
            id = await self.uow.tasks.add_one(task_model)
            await self.uow.commit()
