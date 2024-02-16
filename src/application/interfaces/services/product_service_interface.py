from abc import ABC, abstractmethod

from returns.result import Result

from src.application.common.results.product_result import ProductResult


class IProductService(ABC):
    @abstractmethod
    async def add(self, code: str, batch_number: int, batch_date) -> (ProductResult, str):
        pass

    @abstractmethod
    async def aggregate(self, code: str, batch_id: int) -> (ProductResult, list):
        pass
