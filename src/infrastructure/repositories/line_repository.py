from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.repositories.line_repository_interface import ILineRepository
from src.domain.entities.line import Line
from src.infrastructure.common.base_repository import BaseRepository


class LineRepository(BaseRepository, ILineRepository):

    def __init__(self, session: AsyncSession):
        super().__init__(session=session, entity=Line)

    async def get_by_code(self, code: str) -> Line | None:
        query = select(Line).where(Line.code == code)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_or_create_by_code(self, code: str) -> Line:
        query = select(Line).where(Line.code == code)
        result = await self.session.execute(query)
        result = result.scalar_one_or_none()

        if result is None:
            new_line: Line = Line(code=code)
            self.session.add(new_line)
            await self.session.flush()
            result = new_line

        return result
