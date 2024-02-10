from abc import abstractmethod, ABC

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.configurations.database import BaseModel


class IRepository(ABC):
    model = None

    @abstractmethod
    async def get_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    async def add_one(self, model: BaseModel):
        raise NotImplementedError


class BaseRepository(IRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, model: BaseModel) -> int:
        print("repository - add")

        self.session.add(model)

        return model.id

    async def get_by_id(self, entity_id: int) -> model:

        query = select(self.model).where(self.model.id == entity_id)
        result = await self.session.execute(query)
        return result.scalar_one().to_read_model()
