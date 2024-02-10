from src.application.interfaces.repositories.task_repository_interface import ITaskRepository
from src.domain.entities.task import Task


class TaskRepository(ITaskRepository):
    model = Task




