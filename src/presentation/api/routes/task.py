from fastapi import APIRouter, Depends

from src.presentation.api.depends import TaskServiceDepend
from src.presentation.api.schemas.task import TaskSchemaAdd

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/create")
async def create_task(task_service: TaskServiceDepend, schema: TaskSchemaAdd):
    await task_service.add(schema)
