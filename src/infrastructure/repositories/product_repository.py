from typing import List

from sqlalchemy import select
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

        return [row[0] for row in result.all()]
