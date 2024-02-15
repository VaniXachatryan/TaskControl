from datetime import date as onlydate

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.repositories.batch_repository_interface import IBatchRepository
from src.domain.entities.batch import Batch
from src.infrastructure.common.base_repository import BaseRepository


class BatchRepository(BaseRepository, IBatchRepository):

    def __init__(self, session: AsyncSession):
        super().__init__(session=session, entity=Batch)

    async def get_by_number_and_date(self, number: int, date: onlydate, line_id: int = None) -> Batch | None:
        query = (select(Batch)
                 .where(Batch.number == number)
                 .where(Batch.date == date))

        if line_id is not None:
            query = query.where(Batch.line_id == line_id)

        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_or_create_by_number_and_date(self, number: int, date: onlydate, line_id: int) -> Batch:
        query = (select(Batch)
                 .where(Batch.line_id == line_id)
                 .where(Batch.number == number)
                 .where(Batch.date == date))
        result = await self.session.execute(query)
        result = result.scalar_one_or_none()

        if result is None:
            new_batch: Batch = Batch(number=number, date=date, line_id=line_id)
            self.session.add(new_batch)
            await self.session.flush()
            result = new_batch

        return result
