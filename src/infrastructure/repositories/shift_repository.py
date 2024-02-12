from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.repositories.shift_repository_interface import IShiftRepository
from src.domain.entities.shift import Shift
from src.infrastructure.common.base_repository import BaseRepository


class ShiftRepository(BaseRepository, IShiftRepository):
    model = Shift

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_by_number(self, number: int) -> Shift | None:
        query = select(self.model).where(self.model.number == number)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()