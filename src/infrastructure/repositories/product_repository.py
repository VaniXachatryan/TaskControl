
from typing import List
from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.repositories.product_repository_interface import IProductRepository
from src.domain.entities.product import Product
from src.infrastructure.common.base_repository import BaseRepository


class ProductRepository(BaseRepository, IProductRepository):

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session=session, entity=Product)

    async def get_ids_list_by_batch_id(self, batch_id: int) -> List[int]:
        query = select(Product.id).where(Product.batch_id == batch_id)
        result = await self.session.execute(query)

        return [row for row in result.scalars()]

    async def any_by_code(self, code: str) -> bool:
        query = select(exists().where(Product.code == code))
        result = await self.session.execute(query)
        return result.scalar_one()

    async def get_by_code(self, code: str) -> Product | None:
        query = select(Product).where(Product.code == code)
        result = await self.session.execute(query)

        return result.scalar_one_or_none()
    