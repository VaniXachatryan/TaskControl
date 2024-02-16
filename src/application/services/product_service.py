from datetime import date, datetime

from src.application.common.results.product_result import ProductResult
from src.application.interfaces.services.product_service_interface import IProductService
from src.application.interfaces.unit_of_work_interface import IUnitOfWork
from src.domain.common.errors.batch_errors import BatchErrors
from src.domain.common.errors.product_errors import ProductErrors
from src.domain.entities.batch import Batch
from src.domain.entities.product import Product


class ProductService(IProductService):

    def __init__(self, uow: IUnitOfWork):
        self.uow: IUnitOfWork = uow

    async def add(self, code: str, batch_number: int, batch_date: date) -> (ProductResult, str):
        async with self.uow:
            is_any_code: bool = await self.uow.products.any_by_code(code=code)
            if is_any_code is True:
                return None, ProductErrors.is_exist

            batch: Batch | None = await self.uow.batches.get_by_number_and_date(
                number=batch_number,
                date=batch_date)

            if batch is None:
                return None, BatchErrors.not_found

            product: Product = Product(code=code, batch_id=batch.id)
            await self.uow.products.create(
                entity=product
            )

            await self.uow.commit()

            return ProductResult(
                    id=product.id,
                    code=product.code,
                    batch_number=product.batch.number,
                    batch_date=product.batch.date,
                    is_aggregated=product.is_aggregated,
                    aggregated_at=product.aggregated_at
                ), None

    async def aggregate(self, code: str, batch_id: int) -> (ProductResult, list):
        async with self.uow:
            product: Product | None = await self.uow.products.get_by_code(code=code)
            if product is None:
                return None, [ProductErrors.not_found]

            if product.batch.id != batch_id:
                return None, [ProductErrors.code_attached_to_another_batch]

            if product.is_aggregated is True:
                return None, [ProductErrors.is_aggregated, product.aggregated_at]

            product.is_aggregated = True
            product.aggregated_at = datetime.now()

            await self.uow.products.update(entity=product)
            await self.uow.commit()

            return True, None
